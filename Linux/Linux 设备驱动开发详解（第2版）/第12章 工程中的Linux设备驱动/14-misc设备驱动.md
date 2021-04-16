### 12.5 misc设备驱动

Linux包含了许多的设备驱动类型，而不管分类有多细，总会有些漏网的，这就是我们经常说到的“其他的”、“等等”。在Linux里面，把无法归类的五花八门的设备定义为混杂设备（用miscdevice结构体描述）。Linux内核所提供的miscdevice有很强的包容性，如NVRAM、看门狗、DS1286等实时钟、字符LCD、AMD 768随机数发生器等，体现了大杂烩的本意。

miscdevice共享一个主设备号MISC_MAJOR（即10），但次设备号不同。所有的miscdevice设备形成一个链表，对设备访问时内核根据次设备号查找对应的miscdevice设备，然后调用其file_operations结构体中注册的文件操作接口进行操作。

在内核中，用struct miscdevice结构体表征miscdevice设备，这个结构体的定义如代码清单12.20所示。

代码清单12.20 miscdevice结构体

1 struct miscdevice { 
 
 2 int minor; 
 
 3 const char *name; 
 
 4 const struct file_operations *fops; 
 
 5 struct list_head list; 
 
 6 struct device *parent; 
 
 7 struct device *this_device; 
 
 8 };

miscdevice在本质上仍然属于字符设备，只是被增加了一层封装而已，因此其驱动的主体工作还是file_operations的成员函数。代码清单12.21则给出了源代码drivers/char/nvram.c所实现NVRAM驱动的miscdevice和file_operations实例。

代码清单12.21 NVRAM设备结构体

1 static const struct file_operations nvram_fops = {

2 .owner = THIS_MODULE,

3 .llseek = nvram_llseek,

4 .read = nvram_read,



5 .write = nvram_write, 
 
 6 .ioctl = nvram_ioctl, 
 
 7 .open = nvram_open, 
 
 8 .release = nvram_release, 
 
 9 }; 
 
 10 
 
 11 static struct miscdevice nvram_dev = { 
 
 12 NVRAM_MINOR, 
 
 13 "nvram", 
 
 
 14 &nvram_fops 
 
 15 };

对misddevice的注册和注销分别通过如下两个API完成：

int misc_register(struct miscdevice * misc); 
 
 int misc_deregister(struct miscdevice *misc);

查看drivers/char/nvram.c的模块加载和卸载函数可知，其在加载的时候调用了“misc_register (&nvram_dev);”，而在模块卸载时调用了“misc_deregister(&nvram_dev);”。

