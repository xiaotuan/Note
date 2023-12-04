`uname` 命令格式如下：

```shell
uname [选项]
```

可选的选项参数如下：

+ `-r`：列出当前系统的具体内核版本号。
+ `-s`：列出系统内核名称。
+ `-o`：列出系统信息。

例如：

```shell
xiaotuan@xiaotuan:~$ uname
Linux
xiaotuan@xiaotuan:~$ uname -r
4.15.0-142-generic
xiaotuan@xiaotuan:~$ uname -s
Linux
xiaotuan@xiaotuan:~$ uname -o
GNU/Linux
```

