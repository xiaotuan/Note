可以使用 `ps --forest` 命令展示子 shell 间的嵌套结构：

```shell
$ ps --forest
  PID TTY          TIME CMD
50882 pts/11   00:00:00 bash
 6498 pts/11   00:00:00  \_ bash
 9925 pts/11   00:00:00      \_ ps
```

