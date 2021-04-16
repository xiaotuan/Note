### 20.3.4 USB骨架程序

Linux内核源代码中的driver/usb/usb-skeleton.c文件为我们提供了一个最基础的USB驱动程序，即USB骨架程序，可被看做一个最简单的USB设备驱动实例。尽管具体USB设备驱动千差万别，但其骨架则万变不离其宗。

首先看看USB骨架程序的usb_driver结构体定义，如代码清单20.16所示。

代码清单20.16 USB骨架程序的usb_driver结构体

1 static struct usb_driver skel_driver = { 
 
 2 .name = "skeleton", 
 
 3 .probe = skel_probe, 
 
 4 .disconnect = skel_disconnect, 
 
 5 .suspend = skel_suspend, 
 
 6 .resume = skel_resume, 
 
 7 .pre_reset = skel_pre_reset, 
 
 8 .post_reset = skel_post_reset, 
 
 9 .id_table = skel_table, 
 
 10 .supports_autosuspend = 1, 
 
 11};

从上述代码第9行可以看出，它所支持的USB设备的列表数组为skel_table[]，其定义如代码清单20.17所示。

代码清单20.17 USB骨架程序的id_table

1 static struct usb_device_id skel_table [] = { 
 
 2 { USB_DEVICE(USB_SKEL_VENDOR_ID, USB_SKEL_PRODUCT_ID) }, 
 
 3 { } /* Terminating entry */ 
 
 4 }; 
 
 5 MODULE_DEVICE_TABLE(usb, skel_table);

对上述usb_driver的注册和注销发生在USB骨架程序的模块加载与卸载函数内，如代码清单20.18所示，其分别调用了usb_register()和usb_deregister()。

代码清单20.18 USB骨架程序的模块加载与卸载函数

1 static int __init usb_skel_init(void) 
 
 2 { 
 
 3 int result; 
 
 4 
 
 5 /* 注册USB驱动 */ 
 
 6 result = usb_register(&skel_driver); 
 
 7 if (result) 
 
 8 err("usb_register failed. Error number %d", result);



9 
 
 10 return result; 
 
 11 } 
 
 12 static void __exit usb_skel_exit(void) 
 
 13 { 
 
 14 /* 注销USB驱动 */ 
 
 15 usb_deregister(&skel_driver); 
 
 16 }

usb_driver的probe()成员函数中，会根据usb_interface的成员寻找第一个批量输入和输出端点，将端点地址、缓冲区等信息存入为USB骨架程序定义的usb_skel结构体，并将usb_skel实例的指针传入usb_set_intfdata()作为USB接口的私有数据，最后，它会注册USB设备，如代码清单20.19所示。

代码清单20.19 USB骨架程序的探测函数

1 static int skel_probe(struct usb_interface *interface, const struct usb_device_id *id) 
 
 2 { 
 
 3 struct usb_skel *dev = NULL; 
 
 4 struct usb_host_interface *iface_desc; 
 
 5 struct usb_endpoint_descriptor *endpoint; 
 
 6 size_t buffer_size; 
 
 7 int i; 
 
 8 int retval = -ENOMEM; 
 
 9 
 
 10 /* 分配设备状态的内存并初始化 */ 
 
 11 dev = kzalloc(sizeof(*dev), GFP_KERNEL); 
 
 12 if (dev == NULL) { 
 
 13 err("Out of memory"); 
 
 14 goto error; 
 
 15 } 
 
 16 kref_init(&dev→kref); 
 
 17 sema_init(&dev→limit_sem, WRITES_IN_FLIGHT); 
 
 18 
 
 19 dev→udev = usb_get_dev(interface_to_usbdev(interface)); 
 
 20 dev→interface = interface; 
 
 21 
 
 22 /* 设置端点信息 */ 
 
 23 /* 仅使用第一个bulk-in和bulk-out */ 
 
 24 iface_desc = interface→cur_altsetting; 
 
 25 for (i = 0; i < iface_desc→desc.bNumEndpoints; ++i) { 
 
 26 endpoint = &iface_desc→endpoint[i].desc; 
 
 27 
 
 28 if (!dev→bulk_in_endpointAddr && 
 
 29 ((endpoint→bEndpointAddress & USB_ENDPOINT_DIR_MASK) 
 
 30 == USB_DIR_IN) && 
 
 31 ((endpoint→bmAttributes & USB_ENDPOINT_XFERTYPE_MASK) 
 
 32 == USB_ENDPOINT_XFER_BULK)) { 
 
 33 /* 找到了一个批量IN端点 */ 
 
 34 buffer_size = le16_to_cpu(endpoint→wMaxPacketSize); 
 
 35 dev→bulk_in_size = buffer_size; 
 
 36 dev→bulk_in_endpointAddr = endpoint→bEndpointAddress; 
 
 37 dev→bulk_in_buffer = kmalloc(buffer_size, GFP_KERNEL); 
 
 38 if (!dev→bulk_in_buffer) {



39 err("Could not allocate bulk_in_buffer"); 
 
 40 goto error; 
 
 41 } 
 
 42 } 
 
 43 
 
 44 if (!dev→bulk_out_endpointAddr && 
 
 45 ((endpoint→bEndpointAddress & USB_ENDPOINT_DIR_MASK) 
 
 46 == USB_DIR_OUT) && 
 
 47 ((endpoint→bmAttributes & USB_ENDPOINT_XFERTYPE_MASK) 
 
 48 == USB_ENDPOINT_XFER_BULK)) { 
 
 49 /* 找到了一个批量OUT端点 */ 
 
 50 dev→bulk_out_endpointAddr = endpoint→bEndpointAddress; 
 
 51 } 
 
 52 } 
 
 53 if (!(dev→bulk_in_endpointAddr && dev→bulk_out_endpointAddr)) { 
 
 54 err("Could not find both bulk-in and bulk-out endpoints"); 
 
 55 goto error; 
 
 56 } 
 
 57 
 
 58 /* 在设备结构中保存数据指针 */ 
 
 59 usb_set_intfdata(interface, dev); 
 
 60 
 
 61 /* 注册USB设备 */ 
 
 
 62 retval = usb_register_dev(interface, &skel_class); 
 
 63 if (retval) { 
 
 64 /* something prevented us from registering this driver */ 
 
 65 err("Not able to get a minor for this device."); 
 
 66 usb_set_intfdata(interface, NULL); 
 
 67 goto error; 
 
 68 } 
 
 69 
 
 70 ... 
 
 71 }

usb_skel结构体可以被看作一个私有数据结构体，其定义如代码清单20.20所示，应该根据具体的设备量身定制。

代码清单20.20 USB骨架程序的自定义数据结构usb_skel

1 struct usb_skel { 
 
 2 struct usb_device * udev; /* 该设备的usb_device指针 */ 
 
 3 struct usb_interface * interface; /* 该设备的usb_interface指针 */ 
 
 4 struct semaphore limit_sem; /* 限制进程写的数量 */ 
 
 5 unsigned char * bulk_in_buffer; /* 接收数据的缓冲区 */ 
 
 6 size_t bulk_in_size; /* 接收缓冲区大小 */ 
 
 7 _ _u8 bulk_in_endpointAddr; /*批量IN端点的地址 */ 
 
 8 _ _u8 bulk_out_endpointAddr; /* 批量OUT端点的地址 */ 
 
 9 ... 
 
 10 struct mutex io_mutex; 
 
 11 };

USB骨架程序的断开函数会完成探测函数相反的工作，即设置接口数据为NULL，注销USB设备，如代码清单20.21所示。



代码清单20.21 USB骨架程序的断开函数

1 static void skel_disconnect(struct usb_interface *interface) 
 
 2 { 
 
 3 struct usb_skel *dev; 
 
 4 int minor = interface→minor; 
 
 5 
 
 6 /* 阻止skel_open()与skel_disconnect()的竞争 */ 
 
 7 lock_kernel(); 
 
 8 
 
 9 dev = usb_get_intfdata(interface); 
 
 10 usb_set_intfdata(interface, NULL); 
 
 11 
 
 12 /* 注销usb设备，释放次设备号 */ 
 
 13 usb_deregister_dev(interface, &skel_class); 
 
 14 
 
 15 unlock_kernel(); 
 
 16 
 
 17 /* 减少引用计数 */ 
 
 18 kref_put(&dev→kref, skel_delete); 
 
 19 
 
 20 info("USB Skeleton #%d now disconnected", minor); 
 
 21 }

代码清单20.18第62行的usb_register_dev(interface, &skel_class)中第二个参数包含了字符设备的file_operations结构体指针，而这个结构体中的成员实现也是USB字符设备的另一个组成成分。代码清单20.22给出了USB骨架程序的字符设备文件操作file_operations结构体的定义。

代码清单20.22 USB骨架程序的字符设备文件操作结构体

1 static const struct file_operations skel_fops = { 
 
 2 .owner = THIS_MODULE, 
 
 3 .read = skel_read, 
 
 4 .write = skel_write, 
 
 5 .open = skel_open, 
 
 6 .release = skel_release, 
 
 7 .flush = skel_flush, 
 
 8 };

由于只是一个象征性的骨架程序，open()成员函数的实现非常简单，它根据usb_driver和次设备号通过usb_find_interface()获得USB接口，之后通过usb_get_intfdata()获得接口的私有数据并赋予file→private_data，如代码清单20.23所示。

代码清单20.23 USB骨架程序的字符设备打开函数

1 static int skel_open(struct inode *inode, struct file *file) 
 
 2 { 
 
 3 struct usb_skel *dev; 
 
 4 struct usb_interface *interface; 
 
 5 int subminor; 
 
 6 int retval = 0; 
 
 7 
 
 8 subminor = iminor(inode); 
 
 9 
 
 10 interface = usb_find_interface(&skel_driver, subminor); /*获得接口数据*/ 
 
 11 ...



12 
 
 13 dev = usb_get_intfdata(interface); 
 
 14 ... 
 
 15 
 
 16 kref_get(&dev→kref); 
 
 17 
 
 18 mutex_lock(&dev→io_mutex); 
 
 19 
 
 20 if (!dev→open_count++) { 
 
 21 retval = usb_autopm_get_interface(interface); 
 
 22 if (retval) { 
 
 23 dev→open_count--; 
 
 24 mutex_unlock(&dev→io_mutex); 
 
 25 kref_put(&dev→kref, skel_delete); 
 
 26 goto exit; 
 
 27 } 
 
 28 } 
 
 29 
 
 30 file→private_data = dev;/* 将接口数据保存在file→private_data中 */ 
 
 31 mutex_unlock(&dev→io_mutex); 
 
 32 ... 
 
 33 }

由于在open()函数中并没有申请任何软件和硬件资源，因此与open()函数对应的release()函数不用进行资源的释放，它进行减少在open()中增加的引用计数等工作。

接下来要分析的是读写函数，前面已经提到，在访问USB设备的时候，贯穿于其中的“中枢神经”是urb结构体。

在skel_write()函数中进行的关于urb的操作与20.3.2小节的描述完全对应，即进行了urb的分配（调用usb_alloc_urb()）、初始化（调用usb_fill_bulk_urb()）和提交（调用usb_submit_urb()）的操作，如代码清单20.24所示。

代码清单20.24 USB骨架程序的字符设备写函数

1 static ssize_t skel_write(struct file *file, const char *user_buffer, size_t count, loff_t *ppos) 
 
 2 { 
 
 3 ... 
 
 4 /* 创建urb、urb的缓冲区，将数据复制给urb */ 
 
 5 urb = usb_alloc_urb(0, GFP_KERNEL); 
 
 6 ... 
 
 7 
 
 8 buf = usb_buffer_alloc(dev→udev, writesize, GFP_KERNEL, &urb→transfer_dma); 
 
 9 ... 
 
 10 
 
 11 if (copy_from_user(buf, user_buffer, writesize)) { 
 
 12 retval = -EFAULT; 
 
 13 goto error; 
 
 14 } 
 
 15 ... 
 
 16 
 
 17 /* 初始化urb */ 
 
 18 usb_fill_bulk_urb(urb, dev→udev, 
 
 19 usb_sndbulkpipe(dev→udev, dev→bulk_out_endpointAddr),



20 buf, writesize, skel_write_bulk_callback, dev); 
 
 21 urb→transfer_flags |= URB_NO_TRANSFER_DMA_MAP; 
 
 22 usb_anchor_urb(urb, &dev→submitted); 
 
 23 
 
 24 /* 将数据发送到批量端口 */ 
 
 25 retval = usb_submit_urb(urb, GFP_KERNEL); 
 
 26 ... 
 
 27 
 
 28 /* 释放对urb的引用，USB将最终完全释放之 */ 
 
 29 usb_free_urb(urb); 
 
 30 
 
 31 return writesize; 
 
 32 
 
 33 ... 
 
 34 }

写函数中发起的urb结束后，其完成函数skel_write_bulk_callback()将被调用，它会进行urb→status的判断，如代码清单20.25所示。

代码清单20.25 USB骨架程序的字符设备写操作完成函数

1 static void skel_write_bulk_callback(struct urb *urb, struct pt_regs *regs) 
 
 2 { 
 
 3 struct usb_skel *dev; 
 
 4 
 
 5 dev = (struct usb_skel *)urb→context; 
 
 6 
 
 7 ... 
 
 8 
 
 9 /* 释放被分配的内存 */ 
 
 10 usb_buffer_free(urb→dev, urb→transfer_buffer_length, 
 
 11 urb→transfer_buffer, urb→transfer_dma); 
 
 12 up(&dev→limit_sem); 
 
 13 }

USB骨架程序的字符设备读函数并没有进行类似写函数的一系列针对urb的操作，而是简单地调用usb_bulk_msg()发起一次同步urb传输操作，如代码清单20.26所示。

代码清单20.26 USB骨架程序的字符设备读函数

1 static ssize_t skel_read(struct file *file, char *buffer, size_t count, loff_t *ppos) 
 
 2 { 
 
 3 struct usb_skel *dev; 
 
 4 int retval = 0; 
 
 5 int bytes_read; 
 
 6 
 
 7 dev = (struct usb_skel *)file→private_data; 
 
 8 
 
 9 /* 从设备进行一次阻塞的批量读 */ 
 
 10 retval = usb_bulk_msg(dev→udev, 
 
 11 usb_rcvbulkpipe(dev→udev, dev→bulk_in_endpointAddr), 
 
 12 dev→bulk_in_buffer, 
 
 13 min(dev→bulk_in_size, count), 
 
 14 &bytes_read, 10000);



15 
 
 16 /* 如果读成功，将数据复制到用户空间 */ 
 
 17 if (!retval) { 
 
 18 if (copy_to_user(buffer, dev→bulk_in_buffer, bytes_read)) 
 
 19 retval = -EFAULT; 
 
 20 else 
 
 21 retval = bytes_read; 
 
 22 } 
 
 23 
 
 24 return retval; 
 
 25 }

