`rm` 命令既可以用来删除文件：

```shell
xiaotuan@xiaotuan:~$ ls
a.c  eclipse            examples.desktop  Qt5.9.0  模板  图片  下载  桌面
b.c  eclipse-workspace  phpMyAdmin        公共的   视频  文档  音乐
xiaotuan@xiaotuan:~$ rm a.c
xiaotuan@xiaotuan:~$ ls
b.c      eclipse-workspace  phpMyAdmin  公共的  视频  文档  音乐
eclipse  examples.desktop   Qt5.9.0     模板    图片  下载  桌面
```

可以使用 `-f` 参数来强制删除文件：

```shell
xiaotuan@xiaotuan:~$ rm -f b.c
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  模板  图片  下载  桌面
eclipse-workspace  phpMyAdmin        公共的   视频  文档  音乐
```

也可以用来删除目录，使用 `-rf` 参数：

```shell
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  公共的  视频  文档  音乐
eclipse-workspace  phpMyAdmin        temp     模板    图片  下载  桌面
xiaotuan@xiaotuan:~$ rm -rf temp
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  模板  图片  下载  桌面
eclipse-workspace  phpMyAdmin        公共的   视频  文档  音乐
```

