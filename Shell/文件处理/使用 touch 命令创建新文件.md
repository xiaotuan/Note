`touch` 命令不仅仅可以用来创建文本文档，其他类型的文档也可以创建，命令格式如下：

```shell
touch [参数] [文件名]
```

使用 `touch` 创建文件的时候，如果 `[文件名]` 的文件不存在，那就直接创建一个以 `[文件名]` 命名的文件，如果 `[文件名]` 文件存在的话就仅仅修改一下此文件的最后修改日期，常用的命令参数如下：

+ `-a`：只更改存取时间。
+ `-c`：不建立任何文件。
+ `-d <日期>`：使用指定的日期，而并非现在的日期。
+ `-t <时间>`：使用指定的时间，而非现在的时间。

例如：

```shell
xiaotuan@xiaotuan:~$ ls
eclipse            linux-stable  test1     公共的  图片  音乐
eclipse-workspace  phpMyAdmin    test.txt  模板    文档  桌面
examples.desktop   Qt5.9.0       tmp       视频    下载
xiaotuan@xiaotuan:~$ touch test
xiaotuan@xiaotuan:~$ ls test
test
xiaotuan@xiaotuan:~$ ls test -l
-rw-rw-r-- 1 xiaotuan xiaotuan 0 12月  4 17:35 test
```

