## 10.1　Docker Swarm——简介

Docker Swarm包含两方面：一个企业级的Docker安全集群，以及一个微服务应用编排引擎。

集群方面，Swarm将一个或多个Docker节点组织起来，使得用户能够以集群方式管理它们。Swarm默认内置有加密的分布式集群存储（encrypted distributed cluster store）、加密网络（Encrypted Network）、公用TLS（Mutual TLS）、安全集群接入令牌Secure Cluster Join Token）以及一套简化数字证书管理的PKI（Public Key Infrastructure）。用户可以自如地添加或删除节点，这非常棒！

编排方面，Swarm提供了一套丰富的API使得部署和管理复杂的微服务应用变得易如反掌。通过将应用定义在声明式配置文件中，就可以使用原生的Docker命令完成部署。此外，甚至还可以执行滚动升级、回滚以及扩缩容操作，同样基于简单的命令即可完成。

以往，Docker Swarm是一个基于Docker引擎之上的独立产品。自Docker 1.12版本之后，它已经完全集成在Docker引擎中，执行一条命令即可启用。到2018年，除了原生Swarm应用，它还可以部署和管理Kubernetes应用。即便在本书撰写时，对Kubernetes应用的支持也是新特性。

