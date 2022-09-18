[toc]

### 1. 更多的替换选项

#### 1.1 替换标记

可以使用 `s` 命令在行中替换文本：

```shell
$ cat data3.txt 
This is a test of the test script.
This is the second test of the test script.
$ sed 's/test/trial/' data3.txt
This is a trial of the test script.
This is the second trial of the test script.
```

替换命令在替换多行中的文本时能正常工作，但默认情况下它只替换每行中出现的第一处。要让替换命令能够替换一行中不同地方出现的文本必须使用**替换标记**。替换标记会在替换命令字符串之后设置：

```shell
s/pattern/replacement/flags
```

有 4 种可用的替换标记：

+ 数字，表明新文本将替换第几处模式匹配的地方；
+ g，表明新文本将会替换所有匹配的文本；
+ p，表明原先行的内容要打印出来；
+ w file，将替换的结果写到文件中。

```shell
$ sed 's/test/trial/2' data3.txt
This is a test of the trial script.
This is the second test of the trial script.
```

`p` 替换标记会打印与替换命令中指定的模式匹配的行。这通常会和 `sed` 的 `-n` 选项一起使用。

```shell
$ cat data3.txt
This is a test line.
This is a different line.
$ sed -n 's/test/trial/p' data3.txt
This is a trial line.
```

`-n` 选项将禁止 `sed` 编辑器输出。但 `p` 替换标记会输出修改过的行。将二者配合使用的效果就是只输出被替换命令修改过的行。

`w` 替换标记会产生同样的输出，不过会将输出保存到指定文件中。

```shell
$ sed 's/test/trial/w test.txt' data3.txt
This is a trial line.
This is a different line.
$ cat test.txt
This is a trial line.
```

`sed` 编辑器的正常输出是在 STDOUT 中，而只有那些包含匹配模式的行才会保存在指定的输出文件中。

#### 2. 替换字符

替换文件中的路径名会比较麻烦。比如，如果想用 C shell 替换 `/etc/passwd` 文件中的 bash shell，必须这么做：

```shell
$ sed 's/\/bin\/bash/\/bin\/csh/' /etc/passwd
```

由于正斜线通常用作字符串分隔符，因而如果它出现在了模式文本中的话，必须用反斜线来转义。

`sed` 编辑器允许选择其他字符来作为替换命令中的字符串分隔符：

```shell
$ sed 's!/bin/bash!/bin/csh!' /etc/passwd
```

### 2. 使用地址

默认情况下，在 `sed` 编辑器中使用的命令会作用于文本数据的所有行。如果只想将命令作用于特定行或某些行，则必须用**行寻址**。

在 `sed` 编辑器中有两种形式的行寻址：

+ 以数字形式表示行区间。
+ 用文本模式来过滤出行。

两种形式都使用相同的格式来指定地址：

```shell
[address]command
```

也可以将特定地址的多个命令分组：

```shell
address {
	command1
	command2
	command3
}
```

#### 1. 数字方式的行寻址

当使用数字方式的行寻址时，可以用行在文本流中的位置来引用。`sed` 编辑器会将文本流中的第一行编号为 1，然后继续按顺序为接下来的行分配行号。

在命令中指定的地址可以是单个行号，或是用起始行号、逗号以及结尾行号指定的一定区间范围内的行。

```shell
$ sed '2s/dog/cat/' data1.txt
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
```

也可以使用行地址区间：

```shell
$ sed '2,3s/dog/cat/' data1.txt
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
```

如果想将命令作用到文本中从某行开始的所有行，可以用特殊地址——美元符：

```shell
$ sed '2,$s/dog/cat/' data1.txt
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
```

#### 2.2 使用文本模式过滤器

`sed` 编辑器允许指定文本模式来过滤出命令要作用的行。格式如下：

```shell
/pattern/command
```

必须用正斜线将要指定的 pattern 封起来。`sed` 编辑器会将该命令作用到包含指定文本模式的行上。

```shell
$ sed '/xiaotuan/s/bash/csh/' /etc/passwd
```

`sed` 编辑器在文本模式中采用了一种称为**正则表达式**的特性来帮助你创建匹配效果更好的模式。

#### 2.3 命令组合

如果需要在单行上执行多条命令组合在一起。`sed` 编辑器会处理地址行处列出的每条命令。

```shell
$ sed '2{
> s/fox/elephant/
> s/dog/cat/
> }' data1.txt
The quick brown fox jumps over the lazy dog.
The quick brown elephant jumps over the lazy cat.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
```

### 3. 删除行

文本替换命令不是 `sed` 编辑器唯一的命令。如果需要删除文本流中的特定行，可以用删除命令。

删除命令 `d` 名副其实，它会删除匹配指定寻址模式的所有行。使用该命令时要特别小心，如果你忘记加入寻址模式的话，流中的所有文本行都会被删除。

```shell
$ cat data1.txt
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
$ sed 'd' data1.txt
```

当和指定地址一起使用时，删除命令显然能发挥出最大的功用。可以从数据流中删除特定的文本行，通过行号指定：

```shell
$ cat data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
$ sed '3d' data3.txt
This is line number 1.
This is line number 2.
This is line number 4.
```

或者通过特定行区间指定：

```shell
$ sed '2,3d' data3.txt
This is line number 1.
This is line number 4.
```

或者通过特殊的文件结尾字符：

```shell
$ sed '3,$d' data3.txt
This is line number 1.
This is line number 2.
```

`sed` 编辑器的模式匹配特性也适用于删除命令：

```shell
$ sed '/number 1/d' data3.txt
This is line number 2.
This is line number 3.
This is line number 4.
```

> 提示：`sed` 编辑器不会删除原始文件。你删除的行只是从 `sed` 编辑器的输出中小时了。原始文件仍然包含那些 ”删掉的“ 行。

也可以使用两个文本模式来删除某个区间内的行，但这么做时要小心。你指定的第一个模式会 "打开" 行删除功能，第二个模式会 "关闭" 行删除功能。`sed` 编辑器会删除两个指定行之间的所有行（包括指定的行）。

```shell
$ sed '/1/,/3/d' data3.txt
This is line number 4.
```

除此之外，你要特别小心，因为只要 `sed` 编辑器在数据流中匹配到了开始模式，删除功能就会打开。这可能会导致意外的结果。

```shell
$ cat data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
$ sed '/1/,/3/d' data3.txt
This is line number 4.
```

第二个出现数字 "1" 的行再次触发了删除命令，因为没有找到停止模式，所以就将数据流中的剩余行全部删除了。当然，如果你指定了一个从未在文本中出现的停止模式，显然会出现另外一个问题。

```shell
$ sed '/1/,/5/d' data3.txt
```

因为删除功能的匹配到第一个模式的时候打开了，但一直没匹配到结束模式，所以整个数据流都被删掉了。

### 4. 插入和附加文本

`sed` 编辑器允许向数据流插入和附加文本行。两个操作的区别可能比较让人费解：

+ 插入命令 `i` 会在指定行前增加一个新行；
+ 附加命令 `a` 会在指定行后增加一个新行。

这两条命令的费解之处在于它们的格式。它们不能在命令行上使用。你必须指定是要将行插入还是附加到另一行。格式如下：

```shell
sed '[address]command\
new line'
```

new line 中的文本将会出现在 `sed` 编辑器输出中你指定的位置。记住，当使用插入命令时，文本会出现在数据流文本的前面。

```shell
$ echo "Test Line 2" | sed 'i\Test Line 1'
Test Line 1
Test Line 2
```

当使用附加命令时，文本会出现在数据流文本的后面：

```shell
$ echo "Text Line 2" | sed 'a\Test Line 1'
Text Line 2
Test Line 1
```

要向数据流行内部插入或附加数据，你必须寻址来告诉 `sed` 编辑器你想让数据出现在什么位置。可以在用这些命令时只指定一个行地址。可以匹配一个数字行号或文本模式，但不能用地址区间。这合乎逻辑，因为你只能将文本插入或附加到单个行的前面或后面，而不是行区间的前面或后面。

```shell
$ sed '3i\This is an inserted line.' data3.txt
This is line number 1.
This is line number 2.
This is an inserted line.
This is line number 3.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
```

如果你有一个多行数据流，想要将新行附加到数据流的末尾，只要用代表数据最后一行的美元符就可以了：

```shell
$ sed '$a\This is a new line of text.' data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
This is a new line of text.
```

要插入或附加多行文本，就必须对要插入或附加的新文本中的每一行使用反斜线，直到最后一行：

```shell
$ sed '1i\
> This is one line of new text.\
> This is another line of new text.' data3.txt
This is one line of new text.
This is another line of new text.
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
```

### 5. 修改行

修改命令允许修改数据流中整行文件的内容。它跟插入和附加命令的工作机制一样，你必须在 `sed` 经理中单独指定新行。

```shell
$ sed '3c\This is a changed line of text.' data3.txt
This is line number 1.
This is line number 2.
This is a changed line of text.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
```

也可以用文本模式来寻址：

```shell
$ sed '/number 3/c\This is a changed line of text.' data3.txt
This is line number 1.
This is line number 2.
This is a changed line of text.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
```

文本模式修改命令会修改它匹配的数据流中的任意文本行。

```shell
$ sed '/number 1/c\
> This is a changed line of text.' data3.txt
This is a changed line of text.
This is line number 2.
This is line number 3.
This is line number 4.
This is a changed line of text.
This is text you want to keep.
```

你可以在修改命令中使用地址区间，但结果未必如愿：

```shell
$ sed '2,3c\
> This is a new line of text.' data3.txt
This is line number 1.
This is a new line of text.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
```

`sed` 编辑器会用这一行文本来替换数据流中的两行文本，而不是逐一修改这两行文本。

### 6. 转换命令

转换命令（`y`）是唯一可以处理单个字符的 `sed` 编辑器命令。转换命令格式如下：

```
[address]y/inchars/outchars/
```

转换命令会对 inchars 和 outchars 值进行一对一的映射。inchars 中的第一个字符会被转换为 outchars 中的第一个字符，第二个字符会被转换成 outchars 中的第二个字符。这个映射过程会一直持续到处理完指定字符。如果 inchars 和 outchars 的长度不同，则 `sed` 编辑器会产生一条错误消息。

```shell
$ cat data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
This is line number 1 again.
This is text you want to keep.
This the last line in the file.
$ sed 'y/123/789/' data3.txt
This is line number 7.
This is line number 8.
This is line number 9.
This is line number 4.
This is line number 7 again.
This is text you want to keep.
This the last line in the file.
```

转换命令是一个全局命令，也就是说，它会将文本行中找到的所有指定字符自动进行转换，而不会考虑它们出现的位置。

```shell
$ echo "This 1 is a test of 1 try." | sed 'y/123/456/'
This 4 is a test of 4 try.
```

### 7 回顾打印

另外有 3 个命令也能用来打印数据流中的信息：

+ `p` 命令用来打印文本行；
+ 等号（`=`）命令用来打印行号；
+ `l`（小写的 L）命令用来列出行。

#### 7.1 打印行

`p` 命令可以打印 `sed` 编辑器输出中的一行。如果只用这个命令，也没有什么特别的。

```shell
$ echo "this is a test" | sed 'p'
this is a test
this is a test
```

打印命令最常见的用法是打印包含匹配文本模式的行：

```shell
$ cat data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
$ sed -n '/number 3/p' data3.txt
This is line number 3.
```

在命令行上用 `-n` 选项，你可以禁止输出其他行，只打印包含匹配文本模式的行。

也可以用它来快速打印数据流中的某些行。

```shell
$ sed -n '2,3p' data3.txt
This is line number 2.
This is line number 3.
```

如果需要在修改之前查看行，也可以使用打印命令，比如与替换或修改命令一起使用。可以创建一个脚本在修改行之前显示该行。

```shell
$ sed -n '/3/{
> p
> s/line/test/p
> }' data3.txt
This is line number 3.
This is test number 3.
```

`sed` 编辑器命令会查找包含数字 3 的行，然后执行两条命令。首选，脚本用 `p` 命令来打印出原始行；然后它用 `s` 命令替换文本，并用 `p` 标记打印替换结果。输出同时显示了原来的行文本和新的行文本。

#### 7.2 打印行号

等号命令会打印行在数据流中的当前行号。

```shell
$ cat data1.txt
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
$ sed '=' data1.txt
1
The quick brown fox jumps over the lazy dog.
2
The quick brown fox jumps over the lazy dog.
3
The quick brown fox jumps over the lazy dog.
4
The quick brown fox jumps over the lazy dog.
5
The quick brown fox jumps over the lazy dog.
```

如果你要在数据流中查找特定文本模式的话，等号命令用起来非常方便。

```shell
$ sed -n '/number 4/{=;p;}' data3.txt
4
This is line number 4
```

#### 7.3 列出行

列出命令（`l`）可以打印数据流中的文本和不可打印的 ASCII 字符。任何不可打印字符要么在其八进制值前加一个反斜线，要么使用标准 C风格的命名法（用于常见的不可打印字符），比如 `\t`，来代表制表符。

```shell
$ cat data2.txt
This	line	contains	tabs.
$ sed -n 'l' data2.txt
This\tline\tcontains\ttabs.$
```

制表符的位置使用 `\t` 来显示。行尾的美元符表示换行符。如果数据流包含了转义字符，列出命令会在必要时候用八进制来显示。

### 8. 使用 sed 处理文件

#### 8.1 写入文件

`w` 命令用来向文件写入行。该命令的格式如下：

```shell
[address]w filename
```

filename 可以使用相对路径或绝对路径，当不管哪种，运行 `sed` 编辑器的用户都必须有文件的写权限。地址可以是 `sed` 中支持的任意类型的寻址方式，例如单个行号、文本模式、

行区间或文本模式。

```shell
$ sed '1,2w test.txt' data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
$ cat test.txt
This is line number 1.
This is line number 2.
```

当然，如果你不想让行显示到 STDOUT 上，你可以用 `sed` 命令的 `-n` 选项。

#### 8.2 从文件读取数据

读取命令（`r`）允许你将一个独立文件中的数据插入到数据流中。读取命令的格式如下：

```shell
[address]r filename
```

filename 参数指定了数据文件的绝对路径或相对路径。你在读取命令中使用地址区间，只能指定单独一个行号或文本模式地址。`sed` 编辑器会将文件中的文本插入到指定地址后。

```shell
$ cat data2.txt
This is an added line.
This is the second added line.
$ sed '3r data2.txt' data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is an added line.
This is the second added line.
This is line number 4.
```

`sed` 编辑器会将数据文件中的所有文本行都插入到数据流中。

```shell
$ sed '/number 2/r data2.txt' data3.txt
This is line number 1.
This is line number 2.
This is an added line.
This is the second added line.
This is line number 3.
This is line number 4.
```

如果你要在数据流的末尾添加文本，只需用美元地址符就行了。

```shell
$ sed '$r data2.txt' data3.txt
This is line number 1.
This is line number 2.
This is line number 3.
This is line number 4.
This is an added line.
This is the second added line.
```

读取命令的另一个很酷的用法是和删除命令配合使用：利用另一个文件中的数据来替换文件中的占位文本。

```shell
$ cat notice.std
Would the follwing people:
LIST
please report to the ship's captain.
$ sed '/LIST/{
> r data11.txt
> d
> }' notice.std
Would the follwing people:
Blum, 		R Browncoat
McGuiness, 	A Alliance
Bresnahan, 	C Browncoat
Harken, 	C Alliance
please report to the ship's captain.
```

