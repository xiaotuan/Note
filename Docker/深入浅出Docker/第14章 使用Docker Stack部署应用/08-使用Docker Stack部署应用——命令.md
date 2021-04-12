## 14.3　使用Docker Stack部署应用——命令

+ `docker stsack deploy` 用于根据Stack文件（通常是 `docker-stack.yml` ）部署和更新Stack服务的命令。
+ `docker stack ls` 会列出Swarm集群中的全部Stack，包括每个Stack拥有多少服务。
+ `docker stack ps` 列出某个已经部署的Stack相关详情。该命令支持Stack名称作为其主要参数，列举了服务副本在节点的分布情况，以及期望状态和当前状态。
+ `docker stack rm` 命令用于从Swarm集群中移除Stack。移除操作执行前并不会进行二次确认。

