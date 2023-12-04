`cat` 命令格式如下：

```shell
cat [选项] [文件]
```

选项主要参数如下：

+ `-n`：有 1 开始对所有输出的行进行编号。
+ `-b`：和 `-n` 类似，但是不对空白行编号。
+ `-s`：当遇到连续两个行以上空白行的话就合并为一个行空白行。

例如：

```shell
xiaotuan@xiaotuan:~$ cat /etc/environment -n
     1	PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
```

