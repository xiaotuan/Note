感叹号命令（`!`）用来排除命令，也就是让原本会起作用的命令不起作用。

```shell
$ sed -n '/header/!p' data1.txt
This is the first data line.
This is the second data line.
This is the last line.
```

普通 `p` 命令只打印 data1.txt 文件中包含单词 header 的那行。加了感叹号之后，情况就相反了：除了包含单词 header 那一行外，文件中其他所有的行都被打印出来了。

`sed` 编辑器无法处理数据流中最后一行文本，因为之后再没有其他行了。可以用感叹号来解决这个问题。

```shell
$ sed 'N;
> s/System\nAdministrator/Desktop\nUser/
> s/System Administrator/Desktop User/
> ' data1.txt
On Tuesday, the Linux Desktop
User's group meeting will be held.
All System Administrators should attend.
$ sed '$!N;
> s/System\nAdministrator/Desktop\nUser/
> s/System Administrator/Desktop User/
> ' data1.txt
On Tuesday, the Linux Desktop
User's group meeting will be held.
All Desktop Users should attend.
```

这个例子演示了如何配合使用感叹号与 `N` 命令以及与美元符特殊地址。美元符表示数据流中的最后一行文本，所以当 `sed` 编辑器到了最后一行时，它没有执行 `N` 命令，但它对所有其他行都执行了这个命令。

使用这种方法，你可以反转数据流中文本行的顺序。要实现这个效果（先显示最后一行，最后显示第一行），你得利用保持空间做一些特别的铺垫工作。

你得像这样使用模式空间：

（1）在模式空间中放置一行；

（2）将模式空间中的行放到保持空间中；

（3）在模式空间中放入下一行；

（4）将保持空间附加到模式空间后；

（5）将模式空间中的所有内容都放到保持空间中；

（6）重复执行第（3）~ （5）步，直到所有行都反序放到了保持空间中；

（7）提取并打印行。

下一步是决定如何保持空间文本附加到模式空间文本后面。这可以用 `G` 命令完成。唯一的问题是你不想将保持空间附加到要处理的第一行文本后面。这可以用感叹号命令轻松解决：

```shell
1!G
```

下一步就是将新的模式空间（含有已反转的行）放到保持空间，这也非常简单，只要用 `h` 命令就行了。

将模式空间中的整个数据流都反转了之后，你要做的就是打印结果。当到达数据流中的最后一行时，你就知道已经得到了模式空间的整个数据流。打印结果要用下面的命令：

```shell
$p
```

下面是完整示例：

```shell
$ cat data1.txt
This is the header line.
This is the first data line.
This is the second data line.
This is the last line.
$ sed -n '{1!G ; h ; $p }' data1.txt
This is the last line.
This is the second data line.
This is the first data line.
This is the header line.
```

> 提示：`tac` 命令会倒序显示一个文本文件。

