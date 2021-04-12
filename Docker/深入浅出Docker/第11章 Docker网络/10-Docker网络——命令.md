## 11.3　Docker网络——命令

+ Docker网络有自己的子命令，主要包括以下几种。
+ `docker network ls` 用于列出运行在本地Docker主机上的全部网络。
+ `docker network create` 创建新的Docker网络。默认情况下，在Windows上会采用 `NAT` 驱动，在Linux上会采用 `Bridge` 驱动。读者可以使用 `-d` 参数指定驱动（网络类型）。 `docker network create -d overlay overnet` 会创建一个新的名为overnet的覆盖网络，其采用的驱动为 `Docker Overlay` 。
+ `docker network inspect` 提供Docker网络的详细配置信息。
+ `docker network prune` 删除Docker主机上全部未使用的网络。
+ `docker network rm` 删除Docker主机上指定网络。

