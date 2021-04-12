### 9.2.1　Docker Compose的背景

Docker Compose的前身是Fig。Fig是一个由Orchard公司开发的强有力的工具，在当时是进行多容器管理的最佳方案。Fig是一个基于Docker的Python工具，允许用户基于一个YAML文件定义多容器应用，从而可以使用 `fig` 命令行工具进行应用的部署。Fig还可以对应用的全生命周期进行管理。

内部实现上，Fig会解析YAML文件，并通过Docker API进行应用的部署和管理。这种方式相当不错！

在2014年，Docker公司收购了Orchard公司，并将Fig更名为Docker Compose。命令行工具也从 `fig` 更名为 `docker-compose` ，并自此成为绑定在Docker引擎之上的外部工具。虽然它从未完全集成到Docker引擎中，但是仍然受到广泛关注并得到普遍使用。

直至今日，Docker Compose仍然是一个需要在Docker主机上进行安装的外部Python工具。使用它时，首先编写定义多容器（多服务）应用的YAML文件，然后将其交由 `docker-compose` 命令处理，Docker Compose就会基于Docker引擎API完成应用的部署。

下面通过实战进行介绍。

