[toc]

在 `gawk` 编程语言中，你可以做下面的事情：

+ 定义变量来保护数据；
+ 使用算术和字符操作符来处理数据；
+ 使用结构化编程概念来为数据处理增加处理逻辑；
+ 通过提取数据文件中的数据元素，将其重新排列或格式化，生成格式化报告。

### 1. gawk 命令格式

`gawk` 程序的基本格式如下：

```shell
gawk options program file
```

<center><b>gawk 选项</b></center>

| 选项         | 描述                                 |
| ------------ | ------------------------------------ |
| -F fs        | 指定行中划分数据字段的字段分隔符     |
| -f file      | 从指定的文件中读取程序               |
| -v var=value | 定义 gawk 程序中的一个变量及其默认值 |
| -mf N        | 指定要处理的数据文件中的最大字段数   |
| -mr N        | 指定数据文件中的最大数据行数         |
| -W keyword   | 指定 gawk 的兼容模式或警告等级       |

### 2. 从命令行读取程序脚本

`gawk` 程序脚本用一对花括号来定义。你必须将脚本命令放到两个花括号（`{}`）中。由于 `gawk` 命令行假定脚本时单个文本字符串，你还必须将脚本放到单引号中。

```shell
$ gawk '{print "Hello World!"}'
This is a test
Hello World!
hello
Hello World!
This is another test
Hello World!
```

### 3. 使用数据字段变量

`gawk` 的主要特性之一是其处理文体文件中数据的能力。它会自动给一行中的每个数据元素分配一个变量。默认情况下，`gawk` 会将如下变量分配给它在文本行中发现的数据字段：

+ `$0` 代表整个文本行；
+ `$1` 代表文本行中的第 1 个数据字段；
+ `$2` 代表文本行中的第 2 个数据字段；
+ `$n` 代表文本行中的第 n 个数据字段。

在文本行中，每个数据字段都是通过**字段分隔符**划分的。`gawk` 在读取一行文本时，会用预定义的字段分隔符划分每个数据字段。`gawk` 中默认的字段分隔符是任意的空白字符。

```shell
$ cat data2.txt
One line of test text.
Two lines of test text.
Three lines of test.
$ gawk '{print $1}' data2.txt
One
Two
Three
```

如果你要读取采用了其他字段分隔符的文件，可以用 `-F` 选项指定：

```shell
$ gawk -F: '{print $1}' /etc/passwd
root
daemon
bin
sys
sync
games
man
......
```

### 4. 在程序脚本中使用多个命令

要在命令行上的程序脚本中使用多条命令，只要在命令之间放个分号即可：

```shell
$ echo "My name is Rich" | gawk '{$4="Christine"; print $0}'
My name is Christine
```

也可以用次提示符一次一行地输入程序脚本命令：

```shell
$ gawk '{
> $4="Christine"
> print $0}'
My name is Rich
My name is Christine
```

### 5. 从文件中读取程序

跟 `sed` 编辑器一样，`gawk` 编辑器允许将程序存储到文件中，然后再在命令行中引用。

```shell
$ cat script2.gawk
{print $1 "'s home directory is " $6}
$ gawk -F: -f script2.gawk /etc/passwd
root's home directory is /root
daemon's home directory is /usr/sbin
bin's home directory is /bin
sys's home directory is /dev
sync's home directory is /bin
games's home directory is /usr/games
man's home directory is /var/cache/man
lp's home directory is /var/spool/lpd
mail's home directory is /var/mail
......
```

可以在程序文件中指定多条命令。要这么做的话，只要一条命令放一行即可，不需要用分号。

```shell
$ cat script3.gawk
{
text = "'s home directory is "
print $1 test $6
}
$ gawk -F: -f script3.gawk /etc/passwd
root/root
daemon/usr/sbin
bin/bin
sys/dev
sync/bin
games/usr/games
man/var/cache/man
......
```

> 注意：`gawk` 程序在引用变量值时并未像 shell 脚本一样使用美元符。

### 6. 在处理数据前运行脚本

`gawk` 还允许指定程序脚本何时运行。默认情况下，`gawk` 会从输入中读取一行文本，然后针对该行的数据执行程序脚本。有时可能需要在处理数据前运行脚本，比如为报告创建标题。`BEGIN` 关键字就是用来做这个的。它会强制 `gawk` 在读取数据前执行 `BEGIN` 关键字 后指定的程序脚本。

```shell
$ gawk 'BEGIN {print "Hello World!"}'
Hello World!
```

如果想西永正常的程序脚本中处理数据，必须用另一个脚本区域来定义程序：

```shell
$ cat data3.txt
Line 1
Line 2
Line 3
$ gawk 'BEGIN {print "The data3 File Contents:"}
> {print $0}' data3.txt
The data3 File Contents:
Line 1
Line 2
Line 3
```

在 `gawk` 执行了 BEGIN 脚本后，它会用第二段脚本来处理文件数据。这么做时要小心，两段脚本仍然被认为是 `gawk` 命令行中的一个文本字符串。你需要相应地加上单引号。

### 7. 在处理数据后运行脚本

与 BEGIN 关键字类似，END 关键字允许你指定一个程序脚本，`gawk` 会在读完数据后执行它。

```shell
$ gawk 'BEGIN {print "The data3 File Contents: "}
> {print $0}
> END {print "End of File"} ' data3.txt
The data3 File Contents: 
Line 1
Line 2
Line 3
End of File
```

可以将所有这些内容放到一起组成一个漂亮的小程序脚本文件，用它从一个简单的数据文件中创建一份完整的报告。

```shell
$ cat script3.gawk 
BEGIN {
    print "The latest list of users and shells"
    print " UserID \t Shell"
    print "-------- \t --------"
    FS=":"
}

{
    print $1 "        \t " $7
}

END {
    print "This concludes the listing"
}
$ gawk -f script3.gawk /etc/passwd
The latest list of users and shells
 UserID 	 Shell
-------- 	 --------
root        	 /bin/bash
daemon        	 /usr/sbin/nologin
bin        	 /usr/sbin/nologin
sys        	 /usr/sbin/nologin
sync        	 /bin/sync
games        	 /usr/sbin/nologin
man        	 /usr/sbin/nologin
lp        	 /usr/sbin/nologin
mail        	 /usr/sbin/nologin
news        	 /usr/sbin/nologin
......
```

