可以使用 `strace` 命令去跟踪执行某个命令时的磁盘访问：

```shell
$ strace -e 'trace=file' git status
...
stat(".git", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
lstat(".git/commondir", 0x7ffe03bb1d20) = -1 ENOENT (No such file or directory)
lstat(".git/HEAD", {st_mode=S_IFREG|0664, st_size=23, ...}) = 0
open(".git/HEAD", O_RDONLY)             = 3
lstat(".git/refs/heads/master", 0x7ffe03bb1d50) = -1 ENOENT (No such file or directory)
...
```

> 提示：Mac OS X 可以使用 `dtruss` 命令。
