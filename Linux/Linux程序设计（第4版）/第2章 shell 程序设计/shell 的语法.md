[toc]

### 1. 变量

在 `shell` 里，使用变量之前通常并不需要事先为它们做出声明。你只是通过使用它们（比如当你给它们赋初始值时）来创建它们。

在 `shell` 中，你可以通过在变量名前加一个 `$` 符号来访问它的内容。

```shell
$ salutation=Hello
$ echo $salutation
Hello
$ salutation="Yes Dear"
$ echo $salutation
Yes Dear
$ salutation=7+5
$ echo $salutation
7+5
```

> 注意，如果字符串里包含空格，就必须用引号把它们括起来。此外，等号两边不能有空格。

你可以使用 `read` 命令将用户的输入赋值给一个变量。这个命令需要一个参数，即准备读入用户输入数据的变量名，然后它会等待用户输入数据。通常情况下，在用户按下回车键时，`read` 命令结束。当从终端上读取一个变量时，你一般不需要使用引号，如下所示：

```shell
$ read salutation
Wie geht's?
$ echo $salutation
Wie geht's?
```

#### 1.1 使用引号

一般情况下，脚本文件中的参数以空白字符分隔（例如，一个空格、一个制表符或者一个换行符）。如果你想在一个参数中包含一个或多个空白字符，你就必须给参数加上引号。

像 `$foo` 这样的变量在引号中的行为取决于你所使用的引号类型。如果你把一个 `$` 变量表达式放在双引号中，程序执行到这一行时就会把变量替换为它的值；如果你把它放在单引号中，就不会发生替换现象。你还可以通过在 `$` 字符前面加上一个 `\` 字符以取消它的特殊含义。

**实验　变量的使用**

```shell
$ ./test.sh 
Hi there
Hi there
$myvar
$myvar
Enter some text
Hello World
$myvar now equals Hello World
```

#### 1.2 环境变量

| 环境变量  | 说　　明 |
| :----- | :---- |
| \$HOME |  当前用户的家目录  |
| \$PATH | 以冒号分隔的用来搜索命令的目录列表 |
| \$PS1 | 命令提示符，通常是\$字符，但在 `bas` 中，你可以使用一些更复杂的值。例如，字符串 `[\u@\h\W]\$` 就是一个流行的默认值，它给出用户名、机器名和当前目录名，当然也包括一个 `$` 提示符 |
| \$PS2 | 二级提示符，用来提示后续的输入，通常是 `>` 字符 |
| \$IFS | 输入域分隔符。当 `shell` 读取输入时，它给出用来分隔单词的一组字符，它们通常是空格、制表符和换行符 |
| \$0 | `shell` 脚本的名字 |
| \$# | 传递给脚本的参数个数 |
| \$\$ | `shell` 脚本的进程号，脚本程序通常会用它来生成一个唯一的临时文件，如 `/tmp/tmpfile_$$` |

> 如果想通过执行 `env<command>`命令来查看程序在不同环境下是如何工作的，请查阅 `env` 命令的使用手册。你也将在本章的后面看到如何使用 `export` 命令在子 `shell` 中设置环境变量。

#### 1.3参数变量

即使没有传递任何参数，环境变量 `$#` 也依然存在，只不过它的值是 0 罢了。

| 参数变量 | 说　　明 |
| :---- | :---- |
| \$1,\$2,... | 脚本程序的参数 |
| \$* | 在一个变量中列出所有的参数，各个参数之间用环境变量 `IFS` 中的第一个字符分隔开。如果 `IFS` 被修改了，那么 \$* 将命令行分割为参数的方式就将随之改变 |
| \$@ | 它是 \$* 的一种精巧的变体，它不使用IFS环境变量，所以即使 `IFS` 为空，参数也不会挤在一起 |

通过下面的例子，你可以很容易地看出 `$@` 和 `$*` 之间的区别：

```shell
$ IFS=''
$ set foo bar bam
$ echo "$@"
foo bar bam
$ echo "$*"
foobarbam
$ unset IFS
$ echo "$*"
foo bar bam
```

除了使用 `echo` 命令查看变量的内容外，你还可以使用 `read` 命令来读取它们。

**实验　使用参数和环境变量**

```shell
#!/bin/sh

salutation="Hello"
echo $salutation
echo "The Program $0 is now running"
echo "The second parameter was $2"
echo "The first parameter was $1"
echo "The parameter list was $*"
echo "The user's home directory is $HOME"

echo "Please enter a new greeting"
read salutation

echo $salutation
echo "The script is now complete"
exit 0
```

运行这个脚本程序，你将得到如下所示的输出结果：

```console
$ ./try_var.sh foo bar baz
Hello
The Program ./test.sh is now running
The second parameter was bar
The first parameter was foo
The parameter list was foo bar baz
The user's home directory is /home/xiaotuan
Please enter a new greeting
Sire
Sire
The script is now complete
```

### 2.条件

一个 `shell` 脚本能够对任何可以从命令行上调用的命令的退出码进行测试，其中也包括你自己编写的脚本程序。这也就是为什么要在所有自己编写的脚本程序的结尾包括一条返回值的 `exit` 命令的重要原因。

**test 或 [ 命令**

在实际工作中，大多数脚本程序都会广泛使用 `shell` 的布尔判断命令 `[` 或 `test`。当使用 `[` 命令时，我们还使用符号 `]` 来结尾。

> 因为 `test` 命令在 `shell` 脚本程序以外用得很少，所以那些很少编写 `shell` 脚本的 `Linux` 用户往往会将自己编写的简单程序命名为 `test`。如果程序不能正常工作，很可能是因为它与 `shell` 中的 `test` 命令发生了冲突。要想查看系统中是否有一个指定名称的外部命令，你可以尝试使用`whichtest` 这样的命令来检查执行的是哪一个 `test` 命令，或者使用 `./test` 这种执行方式以确保你执行的是当前目录下的脚本程序。如有疑问，你只需养成在调用脚本的前面加上 `./` 的习惯即可。

检查一个文件是否存在。用于实现这一操作的命令是 `test–f<filename>`，所以在脚本程序里，你可以写出如下所示的代码：

```shell
if test -f fred.c
then
...
fi
```

你还可以写成下面这样：

```shell
if [ -f fred.c ]
then
...
fi
```

> 注意，你必须在 `[` 符号和被检查的条件之间留出空格。要记住这一点，你可以把 `[` 符号看作和 `test` 命令一样，而 `test` 命令之后总是应该有一个空格。如果你喜欢把 `then` 和 `if` 放在同一行上，就必须要用一个分号把 `test` 语句和 `then` 分隔开。如下所示：
>
> ```shell
> if [ -f fred.c ]; then
> ...
> fi
> ```

`test` 命令可以使用的条件类型可以归为 3 类：字符串比较、算术比较和与文件有关的条件测试。

| 字符串比较 | 结　　果 |
| :---- | :---- |
| string1 = string2 | 如果两个字符串相同则结果为真 |
| string1 != string2 | 如果两个字符串不同则结果为真 |
| -n string | 如果字符串不为空则结果为真 |
| -z string | 如果字符串为null（一个空串）则结果为真 |

| 算术比较 | 结　　果 |
| :---- | :---- |
| expression1 -eq expression2 | 如果两个表达式相等则结果为真 |
| expression1 -ne expression2 | 如果两个表达式不等则结果为真 |
| expression1 -gt expression2 | 如果expression1大于expression2则结果为真 |
| expression1 -ge expression2 | 如果expression1大于等于expression2则结果为真 |
|expression1 -lt expression2 | 如果expression1小于expression2则结果为真 |
| expression1 -le expression2 | 如果expression1小于等于expression2则结果为真 |
| ! expression | 如果表达式为假则结果为真，反之亦然 |

| 文件条件测试 | 结　　果 |
| :---- | :---- |
| -d file | 如果文件是一个目录则结果为真 |
| -e file | 如果文件存在则结果为真。要注意的是，历史上 -e 选项不可移植，所以通常使用的是-f选项 |
| -f file | 如果文件是一个普通文件则结果为真 |
| -g file | 如果文件的 set-group-id 位被设置则结果为真 |
| -r file | 如果文件可读则结果为真 |
| -s file | 如果文件的大小不为 0 则结果为真 |
| -u file | 如果文件的 set-user-id 位被设置则结果为真 |
| -w file | 如果文件可写则结果为真 |
| -x file | 如果文件可执行则结果为真 |

> 读者可能想知道什么是 set-group-id 和 set-user-id（也叫做 set-gid 和 set-uid ）位。set-uid 位授予了程序其拥有者的访问权限而不是其使用者的访问权限，而 set-gid 位授予了程序其所在组的访问权限。这两个特殊位是通过 chmod 命令的选项s和g设置的。set-gid 和 set-uid 标志对 shell 脚本程序不起作用，它们只对可执行的二进制文件有用。

接下来的测试 `/bin/bash` 文件状态的例子可以让你看出如何使用它们：

```shell
#！/bin/sh

if [ -f /bin/bash ]
then
	echo "file /bin/bash exists"
fi

if [ -d /bin/bash ]
then
	echo "/bin/bash is a directory"
else
	echo "/bin/bash is NOT a directory"
fi
```

那么 `test` 命令是 `shell` 的内置命令，使用 `help test` 命令可以获得 `test` 命令更详细的信息。

### 3. 控制语句

#### 3.1 if 语句

```shell
if condition
then
	statements
else
	statements
fi
```

**实验　使用 if 语句**

```shell
#!/bin/sh

echo "Is it morning? Please answer yes or no"
read timeofday

if [ $timeofday = "yes" ]; then
	echo "Good morning"
else
	echo "Good afternoon"
fi

exit 0
```

这将给出如下所示的输出：

```console
Is it morning? Please answer yes or no
yes
Good morning
```

#### 3.2 elif 语句

你可以通过使用 `elif` 结构来避免出现这样的情况，它允许你在 `if` 结构的 `else` 部分被执行时增加第二个检查条件。

**实验　用 elif 结构做进一步检查**

```shell
#!/bin/sh

echo "Is it morning? Please answer yes or no"
read timeofday

if [ $timeofday = "yes" ]; then
	echo "Good morning"
elif [ $timeofday = "no" ]; then
	echo "Good afternoon"
else
	echo "Sorry, $timeofday not recognized. Enter yes of no"
	exit 1
fi

exit 0
```

#### 3.3 一个与变量有关的问题

运行这个新的脚本程序，但是这次不回答问题，而是直接按下回车键（或是某些键盘上的 <kbd>Return</kbd>键）。你将看到如下所示的出错信息；

```console
[: =: unexpected operator
```

哪里出问题了呢？问题就在第一个 `if` 语句中。在对变量 timeofday 进行测试的时候，它包含一个空字符串，这使得 `if` 语句成为下面这个样子：

```shell
if [ = "yes" ]
```

而这不是一个合法的条件。为了避免出现这种情况，你必须给变量加上引号，如下所示：

```shell
if [ "$timeofday" = "yes" ]
```

这样，一个空变量提供的就是一个合法的测试了：

```shell
if [ "" = "yes" ]
```

新脚本程序如下所示：

```shell
#!/bin/sh

echo "Is it morning? Please answer yes or no"
read timeofday

if [ "$timeofday" = "yes" ]; then
	echo "Good morning"
elif [ "$timeofday" = "no" ]; then
	echo "Good afternoon"
else
	echo "Sorry, $timeofday not recognized. Enter yes of no"
	exit 1
fi

exit 0
```

> 如果你想让 `echo` 命令去掉每一行后面的换行符，可移植性最好的办法是使用 `printf` 命令（请见本章后面的 `printf` 一节）而不是 `echo` 命令。有的 `shell` 用 `echo -e` 命令来完成这一任务，但并不是所有的系统都支持该命令。`bash` 使用 `echo –n` 命令来去除换行符，所以如果确信自己的脚本程序只运行在 `bash` 上，你就可以使用如下的语法：
>
> ```shell
> echo -n "Is it morning? Please answer yes or no: "
> ```

#### 3.4 for 语句

```shell
for variable in values
do
	statements
done
```

**实验　使用固定字符串的 for 循环**

```shell
#!/bin/sh

for foo in bar fud 43
do
	echo $foo
done
exit 0
```

该程序的输出结果如下所示：

```console
bar
fud
43
```

**实验　使用通配符扩展的 for 循环**

`for` 循环经常与 `shell` 的文件名扩展一起使用。这意味着在字符串的值中使用一个通配符，并由 `shell` 在程序执行时填写出所有的值。

```shell
#!/bin/sh

for file in $(ls t*.sh); do
	echo $file
	lpr $file
done
exit 0
```

> `lpr` 命令用于使用打印机打印文件。

#### 3.5 while 语句

```shell
while condition do
	statements
done
```

请看下面的例子，这是一个非常简陋的密码检查程序：

```shell
#!/bin/sh

echo "Enter password"
read trythis

while [ "$trythis" != "secret" ]; do
	echo "Sorry, try again"
	read trythis
done
exit 0
```

这个脚本程序的一个输出示例如下所示：

```shell
$ ./test.sh 
Enter password
password
Sorry, try again
secret
```

#### 3.6 until 语句

```shell
until condition
do
	statements
done
```

它与 `while` 循环很相似，只是把条件测试反过来了。换句话说，循环将反复执行直到条件为真，而不是在条件为真时反复执行。

> 一般来说，如果需要循环至少执行一次，那么就使用 `while` 循环；如果可能根本都不需要执行循环，就使用 `until` 循环。

```shell
#!/bin/bash

until who | grep "$1" > /dev/null
do
	sleep 60
done

# now ring the bell and announce the expected user.

echo -e '\a'
echo "*** $1 has just logged in **"

exit 0
```

#### 3.7case语句

```shell
case variable in
	pattern [ | pattern ] ...) statements;;
	pattern [ | pattern ] ...) statements;;
	...
esac
```

但 `case` 结构允许你通过一种比较复杂的方式将变量的内容和模式进行匹配，然后再根据匹配的模式去执行不同的代码。这要比使用多条 `if`、`elif` 和 `else` 语句来执行多个条件检查要简单得多。

> 请注意，每个模式行都以双分号（ `;;` ）结尾。因为你可以在前后模式之间放置多条语句，所以需要使用一个双分号来标记前一个语句的结束和后一个模式的开始。

> 你在 `case` 结构的模式中使用如 `*` 这样的通配符时要小心。因为 `case` 将使用第一个匹配的模式，即使后续的模式有更加精确的匹配也是如此。

**实验　case示例一：用户输入**

```shell
#!/bin/sh

echo "Is it morning? Please answer yes or no"
read timeofday

case "$timeofday" in
	yes) echo "Good Morning";;
	no ) echo "Good Afternoon";;
	y  ) echo "Good Morning";;
	n  ) echo "Good Afternoon";;
	*  ) echo "Sorry, answer not recognized";;
esac

exit 0
```

**实验　case示例二：合并匹配模式**

```shell
#!/bin/sh

echo "Is it morning? Please answer yes or no"
read timeofday

case "$timeofday" in
	yes | y |Yes | YES ) echo "Good Morning";;
	n* | N* )			 echo "Good Afternoon";;
	* )					 echo "Sorry, answer not recognized";;
esac

exit 0
```

**实验　case 示例三：执行多条语句**

```shell
#!/bin/sh

echo "Is it morning? Please answer yes or no"
read timeofday

case "$timeofday" in 
	yes | y | Yes | YES)
		echo "Good Morning"
		echo "Up bright and early this morning"
		;;
	[nN]*)
		echo "Good Afternoon"
		;;
	*)
		echo "Sorry, answer not recognized"
		echo "Please answer yes or no"
		exit 1
		;;
esac

exit 0
```

> 请注意，`esac` 前面的双分号（ `;;` ）是可选的。在 C 语言程序设计中，即使少一个 `break` 语句都算是不好的程序设计做法，但在 `shell` 程序设计中，如果最后一个 `case` 模式是默认模式，那么省略最后一个双分号（ `;;` ）是没有问题的，因为后面没有其他的 `case` 模式需要考虑了。

为了让 `case` 的匹配功能更强大，你可以使用如下的模式：

```shell
[yY] | [Yy][Ee][Ss] )
```

#### 3.8 命令列表

有时，你想要将几条命令连接成一个序列。例如，你可能想在执行某个语句之前同时满足好几个不同的条件，如下所示：

```shell
if [ -f this_file ]; then
	if [ -f that_file ] then
		if [ -f the_other_file]; then
			echo "All files present, and correct"
		fi
	fi
fi
```

或者你可能希望至少在这一系列条件中有一个为真，像下面这样：

```shell
if [ -f this_file ]; then
	foo="True"
elif [ -f that_file ]; then
	foo="True"
elif [ -f the_other_file ]; then
	foo="True"
else
	foo="False"
fi
if [ "$foo" = "True" ]; then
	echo "One of the files exists"
fi
```

##### 3.8.1 AND 列表

AND 列表结构允许你按照这样的方式执行一系列命令：只有在前面所有的命令都执行成功的情况下才执行后一条命令。它的语法是：

```shell
statement1 && statement2 && statement3 && ...
```

**实验　AND 列表**

```shell
#!/bin/sh

touch file_one
rm -f file_two

if [ -f file_one ] && echo "hello" && [ -f file_two ] && echo " there"
then
	echo "in if"
else
	echo "in else"
fi

exit 0
```

执行这个脚本程序，你将看到如下所示的结果：

```console
hello
in else
```

##### 3.8.2 OR 列表

```shell
statement1 || statement2 || statement3 || ...
```

沿用上一个例子，但要修改下面程序清单里阴影部分的语句：

```shell
#!/bin/sh

rm -f file_one

if [ -f file_one ] || echo "hello" || echo " there"
then
	echo "in if"
else
	echo "in else"
fi

exit 0
```

这个脚本程序的输出是：

```console
hello
in if
```

但在通常情况下，你应该用括号来强制求值的顺序。

#### 3.9 语句块

如果你想在某些只允许使用单个语句的地方（比如在 AND 或 OR 列表中）使用多条多条语句，你可以把它们括在花括号 `{}`中来构造一个语句块。例如，在本章后面给出的应用程序中，你将看到如下所示的代码：

```shell
get_confirm && {
	grep -v "$cdcatnum" $tracks_file > $temp_file
	cat $temp_file > $tracks_file
	echo
	add_record_tracks
}
```

### 4. 函数

作为另一种选择，你可以把一个大型的脚本程序分成许多小一点的脚本程序，让每个脚本完成一个小任务。但这种做法有几个缺点：在一个脚本程序中执行另外一个脚本程序要比执行一个函数慢得多；返回执行结果变得更加困难，而且可能存在非常多的小脚本。你应该考虑自己的脚本程序中是否有可以明显的单独存在的最小部分，并将其作为是否应将一个大型脚本程序分解为一组小脚本的衡量尺度。

要定义一个 shell 函数，你只需写出它的名字，然后是一对空括号，再把函数中的语句放在一对花括号中，如下所示：

```shell
function_name() {
	statements
}
```

**实验　一个简单的函数**

```shell
#!/bin/sh

foo() {
	echo "Function foo is executing"
}

echo "script starting"
foo
echo "script ended"

exit 0
```

你必须在调用一个函数之前先对它进行定义.

当一个函数被调用时，脚本程序的位置参数（ `$*`、`$@`、`$#`、`$1`、`$2`等）会被替换为函数的参数。这也是你读取传递给函数的参数的办法。当函数执行完毕后，这些参数会恢复为它们先前的值。

> 一些老版本的 shell 在函数执行之后可能不会恢复位置参数的值。所以如果你想让自己的脚本程序具备可移植性，就最好不要依赖这一行为。

你可以通过 return 命令让函数返回数字值。让函数返回字符串值的常用方法是让函数将字符串保存在一个变量中，该变量然后可以在函数结束之后被使用。此外，你还可以 `echo` 一个字符串并捕获其结果，如下所示：

```shell
foo () { echo JAY; }
...
result = "$(foo)"
```

>  请注意，你可以使用 `local` 关键字在 shell 函数中声明局部变量，局部变量将仅在函数的作用范围内有效。此外，函数可以访问全局作用范围内的其他shell变量。如果一个局部变量和一个全局变量的名字相同，前者就会覆盖后者，但仅限于函数的作用范围之内。例如，你可以对上面的脚本程序进行如下的修改来查看执行结果：

```shell
#!/bin/sh

sample_text="global variable"

foo() {
	local sample_text="local variable"
	echo "Function foo is executing"
	echo $sample_text
}

echo "script starting"
echo $sample_text

foo

echo "script ended"
echo $sample_text

exit 0
```

如果在函数里没有使用 `return` 命令指定一个返回值，函数返回的就是执行的最后一条命令的退出码。

**实验　从函数中返回一个值**

```shell
#!/bin/sh

yes_or_no() {
	echo "Is your name $* ?"
	while true
	do
		echo -n "Enter yes or no: "
		read x
		case "$x" in
			y | yes )	return 0;;
			n | no  )	return 1;;
			* )			echo "Answer yes or no"
		esac
	done
}

echo "Original parameters are $*"

if yes_or_no "$1"
then
	echo "Hi $1, nice name"
else
	echo "Never mind"
fi
exit 0
```

这个脚本程序的典型输出如下所示：

```shell
$ ./test.sh Rick Neil
Original parameters are Rick Neil
Is your name Rick ?
Enter yes or no: yes
Hi Rick, nice name
```

### 5. 命令

你可以在 shell 脚本程序内部执行两类命令。一类是可以在命令提示符中执行的 “普通” 命令，也称为外部命令（externalcommand），一类是我们前面提到的 “内置” 命令，也称为内部命令（internalcommand）。内置命令是在 shell 内部实现的，它们不能作为外部程序被调用。

#### 5.1 break 命令

你可以用这个命令在控制条件未满足之前，跳出 `for`、`while` 或 `until` 循环。你可以为 `break` 命令提供一个额外的数值参数来表明需要跳出的循环层数，但我们并不建议读者这么做，因为它将大大降低程序的可读性。在默认情况下，`break` 只跳出一层循环。

```shell
#!/bin/sh

rm -rf fred*
echo > fred1
echo > fred2
mkdir fred3
echo > fred4

for file in fred*
do
	if [ -d "$file" ]; then
		break;
	fi
done

echo first directory starting fred was $file

rm -rf fred*
exit 0
```

#### 5.2 : 命令

冒号（ `:` ）命令是一个空命令。它偶尔会被用于简化条件逻辑，相当于 true 的一个别名。由于它是内置命令，所以它运行的比 true 快，但它的输出可读性较差。

`:` 结构也会被用在变量的条件设置中，例如：

```shell
: ${var:=value}
```

如果没有 `:`，shell 将试图把 `$var` 当作一条命令来处理。

> 在一些 shell 脚本，主要是一些旧的 shell 脚本中，你可能会看到冒号被用在一行的开头来表示一个注释。但现代的脚本总是用 `#` 来开始一个注释行，因为这样做执行效率更高。

```shell
#!/bin/sh

rm -f fred
if [ -f fred ]; then
	:
else
	echo file fred did not exits
fi

exit 0
```

#### 5.3 continue 命令

这个命令使 `for`、`while` 或 `until` 循环跳到下一次循环继续执行，循环变量取循环列表中的下一个值。

```shell
#!/bin/sh

rm -rf fred*
echo > fred1
echo > fred2
mkdir fred3
echo > fred4

for file in fred*
do
	if [ -d "$file" ]; then
		echo "skipping directory $file"
		continue
	fi
	echo file is $file
done

rm -rf fred*
exit 0
```

`continue` 可以带一个可选的参数以表示希望继续执行的循环嵌套层数，也就是说你可以部分地跳出嵌套循环。这个参数很少使用，因为它会导致脚本程序极难理解。例如：

```shell
for x in 1 2 3
do 
	echo before $x
	continue 1
	echo after $x
done
```

#### 5.4 . 命令

点（ `.` ）命令用于在当前 shell 中执行命令：

```shell
../shell_script
```

通常，当一个脚本执行一条外部命令或脚本程序时，它会创建一个新的环境（

环境（一个子 shell），命令将在这个新环境中执行，在命令执行完毕后，这个环境被丢弃，留下退出码返回给父 shell。但外部的 `source` 命令和点命令（这两个命令差不多是同义词）在执行脚本程序中列出的命令时，使用的是调用该脚本程序的同一个 shell。

因为在默认情况下，shell 脚本程序会在一个新创建的环境中执行，所以脚本程序对环境变量所作的任何修改都会丢失。而点命令允许执行的脚本程序改变当前环境。当你要把一个脚本当作 “包裹器” 来为后续执行的一些其他命令设置环境时，这个命令通常就很有用。

**实验　点（ . ）命令**

1. 假设你有两个包含环境设置的文件，它们分别针对两个不同的开发环境。为了设置老的、经典命令的环境，你可以使用文件 classic_set，它的内容如下所示：

   ```shell
   #!/bin/sh
   
   version=classic
   PATH=/usr/local/old_bin:/usr/bin:/bin:.
   PS1="classic> "
   ```

2. 对于新命令，使用文件 latest_set：

   ```shell
   #!/bin/sh
   
   version=latest
   PATH=/usr/local/new_bin:/usr/bin:/bin:.
   PS1="lastest version> "
   ```

你可以通过将这些脚本程序和点命令结合来设置环境，就像下面的示例那样：

```console
$ . ./test.sh 
classic> echo $version
classic
classic> . ./lastest_set.sh 
lastest version> echo $version
latest
lastest version> 
```

#### 5.5 echo 命令

虽然，X/Open 建议在现代 shell 中使用 `printf` 命令，但我们还是依照常规使用 echo 命令来输出结尾带有换行符的字符串。

一个常见的问题是如何去掉换行符。遗憾的是，不同版本的 UNIX 对这个问题有着不同的解决方法。Linux 常用的解决方法如下所示：

```shell
echo -n "string to output"
```

但你也经常会遇到：

```shell
echo -e "string to output\c"
```

第二种方法 `echo -e` 确保启用了反斜线转义字符（如 `\c` 代表去掉换行符，`\t` 代表制表符，`\n` 代表回车）的解释。在老版本的 bash 中，对反斜线转义字符的解释通常都是默认启用的，但最新版本的 bash 通常在默认情况下都不对反斜线转义字符进行解释。你所使用的 Linux 发行版的详细行为请查看相关手册。

> 如果你需要一种删除结尾换行符的可移植方法，则可以使用外部命令 `tr` 来删除它，但它执行的速度比较慢。如果你需要自己的脚本兼容 UNIX 系统并且需要删除换行符，最好坚持使用 `printf` 命令。如果你的脚本只需要运行在 Linux 和 bash 上，那么 `echo -n` 是不错的选择，虽然你可能需要在脚本的开头加上 `#!/bin/bash` ，以明确表示你需要 bash 风格的行为。

#### 5.6 eval 命令

`eval` 命令允许你对参数进行求值。它是 shell 的内置命令，通常不会以单独命令的形式存在。我们借用X/Open 规范中的一个小例子来演示它的用法：

```shell
foo=10
x=foo
y='$'$x
echo $y
```

它输出 `$foo`，而

```shell
foo=10
x=foo
eval y='$'$x
echo $y
```

输出 10。因此，`eval` 命令有点像一个额外的 `$`，它给出一个变量的值的值。

`eval` 命令十分有用，它允许代码被随时生成和运行。虽然它的确增加了脚本调试的复杂度，但它可以让你完成使用其他方法难以或者根本无法完成的事情。

#### 5.7 exec 命令

`exec` 命令有两种不同的用法。它的典型用法是将当前 shell 替换为一个不同的程序。例如：

```shell
exec wall "Thanks for all the fish"
```

脚本中的这个命令会用 `wall` 命令替换当前的 shell。脚本程序中 `exec` 命令后面的代码都不会执行，因为执行这个脚本的 shell 已经不存在了。

`exec` 的第二种用法是修改当前文件描述符：

```shell
exec 3< afile
```

这使得文件描述符3被打开以便从文件 afile 中读取数据。这种用法非常少见。

#### 5.8 exit n 命令

`exit` 命令使脚本程序以退出码 `n` 结束运行。如果你在任何一个交互式 shell 的命令提示符中使用这个命令，它会使你退出系统。如果你允许自己的脚本程序在退出时不指定一个退出状态，那么该脚本中最后一条被执行命令的状态将被用作为返回值。在脚本程序中提供一个退出码总是一个良好的习惯。

在 shell 脚本编程中，退出码 0 表示成功，退出码 1~125 是脚本程序可以使用的错误代码。其余数字具有保留含义，如表2-7所示。

| 退　出　码 | 说　　明 |
| :-: | :----- |
| 126 | 文件不可执行 |
| 127 | 命令未找到 |
| 128及以上 | 出现一个信号 |

下面是一个简单的例子，如果当前目录下存在一个名为 .profile 的文件，它就返回 0 表示成功：

```shell
#!/bin/sh

if [ -f .profile ]; then
	exit 0
fi

exit 1
```

如果你是个精益求精的人，或至少追求更简洁的脚本，那么你可以组合使用前面介绍过的AND和OR列表来重写这个脚本程序，只需要一行代码：

```shell
[ -f .profile ] && exit 0 || exit 1
```

#### 5.9 export 命令

`export` 命令将作为它参数的变量导出到子 shell 中，并使之在子 shell 中有效。在默认情况下，在一个 shell 中被创建的变量在这个 shell 调用的下级（子）shell 中是不可用的。`export` 命令把自己的参数创建为一个环境变量，而这个环境变量可以被当前程序调用的其他脚本和程序看见。从更技术的角度来说，被导出的变量构成从该 shell 衍生的任何子进程的环境变量。

**实验　导出变量**

1. 我们先列出脚本程序 export2：

   ```shell
   #!/bin/sh
   
   echo "$foo"
   echo "$bar"
   ```

2. 然后是脚本程序 export1。在这个脚本的结尾，我们调用了 export2：

   ```shell
   #!/bin/sh
   
   foo="The first meta-syntactic variable"
   export bar="The second meta-syntactic variable"
   
   ./export2
   ```

如果你运行这个脚本程序，你将得到如下的输出：

```shell
$ ./lastest_set.sh 

The second meta-syntactic variable
```

> `set -a`或 `set -allexport` 命令将导出它之后声明的所有变量。

#### 5.10 expr 命令

`expr` 命令将它的参数当作一个表达式来求值。它的最常见用法就是进行如下形式的简单数学运算：

```shell
x=`expr $x + 1`
```

反引号字符使 x 取值为命令 `expr $x + 1` 的执行结果。你也可以用语法 `$()` 替换反引号，如下所示：

```shell
x=$(expr $x + 1)
```

`expr` 命令的功能十分强大，它可以完成许多表达式求值计算。表 2-8 列出了主要的一些求值计算。

| 表达式求值 | 说　　明 |
| :---- | :---- |
| expr1 \| expr2 | 如果expr1非零，则等于expr1，否则等于expr2 |
| expr1 & expr2 | 只要有一个表达式为零，则等于零，否则等于expr1 |
| expr1 = expr2 | 等于 |
| expr1 > expr2 | 大于 |
| expr1 >= expr2 | 大于等于 |
| expr1 < expr2 | 小于 |
| expr1 <= expr2 | 小于等于 |
| expr1 != expr2 | 不等于 |
| expr1 + expr2 | 加法 |
| expr1 - expr2 | 减法 |
| expr1 * expr2 | 乘法 |
| expr1 / expr2 | 整除 |
| expr1 % expr2 | 取余 |

在较新的脚本程序中，`expr` 命令通常被替换为更有效的 `$((...))` 语法。

#### 5.11 printf 命令

它的语法是：

```shell
printf "format string" parameter1 parameter2 ...
```

格式字符串与 C/C++ 中使用的非常相似，但有一些自己的限制。主要是不支持浮点数，因为 shell 中所有的算术运算都是按照整数来进行计算的。格式字符串由各种可打印字符、转义序列和字符转换限定符组成。格式字符串中除了%和\之外的所有字符都将按原样输出。

| 转义序列 | 说　　明 |
| :---- | :---- |
| \\" | 双引号 |
| \\\\ | 反斜线字符 |
| \\a | 报警（响铃或蜂鸣） |
| \\b | 退格字符 |
| \\c | 取消进一步的输出 |
| \\f | 进纸换页字符 |
| \\n | 换行符 |
| \\r | 回车符 |
| \\t | 制表符 |
| \\v | 垂直制表符 |
| \\ooo | 八进制值 ooo 表示的单个字符 |
| \\xHH | 十六进制值 HH 表示的单个字符 |

字符转换限定符由一个 % 和跟在后面的一个转换字符组成。主要的转换字符如表2-10所示。

| 字符转换限定符 | 说　　明 |
| :---- | :---- |
| d | 输出一个十进制数字 |
| C | 输出一个字符 |
| S | 输出一个字符串 |
| % | 输出一个%字符 |

格式字符串然后被用来解释 `printf` 后续参数的含义并输出结果。例如：

```shell
$ printf "%s\n" hello
hello
$ printf "%s %d\t%s" "Hi There" 15 people
Hi There 15	people
```

#### 5.12 return 命令

`return` 命令有一个数值参数，这个参数在调用该函数的脚本程序里被看做是该函数的返回值。如果没有指定参数，`return` 命令默认返回最后一条命令的退出码。

#### 5.13 set 命令

`set` 命令的作用是为 shell 设置参数变量。许多命令的输出结果是以空格分隔的值，如果需要使用输出结果中的某个域，这个命令就非常有用。

假设你想在一个 shell 脚本中使用当前月份的名字。系统本身提供了一个 `date` 命令，它的输出结果中包含了字符串形式的月份名称，但是你需要把它与其他区域分隔开。你可以将 `set` 命令和 `$(...)` 结构相结合来执行 `date` 命令，并且返回想要的结果。`date` 命令的输出把月份字符串作为它的第二个参数：

```shell
#!/bin/sh

echo the date is $(date)
set $(date)
echo The month is $2

exit 0
```

这个程序把 `date` 命令的输出设置为参数列表，然后通过位置参数 `$2` 获得月份。

```console
the date is 2021年 04月 08日 星期四 14:18:32 CST
The month is 04月
```

你还可以通过 `set` 命令和它的参数来控制 shell 的执行方式。其中最常用的命令格式是 `set -x`，它让一个脚本程序跟踪显示它当前执行的命令。

#### 5.14 shift 命令

`shift` 命令把所有参数变量左移一个位置，使 `$2` 变成 `$1`，`$3` 变成 `$2`，以此类推。原来 `$1` 的值将被丢弃，而 `$0` 仍将保持不变。如果调用 `shift` 命令时指定了一个数值参数，则表示所有的参数将左移指定的次数。`$*`、`$@` 和 `$#` 等其他变量也将根据参数变量的新安排做相应的变动。

例如，你可以像下面这样依次扫描所有的位置参数：

```shell
#!/bin/sh

while [ "$1" != "" ]; do
	echo "$1"
	shift
done

exit 0
```

#### 5.15 trap 命令

`trap` 命令用于指定在接收到信号后将要采取的行动，信号。`trap` 命令的一种常见用途是在脚本程序被中断时完成清理工作。历史上，shell 总是用数字来代表信号，但新的脚本程序应该使用信号的名字，它们定义在头文件 `signal.h` 中，在使用信号名时需要省略 SIG 前缀。你可以在命令提示符下输入命令`trap -l` 来查看信号编号及其关联的名称。

`trap` 命令有两个参数，第一个参数是接收到指定信号时将要采取的行动，第二个参数是要处理的信号名。

```shell
trap command signal
```

请记住，脚本程序通常是以从上到下的顺序解释执行的，所以你必须在你想保护的那部分代码之前指定 `trap` 命令。

如果要重置某个信号的处理方式到其默认值，只需将 command 设置为 `-`。如果要忽略某个信号，就把 command 设置为空字符串 `''`。一个不带参数的 `trap` 命令将列出当前设置的信号及其行动的清单。

| 信　　号 | 说　　明 |
| :---- | :---- |
| HUP(1) | 挂起，通常因终端掉线或用户退出而引发 |
| INT(2) | 中断，通常因按下Ctrl+C组合键而引发QUIT(3)退出，通常因按下Ctrl+\\组合键而引发 |
| ABRT(6) | 中止，通常因某些严重的执行错误而引发 |
|ALRM(14) | 报警，通常用来处理超时 |

**实验　信号处理**

```shell
#!/bin/sh

trap 'rm -f /tmp/my_tmp_file_$$' INT
echo creating file /tmp/my_tmp_file_$$
date > /tmp/my_tmp_file_$$

echo "press interrupt (CTRL-C) to interrupt ...."
while [ -f /tmp/my_tmp_file_$$ ]; do
	echo File exists
	sleep 1
done
echo The file no longer exists

trap INT
echo creating file /tmp/my_tmp_file_$$
date > /tmp/my_tmp_file_$$

echo "press interrupt (CTRL-C) to interrupt ...."
while [ -f /tmp/my_tmp_file_$$ ]; do
	echo File exists
	sleep 1
done

echo we never get here
exit 0
```

如果你运行这个脚本，在每次循环时按下 <kbd>Ctrl</kbd>+<kbd>C</kbd> 组合键（或任何你系统上设定的中断键），将得到如下所示的输出：

```console
creating file /tmp/my_tmp_file_4399
press interrupt (CTRL-C) to interrupt ....
File exists
File exists
File exists
^CThe file no longer exists
creating file /tmp/my_tmp_file_4399
press interrupt (CTRL-C) to interrupt ....
File exists
File exists
File exists
File exists
File exists
File exists
```

#### 5.16 unset 命令

`unset` 命令的作用是从环境中删除变量或函数。这个命令不能删除 shell 本身定义的只读变量（如 IFS ）。这个命令并不常用。

下面的脚本第一次输出字符串 HelloWorld，但第二次只输出一个换行符：

```shell
#!/bin/sh

foo="Hello World"
echo $foo

unset foo
echo $foo
```

> 使用 `foo=` 语句产生的效果与上面脚本中的 `unset` 命令产生的效果差不多，但并不等同。`foo=` 语句将变量 foo 设置为空，但变量 foo 仍然存在，而使用 `unset foo` 语句的效果是把变量 foo 从环境中删除。

#### 5.17 另外两个有用的命令和正则表达式

+ **find 命令**

让我们首先看一个非常简单的例子，它用来在本地机器上查找名为 test 的文件。为了确保你具有搜索整个机器的权限，请以 root 用户身份来执行这个命令：

```console
# find / -name test -print
/usr/bin/test
#
```

然而，这个命令的执行确实需要花费很长的时间，这就是我们要介绍的第一个选项发挥作用的时候了。如果你指定 `-mount` 选项，你就可以告诉 `find` 命令不要搜索挂载的其他文件系统的目录。

```console
# find / -mount -name test -print
/usr/bin/test
#
```

`find` 命令的完整语法格式如下所示：

```shell
find [path][options][tests][actions]
```

`find` 命令有许多选项可用，表 2-12 列出了一些主要的选项。

| 选　　项 | 含　　义 |
| :---- | :---- |
| -depth | 在查看目录本身之前先搜索目录的内容 |
| -follow | 跟随符号链接 |
| -maxdepths N | 最多搜索N层目录 |
| -mount (或 -xdev) | 不搜索其他文件系统中的目录 |

下面是测试部分。可以提供给 `find` 命令的测试非常多，每种测试返回的结果有两种可能：true 或 false。`find` 命令开始工作时，它按照顺序将定义的每种测试依次应用到它搜索到的每个文件上。如果一个测试返回 false，`find` 命令就停止处理它当前找到的这个文件，并继续搜索。如果一个测试返回true，`find` 命令将继续下一个测试或对当前文件采取行动。表2-13只列出了最常用的测试，请参考 `find` 命令的手册页以了解所有可以使用的测试。

| 测　　试 | 含　　义 |
| :---- | :---- |
| -atime N | 文件在 N 天之前被最后访问过 |
| -mtime N | 文件在 N 天之前被最后修改过 |
| -name pattern | 文件名（不包括路径名）匹配提供的模式 pattern，为了确保 pattern 被传递给find 命令而不是由 shell 来处理，pattern 必须总是用引号括起 |
| -newer otherfile | 文件比 otherfile 文件要新 |
| -type c | 文件的类型为 c，c 是一个特殊类型。最常见的是 d（目录）和 f（普通文件）。其他可用的类型请参考手册页 |
| -useruser name | 文件的拥有者是指定的用户 username |

**实验 　 使用带测试的 find 命令**

```shell
$ find . -newer while2 -print
.
./elif3
./words.txt
./words2.txt
./_trap
$
```
`-exec` 和 `-ok` 命令将命令行上后续的参数作为它们参数的一部分，直到被 `\;` 序列终止。实际上，`- exec`  和 `-ok` 命令执行的是一个嵌入式命令，所以嵌入式命令必须以一个转义的分号结束，使得 `find` 命令可以决定什么时候它可以继续查找用于它自己的命令行选项。魔术字符串 `{}` 是 `-exec` 或 `-ok` 命令的一个特殊类型的参数，它将被当前文件的完整路径取代。

| 动作 | 含义 |
| :---- | :---- |
| -exec command | 执行一条命令。这是最常见的动作之一。请见这个表格之后的解释以了解参数是如何传递给这个命令的。这个动作必须使用 `\;` 字符对来结束 |
| -ok command | 与 `-exec` 类似，但它在执行命令之前会针对每个要处理的文件，提示用户进行确认。这个动作必须使用 `\;` 字符对来结束 |
| -print | 打印文件名 |
| -ls | 对当前文件使用命令 `ls –dils` |

我们来看一个比较简单的例子，它使用一条非常安全的命令 `ls`：

```shell
$ find . \(-name "_*" -or -newer while2 \) -type f -print
./elif3
./elif3 
./words.txt 
./words2.txt 
./_break
./_if 
./_set 
./_shift 
./_trap 
./_unset 
./_until 
$
```

+ **grep 命令**

这个不寻常的名字代表的是通用正则表达式解析器（General Regular Expression Parser，简写为grep）。你使用 `find` 命令在系统中搜索文件，而使用 `grep` 命令在文件中搜索字符串。事实上，一种非常常见的用法是在使用 `find` 命令时，将 `grep` 作为传递给 `-exec` 的一条命令。

`grep` 命令使用一个选项、一个要匹配的模式和要搜索的文件，它的语法如下所示：

```shell
grep [options] PATTERN [FILES]
```

如果没有提供文件名，则 `grep` 命令将搜索标准输入。我们首先来查看 `grep` 命令的一些主要选项，它们列在了表 2-16 中，完整的选项列表请见 `grep` 命令的手册页。

| 选　　项 | 含　　义 |
| :---- | :---- |
| -c | 输出匹配行的数目，而不是输出匹配的行 |
| -E | 启用扩展表达式 |
| -h | 取消每个输出行的普通前缀，即匹配查询模式的文件名 |
| -i | 忽略大小写 |
| -l | 只列出包含匹配行的文件名，而不输出真正的匹配行 |
| -v | 对匹配模式取反，即搜索不匹配行而不是匹配行 |

**实验　基本的grep命令用法**

```shell
$ grep in words.txt 
When shall we three meet again. In thunder, lightning, or in rain? 
I come, Graymalkin!
$ grep -c in words.txt words2.txt 
words.txt: 2 
words2.txt: 14 
$ grep -c -v in words.txt words2.txt 
words.txt: 9 
words2.txt: 16 
$
```

+ **正则表达式**

在正则表达式的使用过程中，一些字符是以特定方式处理的。最常使用的特殊字符如表2-17所示。

| 字　　符 | 含　　义 |
| :---- | :---- |
| ^ | 指向一行的开头 |
| \$ | 指向一行的结尾 |
| . | 任意单个字符 |
| [] | 方括号内包含一个字符范围，其中任何一个字符都可以被匹配，例如字符范围 a～e，或在字符范围前面加上 ^ 符号表示使用反向字符范围，即不匹配指定范围内的字符 |

如果想将上述字符用作普通字符，就需要在它们前面加上 `\ `字符。例如，如果想使用 `$` 字符，你需要将它写为 `$`。

在方括号中还可以使用一些有用的特殊匹配模式，如表 2-18 所示。

| 匹配模式 | 含　　义 |
| :---- | :---- |
| [:alnum:] | 字母与数字字符 |
| [:alpha:] | 字母 |
| [:ascii:] | ASCII 字符 |
| [:blank:] | 空格或制表符 |
| [:cntrl:] | ASCII 控制字符 |
| [:digit:] | 数字 |
| [:graph:] | 非控制、非空格字符 |
| [:lower:] | 小写字母 |
| [:print:] | 可打印字符 |
| [:punct:] | 标点符号字符 |
| [:space:] | 空白字符，包括垂直制表符 |
| [:upper:] | 大写字母 |
| [:xdigit:] | 十六进制数字 |

另外，如果指定了用于扩展匹配的 `-E` 选项，那些用于控制匹配完成的其他字符可能会遵循正则表达式的规则（见表2-19）。对于 `grep` 命令来说，我们还需要在这些字符之前加上 `\` 字符。

| 选　　项 | 含　　义 |
| :---- | :---- |
| ? | 匹配是可选的，但最多匹配一次 |
| * | 必须匹配 0 次或多次 |
| + | 必须匹配 1 次或多次 |
| {n} | 必须匹配 n 次 |
| {n,} | 必须匹配 n 次或 n 次以上 |
| {n,m} | 匹配次数在 n 到 m 之间，包括 n 和 m |

1. 我们的第一个例子是查找以字母 e 结尾的行。你可能会猜到需要使用特殊字符 \$，如下所示：

   ```shell
   $ grep e$ words2.txt
   Art thou not, fatal vision, sensible
   I see thee yet, in form as palpable
   Nature seems dead, and wicked dreams abuse 
   $
   ```

2. 现在假设想要查找以字母a结尾的单词。要完成这一任务，你需要使用方括号括起的特殊匹配字符。在本例中，你将使用的是[[:blank:]]，它用来测试空格或制表符：

   ```shell
   $ grep a[[:blank:]] words2.txt
   Is this a dagger which I see before me,
   A dagger of the mind, a false creation,
   Moves like a ghost. Thou sure and firm- set earth,
   $
   ```

3. 下面我们来查找以Th开头的由3个字母组成的单词。在本例中，你既需要使用[[:space:]]来划定单词的结尾，还需要用字符（.）来匹配一个额外的字符：

   ```shell
   $ grep Th.[[:space:]] words2.txt
   The handle toward my hand? Come, let me clutch thee.
   The curtain' d sleep; witchcraft celebrates
   Thy very stones prate of my whereabout,
   $
   ```

4. 最后，我们用扩展 `grep` 模式来搜索只有 10 个字符长的全部由小写字母组成的单词。我们通过指定一个匹配字母 a 到 z 的字符范围和一个重复 10 次的匹配来完成这一任务：

   ```shell
   $ grep -E [a-z]\{10\} words2.txt 
   Proceeding from the heat- oppressed brain?
   And such an instrument I was to use.
   The curtain' d sleep; witchcraft celebrates
   Thy very stones prate of my whereabout,
   $
   ```

### 6. 命令的执行

编写脚本程序时，你经常需要捕获一条命令的执行结果，并把它用在 shell 脚本程序中。也就是说，你想要执行一条命令，并把该命令的输出放到一个变量中。你可以用在本章前面 `set` 命令示例中介绍的`$(command)` 语法来实现，也可以用一种比较老的语法形式 `command`，这种用法目前依然很常见。

所有的新脚本程序都应该使用 `\$(...)` 形式，引入这一形式的目的是为了避免在使用反引号执行命令时，处理其内部的\$、`、\ 等字符所需要应用的相当复杂的规则。如果在反引号`...`结构中需要用到反引号，它就必须通过 \\ 字符进行转义。这些相对晦涩的字符往往会让程序员感到困惑，有时即使是经验丰富的 shell 脚本程序员也必须反复进行实验，才能确保在反引号命令中引号的使用不会出错。

`$(command)` 的结果就是其中命令的输出。注意，这不是该命令的退出状态，而是它的字符串形式的输出结果。例如：

```shell
#!/bin/sh

echo The current directory is $PWD
echo The current users are $(who)

exit 0
```

如果想要将命令的结果放到一个变量中，你可以按通常的方法来给它赋值，如下所示：

```shell
whoisthere=$(who)
echo $whoisthere
```

很容易。如果需要把一条命令在标准输出上的输出转换为一组参数，并且将它们用做为另一个程序的参数，你会发现命令 `xargs` 可以帮你完成这一工作。

#### 6.1 算术扩展

我们已经介绍过 `expr` 命令，通过它可以处理一些简单的算术命令，但这个命令执行起来相当慢，因为它需要调用一个新的shell来处理expr命令。一种更新更好的办法是使用 `$((...))` 扩展。把你准备求值的表达式括在 `$((...))` 中能够更有效地完成简单的算术运算。如下所示：

```shell
#!/bin/sh

x=0
while [ "$x" -ne 10 ]; do
	echo $x
	x=$(($x + 1))
done

exit 0
```

> 注意，这与 `x=\$(...)` 命令不同，两对圆括号用于算术替换，而我们之前见到的一对圆括号用于命令的执行和获取输出。

#### 6.2 参数扩展

你已经见过形式最简单的参数赋值和扩展了，如下所示：

```shell
foo=fred
echo $foo
```

但当你想在变量名后附加额外的字符时就会遇到问题。假设你想编写一个简短的脚本程序，来处理名为1_tmp 和 2_tmp 的两个文件。你可能会这样写：

```shell
#!/bin/sh

for i in 1 2
do
	my_secret_process $i_tmp
done
```

但是在每次循环中，你都会看到如下所示的出错信息：

```shell
my_secret_process: too few arguments
```

为了保护变量名中类似于 `$i` 部分的扩展，你需要把i放在花括号中，如下所示：

```shell
#!/bin/sh

for i in 1 2
do
	my_secret_process ${i}_tmp
done
```

你可以在 shell 中采用多种参数替换方法。对于多参数处理问题来说，这些方法通常会提供一种精巧的解决方案。表 2-20 列出了一些常见的参数扩展方法。

| 参数扩展 | 说　　明 |
| :---- | :---- |
| \${param:-default} | 如果 param 为空，就把它设置为 default 的值 |
| \${#param} | 给出 param 的长度 |
| ${param%word} | 从 param 的尾部开始删除与 word 匹配的最小部分，然后返回剩余部分 |
| \${param%%word} | 从 param 的尾部开始删除与 word 匹配的最长部分，然后返回剩余部分 |
| \${param#word} | 从 param 的头部开始删除与 word 匹配的最小部分，然后返回剩余部分 |
| \${param##word} | 从 param 的头部开始删除与 word 匹配的最长部分，然后返回剩余部分 |

**实验　参数的处理**

```shell
#!/bin/sh

unset foo
echo ${foo:-bar}

foo=fud
echo ${foo:-bar}

foo=/usr/bin/X11/startx
echo ${foo#*/}
echo ${foo##*/}

bar=/usr/local/etc/local/networks
echo ${bar%local*}
echo ${bar%%local*}

exit 0
```

它的输出结果如下：

```shell
bar
fud
usr/bin/X11/startx
startx
/usr/local/etc/
/usr/
```

#### 6.7 here 文档

在 shell 脚本程序中向一条命令传递输入的一种特殊方法是使用 here 文档。它允许一条命令在获得输入数据时就好像是在读取一个文件或键盘一样，而实际上是从脚本程序中得到输入数据。

here 文档以两个连续的小于号 `<<` 开始，紧跟着一个特殊的字符序列，该序列将在文档的结尾处再次出现。`<<` 是 shell 的标签重定向符，在这里，它强制命令的输入是一个 here 文档。这个特殊字符序列的作用就像一个标记，它告诉 shell here 文档结束的位置。因为这个标记序列不能出现在传递给命令的文档内容中，所以应该尽量使它既容易记忆又相当不寻常。

**实验　使用 here 文档**

```shell
#!/bin/sh

cat <<!FUNKY!
hello
this is a here
document
!FUNKY!
```

它的输出如下所示：

```shell
hello
this is a here
document
```

**实验　here 文档的另一个用法**

1. 我们从名为 a_text_file 的文件开始，它的内容如下所示：

   ```txt
   That is line 1
   That is line 2
   That is line 3
   That is line 4
   ```

2. 你可以通过结合使用here文档和ed编辑器来编辑这个文件：

   ```shell
   #!/bin/sh
   
   ed a_text_file <<!FunkyStuff!
   3
   d
   ., \$s/ is/ was/
   w
   q
   !FunkyStuff!
   
   exit 0
   ```

运行这个脚本程序，现在这个文件的内容是：

```console
That is line 1
That is line 2
That was line 4
```

**实验解析**

这个脚本程序只是调用 `ed` 编辑器并向它传递命令，先让它移动到第三行，然后删除该行，再把当前行（因为第三行刚刚被删除了，所以当前行现在就是原来的最后一行，即第四行）中的 is 替换为 was。完成这些操作的 `ed` 命令来自脚本程序中的 here 文档——在标记 `!FunkyStuff!` 之间的那些内容。

> 注意，我们在 here 文档中用 `\` 字符来防止 `$` 字符被 shell 扩展。`\` 字符的作用是对 `$` 进行转义，让 shell 知道不要尝试把 `$s/is/was/` 扩展为它的值，而它也确实没有值。shell 把 `\$` 传递为 `$` ，再由 `ed` 编辑器对它进行解释。
>

### 8. 调试脚本程序

出现错误时，`shell` 一般都会打印出包含错误的行的行号。如果这个错误并不是非常明显，你可以添加一些额外的 `echo` 语句来显示变量的内容，也可以通过在 `shell` 中交互式地输入代码片段来对它们进行测试。

因为脚本程序是解释执行的，所以在脚本程序的修改和重试过程中没有编译方面的额外开支。跟踪脚本程序中复杂错误的主要方法是设置各种 `shell` 选项。为此，你可以在调用 `shell` 时加上命令行选项，或是使用 `set` 命令。表 2-21 列出列出了各种选项。

| 命令行选项 | set选项 | 说　　明 |
| :---- | :---- | ----- |
| sh –n \<script> | set –o noexec<br/>set -n | 只检查语法错误，不执行命令 |
| sh –v \<script> | set –o verbose<br/>set –v | 在执行命令之前回显它们 |
| sh –x \<script> | set –o xtrace<br/>set –x | 在处理完命令之后回显它们 |
| sh –u \<script> | set –o nounset<br/>set –u | 如果使用了未定义的变量，就给出出错消息 |

你可以用 `-o` 选项启用 `set` 命令的选项标志，用+o选项取消设置，对简写版本也是一样的处理方法。你可以通过使用 `xtrace` 选项来得到一份简单的执行跟踪报告。在调试的初始阶段，你可以先使用命令行选项的方法，但如果想获得更好的调试效果，你可以将 `xtrace` 标志（用来启用或关闭执行命令的跟踪）放到脚本程序中问题代码的前后。执行跟踪功能让 `shell` 在执行每行语句之前，先输出该行并对该行中变量进行扩展。

使用下面的命令来启用 xtrace 选项：

```shell
set -o xtrace
```

再用下面的命令来关闭 xtrace 选项：

```shell
set +o xtrace
```

在 shell 中，你还可以通过捕获 EXIT 信号，从而在脚本程序退出时查看到程序的状态。具体做法是在脚本程序的开始处添加类似下面这样的一条语句：

```shell
trap 'echo Exiting: critical variable = $critical_variable' EXIT
```

