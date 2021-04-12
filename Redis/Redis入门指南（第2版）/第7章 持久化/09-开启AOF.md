### 7.2.1 开启AOF

默认情况下Redis没有开启AOF（append only file）方式的持久化，可以通过 `appendonly` 参数启用：

```shell
appendonly yes

```

开启AOF持久化后每执行一条会更改Redis中的数据的命令，Redis就会将该命令写入硬盘中的AOF文件。AOF文件的保存位置和RDB文件的位置相同，都是通过 `dir` 参数设置的，默认的文件名是appendonly.aof，可以通过 `appendfilename` 参数修改：

```shell
appendfilename appendonly.aof

```

