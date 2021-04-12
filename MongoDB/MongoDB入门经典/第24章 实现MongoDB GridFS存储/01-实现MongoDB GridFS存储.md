### 第24章　实现MongoDB GridFS存储

**本章介绍如下内容：**

+ 使用MongoDB GridFS存储；
+ 从控制台访问MongoDB GridFS存储；
+ 在Java中实现MongoDB GridFS存储；
+ 在PHP中实现MongoDB GridFS存储；
+ 在Python中实现MongoDB GridFS存储；
+ 在Node.js中实现MongoDB GridFS存储。

有时候，需要使用MongoDB存储和检索超过大小限制（16MB）的数据，例如，您可能存储大型图像、ZIP文件、电影等；为满足这种需求，MongoDB提供了GridFS框架。GridFS框架提供了分块存储大型文件的功能，同时让您能够通过MongoDB接口访问它们。

本章首先介绍GridFS存储的工作原理，然后探讨如何通过命令行和一些MongoDB驱动程序来使用它。有关如何通过驱动程序来使用GridFS的各节都自成一体，如果您对相关的语言不感兴趣，可跳过它们。

