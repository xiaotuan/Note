`rmdir` 命令用于删除文件夹，

```shell
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  公共的  视频  文档  音乐
eclipse-workspace  phpMyAdmin        text     模板    图片  下载  桌面
xiaotuan@xiaotuan:~$ rmdir text
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  模板  图片  下载  桌面
eclipse-workspace  phpMyAdmin        公共的   视频  文档  音乐
```

如果要删除的目录不为空目录，则 `rmdir` 命令将无法删除。只有将目录中的文件及其目录删除后才可以使用 `rmdir` 命令删除该目录。

```shell
xiaotuan@xiaotuan:~$ ls
eclipse            examples.desktop  Qt5.9.0  公共的  视频  文档  音乐
eclipse-workspace  phpMyAdmin        text     模板    图片  下载  桌面
xiaotuan@xiaotuan:~$ ls text/
a.c
xiaotuan@xiaotuan:~$ rmdir text
rmdir: 删除 'text' 失败: 目录非空
```

要向删除非空目录可以使用 `rm -rf` 命令：

```shell
xiaotuan@xiaotuan:~$ rm -rf text
```

