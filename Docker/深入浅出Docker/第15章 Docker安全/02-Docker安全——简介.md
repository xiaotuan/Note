## 15.1　Docker安全——简介

安全本质就是分层！通俗地讲，拥有更多的安全层，就能拥有更多的安全性。而Docker提供了很多安全层。图15.1展示了本章接下来会介绍的一部分安全技术。

![91.png](./images/91.png)
<center class="my_markdown"><b class="my_markdown">图15.1　Docker安全技术</b></center>

Linux Docker利用了大部分Linux通用的安全技术。这些技术包括了命名空间（Namespace）、控制组（CGroup）、系统权限（Capability），强制访问控制（MAC）系统以及安全计算（Seccomp）。对于上述每种技术，Docker都设置合理的默认值，实现了流畅的并且适度安全的开箱即用体验。同时，Docker也允许用户根据特定需求自定义调整每项安全配置。

Docker平台本身也提供了一些非常棒的原生安全技术。并且重要的是，这些技术 **使用起来都很简单！**

+ **Docker Swarm模式：** 默认是开启安全功能的。无须任何配置，就可以获得加密节点ID、双向认证、自动化CA配置、自动证书更新、加密集群存储、加密网络等安全功能。
+ **Docker内容信任（Docker Content Trust, DCT）：** 允许用户对镜像签名，并且对拉取的镜像的完整度和发布者进行验证。
+ **Docker安全扫描（Docker Security Scanning）：** 分析Docker镜像，检查已知缺陷，并提供对应的详细报告。
+ **Docker密钥：** 使安全成为Docker生态系统中重要的一环。Docker密钥存储在加密集群存储中，在容器传输过程中实时解密，使用时保存在内存文件系统，并运行了一个最小权限模型。

重要的是，要知道Docker在使用主流Linux安全技术的同时，还提供了额外的扩展以及一些新的安全技术。Linux安全技术看起来可能略为复杂，但是Docker平台的安全技术却非常简单。

