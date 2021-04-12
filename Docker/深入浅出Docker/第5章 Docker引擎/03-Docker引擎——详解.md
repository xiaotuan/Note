## 5.2　Docker引擎——详解

Docker首次发布时，Docker引擎由两个核心组件构成：LXC和Docker daemon。

Docker daemon是单一的二进制文件，包含诸如Docker客户端、Docker API、容器运行时、镜像构建等。

LXC提供了对诸如命名空间（Namespace）和控制组（CGroup）等基础工具的操作能力，它们是基于Linux内核的容器虚拟化技术。

图5.2阐释了在Docker旧版本中，Docker daemon、LXC和操作系统之间的交互关系。

![20.png](./images/20.png)
<center class="my_markdown"><b class="my_markdown">图5.2　先前的Docker架构</b></center>

