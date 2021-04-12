## 5.1　Docker引擎——简介

Docker 引擎是用来运行和管理容器的核心软件。通常人们会简单地将其代指为 Docker或Docker平台。如果有读者对VMware略知一二，那么可以将Docker引擎理解为ESXi的角色。

基于开放容器计划（OCI）相关标准的要求，Docker引擎采用了模块化的设计原则，其组件是可替换的。

从多个角度来看，Docker引擎就像汽车引擎——二者都是模块化的，并且由许多可交换的部件组成。

+ 汽车引擎由许多专用的部件协同工作，从而使汽车可以行驶，例如进气管、节气门、气缸、火花塞、排气管等。
+ Docker引擎由许多专用的工具协同工作，从而可以创建和运行容器，例如API、执行驱动、运行时、shim进程等。

至本书撰写时，Docker引擎由如下主要的组件构成：Docker客户端（Docker Client）、Docker守护进程（Docker daemon）、containerd以及runc。它们共同负责容器的创建和运行。

总体逻辑如图5.1所示。

![19.png](./images/19.png)
<center class="my_markdown"><b class="my_markdown">图5.1　Docker总体逻辑</b></center>

本书中，当提到 `runc` 和 `containerd` 时，将一律使用小写的“r”和“c”。

