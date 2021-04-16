### 13.2.1 block_device_operations结构体

在块设备驱动中，有一个类似于字符设备驱动中file_operations结构体的block_device_operations结构体，它是对块设备操作的集合，定义如代码清单13.1所示。

代码清单13.1 block.device.operations结构体

1 struct block_device_operations { 
 
 2 int (*open) (struct block_device *, fmode_t); 
 
 3 int (*release) (struct gendisk *, fmode_t); 
 
 4 int (*locked_ioctl) (struct block_device *, fmode_t, unsigned, unsigned long);



5 int (*ioctl) (struct block_device *, fmode_t, unsigned, unsigned long); 
 
 6 int (*compat_ioctl) (struct block_device *, fmode_t, unsigned, unsigned long); 
 
 7 int (*direct_access) (struct block_device *, sector_t, 
 
 8 void **, unsigned long *); 
 
 9 int (*media_changed) (struct gendisk *); 
 
 10 int (*revalidate_disk) (struct gendisk *); 
 
 11 int (*getgeo)(struct block_device *, struct hd_geometry *); 
 
 12 struct module *owner; 
 
 13 };

下面对其主要的成员函数进行分析。

#### 1．打开和释放

int (*open)(struct gendisk *disk, fmode_t mode); 
 
 int (*release)(struct gendisk *disk, fmode_t mode);

与字符设备驱动类似，当设备被打开和关闭时将调用它们。

#### 2．I/O控制

int (*ioctl) (struct block_device *bdev, fmode_t mode, unsigned cmd, 
 
 unsigned long arg);

上述函数是ioctl()系统调用的实现，块设备包含大量的标准请求，这些标准请求由Linux块设备层处理，因此大部分块设备驱动的ioctl()函数相当短。

#### 3．介质改变

int (*media_changed) (struct gendisk *gd);

被内核调用来检查是否驱动器中的介质已经改变，如果是，则返回一个非0值，否则返回0。这个函数仅适用于支持可移动介质的驱动器，通常需要在驱动中增加一个表示介质状态是否改变的标志变量，非可移动设备的驱动不需要实现这个方法。

#### 4．使介质有效

int (*revalidate_disk) (struct gendisk *gd);

revalidate_disk()函数被调用来响应一个介质改变，它给驱动一个机会来进行必要的工作以使新介质准备好。

#### 5．获得驱动器信息

int (*getgeo)(struct block_device *, struct hd_geometry *);

该函数根据驱动器的几何信息填充一个hd_geometry结构体，hd_geometry结构体包含磁头、扇区、柱面等信息，其定义于include/linux/hdreg.h头文件。

#### 6．模块指针

struct module *owner;

一个指向拥有这个结构体的模块的指针，它通常被初始化为THIS_MODULE。

