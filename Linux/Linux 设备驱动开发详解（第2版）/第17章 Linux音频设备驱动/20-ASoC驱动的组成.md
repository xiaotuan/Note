### 17.5.1 ASoC驱动的组成

ASoC（ALSA System on Chip）是ALSA在SoC方面的发展和演变，它在本质上仍然属于ALSA，但是在ALSA架构基础上对CPU相关的代码和Codec相关的代码进行了分离。其原因是，采用传统ALSA架构的情况下，同一型号的Codec工作于不同的CPU时，需要不同的驱动，这不符合代码重用的要求。

对于目前嵌入式系统上的声卡驱动开发，我们建议读者尽量采用ASoC框架，ASoC主要由3部分组成。

（1）Codec驱动。这一部分只关心Codec本身，与CPU平台相关的特性不由此部分操作。

（2）平台驱动。这一部分只关心CPU本身，不关心Codec。它主要处理两个问题：DMA引擎和SoC集成的PCM、I2S或AC '97数字接口控制。

（3）板驱动（也称为machine驱动）。这一部分将平台驱动和Codec驱动绑定在一起，描述了板一级的硬件特征。

在以上3部分中，1和2基本都可以仍然是通用的驱动了，也就是说，Codec驱动认为自己可以连接任意CPU，而CPU的I2S、PCM或AC '97接口对应的平台驱动则认为自己可以连接任意符合其接口类型的Codec，只有3是不通用的，由特定的电路板上具体的CPU和Codec确定，因此它很像一个插座，上面插上了Codec和平台这两个插头。

在以上三部分之上的是ASoC核心层，由内核源代码中的sound/soc/soc-core.c实现，查看其源代码发现它完全是一个传统的ALSA驱动。因此，对于基于ASoC架构的声卡驱动而言，alsa-lib以及ALSA的一系列utility仍然是可用的，如amixer、aplay均无需针对ASoC进行任何改动。而ASoC的用户编程方法也与ALSA完全一致。

内核源代码的Documentation/sound/alsa/soc/目录包含了ASoC相关的文档。

