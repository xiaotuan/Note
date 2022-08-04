`kill` 命令可通过进程 ID（PID）给进程发信号。默认情况下，`kill` 命令会向命令行中列出的全部 PID 发送一个 TERM 信号。

要发送进程信号，你必须是进程的属主或登录为 root 用户。例如：

```shell
$ kill 3940
-bash: kill: (3940) - Operation not permitted
```

如果要强制终止，`-s` 参数支持指定其他信号（用信号名或信号值）。例如：

```shell
$ kill -s HUP 3940
```

要检查 `kill` 命令是否有效，可再运行 `ps` 或 `top` 命令，看看问题进程是否已停止。