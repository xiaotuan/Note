### 2.2.2　停止Redis

考虑到Redis有可能正在将内存中的数据同步到硬盘中，强行终止Redis进程可能会导致数据丢失。正确停止Redis的方式应该是向Redis发送 `SHUTDOWN` 命令，方法为：

```shell
$redis-cli SHUTDOWN

```

当Redis收到 `SHUTDOWN` 命令后，会先断开所有客户端连接，然后根据配置执行持久化，最后完成退出。

Redis可以妥善处理 `SIGTERM` 信号，所以使用 `kill Redis` 进程的 `PID` 也可以正常结束Redis，效果与发送 `SHUTDOWN` 命令一样。

