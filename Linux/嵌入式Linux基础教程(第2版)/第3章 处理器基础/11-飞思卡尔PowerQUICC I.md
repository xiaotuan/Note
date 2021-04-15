### 3.2.3　飞思卡尔PowerQUICC I

PowerQUICC I家族包含原来的基于Power架构实现的PowerQUICC处理器，由MPC8xx系列处理器组成。这些集成处理器运行在50~133 MHz的时钟频率上，它们的特点是拥有一个Power架构的8xx核心。PowerQUICC I家族的处理器用于ATM和以太网的边缘设备中，比如面向SOHO市场的路由器、家庭网关、ADSL和有线调制解调器等。

CPM或QUICC引擎包含两个独特强大的通信控制器。串行通信控制器（Serial Communication Controller，SCC）是一个灵活的串行接口，它可以实现很多基于串行方式进行通信的协议，包括以太网、HDLC/SDLC、AppleTalk、同步和异步UART、IrDA和其他的比特流数据。

串行管理控制器（Serial Management Controller，SMC）模块实现了一些类似的串行通信协议。包括对ISDN、串行UART、和SPI协议的支持。

结合使用这些SCC和SMC，你可以设计出灵活的I/O组合方案。内部的时分多路复用器甚至允许这些接口实现一些通道化的通信协议，比如T1和E1接口。

表3-1总结了PowerQUICC I产品线中的一小部分产品。

<center class="my_markdown"><b class="my_markdown">表3-1　飞思卡尔PowerQUICC I系列产品特性</b></center>

| 特征 | MPC850 | MPC860 | MPC875 | MPC885 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 核心 | PPC 8xx | PPC 8xx | PPC 8xx | PPC 8xx |
| 时钟频率 | 高达80 MHz | 高达80 MHz | 高达133 MHz | 高达133 MHz |
| DRAM控制器 | 是 | 是 | 是 | 是 |
| USB | 是 | 否 | 是 | 是 |
| SPI控制器 | 是 | 是 | 是 | 是 |
| I<sup class="my_markdown">2</sup>C控制器 | 是 | 是 | 是 | 是 |
| SCC控制器 | 2 | 4 | 1 | 3 |
| SMC控制器 | 2 | 2 | 1 | 1 |
| 安全引擎 | 否 | 否 | 是 | 是 |
| 专用快速以太网控制器 | 否 | 否 | 2 | 2 |

