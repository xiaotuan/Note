`pkill` 命令和 `kill` 命令类似，不过默认情况下 `pkill` 接受的是进程名，而非进程 ID。例如：

```shell
$ pkill process_name
$ pkill -s SIGNAL process_name
```

SIGNAL 是信号编号。`pkill` 不支持信号名称。

