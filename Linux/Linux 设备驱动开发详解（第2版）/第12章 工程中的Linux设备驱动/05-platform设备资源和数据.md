### 12.1.3 platform设备资源和数据

留意一下代码清单12.1中platform_device结构体定义的第5～6行，描述了platform_device的资源，资源本身由resource结构体描述，其定义如代码清单12.7所示。

代码清单12.7 resouce结构体定义

1 struct resource { 
 
 2 resource__size_t start; 
 
 3 resource_size_t end; 
 
 4 const char *name; 
 
 5 unsigned long flags; 
 
 6 struct resource *parent, *sibling, *child; 
 
 7 };

我们通常关心start、end和flags这3个字段，分别标明资源的开始值、结束值和类型，flags可以为IORESOURCE_IO、IORESOURCE_MEM、IORESOURCE_IRQ、IORESOURCE_DMA等。start、end的含义会随着flags而变更，如当flags为IORESOURCE_MEM时，start、end分别表示该platform_device占据的内存的开始地址和结束地址；当flags为IORESOURCE_IRQ时，start、end分别表示该platform_device使用的中断号的开始值和结束值，如果只使用了1个中断号，开始和结束值相同。对于同种类型的资源而言，可以有多份，例如说某设备占据了2个内存区域，则可以定义2个IORESOURCE_MEM资源。

对resource的定义也通常在BSP的板文件中进行，而在具体的设备驱动中透过platform_get_ resource()这样的API来获取，此API的原型为：

struct resource *platform_get_resource(struct platform_device *, unsigned int, unsigned int);

例如在LDD6410开发板的板文件中为DM9000网卡定义了如下resouce：

static struct resource ldd6410_dm9000_resource[] = { 
 
 [0] = { 
 
 .start = 0x18000000, 
 
 .end = 0x18000000 + 3, 
 
 .flags = IORESOURCE_MEM 
 
 }, 
 
 [1] = { 
 
 .start = 0x18000000 + 0x4, 
 
 .end = 0x18000000 + 0x7, 
 
 .flags = IORESOURCE_MEM 
 
 }, 
 
 [2] = { 
 
 .start = IRQ_EINT(7), 
 
 .end = IRQ_EINT(7), 
 
 .flags = IORESOURCE_IRQ | IORESOURCE_IRQ_HIGHLEVEL, 
 
 } 
 
 };

在DM9000网卡的驱动中则是通过如下办法拿到这3份资源：

db->addr_res = platform_get_resource(pdev, IORESOURCE_MEM, 0); 
 
 db->data_res = platform_get_resource(pdev, IORESOURCE_MEM, 1); 
 
 db->irq_res = platform_get_resource(pdev, IORESOURCE_IRQ, 0);

对于IRQ而言，platform_get_resource()还有一个进行了封装的变体platform_get_irq()，其原型为：

int platform_get_irq(struct platform_device *dev, unsigned int num);

它实际上调用了“platform_get_resource(dev, IORESOURCE_IRQ, num);”。

设备除了可以在BSP中定义资源以外，还可以附加一些数据信息，因为对设备的硬件描述除了中断、内存、DMA通道以外，可能还会有一些配置信息，而这些配置信息也依赖于板，不适宜直接放置在设备驱动本身，因此，platform也提供了platform_data的支持。platform_data的形式是自定义的，如对于DM9000网卡而言，platform_data为一个dm9000_plat_data结构体，我们就可以将MAC地址、总线宽度、板上有无EEPROM信息等放入platform_data：

static struct dm9000_ 
 plat_ 
 data ldd6410_ 
 dm9000_ 
 platdata = {

.flags 
 = DM9000_ 
 PLATF_ 
 16BITONLY | DM9000_ 
 PLATF_ 
 NO_ 
 EEPROM, .dev_ 
 addr = { 0x0, 0x16, 0xd4, 0x9f, 0xed, 0xa4 }, };

static struct platform_device ldd6410_dm9000 = { 
 
 .name= "dm9000", 
 
 .id= 0, 
 
 .num_resources= ARRAY_SIZE(ldd6410_dm9000_resource), 
 
 .resource =ldd6410_dm9000_resource, 
 
 .dev = { 
 
 
 .platform_ 
 data = &ldd6410_ 
 dm9000_ 
 platdata, 
 
 } 
 
 };

而在DM9000网卡的驱动中，通过如下方式就拿到了platform_data：

struct dm9000_plat_data *pdata = pdev->dev.platform_data;

其中，pdev为platform_device的指针。

由以上分析可知，设备驱动中引入platform的概念至少有如下两大好处。

（1）使得设备被挂接在一个总线上，因此，符合Linux 2.6的设备模型。其结果是，配套的sysfs结点、设备电源管理都成为可能。

（2）隔离BSP和驱动。在BSP中定义platform设备和设备使用的资源、设备的具体配置信息，而在驱动中，只需要通过通用API去获取资源和数据，做到了板相关代码和驱动代码的分离，使得驱动具有更好的可扩展性和跨平台性。

