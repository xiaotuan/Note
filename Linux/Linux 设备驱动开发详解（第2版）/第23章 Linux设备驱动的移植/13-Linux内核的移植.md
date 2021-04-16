### 23.5 Linux内核的移植

Linux内核的移植主要含义是将Linux内核运行于一块新的SoC芯片或一块新的电路板之上，其实质含义就是建立Linux的板级支持包（BSP）。BSP的本质作用有二：为内核的运行提供底层支撑；屏蔽与板相关的硬件细节。对于ARM而言，BSP代码位于arch/arm/的各个plat和mach目录下，结构如下：

plat-xxx

linux-2.6/arch/arm/



plat-omap/ 
 
 plat-pxa/ 
 
 plat-s3c/ 
 
 plat-s3c24xx/ 
 
 plat-s3c64xx/ 
 
 plat-stmp3xxx/ 
 
 
 mach-xxx 
 
 linux-2.6/arch/arm/ 
 
 mach-s3c2400/ 
 
 mach-s3c2410/ 
 
 mach-s3c2412/ 
 
 mach-s3c2440/ 
 
 mach-s3c2442/ 
 
 mach-s3c2443/ 
 
 mach-s3c24a0/ 
 
 mach-s3c6400/ 
 
 mach-s3c6410/

所有S3C6410板的板文件都位于arch/arm/mach-s3c6410/，如LDD6410的即为arch/arm/ mach-s3c6410/mach-ldd6410.c，而所有S3C系列芯片BSP公用的部分又被提炼到arch/arm/plat-s3c/。

这些代码完成的主要工作如下。

#### 1．时钟tick（Hz）的产生

系统节拍是Linux操作系统得以运行的基本条件之一，为Linux建立节拍只需要在硬件上指定一个定时器，并以sys_timer的形式对其进行封装，根据Hz调整定时器硬件计数器，并在定时器中断的处理函数中调用timer_tick()。代码清单23.15列出了S3C6410处理器的系统定时器。

代码清单23.15 S3C6410处理器的系统定时器

1 struct sys_timer s3c64xx_timer = { 
 
 2 .init = s3c64xx_timer_init, 
 
 3 .offset = s3c2410_gettimeoffset, 
 
 4 .resume = s3c64xx_timer_setup 
 
 5 }; 
 
 6 
 
 7 static void __init s3c64xx_timer_init(void) 
 
 8 { 
 
 9 s3c64xx_timer_setup(); 
 
 10 setup_irq(IRQ_TIMER4, &s3c2410_timer_irq); 
 
 11 } 
 
 12 
 
 13 static irqreturn_t 
 
 14 s3c2410_timer_interrupt(int irq, void *dev_id) 
 
 15 { 
 
 16 timer_tick(); 
 
 17 return IRQ_HANDLED; 
 
 18 } 
 
 19 
 
 20 static struct irqaction s3c2410_timer_irq = { 
 
 21 .name = "S3C2410 Timer Tick", 
 
 22 .flags = IRQF_DISABLED | IRQF_TIMER | IRQF_IRQPOLL, 
 
 23 .handler = s3c2410_timer_interrupt, 
 
 24 };

sys_timer结构体的init()成员函数用于定时器的初始化（设置硬件计数器以产生Hz、中断）。由于系统以Hz为单位更新墙上时间，因此Linux的gettimeofday() API如果没有offset()的帮助是无法达到微秒级精度的，offset()函数实际是计算当前硬件计数值与节拍之前的差异。

#### 2．系统中断控制的方法

BSP中需要将系统的所有中断以irq_chip结构体的形式进行组织，并实现各中断的mask()、unmake()、ack()、mask_ack()方法，代码清单23.16给出了S3C6410处理中断的部分代码片段。

代码清单23.16 S3C6410 BSP中断处理

1 static struct irq_chip s3c_irq_uart = { 
 
 2 .name = "s3c-uart", 
 
 3 .mask = s3c_irq_uart_mask, 
 
 4 .unmask = s3c_irq_uart_unmask, 
 
 5 .mask_ack = s3c_irq_uart_maskack, 
 
 6 .ack = s3c_irq_uart_ack, 
 
 7 }; 
 
 8 static void __init s3c64xx_uart_irq(struct uart_irq *uirq) 
 
 9 { 
 
 10 for (offs = 0; offs < 3; offs++) { 
 
 11 irq = uirq->base_irq + offs; 
 
 12 set_irq_chip(irq, &s3c_irq_uart); 
 
 13 set_irq_chip_data(irq, uirq); 
 
 14 set_irq_handler(irq, handle_level_irq); 
 
 15 set_irq_flags(irq, IRQF_VALID); 
 
 16 } 
 
 17 set_irq_chained_handler(uirq->parent_irq, s3c_irq_demux_uart); 
 
 18 } 
 
 19 void __init s3c64xx_init_irq(u32 vic0_valid, u32 vic1_valid) 
 
 20 { 
 
 21 set_irq_chip(irq, &s3c_irq_timer); 
 
 22 ... 
 
 23 for (uart = 0; uart < ARRAY_SIZE(uart_irqs); uart++) 
 
 24 s3c64xx_uart_irq(&uart_irqs[uart]); 
 
 25 }

#### 3．GPIO、DMA、时钟资源的统一管理

在BSP中，通常需要将所有GPIO以gpio_chip结构体的形式进行组织，这个结构体中的成员函数用于设置GPIO的方向、读取和设置GPIO的电平，如代码清单23.17所示。

代码清单23.17 gpio_chip结构体

1 struct gpio_chip { 
 
 2 int (*request)(struct gpio_chip *chip, 
 
 3 unsigned offset); 
 
 4 void (*free)(struct gpio_chip *chip, 
 
 5 unsigned offset); 
 
 6 int (*direction_input)(struct gpio_chip *chip, 
 
 7 unsigned offset); 
 
 8 int (*get)(struct gpio_chip *chip, 
 
 9 unsigned offset); 
 
 10 int (*direction_output)(struct gpio_chip *chip, 
 
 11 unsigned offset, int value); 
 
 12 void (*set)(struct gpio_chip *chip, 
 
 13 unsigned offset, int value); 
 
 14 };

Linux会提供如下一组通用关于GPIO的API：

int gpio_request(unsigned gpio, const char *label); 
 
 void gpio_free(unsigned gpio); 
 
 int gpio_direction_input(unsigned gpio); 
 
 int gpio_direction_output(unsigned gpio, int value); 
 
 int gpio_get_value_cansleep(unsigned gpio);

这样做的好处是驱动的代码完全可以以与平台无关的方式申请和使用GPIO，而不是各自为政，通过读写寄存器来访问GPIO，大大提高了驱动的可移植性。

同样的，BSP也要实现针对DMA通用API，如：

int request_dma(unsigned int chan, const char * device_id); 
 
 void free_dma(unsigned int chan); 
 
 void enable_dma(unsigned int chan); 
 
 void disable_dma(unsigned int chan); 
 
 void set_dma_mode (unsigned int chan, unsigned int mode); 
 
 void set_dma_sg (unsigned int chan, struct scatterlist *sg, int nr_sg);

同样的，BSP也要实现针对时钟的通用API，包括clk_get()、clk_put()、clk_enable()、clk_disable()、clk_get_rate()、clk_round_rate()、clk_set_rate()、clk_get_parent()、clk_set_parent()。

#### 4．静态映射的I/O内存

在BSP中，可以通过map_desc结构体和iotable_init()函数提前建立某段物理地址和虚拟地址之间的静态映射，该知识点我们在第11章“I/O内存静态映射”一节已经进行过讲解。

#### 5．设备的I/O、中断、DMA等资源封装平台数据

主要是platform信息、SPI board信息和I2C board信息，这些内容我们在前面各章节已经进行过讲解，这里就不再赘述。

最后，对于一块ARM电路板而言，我们会将它的中断初始化、静态内存映射、系统定时器等板级信息透过MACHINE_START和MACHINE_END之间的宏绑定在一起。代码清单23.18给出了LDD6410的例子。

代码清单23.18 LDD6410开发板的MACHINE_START和MACHINE_END

1 MACHINE_START(SMDK6410, "LDD6410") 
 
 2 /* Maintainer: Barry Song <21cnbao@gmail.com> */ 
 
 3 .phys_io = S3C_PA_UART & 0xfff00000, 
 
 4 .io_pg_offst = (((u32)S3C_VA_UART) >> 18) & 0xfffc, 
 
 5 .boot_params = S3C64XX_PA_SDRAM + 0x100, 
 
 6 
 
 7 .init_irq = s3c6410_init_irq, 
 
 8 .map_io = ldd6410_map_io, 
 
 9 .init_machine = ldd6410_machine_init, 
 
 10 .timer = &s3c64xx_timer, 
 
 11 MACHINE_END

从代码清单23.18第1行“MACHINE_START(SMDK6410, "LDD6410")”可以看出，LDD6410仍然使用了SMDK6410的mach ID，实际上可以透过Linux ARM的邮件列表获得一个新的mach ID。

大多数工程师就职于设备提供商，因此不涉及SoC级的移植，也就是说芯片公司已经将系统定时器、GPIO、DMA、时钟等都封装好了，工程师只需要进行板相关的移植。这里我们给出Linux板级移植的原则：切忌直接修改现有电路板的代码作为自身电路板的代码，例如，如果电路板与SMDK6410有差异，就直接修改arch/arm/mach-s3c6410/mach-smdk6410.c，这是完全错误的，正确的方法是新建自己的板文件，将本身的设备和资源填写在新的板文件里面。

除了SoC芯片级和板级Linux移植外，移植工作量最大的是体系结构相关的Linux移植，例如将Linux移植到一个全新的CPU体系架构，如TI的DSP芯片。则工作量还涉及内存管理、进程调度、异常和陷阱等。

