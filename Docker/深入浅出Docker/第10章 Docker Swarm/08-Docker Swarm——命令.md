## 10.3　Docker Swarm——命令

+ `docker swarm init` 命令用户创建一个新的Swarm。执行该命令的节点会成为第一个管理节点，并且会切换到Swarm模式。
+ `docker swarm join-token` 命令用于查询加入管理节点和工作节点到现有Swarm时所使用的命令和Token。要获取新增管理节点的命令，请执行 `docker swarm join-token manager` 命令；要获取新增工作节点的命令，请执行 `docker swarm join-token worker` 命令。
+ `docker node ls` 命令用于列出Swarm中的所有节点及相关信息，包括哪些是管理节点、哪个是主管理节点。
+ `docker service create` 命令用于创建一个新服务。
+ `docker service ls` 命令用于列出Swarm中运行的服务，以及诸如服务状态、服务副本等基本信息。
+ `docker service ps <service>` 命令会给出更多关于某个服务副本的信息。
+ `docker service inspect` 命令用于获取关于服务的详尽信息。附加 `--pretty` 参数可限制仅显示重要信息。
+ `docker service scale` 命令用于对服务副本个数进行增减。
+ `docker service update` 命令用于对运行中的服务的属性进行变更。
+ `docker service logs` 命令用于查看服务的日志。
+ `docker service rm` 命令用于从Swarm中删除某服务。该命令会在不做确认的情况下删除服务的所有副本，所以使用时应保持警惕。

