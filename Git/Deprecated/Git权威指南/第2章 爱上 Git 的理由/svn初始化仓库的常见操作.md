（1）创建版本库。

```shell
$ svnadmin create /path/to/repos/project1
```

（2）在需要版本控制的目录下检出刚刚建立的空版本库。

```shell
$ svn checkout file:///path/to/repos/project1 .
```

（3）添加文件。

```shell
$ svn add *
$ svn ci -m "initialized"
```

（4）提交代码。

```shell
$ svn ci
```

（5）生成补丁文件。

```shell
$ svn diff -r1 > hacks.patch
```

> 注意：SVN 的补丁文件不支持二进制文件。可以通过 `svnadmin` 命令将版本库导出，例如：
>
> ```shell
> $ svnadmin dump --incremental -r2:HEAD \ /path/to/repos/project1/ > hacks.dump
> ```
>
> 