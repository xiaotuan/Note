你可能认为删除 HTML 标签的办法就是查找以小于号（`<`）开头、大于号（`>`）结尾且其中有数据的文本字符串：

```shell
s/<.*>//g
```

很遗憾，这个命令会出现一些意料之外的结果：

```shell
$ cat data1.txt
<html>
<head>
<title>This is the page title</title>
</head>
<body>
<p>
This is the <b>first</b> line in the Web page.
This should provide some <i>useful</i>
information to use in our sed script.
</body>
</html>
$ sed 's/<.*>//g' data1.txt






This is the  line in the Web page.
This should provide some 
information to use in our sed script.

```

注意，标题文本以及加粗和倾斜的文本都不见了。`sed` 编辑器将这个脚本忠实地理解为小于号和大于号之间的任何文本，且包括其他的小于号和大于号。每次文本出现在 HTML 标签中（比如`<b>first</b>b>`），这个 `sed` 脚本都会删掉整个文本。

这个问题的解决办法是让 `sed` 编辑器忽略掉任何嵌入到原始标签中的大于号。要这么做的话，你可以创建一个字符组来排除大于号。脚本改为：

```shell
s/<[^>]*>//g
```

这个脚本能够正常工作了：

```shell
$ sed 's/<[^>]*>//g' data1.txt


This is the page title



This is the first line in the Web page.
This should provide some useful
information to use in our sed script.

```

要想看起来更清晰一些，可以加一条删除命令来删除多余的空白行：

```shell
$ sed 's/<[^>]*>//g ; /^$/d' data1.txt
This is the page title
This is the first line in the Web page.
This should provide some useful
information to use in our sed script.
```

