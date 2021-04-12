### A.4 REDIS_CMD_RANDOM

当一个脚本执行了拥有 REDIS_CMD_RANDOM 属性的命令后，就不能执行拥有REDIS_CMD_WRITE属性的命令了（见6.4.2节介绍）。

拥有REDIS_CMD_RANDOM的命令如下：

```shell
SPOP
SRANDMEMBER
RANDOMKEY
TIME

```

