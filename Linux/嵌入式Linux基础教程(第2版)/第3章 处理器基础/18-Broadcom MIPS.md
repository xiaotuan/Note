### 3.2.10　Broadcom MIPS

Broadcom是业内领先的SOC（片上系统）解决方案供应商。主要面向有线电视机顶盒、有线调制解调器高清电视、无线网络、吉比特以太网和VoIP（Voice over IP）等产品市场。在这些产品领域，Broadcom公司的SOC芯片很流行。我们之前提到过，在你家里也许就运行着Linux的产品，只是你自己可能还不知道。如果你注意一下，很可能会发现Linux可能就跑在Braodcom基于MIPS的SOC芯片上。

在2000年，Broadcom收购了SiByte公司，并开始销售其通信处理器产品。这些处理器有单核、双核和四核等不同配置。Broadcom仍称它们为SiByte处理器。

单核SiByte处理器包括BCM1122和BCM1125H。它们都基于MIPS64核心，并运行在400~900 MHz的时钟频率上。它们包含了片上外设控制器，比如DDR SDRAM控制器，10/100 Mbit/s以太网，和PCI主机控制器。这两款芯片都包含了SMBus串行配置接口、PCMCIA和两个用于串行端口连接的UART。BCM1125H还包含了一个3速10/100/1000 Mbit/s的以太网控制器。这些处理器的一大特性就是它们的功耗很低。这两款芯片运行在400 MHz的时钟频率上时，功耗大约为4瓦特。

双核SiByte处理器包括BCM1250、BCM1255和BCM1280。它们同样基于MIPS64核心，运行在从600 MHz（BCM1250）到1.2 GHz（BCM1255和BCM1280）的时钟频率上。这些双核芯片集成了外设控制器，比如DDR SDRAM控制器，各种组合的吉比特以太网控制器，64位PCI-X接口，和SMBus、PCMCIA以及多个UART接口。像单核处理器一样，这些双核处理器也有低功耗的特点。例如，BCM1225运行在1 GHz的时钟频率上时，其功耗为13瓦特。

四核SiByte处理器包括BCM1455和BCM1480通信处理器。和其他的SiByte处理器一样，它们也是基于MIPS64核心。这些核心可以运行在800 MHz~1.2 GHz的时钟频率上。这些SOC芯片集成了DDR SDRAM控制器、4个单独的吉比特以太网MAC控制器和64位PCI主机控制器。它们还包含SMBus、PCMCIA和4个串行UART。

表3-10总结了Broadcom SiByte处理器的一些特性。

<center class="my_markdown"><b class="my_markdown">表3-10　Broadcom SiByte处理器特性</b></center>

| 特征 | BCM1125H | BCM1250 | BCM1280 | BCM1480 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 核心 | SB-1 MIPS64 | 双核SB-1 MIPS64 | 双核SB-1 MIPS64 | 四核SB-1 MIPS64 |
| 核心频率 | 400~900 MHz | 600~1000 MHz | 800~1200 MHz | 800~1200 MHz |
| DRAM控制器 | Y-DDR | Y-DDR | Y-DDR | Y-DDR |
| 串行接口 | 2~55 Mbit/s | 2~55 Mbit/s | 4个UART | 4个UART |
| SMBus接口 | 2 | 2 | 2 | 2 |
| PCMCIA | 是 | 是 | 是 | 是 |
| 吉比特以太网 （10/100/100 Mbit/s） | 2 | 3 | 4 | 4 |
| PCI控制器 | 是 | 是 | PCI/PCI-X | PCI/PCI-X |
| 安全引擎 | 否 | 否 | 否 | — |
| 高速I/O（HyperTransport） | 1 | 1 | 3 | 3 |

