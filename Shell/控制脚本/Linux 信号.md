<center><b>Linux 信号</b></center>

| 信号 | 值      | 描述                           |
| ---- | ------- | ------------------------------ |
| 1    | SIGHUP  | 挂起进程                       |
| 2    | SIGINT  | 终止进程                       |
| 3    | SIGQUIT | 停止进程                       |
| 9    | SIGKILL | 无条件终止进程                 |
| 15   | SIGTERM | 尽可能终止进程                 |
| 17   | SIGSTOP | 无条件停止进程，但不是终止进程 |
| 18   | SIGTSTP | 停止或暂停进程，但不终止进程   |
| 19   | SIGCONT | 继续运行停止的进程             |

默认情况下，bash shell 会忽略收到的任何 `SIGQUIT（3）` 和 `SIGTERM（5）`信号（正因为这样，交互式 shell 才不会被意外终止）。但是 bash shell 会处理收到的 `SIGHUP（1）` 和 `SIGINT（2）` 信号。