[toc]

举个例子，如果你正在数据中查找短语 Linux System Administrators Group，它很有可能出现在两行中，每行各包含其中一部分短语。如果用普通的 `sed` 编辑器命令来处理问呗，就不可能发现这种分开的短语。

`sed` 编辑器包含了三个可用来处理多行文本的特殊命令。

+ `N`：将数据流中的下一行加进来创建一个多行组来处理。
+ `D`：删除多行组中的一行。
+ `P`：打印多行组中的一行。

### 1. next 命令

#### 1.1 单行的 next 命令

小写的 `n` 命令会告诉 `sed` 编辑器移动到数据流中的下一文本行，而不用重新回到命令的最开始再执行一遍。记住，通常 `sed` 编辑器在移动数据流中的下一文本行之前，会在当前行上执行完所有定义好的命令。单行 `next` 命令改变了这个流程。

例如你有个数据文件，共有 5 行内容，其中的两行是空的。目标是删除首行之后的空白行，而留下最后一行之前的空白行。如果写一个删除掉空白行的 `sed` 脚本，你会删掉两个空白行。

```shell
$ cat data1.txt
This is the header line.

This is a data line.

This is the last line.
$ sed '/^$/d' data1.txt
This is the header line.
This is a data line.
This is the last line.
```

解决办法是用 `n` 命令。在这个例子中，脚本要查找含有单词 header 的那一行。找到之后，`n` 命令会让 `sed` 编辑器移动到文本的下一行，也就是那个空行。

```shell
$ cat data1.txt
This is the header line.

This is a data line.

This is the last line.
$ sed '/header/{n;d}' data1.txt
This is the header line.
This is a data line.

This is the last line.
```

### 2. 合并文本行

单行 next 命令会将数据流中的下一文本行移动到 `sed` 编辑器的工作空间（称为**模式空间**）。多行版本的 next 命令（用大写 `N`）会将下一文本行添加到模式空间中已有的文本后。

这样的作用是将数据流中的两个文本行合并到同一个模式空间中。文本行仍然用换行符分隔，但 `sed` 编辑器现在会将两行文本当成一行来处理。

```shell
$ cat data1.txt 
This is the header line.
This is the first data line.
This is the second data line.
This is the last line.
$ sed '/first/{N;s/\n/ /}' data1.txt
This is the header line.
This is the first data line. This is the second data line.
This is the last line.x
```

如果要在数据文件中查找一个可能会分散在两行中的文本短语的话，这是个很实用的应用程序。

```shell
$ cat data1.txt
On Tuesday, the Linux System
Administrator's group meeting will be held.
All System Administrators should attend.
Thank you for your attendance.
$ sed 'N ; s/System.Administrator/Desktop User/' data1.txt
On Tuesday, the Linux Desktop User's group meeting will be held.
All Desktop Users should attend.
Thank you for your attendance.
```

> 注意：替换命令在 System 和 Administrator 之间用了通配符模式（`.`）来匹配空格和换行符这两种情况。但当它匹配了换行符时，它就从字符串中删掉了换行符，导致两行合并成一行。这可能不是你想要的。

要解决这个问题，可以在 `sed` 编辑器脚本中用两个替换命令：一个用来匹配短语出现在多行中的情况，一个用来匹配短语出现在单行中的情况。

```shell
$ cat data1.txt
On Tuesday, the Linux System
Administrator's group meeting will be held.
All System Administrators should attend.
Thank you for your attendance.
$ sed 'N
> s/System\nAdministrator/Desktop\nUser/
> s/System Administrator/Desktop User/
> ' data1.txt
On Tuesday, the Linux Desktop
User's group meeting will be held.
All Desktop Users should attend.
Thank you for your attendance.
```

但这个脚本中仍有个小问题。这个脚本总是在执行 `sed` 编辑器命令前将下一行文本读入到模式空间。当它到了最后一行文本时，就没有下一行可读了，所以 `N` 命令会叫 `sed` 编辑器停止。如果要匹配的文本正好在数据流的最后一行上，命令就不会发现要匹配的数据。

```shell
$ cat data1.txt
On Tuesday, the Linux System
Administrator's group meeting will be held.
All System Administrators should attend.
$ sed 'N
> s/System\nAdministrator/Desktop\nUser/
> s/System Administrator/Desktop User/
> ' data1.txt
On Tuesday, the Linux Desktop
User's group meeting will be held.
All System Administrators should attend.
```

你可以轻松地解决这个问题——将单行命令放到 `N` 命令前面，并将多行命令放到 `N` 命令后面，例如：

```shell
$ cat data1.txt
On Tuesday, the Linux System
Administrator's group meeting will be held.
All System Administrators should attend.
$ sed '
> s/System Administrator/Desktop User/
> N
> s/System\nAdministrator/Desktop\nUser/
> ' data1.txt
On Tuesday, the Linux Desktop
User's group meeting will be held.
All Desktop Users should attend.
```

### 3. 多行删除命令

`sed` 编辑器用它来删除模式空间中的当前行。但和 `N` 命令一起使用时，使用单行删除命令就要小心了。

```shell
$ sed 'N ; /System\nAdministrator/d' data1.txt
All System Administrators should attend.
```

删除命令会在不同的行中查找单词 System 和 Administrator，然后在模式空间中将两行都删掉。这未必是你想要的结果。

`sed` 编辑器提供了多行删除命令 `D`，它只删除模式空间中的第一行。该命令会删除到换行符（含换行符）为止的所有字符。

```shell
$ sed 'N ; /System\nAdministrator/D' data1.txt
Administrator's group meeting will be held.
All System Administrators should attend.
```

如果需要删掉目标数据字符串所在行的前一文本行，它能派得上用场：

```shell
$ cat data1.txt

This is the header line.
This is a data line.

This is the last line.
$ sed '/^$/{N ; /header/D}' data1.txt
This is the header line.
This is a data line.

This is the last line.
```

### 3. 多行打印命令

多行打印命令（`P`）沿用了同样的方法。它只打印多行模式空间中的第一行。这包括模式空间中直到换行符为止的所有字符。当你用 `-n` 选项来阻止脚本输出时，它和显示文本的单行 `p` 命令的用法大同小异。

```shell
$ sed -n 'N ; /System\nAdministrator/P' data1.txt
On Tuesday, the Linux System
```

多行 `P` 命令的强大之处在和 `N` 命令组合使用时才能显现出来。`D` 命令的独特之处在于强制 `sed` 编辑器返回到脚本的起始处，对同一模式空间中的内容重新执行这些命令（它不会从数据流中读取新的文本行）。在命令脚本中加入 `N` 命令，你就能单步扫过整个模式空间，将多行一起匹配。