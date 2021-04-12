### A.2 REDIS_CMD_DENYOOM

拥有 REDISCMD_DENYOOM 属性的命令有可能增加 Redis 占用的存储空间，显然拥有该属性的命令都拥有 REDIS_CMD_WRITE 属性，但反之则不然。例如， `DEL` 命令拥有 REDIS CMDWRITE 属性，但其总是会减少数据库的占用空间，所以不拥有 REDIS CMD_DENYOOM属性。

当数据库占用的空间达到了配置文件中 `maxmemory` 参数指定的值且根据 `maxmemory- policy` 参数的空间释放规则无法释放空间时，Redis 会拒绝执行拥有 REDISCMD DENYOOM属性的命令。

提示

> 拥有REDIS_CMD_DENYOOM属性的命令每次调用时不一定都会使数据库的占用空间增大，只是有可能而已。例如，SET命令当新值长度小于旧值时反而会减少数据库的占用空间。但无论如何，当数据库占用空间超过限制时，Redis都会拒绝执行拥有 REDIS_CMD_DENYOOM 属性的命令，而不会分析其实际上是不是会真的增加空间占用。

拥有REDIS_CMD_DENYOOM属性的命令如下：

```shell
SET
SETNX
SETEX
PSETEX
APPEND
SETBIT
SETRANGE
INCR
DECR
RPUSH
LPUSH
RPUSHX
LPUSHX
LINSERT
BRPOPLPUSH
LSET
RPOPLPUSH
SADD
SINTERSTORE
SUNIONSTORE
SDIFFSTORE
ZADD
ZINCRBY
ZUNIONSTORE
ZINTERSTORE
HSET
HSETNX
HMSET
HINCRBY
HINCRBYFLOAT
INCRBY
DECRBY
INCRBYFLOAT
GETSET
MSET
MSETNX
SORT
RESTORE
BITOP

```

