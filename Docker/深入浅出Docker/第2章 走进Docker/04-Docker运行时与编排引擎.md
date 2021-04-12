## 2.3　Docker运行时与编排引擎

多数技术人员在谈到Docker时，主要是指Docker引擎。

Docker引擎是用于运行和编排容器的基础设施工具。有VMware管理经验的读者可以将其类比为ESXi。ESXi是运行虚拟机的核心管理程序，而Docker引擎是运行容器的核心容器运行时。

其他Docker公司或第三方的产品都是围绕Docker引擎进行开发和集成的。如图2.2所示，Docker引擎位于中心，其他产品基于Docker引擎的核心功能进行集成。

Docker引擎可以从Docker网站下载，也可以基于GitHub上的源码进行构建。无论是开源版本还是商业版本，都有Linux和Windows版本。

在本书撰写时，Docker引擎主要有两个版本：企业版（EE）和社区版（CE）。

每个季度，企业版和社区版都会发布一个稳定版本。社区版本会提供4个月的支持，而企业版本会提供12个月的支持。

社区版还会通过Edge方式发布月度版。

![10.png](./images/10.png)
<center class="my_markdown"><b class="my_markdown">图2.2　围绕Docker引擎进行开发和集成的产品</b></center>

从2017年第一季度开始，Docker版本号遵循YY.MM-xx格式，类似于Ubuntu等项目。例如，2018年6月第一次发布的社区版本为18.06.0-ce。

注：

> 2017年第一季度以前，Docker版本号遵循大版本号.小版本号的格式。采用新格式前的最后一个版本是Docker 1.13。

