[toc]

我们可以用管道将一个命令的 stdout （标准输出）重定向到另一个命令的 stdin （标准输入）。例如：

```console
$ cat foo.txt | grep "test"
```

但是，有些命令只能以命令行参数的形式接受数据，而无法通过 stdin 接受数据流。在这种情况下，我们没法用管道来提供哪些只有通过命令行参数才能提供的数据。

那就只能另辟蹊径了。该 `xargs` 命令出场了，它擅长将标准输入数据转换成命令行参数。`xargs` 能够处理 `stdin` 并将其转换为特定命令的命令行参数。`xargs` 也可以将单行或多行文本输入转换成其他格式，例如单行变多行或是多行变单行。

### 1. 预备知识

`xargs` 命令应该紧跟在管道操作符之后，以标准输入作为主要的源数据流。它使用 stdin 并通过提供命令行参数来执行其他命令。例如：

```console
command | xargs
```

### 2. 实战演练

`xargs` 命令把从 `stdin` 接收到的数据重新格式化，再将其作为参数提供给其他命令。

`xargs` 可以作为一种替代，其作用类似于 `find` 命令中的 `-exec`。下面是各种 `xargs` 命令的

+ 将多行输入转换成单行输出。

  只需要将换行符移除，再用 " "（空格）进行替代，就可以实现多行输入的转换。'\n' 被解释成一个换行符，换行符其实就是多行文本之间的定界符。利用 xargs，我们可以用空格替换掉换行符，这样就能够将多行文本转换成单行文本：

  ```console
  $ cat example.txt # 样例文件
  1 2 3 4 5 6
  7 8 9 10
  11 12
  
  $ cat example.txt | xargs
  1 2 3 4 5 6 7 8 9 10 11 12
  ```

+ 将单行输入转换成多行输出。

  指定每行最大的参数数量 n，我们可以将任何来自 `stdin` 的文本划分成多行，每行 n 个参数。每一个参数都是由 " "（空格）隔开的字符串。空格是默认的定界符。下面的方法可以将单行划分成多行：

  ```console
  $ cat example.txt | xargs -n 3
  1 2 3
  4 5 6 
  7 8 9
  10 11 12
  ```

### 3. 工作原理

可以用自己的定界符来分隔参数。用 `-d` 选项为输入指定一个定制的定界符：

```console
$ echo "splitxsplitxsplitxsplit" | xargs -d x
split split split split
```

结合 `-n` 选项，我们可以将输入划分成多行，而每行包含两个参数：

```console
$ $ echo "splitxsplitxsplitxsplit" | xargs -d x -n 2
split split
split split
```

### 4. 补充内容

我们已经从上面的例子中学到了如何将 stdin 格式化成不同的输出形式以作为参数。现在让我们来学习如何将这些参数传递给命令。

#### 4.1 读取 `stdin`，将格式化参数传递个命令

编写一个小型的定制版 echo 来更好地理解用 xargs 提供命令行参数的方法：

```shell
#!/bin/bash
# 文件名：cecho.sh

echo $*'#'
```

当参数被传递给文件 cecho.sh 后，它会将这些参数打印出来，并以 # 字符作为结尾。例如：

```console
$ ./cecho.sh arg1 arg2
arg1 arg2#
```

让我们来看下面这个问题。

+ 有一个包含着参数列表的文件（每行一个参数）。我们需要用两种方法将这些参数传递给一个命令（比如 cecho.sh）。第一种方法，需要每次提供一个参数：

  ```console
  ./cecho.sh arg1
  ./cecho.sh arg2
  ./cecho.sh arg3
  ```

  或者，每次需要提供两个或三个参数。提供两个参数时，它看起来像这样：

  ```console
  ./cecho.sh arg1 arg2
  ./cecho.sh arg3
  ```

+ 第二种方法，需要一次性提供所有的命令参数：

  ```console
  ./cecho.sh arg1 arg2 arg3
  ```

上面的问题也可以用 `xargs` 来解决。我们有一个名为 args.txt 的参数列表文件，这个文件的内容如下：

```txt
$ cat args.txt
arg1
arg2
arg3
```

就第一个问题，我们可以将这个命令执行多次，每次使用一个参数：

```console
cat args.txt | xargs -n 1 ./cecho.sh
arg1#
arg2#
arg3#
```

每次执行需要 x 个参数的命令时，使用：

```console
INPUT | xargs -n x
```

例如：

```console
$ cat args.txt | xargs -n 2 ./cecho.sh
arg1 arg2#
arg3#
```

就第二个问题，为了在执行命令时一次性提供所有的参数，可以使用：

```console
$ cat args.txt | xargs ./cecho.sh
arg1 arg2 arg3#
```

在上面的例子中，我们直接为特定的命令（例如 cecho.sh）提供命令行参数。这些参数都源于 args.txt 文件。但实际上除了它们外，我们还需要一些固定不变的命令参数。思考下面这种命令格式：

```console
$ ./cecho.sh -p arg1 -l
```

在上面的命令执行过程中，arg1 是唯一的可变内容，其余部分都保持不变。我们可以从文件（args.txt）中读取参数，并按照下面的方式提供给命令：

```console
./cecho.sh -p arg1 -l
./cecho.sh -p arg2 -l
./cecho.sh -p arg3 -l
```

`xargs` 有一个选项 `-I`，可以提供上面这种形式的命令执行序列。我们可以用 `-I` 指定替换字符串，这个字符串在 `xargs` 扩展时会被替换掉。如果将 `-I` 与 `xargs` 结合使用，对于每一个参数，命名都会被执行一次。

试试下面的用法：

```console
$ cat args.txt | xargs -I {} ./cecho.sh -p {} -l
-p arg1 -l#
-p arg2 -l#
-p arg3 -l#
```

> 使用 `-I` 的时候，命令以循环的方式执行。如果有 3 个参数，那么命令就会连同 {} 一起呗执行 3 次。在每一次执行中 {} 都会被替换为相应的参数。

#### 4.2 结合 `find` 使用 `xargs`

`xargs` 和 `find` 算是一对死党。两者结合使用可以让任务变得更轻松。不过人们通常却是以一种错误的组合方式使用它们。例如：

```console
$ find . -type f -name "*.txt" | xargs rm -f
```

这样做很危险。有时可能会删除不必要删除的文件。我们没法预测分隔 `find` 命令输出结果的定界符究竟是什么。很多文件名中都可能会包含空格符（' '），因此 `xargs` 很可能会误认为它们是定界符。

只要我们把 `find` 的输出作为 `xargs` 的输入，就必须将 `-print0` 与 `find` 结合使用，以字符串 null （'\0'）来分隔输出。

用 `find` 匹配并列出所有的 .txt 文件，然后用 `xargs` 将这些文件删除：

```console
$ find . -type f -name "*.txt" -print0 | xargs -0 rm -f
```

这样就可以删除所有的 .txt 文件。`-xargs -0` 将 `\0` 作为输入定界符。

#### 4.3 统计源代码目录中所有 C 程序文件的行数

统计所有 C 程序文件的行数是大多数程序员都会遇到的任务。完成这项任务的代码如下：

```console
$ find . -type f -name "*.c" -print0 | xargs -0 wc -l
```

> 如果你想获得有关个人源代码更多的统计信息，有个叫做 SLOCCount 的工具可以派上用场。现代 GNU/Linux 发行版一般都包含这个软件包，或者你也可以从 <http://www.dwheeler.com/sloccount/> 处下载。

#### 4.4 结合 `stdin`，巧妙运用 `while` 语句和子句 `shell`

`xargs` 只能以有限的几种方式来提供参数，而且它也不能为多组命令提供参数。要执行包含来自标准输入的多个参数的命令，有一种非常灵活的方法。包含 `while` 循环的子 shell 可以用来读取参数，然后通过一种巧妙的方式执行命令：

```console
$ cat files.txt | (while read arg; do cat $arg; done)
# 等同于 cat files.txt | xargs -I {} cat {}
```

在 `while` 循环中，可以将 `cat $arg` 替换成任意数量的命令，这样我们就可以对同一个参数执行多条命令。也可以不借助管道，将输出传递给其他命令。这个技巧能够适用于各种问题场景。子 shell 操作符内部的多个命令可作为一个整体来运行。

```console
$ cmd0 | (cmd1;cmd2;cmd3) | cmd4
```

如果 cmd1 是 `cd /`，那么就会改变子 shell 工作目录，然而这种改变仅局限于子 shell 内部。 cmd4 则完全不知道工作目录发生了变化。