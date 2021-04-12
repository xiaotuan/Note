## 12.3　Docker覆盖网络——命令

+ `docker network create` 是创建新网络所使用的命令。 `-d` 参数允许用户指定所用驱动，常见的驱动是 `Overlay` 。也可以选择使用第三方驱动。对于覆盖网络，控制层默认是加密的。需要指定 `-o encrypted` 对数据层进行加密（会导致额外的性能开销）。
+ `docker network ls` 用于列出Docker主机上全部可见的容器网络。Swarm模式下的Docker主机只能看到已经接入运行中的容器的网络。这种方式保证了网络Gossip开销最小化。
+ `docker network inspect` 用于查看特定容器网络的详情。其中包括范围、驱动、IPv6、子网配置、VXLAN网络ID以及加密状态。
+ `docker network rm` 删除指定网络。

