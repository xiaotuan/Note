[toc]

### 1. 基本用法

`gzip` 软件包是 GNU 项目的产物，意在编写一个能够替代原型 Unix 中 `compress` 工具的免费版本。这个软件包含有下面的工具：

+ `gzip`：用来压缩文件。
+ `gzcat`：用来查看压缩过的文本文件的内容。
+ `gunzip`：用来解压文件。

```shell
$ gzip myprog
$ ls -l my*
-rwxrwxr-x 1 rich rich 2197 2007-09-13 11:29 myprog.gz 
$
```

### 2. 批量压缩文件

`gzip` 命令会压缩你在命令行指定的文件。也可以在命令行指定多个文件名甚至用通配符来一次性批量压缩文件。

```shell
$ gzip my*
$ ls -l my*
-rwxr--r-- 1 rich rich 103 Sep 6 13:43 myprog.c.gz
-rwxr-xr-x 1 rich rich 5178 Sep 6 13:43 myprog.gz
-rwxr--r-- 1 rich rich 59 Sep 6 13:46 myscript.gz
-rwxr--r-- 1 rich rich 60 Sep 6 13:44 myscript2.gz
```

