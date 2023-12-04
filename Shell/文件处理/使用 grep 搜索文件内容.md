`grep` 命令用于查找包含指定关键字的文件，如果发现某个文件的内容包含所指定的关键字，`grep` 命令就会把包含指定关键字的这一行标记出来，`grep` 命令格式如下：

```shell
grep [参数] 关键字 文件列表
```

`grep` 命令一次只能查一个关键字，主要参数如下：

+ `-b`：在显示符合关键字的那一列前，标记该列第 1 个字符的位编号。
+ `-c`：计算符合关键字的列数。
+ `-d <进行动作>`：当指定要查找的目录而非文件时，必须使用此参数！否则 `grep` 指令将回报信息并停止搜索。
+ `-i`：忽略字符大小写。
+ `-v`：反转查找，只显示不匹配的行。
+ `-r`：在指定目录中递归查找。

例如：

```shell
$ grep -ir "Ubuntu" /usr
/usr/share/python-apt/templates/Ubuntu.mirrors:mirror://mirrors.ubuntu.com/mirrors.txt
/usr/share/python-apt/templates/Ubuntu.mirrors:https://al.mirror.kumi.systems/ubuntu/
/usr/share/python-apt/templates/Ubuntu.mirrors:http://mirrors.asnet.am/ubuntu/
/usr/share/python-apt/templates/Ubuntu.mirrors:http://mirrors.eze.sysarmy.com/ubuntu/
......
```

