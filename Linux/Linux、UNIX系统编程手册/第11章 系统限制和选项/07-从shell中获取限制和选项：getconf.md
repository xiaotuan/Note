### 从shell中获取限制和选项：getconf

在shell中，可以使用getconf命令获取特定UNIX系统中已然实现的限制和选项。该命令的格式一般如下：



![262.png](../images/262.png)
variable-name标识用户意欲获取的限制，应是符合SUSV3标准的限制名称，例如：ARG_MAX或NAME_MAX。但凡限制与路径名相关，则还需要指定一个路径名，作为命令的第二个参数，如下第二个实例所示。



![263.png](../images/263.png)
