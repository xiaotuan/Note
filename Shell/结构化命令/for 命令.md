[toc]

bash shell 提供了 `for` 命令，允许你创建一个遍历一系列值的循环。每次迭代都使用其中一个值来执行已定义好的一组命令。下面是 bash shell 中 `for` 命令的基本格式：

```shell
for var in list
do
	commands
done
```

在 do 和 done 语句之间输入的命令可以是一条或多条标准的 bash shell 命令。在这些命令中， `$var` 变量包含着这次迭代对应的当前列表项中的值。

> 提示：只要你愿意，也可以将 `do` 语句和 `for` 语句放在同一行，但必须用分号将其同列表中的值分开：`for var in list; do`。

### 1. 读取列表中的值

`for` 命令最基本的用法就是遍历 `for` 命令自身所定义的一系列值：

```shell
#!/bin/bash
# basic for command

for test in Alabama Alaska Arizona Arkansas California Colorado
do
	echo The next state is $test
done
```

### 2. 读取列表中的复杂值

下面是给 shell 脚本程序员带来麻烦的典型例子：

```shell
#!/bin/bash
# another example for how not to use the for command

for test in I don't know if this'll work
do 
	echo "word:$test"
done
```

运行结果如下：

```shell
$ ./test.sh 
word:I
word:dont know if thisll
word:work
```

shell 看到了列表值中的单引号并尝试使用它们来定义一个单独的数据值。有两种办法可解决这个问题：

+ 使用转义字符（反斜线）来将单引号转义；
+ 使用双引号来定义用到单引号的值

```shell
#!/bin/bash
# another example of how not to use the for command

for test in I don\'t know if "this'll" work
do 
	echo "word:$test"
done
```

你可能遇到的另一个问题是有多个词的值。记住，`for` 循环假定每个值都是用空格分割的。如果有包含空格的数据值，你就陷入麻烦了。

```shell
#!/bin/bash
# another example of how not to use the for command

for test in Nevada New Hampshire New Mexico New York North Carolina
do 
	echo "Now going to $test"
done
```

运行结果如下：

```shell
$ ./test.sh 
Now going to Nevada
Now going to New
Now going to Hampshire
Now going to New
Now going to Mexico
Now going to New
Now going to York
Now going to North
Now going to Carolina
```

`for` 命令用空格来划分列表中的每个值。如果在单独数据值中有空格，就必须用双引号将这些值圈起来。

```shell
#!/bin/bash
# another example of how not to use the for command

for test in Nevada "New Hampshire" "New Mexico" "New York"
do 
	echo "Now going to $test"
done
```

### 3. 从变量读取列表

通常 shell 脚本遇到的情况是，你将一系列值都几种存储在了一个变量中，然后需要遍历变量中的整个列表：

```shell
#!/bin/bash
# using a variable to hold the list

list="Alabama Alaska Arizona Arkansas Colorado"
list=$list" connecticut"

for state in $list
do
	echo "Have you ever visited $state？"
done
```

### 4. 从命令读取值

生成列表中所需值的另外一个途径就是使用命令的输出。可以用命令替换来执行任何能产生输出的命令，然后在 `for` 命令中使用该命令的输出：

```shell
#!/bin/bash
# reading values from a file

file="states"

for state in $(cat $file)
do
	echo "Visit beautiful $state"
done
```

运行结果如下：

```shell
$ cat states
Alabama
Alaska
Arizona
Arkansas
Colorado
Connecticut
Delaware
Florida
$ ./test.sh 
Visit beautiful Alabama
Visit beautiful Alaska
Visit beautiful Arizona
Visit beautiful Arkansas
Visit beautiful Colorado
Visit beautiful Connecticut
Visit beautiful Delaware
Visit beautiful Florida
Visit beautiful Georgia
```

你会注意到 `states` 文件中每一行有一个州，而不是通过空格分隔的。`for` 命令仍然以每次一行的方式遍历了 `cat` 命令的输出，假定每个州都是在单独的一行上。但这并没有解决数据中有空格的问题。如果你列出了一个名字中有空格的州，`for` 命令仍然会将每个单词当作单独的值。

### 5. 更改字段分隔符

造成上面这个问题的原因是特殊的环境变量 `IFS`，叫作**内部字段分隔符**。`IFS` 环境变量定义了 bash shell 用作字段分隔符的一系列字符。默认情况下，bash shell 会将下列字符当作字段分隔符：

+ 空格
+ 制表符
+ 换行符

如果 bash shell 在数据中看到了这些字符中的任意一个，它就会假定这表明了列表中一个新数据字段的开始。在处理可能含有空格的数据时，可以在 shell 脚本中临时更改 `IFS` 环境变量的值来限制被 bash shell 当作字段分隔符的字符。

```shell
IFS=$'\n'
```

例如：

```shell
#!/bin/bash
# reading values from a file

file="states"

IFS=$'\n'

for state in $(cat $file)
do
	echo "Visit beautiful $state"
done
```

> 警告：在处理代码量较大的脚本时，可能在一个地方需要修改 IFS 的值，然后忽略这次修改，在脚本的其他地方继续沿用 IFS 的默认值。一个可参考的安全实践是在改变 IFS 之前保存原来的 IFS 值，之后再恢复它：
>
> ```shell
> IFS.OLD=$IFS
> IFS=$'\n'
> <在代码中使用新的 IFS 值>
> IFS=$IFS.OLD
> ```

如果要指定多个IFS 字符，只要将它们在复制行串起来就行：

```shell
IFS=$'\n':;""
```

这个赋值会将换行符、冒号、分号和双引号作为字段分隔符。如何使用 IFS 字符解析数据没有任何限制。

### 6. 用通配符读取目录

可以用 `for` 命令来自动遍历目录中的文件。进行此操作时，必须在文件名或路径名中使用通配符。它会强制 shell 使用**文件扩展匹配**。文件扩展匹配是生成匹配指定通配符的文件名或路径名的过程。

```shell
#!/bin/bash
# iterate through all the files in a directory

for file in /home/richtest/*
do 
	if [ -d "$file" ]
	then
		echo "$file is a directory"
	elif [ -f "$file" ]
	then 
		echo "$file is a file"
	fi
done
```

> 注意：我们在这个例子的 `if` 语句中做了一些不同的处理：
>
> ```shell
> if [ -d "$file" ]
> ```
>
> 在 Linux 中，目录名和文件名中包含空格当然是合法的。要适应这种情况，应该将 `$file` 变量用双引号圈起来。如果不这么做，遇到含有空格的目录名或文件名时就会有错误产生。

也可以在 `for` 命令中列出多个目录通配符，将目录查找和列表合并进同一个 `for` 语句。

```shell
#!/bin/bash
# iterate through all the files in a directory

for file in /home/rich/.b* /home/rich/badtest
do 
	if [ -d "$file" ]
	then
		echo "$file is a directory"
	elif [ -f "$file" ]
	then 
		echo "$file is a file"
	else
		echo "$file doesn't exist"
	fi
done
```

> 警告：你可以在数据列表中放入任何东西。即使文件或目录不存在，`for` 语句也会尝试处理列表中的内容。在处理文件或目录时，这可能会是个问题。你无法知道你正在尝试遍历的目录是否存在：在处理之前测试一下文件的目录总是好的。