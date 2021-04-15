### 3.2.7　飞思卡尔QorIQTM

QorIQ，读音为“core eye queue”，是飞思卡尔基于Power架构的最新技术。QorIQ家族的很多芯片都是基于e500和e500mc核心的多核处理器。目前，飞思卡尔在其官方网站<a class="my_markdown" href="['#anchor035']"><sup class="my_markdown">[5]</sup></a>上描述了QorIQ家族的3个平台。相关信息总结如下。

<a class="my_markdown" href="['#ac035']">[5]</a>　<a href="http://www.freescale.com/QorIQ</p%3E">www.freescale.com/QorIQ</a>.

P1系列包括P1011/P1020和P1013/P1022。这些处理器内含e500 Power架构核心，并且集成了一套专用外设，以面向网络、通信和控制面板等应用。它们有一个或两个核心，而且功耗相当低，大概3.5瓦特。表3-5总结了P1系列处理器的主要特性。

<center class="my_markdown"><b class="my_markdown">表3-5　飞思卡尔QorIQ P1系列产品特性</b></center>

| 特征 | P1011 | P1020 | P1013 | P1022 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 核心 | e500 | e500 | e500 | e500 |
| 时钟频率 | 高达800 MHz | 高达800 MHz | 高达1055 MHz | 高达1055 MHz |
| 核心数量 | 1 | 2 | 1 | 2 |
| USB | 2.0 | 2.0 | 2.0 | 2.0 |
| SPI控制器 | 是 | 是 | 是 | 是 |
| I<sup class="my_markdown">2</sup>C控制器 | 是 | 是 | 是 | 是 |
| 以太网 | 3个吉比特以太网 | 3个吉比特以太网 | 2个吉比特以太网 | 2个吉比特以太网 |
| DUART | 2 | 2 | 2 | 2 |
| PCI | 2个PCI Express | 2个PCI Express | 3个PCI Express | 3个PCI Express |
| SATA | — | — | 2个SATA | 2个SATA |
| 安全引擎 | 是 | 是 | 是 | 是 |
| SD/MMC | 是 | 是 | 是 | 是 |

P2系列包括P2010和P2020。这个系列的处理器同样包含一个或两个核心。它们的性能比P1系列处理器更强，核心时钟频率可以达到1.2 GHz，并且它们的片上缓存容量更大。P2系列的典型功耗为6瓦特左右。表3-6总结了P2系列处理器的主要特性。

<center class="my_markdown"><b class="my_markdown">表3-6　飞思卡尔QorIQ P2系列产品特性</b></center>

| 特征 | P2010 | P2020 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 核心 | e500 | e500 |
| 核心频率 | 高达1.2 GHz | 高达1.2 GHz |
| 核心数量 | 1 | 2 |
| USB | 2.0 | 2.0 |
| SPI控制器 | 是 | 是 |
| I<sup class="my_markdown">2</sup>C控制器 | 是 | 是 |
| 以太网 | 3个吉比特以太网 | 3个吉比特以太网 |
| DUART | 2 | 2 |
| PCI | 3个PCI Express | 3个PCI Express |
| 串行RapidIO | 两个SRIO | 两个SRIO |
| 安全引擎 | 可选 | 可选 |
| SD/MMC | 是 | 是 |

P4系列包括P4040和P4080。这个系列的处理器最多可以包含8个核心，并且它们基于专门针对多核处理器优化了的e500核心，称为e500mc。这些核心包含了对管理程序、私有背部缓存（private back-side cache）的硬件支持，并支持浮点运算。这个家族拥有一项独特技术，称为数据路径加速架构（Data Path Acceleration Architecture，DPAA），是针对超高速数据面应用而开发的。这个系列的处理器同时也包含了增强的调试和追踪功能。表3-7总结了P4系列处理器的主要特性。

<center class="my_markdown"><b class="my_markdown">表3-7　飞思卡尔QorIQ P4系列产品特性</b></center>

| 特征 | P4040 | P4080 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 核心 | e500mc | e500mc |
| 核心频率 | 高达1.5 GHz | 高达1.5 GHz |
| 核心数量 | 4 | 8 |
| USB | 两个2.0 | 两个2.0 |
| SPI控制器 | 是 | 是 |
| I<sup class="my_markdown">2</sup>C控制器 | 是 | 是 |
| 以太网 | 8个10/100/1000 | 8个10/100/1000 |
| 10吉比特以太网 | 2 | — |
| DUART | 2 | 2 |
| PCI | 3个PCI Express V2 | 3个PCI Express V2 |
| 串行RapidIO | 2 | 2 |
| 安全引擎 | 是 | 是 |
| SD/MMC | 是 | 是 |

