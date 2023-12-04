可以使用 `ls -l` 命令来查看文件类型：

```shell
xiaotuan@xiaotuan:~/桌面$ ls -l
总用量 96
-rwxrwxr-x 1 xiaotuan xiaotuan 13656 12月  4 11:33 a.out
-rw-r--r-- 1 root     root        84 10月 23 17:22 audio.txt
-rw-r--r-- 1 root     root        81 10月  8 19:23 carinfo.txt
-rw-rw-r-- 1 xiaotuan xiaotuan  1310 12月  4 11:33 cinfish.cpp
-rw-rw-r-- 1 xiaotuan xiaotuan  1202 6月  19 10:51 color.c
-rw-rw-r-- 1 xiaotuan xiaotuan 17126 9月  12 16:32 curses_app.c
-rw-rw-r-- 1 xiaotuan xiaotuan   802 12月  4 10:16 hotel.c
-rw-rw-r-- 1 xiaotuan xiaotuan   443 8月  18 10:21 hotel.h
-rw-rw-r-- 1 xiaotuan xiaotuan   559 8月  18 11:21 loccheck.c
-rw-r--r-- 1 root     root       900 10月 23 17:22 log
drwxrwxr-x 3 xiaotuan xiaotuan  4096 11月 23 15:19 my_website
drwxrwxr-x 3 xiaotuan xiaotuan  4096 11月 23 11:17 public_html
-rw-rw-r-- 1 xiaotuan xiaotuan   188 6月  27 09:52 rewho.py
-rw-rw-r-- 1 xiaotuan xiaotuan    46 10月  8 19:56 scores.txt
-rw-rw-r-- 1 xiaotuan xiaotuan   640 9月  12 11:36 swap1.c
-rw-r--r-- 1 root     root       111 9月  12 16:33 title.cdb
-rw-rw-r-- 1 xiaotuan xiaotuan   672 8月  18 10:08 usehotel.c
```

每行最前面的符号标记了当前文件类型，比如 my_website 的第一个字符是 "d"，rewho.py 文件第一个字符是 "_"。这些字符表示的文件类型如下：

+ `-`：普通文件，一些应用程序创建的，比如文档、图片、音乐等等。
+ `d`：目录文件。
+ `c`：字符设备文件，Linux 驱动里面的字符设备驱动，比如串口设备，音频设备等。
+ `b`：块设备文件，存储设备驱动，比如硬盘、U盘等。
+ `l`：符号链接文件，相当于 Windows 下的快捷方式。
+ `s`：套接字文件。
+ `p`：管道文件，主要指 FIFO 文件。

