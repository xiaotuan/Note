[toc]

### 1. 实战演练

用 cat 读取文件内容的一般写法是：

```console
$ cat file1 file2 file3 ...
```

这个命令将作为命令行参数的文件内容拼接在一起。

+ 打印单个文件的内容：

  ```console
  $ cat file.txt
  This is a line inside file.txt
  This is the second line inside file.txt
  ```

+ 打印多个文件的内容：

  ```console
  $ cat one.txt two.txt
  This is line from one.txt
  This is line from two.txt
  ```

### 2. 工作原理

cat 命令不仅可以读取文件、拼接数据，还能够从标准输入中进行读取。

从标准输入中读取需要使用管道操作符：

```console
$ OUTPUT_FROM_SOME COMMANDS | cat
```

类似地，我们可以用 cat 将来自输入文件的内容与标准输入拼接在一起，将 stdin 和另一个文件中的数据结合起来。方法如下：

```console
$ echo 'Text through stdin' | cat - file.txt
```

在上面的代码中， `-` 被作为 stdin 文本的文件名。

### 3. 补充内容

#### 3.1 摆脱多余的空白行

有时候文本文件中可能包含多处连续的空白行。如果你需要删除这些额外的空白行，使用下面的方法：

```console
$ cat -s file
```

例如：

```console
$ cat multi_blanks.txt
line 1


line2


line3


line4

$ cat -s multi_blanks.txt # 压缩相邻的空白行
line1

line2

line3

line4
```

另外，也可以用 tr 删除所有的 z 空白行，可以参阅 《[用tr进行转换](./05-用tr进行转换.md)》。

#### 3.2 将制表符显示为 ^I

在用 Python 编写程序时，用于代码缩进的制表符以及空格是具有特殊含义的。因此，若在应该使用空格的地方误用了制表符的话，就会产生缩进错误。仅仅在文本编辑器中进行观察是很难发现这种错误的。cat 有一个特性，可以将制表符着重标记出来。该特性对排除缩进错误非常有用。用 cat 命令的 -T 选项能够将制表符标记成 ^I。例如：

```console
$ cat file.py
def function():
	var = 5
        next = 6
	third = 7	
	
$ cat -T file.py
def function():
^Ivar = 5
        next = 6
^Ithird = 7^I
```

#### 3.3 行号

使用 cat 命令的 -n 选项会在输出的每一行内容之前加上行号。别担心，cat 命令绝不会修改你的文件，它只是根据用户提供的选项在 stdout 中生成一个修改过的输出而已。例如：

```console
$ cat lines.txt
line
line
line

$ cat -n lines.txt
   1 line
   2 line
   3 line
```

> 注意：-n 甚至会为空白行加上行号。如果你想跳过空白行，那么可以使用选项 -b。

