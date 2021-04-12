### A.6 REDIS_CMD_LOADING

当 Redis 正在启动时（将数据从硬盘载入到内存中），Redis 只会执行拥有REDIS_ CMD_LOADING属性的命令。

拥有REDIS_CMD_LOADING属性的命令如下：

```shell
INFO
SUBSCRIBE
UNSUBSCRIBE
PSUBSCRIBE
PUNSUBSCRIBE
PUBLISH

```

2.6.11版本加入了 `AUTH` ，2.6.12版本加入了 `SELECT` 。



