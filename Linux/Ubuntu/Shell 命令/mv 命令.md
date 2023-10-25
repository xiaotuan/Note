`mv` 命令用于移动文件或文件夹，它的另一个作用是重命名：

```shell
xiaotuan@xiaotuan:~$ touch a.c
xiaotuan@xiaotuan:~$ ls
a.c      eclipse-workspace  phpMyAdmin  test1   模板  图片  下载  桌面
eclipse  examples.desktop   Qt5.9.0     公共的  视频  文档  音乐
xiaotuan@xiaotuan:~$ mv a.c test1/
xiaotuan@xiaotuan:~$ ls test1/
a.c
xiaotuan@xiaotuan:~$ 
```

重命名操作如下：

```shell
xiaotuan@xiaotuan:~$ touch a.c
xiaotuan@xiaotuan:~$ ls
a.c      eclipse-workspace  phpMyAdmin  公共的  视频  文档  音乐
eclipse  examples.desktop   Qt5.9.0     模板    图片  下载  桌面
xiaotuan@xiaotuan:~$ mv a.c b.c
xiaotuan@xiaotuan:~$ ls
b.c      eclipse-workspace  phpMyAdmin  公共的  视频  文档  音乐
eclipse  examples.desktop   Qt5.9.0     模板    图片  下载  桌面
xiaotuan@xiaotuan:~$ rm -rf b.c
xiaotuan@xiaotuan:~$ mkdir test
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  公共的  视频  文档  音乐
eclipse-workspace  phpMyAdmin        test     模板    图片  下载  桌面
xiaotuan@xiaotuan:~$ mv test test1
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  公共的  视频  文档  音乐
eclipse-workspace  phpMyAdmin        test1    模板    图片  下载  桌面

```

