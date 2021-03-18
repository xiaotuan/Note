### 1.3.2　Java虚拟机概述

Kotlin 是一门依赖 Java 虚拟机运行的计算机语言，因此初学者有必要了解一下 Java 虚拟机的知识及其运作原理。

Java 应用程序能够跨平台运行，主要是通过 Java 虚拟机实现的。如图 1-4 所示，不同软硬件平台的 Java 虚拟机是不同的，Java 虚拟机向下是不同的操作系统和 CPU 硬件，使用或开发时需要下载不同的 JRE 或 JDK 版本；Java 虚拟机向上是 Java 应用程序，Java 虚拟机屏蔽了不同软硬件平台，Java 应用程序不需要作出任何修改，也不需要重新编译就可以直接在其他平台上运行。

![8.png](../images/8.png)
<center class="my_markdown"><b class="my_markdown">图1-4　Java 虚拟机模型</b></center>

