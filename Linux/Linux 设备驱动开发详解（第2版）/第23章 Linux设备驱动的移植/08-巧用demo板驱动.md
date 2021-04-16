### 23.2.1 巧用demo板驱动

对于推出的重要芯片，芯片厂商往往会同时提供一套demo板。这样的demo板不仅在硬件设计中被硬件工程师充分利用并进行参考，而且其提供的驱动程序往往在新设计的硬件系统中被参考。

借用demo板驱动的方法主要是寻找共性中的差异，例如共性是芯片相同，差异则可能体现在所使用的I/O内存（片选）、中断和DMA资源不同，在这种情况下，简单地修改I/O内存基地址、中断号以及DMA通道，demo板的驱动就可以用在目标电路板上。而如果除了芯片相同以外，外围芯片与CPU连接所用的内存、中断和DMA资源都相同的话，则demo板驱动基本上可以不加任何修改地搬到目标电路板上。

如果demo板和目标电路板所用资源不同，而demo板对应设备被定义为pltaform_device，且其资源并定义在resource结构体数组中，则直接修改resource结构体即可，如下所示：

static struct resource xxx_resource[] = { 
 
 [0] = { 
 
 .start = XXX_MEM_START, /* 修改这里替换I/O内存基地址 */ 
 
 .end = XXX_MEM_START + XXX_MEM_SIZE, 
 
 .flags = IORESOURCE_MEM, 
 
 },

[1] = { 
 
 .start = XXX_INT_START, /* 修改这里换中断 */ 
 
 .end = XXX_INT_END, 
 
 .flags = IORESOURCE_IRQ, 
 
 } 
 
 };

同时，我们在编写新驱动的时候永远要牢记这样的设计理念：将硬件和平台相关的信息（内存地址、中断号、DMA通道、硬件设置等）放入BSP中，作为platform信息、SPI board信息、I2C board信息等，而不是直接放在驱动里面。

