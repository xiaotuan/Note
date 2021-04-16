### 12.1.1 platform总线、设备与驱动

在Linux 2.6的设备驱动模型中，关心总线、设备和驱动这3个实体，总线将设备和驱动绑定。在系统每注册一个设备的时候，会寻找与之匹配的驱动；相反的，在系统每注册一个驱动的时候，会寻找与之匹配的设备，而匹配由总线完成。

一个现实的Linux设备和驱动通常都需要挂接在一种总线上，对于本身依附于PCI、USB、I2C、SPI等的设备而言，这自然不是问题，但是在嵌入式系统里面，SoC系统中集成的独立的外设控制器、挂接在SoC内存空间的外设等确不依附于此类总线。基于这一背景，Linux发明了一种虚拟的总线，称为platform总线，相应的设备称为platform_device，而驱动成为platform_driver。

注意，所谓的platform_device并不是与字符设备、块设备和网络设备并列的概念，而是Linux系统提供的一种附加手段，例如，在S3C6410处理器中，把内部集成的I2C、RTC、SPI、LCD、看门狗等控制器都归纳为platform_device，而它们本身就是字符设备。platform_device结构体的定义如代码清单12.1所示。

代码清单12.1 platform.device结构体

1 struct platform_device { 
 
 2 const char * name; / * 设备名 */ 
 
 3 u32 id; 
 
 4 struct device dev; 
 
 5 u32 num_resources; / * 设备所使用各类资源数量 */ 
 
 6 struct resource * resource; / * 资源 */ 
 
 7 };

platform_driver这个结构体中包含probe()、remove()、shutdown()、suspend()、resume()函数，通常也需要由驱动实现，如代码清单12.2所示。

代码清单12.2 platform.driver结构体

1 struct platform_driver { 
 
 2 int (*probe)(struct platform_device *); 
 
 3 int (*remove)(struct platform_device *); 
 
 4 void (*shutdown)(struct platform_device *); 
 
 5 int (*suspend)(struct platform_device *, pm_message_t state); 
 
 6 int (*suspend_late)(struct platform_device *, pm_message_t state); 
 
 7 int (*resume_early)(struct platform_device *); 
 
 8 int (*resume)(struct platform_device *); 
 
 9 struct pm_ext_ops *pm; 
 
 10 struct device_driver driver; 
 
 11};

系统中为platform总线定义了一个bus_type的实例platform_bus_type，其定义如代码清单12.3所示。

代码清单12.3 platform总线的bus.type实例platform.bus.type

1 struct bus_type platform_bus_type = { 
 
 2 .name = "platform", 
 
 3 .dev_attrs = platform_dev_attrs,



4 .match = platform_match, 
 
 5 .uevent = platform_uevent, 
 
 6 .pm = PLATFORM_PM_OPS_PTR, 
 
 7 }; 
 
 8 EXPORT_SYMBOL_GPL(platform_bus_type);

这里要重点关注其match()成员函数，正是此成员函数确定了platform_device和platform_driver之间如何匹配，如代码清单12.4所示。

代码清单12.4 platform.bus.type的match()成员函数

1 static int platform_match(struct device *dev, struct device_driver *drv) 
 
 2 { 
 
 3 struct platform_device *pdev; 
 
 4 
 
 5 pdev = container_of(dev, struct platform_device, dev); 
 
 
 6 return (strncmp(pdev->name, drv->name, BUS_ 
 ID_ 
 SIZE) == 0); 
 
 7 }

从代码清单12.4的第6行可以看出，匹配platform_device和platform_driver主要看两者的name字段是否相同。

对platform_device的定义通常在BSP的板文件中实现，在板文件中，将platform_device归纳为一个数组，最终通过platform_add_devices()函数统一注册。platform_add_devices()函数可以将平台设备添加到系统中，这个函数的原型为：

int platform_add_devices(struct platform_device **devs, int num);

该函数的第一个参数为平台设备数组的指针，第二个参数为平台设备的数量，它内部调用了platform_device_register()函数用于注册单个的平台设备。

