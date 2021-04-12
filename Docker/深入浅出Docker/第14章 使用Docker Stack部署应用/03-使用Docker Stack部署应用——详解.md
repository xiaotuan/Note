## 14.2　使用Docker Stack部署应用——详解

如果了解Docker Compose，就会发现Docker Stack非常简单。事实上在许多方面，Stack一直是期望的Compose——完全集成到Docker中，并能够管理应用的整个生命周期。

从体系结构上来讲，Stack位于Docker应用层级的最顶端。Stack基于服务进行构建，而服务又基于容器，如图14.1所示。

![87.png](./images/87.png)
<center class="my_markdown"><b class="my_markdown">图14.1　AtSea商店架构图</b></center>

接下来的章节分为如下几部分。

+ 简单应用。
+ 深入分析Stack文件。
+ 部署应用。
+ 管理应用。

