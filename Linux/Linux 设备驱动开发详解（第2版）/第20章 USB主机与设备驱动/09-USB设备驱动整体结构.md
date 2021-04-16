### 20.3.1 USB设备驱动整体结构

这里所说的USB设备驱动指的是从主机角度观察，怎样访问被插入的USB设备，而不是指USB设备内部本身运行的固件程序。Linux系统实现了几类通用的USB设备驱动（也称客户驱动），划分为如下几个设备类。

● 音频设备类。

● 通信设备类。

● HID（人机接口）设备类。

● 显示设备类。

● 海量存储设备类。

● 电源设备类。

● 打印设备类。

● 集线器设备类。

一般的通用的Linux设备（如U盘、USB鼠标、USB键盘等）都不需要工程师再编写驱动，需要编写的是特定厂商、特定芯片的驱动，而且往往也可以参考内核中已提供的驱动的模板。

Linux内核为各类USB设备分配了相应的设备号，如ACM USB调制解调器的主设备号为166（默认设备名/dev/ttyACMn）、USB打印机的主设备号为180，次设备号为0～15（默认设备名/dev/lpn）、USB串口的主设备号为188（默认设备名/dev/ttyUSBn）等，详见http://www.lanana.org/网站的设备列表。

内核中提供了USB设备文件系统（usbdevfs，Linux 2.6改为usbfs，即USB文件系统），它和/proc类似，都是动态产生的。通过在/etc/fstab文件中添加如下一行：

none /proc/bus/usb usbfs defaults

或者输入命令：

mount -t usbfs none /proc/bus/usb

可以实现USB设备文件系统的挂载。

一个典型的/proc/bus/usb/devices文件的结构如下（笔者在PC上插入了一个SanDisk U盘）：

T: Bus=01 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#= 1 Spd=12 MxCh= 2 
 
 B: Alloc= 0/900 us ( 0%), #Int= 0, #Iso= 0 
 
 D: Ver= 1.10 Cls=09(hub ) Sub=00 Prot=00 MxPS=64 #Cfgs= 1 
 
 P: Vendor=0000 ProdID=0000 Rev= 2.06 
 
 S: Manufacturer=Linux 2.6.15.5 uhci_hcd 
 
 S: Product=UHCI Host Controller 
 
 S: SerialNumber=0000:00:07.2 
 
 C:* #Ifs= 1 Cfg#= 1 Atr=c0 MxPwr= 0mA 
 
 I: If#= 0 Alt= 0 #EPs= 1 Cls=09(hub ) Sub=00 Prot=00 Driver=hub 
 
 E: Ad=81(I) Atr=03(Int.) MxPS= 2 Ivl=255ms

T: Bus=01 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#= 2 Spd=12 MxCh= 0 
 
 D: Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs= 1 
 
 P: Vendor=0781 ProdID=5151 Rev= 0.10 
 
 S: Manufacturer=SanDisk Corporation 
 
 S: Product=Cruzer Micro 
 
 S: SerialNumber=20060877500A1BE1FDE1 
 
 C:* #Ifs= 1 Cfg#= 1 Atr=80 MxPwr=200mA 
 
 I: If#= 0 Alt= 0 #EPs= 2 Cls=08(stor.) Sub=06 Prot=50 Driver=(none) 
 
 E: Ad=81(I) Atr=02(Bulk) MxPS= 512 Ivl=0ms 
 
 E: Ad=01(O) Atr=02(Bulk) MxPS= 512 Ivl=0ms

通过分析usbfs中记录的信息，可以得到系统中USB完整的信息，例如，usbview可以以图形化的方式显示系统中的USB设备。

当然，在编译Linux内核时，应该包括“USB device filesystem”。usbfs动态跟踪总线上插入和移除的设备，通过它可以查看系统中USB设备的信息，包括拓扑、带宽、设备描述符信息、产品ID、字符串描述符、配置描述符、接口描述符、端点描述符等。

此外，在sysfs文件系统中，同样包含了USB相关信息的描述，但只限于接口级别。USB设备和USB接口在sysfs中均表示为单独的USB设备，其目录命名规则如下：

根集线器-集线器端口号（-集线器端口号-...）:配置.接口

下面讲解/sys/bus/usb目录的树形结构实例，其中的多数文件都是到/sys/devices及/sys/drivers中相应文件的链接。

usb 
 
 |-- devices 
 
 | |-- 1-0:1.0 → ../../../devices/pci0000:00/0000:00:07.2/usb1/1-0:1.0 
 
 | |-- 1-1 → ../../../devices/pci0000:00/0000:00:07.2/usb1/1-1 
 
 | |-- 1-1:1.0 → ../../../devices/pci0000:00/0000:00:07.2/usb1/1-1/1-1:1.0 
 
 | '-- usb1 → ../../../devices/pci0000:00/0000:00:07.2/usb1 
 
 '-- drivers 
 
 |-- hub 
 
 | |-- 1-0:1.0 → ../../../../devices/pci0000:00/0000:00:07.2/usb1/1-0:1.0 
 
 | |-- bind 
 
 | |-- module → ../../../../module/usbcore 
 
 | '-- unbind 
 
 |-- usb 
 
 | |-- 1-1 → ../../../../devices/pci0000:00/0000:00:07.2/usb1/1-1 
 
 | |-- bind 
 
 | |-- module → ../../../../module/usbcore 
 
 | |-- unbind 
 
 | '-- usb1 → ../../../../devices/pci0000:00/0000:00:07.2/usb1 
 
 '-- usbfs 
 
 |-- bind 
 
 |-- module → ../../../../module/usbcore 
 
 '-- unbind

正如tty_driver、i2c_driver等，在Linux内核中，使用usb_driver结构体描述一个USB设备驱动，usb_driver结构体的定义如代码清单20.11所示。

代码清单20.11 usb_driver结构体

1 struct usb_driver { 
 
 2 const char *name; /* 驱动名称 */ 
 
 3 int (*probe) (struct usb_interface *intf, 
 
 4 const struct usb_device_id *id); /*探测函数*/ 
 
 5 void (*disconnect) (struct usb_interface *intf); /*断开函数*/ 
 
 6 int (*ioctl) (struct usb_interface *intf, unsigned int code, 
 
 7 void *buf); /* I/O控制函数 */ 
 
 8 int (*suspend) (struct usb_interface *intf, pm_message_t message);/*挂起函数*/ 
 
 9 int (*resume) (struct usb_interface *intf); /* 恢复函数 */ 
 
 10 int (*reset_resume)(struct usb_interface *intf); 
 
 11 void (*pre_reset) (struct usb_interface *intf); 
 
 12 void (*post_reset) (struct usb_interface *intf); 
 
 13 const struct usb_device_id *id_table;/* usb_device_id表指针 */ 
 
 14 struct usb_dynids dynids; 
 
 15 struct usbdrv_wrap drvwrap;



16 unsigned int no_dynamic_id:1; 
 
 17 unsigned int supports_autosuspend:1; 
 
 18 unsigned int soft_unbind:1; 
 
 19 };

在编写新的USB设备驱动时，主要应该完成的工作是probe()和disconnect()函数，即探测和断开函数，它们分别在设备被插入和拔出的时候被调用，用于初始化和释放软硬件资源。对usb_driver的注册和注销通过这两个函数完成：

int usb_register(struct usb_driver *new_driver) 
 
 void usb_deregister(struct usb_driver *driver);

usb_driver结构体中的id_table成员描述了这个USB驱动所支持的USB设备列表，它指向一个usb_device_id数组，usb_device_id结构体用于包含USB设备的制造商ID、产品ID、产品版本、设备类、接口类等信息及其要匹配标志成员match_flags（标明要与哪些成员匹配，包含DEV_LO、DEV_HI、DEV_CLASS、DEV_SUBCLASS、DEV_PROTOCOL、INT_CLASS、INT_SUBCLASS、INT_PROTOCOL）。可以借助下面一组宏来生成usb_device_id结构体的实例：

USB_DEVICE(vendor, product)

该宏根据制造商ID和产品ID生成一个usb_device_id结构体的实例，在数组中增加该元素将意味着该驱动可支持匹配制造商ID、产品ID的设备。

USB_DEVICE_VER(vendor, product, lo, hi)

该宏根据制造商ID、产品ID、产品版本的最小值和最大值生成一个usb_device_id结构体的实例，在数组中增加该元素将意味着该驱动可支持匹配制造商ID、产品ID和lo～hi范围内版本的设备。

USB_DEVICE_INFO(class, subclass, protocol)

该宏用于创建一个匹配设备指定类型的usb_device_id结构体实例。

USB_INTERFACE_INFO(class, subclass, protocol)

该宏用于创建一个匹配接口指定类型的usb_device_id结构体实例。

代码清单20.12所示为两个用于描述某USB驱动所支持的USB设备的usb_device_id结构体数组实例。

代码清单20.12 usb_device_id结构体数组实例

1 /* 本驱动支持的USB设备列表 */ 
 
 2 
 
 3 /* 实例1 */ 
 
 4 static struct usb_device_id id_table [] = { 
 
 5 { USB_DEVICE(VENDOR_ID, PRODUCT_ID) }, 
 
 6 { }, 
 
 7 }; 
 
 8 MODULE_DEVICE_TABLE (usb, id_table); 
 
 9 
 
 10 /* 实例2 */ 
 
 11 static struct usb_device_id id_table [] = { 
 
 12 { .idVendor = 0x10D2, .match_flags = USB_DEVICE_ID_MATCH_VENDOR, }, 
 
 13 { }, 
 
 14 }; 
 
 15 MODULE_DEVICE_TABLE (usb, id_table);

当USB核心检测到某个设备的属性和某个驱动程序的usb_device_id结构体所携带的信息一致时，这个驱动程序的probe()函数就被执行。拔掉设备或者卸掉驱动模块后，USB核心就执行disconnect()函数来响应这个动作。

上述usb_driver结构体中的函数是USB设备驱动中USB相关的部分，而USB只是一个总线，真正的USB设备驱动的主体工作仍然是USB设备本身所属类型的驱动，如字符设备、tty设备、块设备、输入设备等。因此USB设备驱动包含其作为总线上挂在设备的驱动和本身所属设备类型的驱动两部分。

与platform_driver类似，usb_driver起到了“牵线”的作用，即在probe()里注册相应的字符、tty等设备，在disconnect()注销相应的字符、tty等设备，而原先对设备的注册和注销一般直接发生在模块加载和卸载函数中。

尽管USB本身所属设备驱动的结构与其不挂在USB总线上时完全相同，但是在访问方式上却发生了很大的变化，例如，对于USB接口的字符设备而言，尽管仍然是write()、read()、ioctl()这些函数，但是在这些函数中，贯穿始终的是称为URB的USB请求块。

如图20.4所示，在这棵树里，我们把树根比作主机控制器，树叶比作具体的USB设备，树干和树枝就是USB总线。树叶本身与树枝通过usb_driver连接，而树叶本身的驱动（读写、控制）则需要通过其树叶设备本身所属类设备驱动来完成。树根和树叶之间的“通信”依靠在树干和树枝里“流淌”的URB来完成。

![P541_51718.jpg](../images/P541_51718.jpg)
由此可见，usb_driver本身只是起到了找到USB设备、管理USB设备连接和断开的作用，也就是说，它是公司入口处的“打卡机”，可以获得员工（USB设备）的上/下班情况。树叶和员工一样，可以是研发工程师也可以是销售工程师，而作为USB设备的树叶可以是字符树叶、网络树叶或块树叶，因此必须实现相应设备类的驱动。



