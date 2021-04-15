### 3.2.13　德州仪器ARM

德州仪器（Texas Instruments，TI）在其DaVinci、OMAP和其他系列集成处理器中使用了ARM核心。这些处理器包含很多集成外设，是针对消费电子产品的单芯片解决方案，目标产品包括手机、PDA和类似的多媒体平台。除了一些集成处理器中常见的接口，比如UART和I<sup class="my_markdown">2</sup>C，OMAP处理器还包含了很多特殊用途的接口，包括：

+ LCD显示屏和背光控制器；
+ 蜂鸣器驱动；
+ 相机接口；
+ MMC/SD卡控制器；
+ 电池管理硬件；
+ USB主从接口；
+ 无线调制解调器接口逻辑；
+ 集成的2D或3D图形加速器；
+ 集成的安全加速器；
+ S-Video输出；
+ IrDA控制器；
+ 针对直接TV（PAL/NTSC）视频输出的DAC；
+ 针对音视频处理的集成DSP（Digital Signal Processor，数字信号处理器）。

市面上很多受欢迎的手机和PDA设备都采用了德州仪器的OMAP平台。这些处理器都是基于ARM核心的，Linux提供了完善的支持。表3-11比较了德州仪器最新的几款ARM处理器。

<center class="my_markdown"><b class="my_markdown">表3-11　德州仪器ARM处理器特性</b></center>

| 特征 | OMAP-L138 | DaVinci6467 | OMAP3515/03 | OMAP3530 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 核心 | ARM926EJ-S | ARM926EJ-S | ARM Cortex A8 | ARM Cortex A8 |
| 时钟频率 | 300 MHz | 高达365 MHz | 高达720 MHz | 550 MHz |
| DRAM控制器 | DDR2 | DDR2 | DDR2 | 是 |
| 板载DSP | 300 MHz C674x | 300 MHz C64X+ | — | C64X+ 视频/图像加速器子系统 |
| UART | 3 | 3 | 3 | 3 |
| USB | USB 1.1 host USB 2.0 OTG | USB 2.0 host USB 2.0 client | USB 2.0 host USB 2.0 client | USB 2.0 host USB 2.0 client |
| I<sup class="my_markdown">2</sup>C控制器/总线 | 2 | 1 | 是 | 是 |
| MMC-SD接口 | 2 | — | 是 | 是 |
| 相机接口 | 参见视频端口 | 参见视频端口 | 是 | 是 |
| 视频端口 | 2进，2出 | 2进，2出 | S-Video或CVBS | S-Video或CVBS |
| 视频加速硬件 | — | 两个高清视频图像协处理器 | POWERVR SGX显示控制器 | 图像视频加速器（IVA 2+） |
| 音频编解码器 | AC97<a class="my_markdown" href="['#anchor037']"><sup class="my_markdown">[7]</sup></a>接口 | AC97接口 | 通过DSP | 通过DSP |
| LCD控制器 | 是 | 是 | 是 | 是 |
| 显示控制器 | LCD控制器和视频输入/输出 | LCD控制器和视频输入/输出 | 双输出3层显示处理器 | 双输出3层显示处理器 |

<a class="my_markdown" href="['#ac037']">[7]</a>　这些芯片内部支持与AC97音频流的连接。除此以外，要知道芯片中集成的DSP可以实现多种音视频编解码器。

#### BeagleBoard开发板

如果接触过一段时间的嵌入式Linux，你肯定会听说过BeagleBoard开发板。它之所以受欢迎，是因为价格低，容易买到，并且有广泛的社区支持。BeagleBoard开发板支持流行的U-Boot引导加载程序，从而方便了内核的集成。BeagleBoard开发板基于德州仪器OMAP3530处理器。它可以外接键盘和显示器，可以插SD卡用于内核和根文件系统。它还包含一个用于控制台的串行连接，以及一个双模USB 2.0端口。

BeagleBoard开发板是一个可用于实验和学习的优秀平台，同样也是一个完美的开发平台，可用于多种OMAP相关的开发项目中。BeagleBoard开发板的唯一缺点是它缺少以太网端口。幸运的是，这个问题被一家名叫Tin Can Tools的公司解决了。它开发了一个配套使用的板卡，称为BeagleBuddy Zippy以太网复合板。除了增加了一个以太网端口，这块板卡还增加了SD/MMC接口，电池供电的实时时钟，I<sup class="my_markdown">2</sup>C扩展接口和串行端口。你可以在以下网址了解更多相关信息：<a class="my_markdown" href="['http://www.tincantools.com/product.php?productid=16147&cat=255&page=1']">www.tincantools.com/product.php?productid=16147&cat=255&page=1</a>。

