`ls` 命令格式如下：

```shell
ls [选项] [路径]
```

`ls` 命令主要用于显示指定目录下的内容，列出指定目录下包含的所有的文件以及子目录，它的主要参数有：

+ `-a`：显示所有的文件以及子目录，包括以 `.` 开头的隐藏文件。
+ `-l`：显示文件的详细信息，比如文件的形态、权限、所有者、大小等信息。
+ `-t`：将文件按照创建时间排序列出。
+ `-A` 和 `-a` 一样，但是不列出 `.` （当前目录）和 `..`（父目录）。
+ `-R`：递归列出所有文件，包括子目录中的文件。

Shell 命令里面的参数是可以组合在一起用的，比如组合 `-al` 就是显示所有文件的详细信息，包括以 `.` 开头的隐藏文件：

```shell
xiaotuan@xiaotuan:~/tmp$ ls 
a  b  c
xiaotuan@xiaotuan:~/tmp$ ls -a
.  ..  a  b  c
xiaotuan@xiaotuan:~/tmp$ ls -al
总用量 8
drwxrwxr-x  2 xiaotuan xiaotuan 4096 12月  1 10:35 .
drwxr-xr-x 29 xiaotuan xiaotuan 4096 12月  1 10:35 ..
-rw-rw-r--  1 xiaotuan xiaotuan    0 12月  1 10:35 a
-rw-rw-r--  1 xiaotuan xiaotuan    0 12月  1 10:35 b
-rw-rw-r--  1 xiaotuan xiaotuan    0 12月  1 10:35 c
```

