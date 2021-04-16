### 20.4.1 UDC和gadget驱动关键数据结构与API

这里的USB设备控制器（UDC）驱动指作为其他USB主机控制器外设的USB硬件设备上底层硬件控制器的驱动，该硬件和驱动负责将一个USB设备依附于一个USB主机控制器上。例如，当某运行Linux的手机作为PC的U盘时，手机中的底层USB控制器行使USB设备控制器的功能，这时候运行在底层的是UDC驱动，而手机要成为U盘，在UDC驱动之上仍然需要另外一个驱动，对于USB大容量存储器为file storage驱动，这一驱动称为gadget驱动。从图20.1左边可以看出，USB设备驱动调用USB核心的API，因此具体驱动与SoC无关；同样，从图20.1右边可以看出，USB gadget驱动调用通用的gadget API，因此具体gadget驱动也变得与SoC无关。软件分层设计的好处再一次得到了深刻的体现。

UDC驱动和gadget驱动都位于内核的drivers/usb/gadget目录，omap_udc.c、pxa27x_udc.c、m66592-udc.c、s3c2410_udc.c等是对应SoC平台上的UDC驱动，ether.c、f_serial.c、file_storage.c等文件实现了一些gadget驱动，重要的gadget驱动如下所示。

Gadget Zero：该驱动用于测试udc驱动，它会帮助您通过USB-IF测试。

Ethernet over USB：该驱动模拟以太网网口，它支持多种运行方式—CDC Ethernet（实现标准的Communications Device Class "Ethernet Model" 协议）、CDC Subset（由于硬件受限，仅实现CDC Ethernet的一个子集，不含altsetting）以及RNDIS（微软公司对 CDC Ethernet 的变种实现）这几种模式。

File-backed Storage Gadget：最常见的U盘功能实现。

Serial Gadget：包括Generic Serial实现（只需要Bulk-in/Bulk-out端点+ep0）和CDC ACM 规范实现。内核源代码中的Documentation/usb/gadget_serial.txt文档讲解了如何将Serial Gadget与Windows和Linux主机连接。

Gadget MIDI：暴露ALSA MIDI接口。

另外，drivers/usb/gadget源代码还实现了一个Gadget文件系统（GadgetFS），可以将Gadget API接口暴露给应用层，以便在应用层实现用户空间的驱动。

在USB设备控制器与gadget驱动中，我们主要关心几个核心的数据结构，这些数据结构包括描述一个USB设备控制器的usb_gadget、描述一个gadget驱动的usb_gadget_driver、表示一个传输请求的usb_request（与从主机端看到的urb相似）、描述一个端点的usb_ep、描述端点操作的usb_ep_ops结构体。UDC和gadget驱动围绕这些数据结构及其成员函数而展开，代码清单20.31列出了这些关键的数据结构，都定义于include/linux/usb/gadget.h文件。

代码清单20.31 UDC和gadget驱动关键数据结构

1 struct usb_gadget { 
 
 2 /* 针对gadget驱动只读 */ 
 
 3 const struct usb_gadget_ops *ops; /* 访问硬件的函数 */ 
 
 4 struct usb_ep *ep0; /* endpoint 0，setup使用 */ 
 
 5 struct list_head ep_list; /* 其他endpoint的列表 */ 
 
 6 enum usb_device_speed speed; 
 
 7 unsigned is_dualspeed:1;7 
 
 8 unsigned is_otg:1; 
 
 9 unsigned is_a_peripheral:1; 
 
 10 unsigned b_hnp_enable:1; /* A-HOST使能了HNP支持 */ 
 
 11 unsigned a_hnp_support:1; /* A-HOST支持HNP */ 
 
 12 unsigned a_alt_hnp_support:1; 
 
 13 const char *name;



14 struct device dev; 
 
 15 }; 
 
 16 
 
 17 struct usb_gadget_driver { 
 
 18 char *function; /* 描述gadget功能的字符串 */ 
 
 19 enum usb_device_speed speed; 
 
 20 int (*bind)(struct usb_gadget *); /* 当驱动与gadget绑定时调用 */ 
 
 21 void (*unbind)(struct usb_gadget *); 
 
 22 int (*setup)(struct usb_gadget *, /* 处理硬件驱动未处理的ep0请求 */ 
 
 23 const struct usb_ctrlrequest *); 
 
 24 void (*disconnect)(struct usb_gadget *); 
 
 25 void (*suspend)(struct usb_gadget *); 
 
 26 void (*resume)(struct usb_gadget *); 
 
 27 
 
 28 struct device_driver driver; 
 
 29 }; 
 
 30 
 
 31 struct usb_request { 
 
 32 void *buf; 
 
 33 unsigned length; 
 
 34 dma_addr_t dma; 
 
 35 
 
 36 unsigned no_interrupt:1; 
 
 37 unsigned zero:1; 
 
 38 unsigned short_not_ok:1; 
 
 39 
 
 40 void (*complete)(struct usb_ep *ep, 
 
 41 struct usb_request *req); /* 当请求完成时调用的函数 */ 
 
 42 void *context; 
 
 43 struct list_head list; 
 
 44 
 
 45 int status; 
 
 46 unsigned actual; 
 
 47 }; 
 
 48 
 
 49 struct usb_ep { 
 
 50 void *driver_data; 
 
 51 
 
 52 const char *name; 
 
 53 const struct usb_ep_ops *ops; 
 
 54 struct list_head ep_list; 
 
 55 unsigned maxpacket:16; 
 
 56 }; 
 
 57 
 
 58 struct usb_ep_ops { 
 
 59 int (*enable) (struct usb_ep *ep, 
 
 60 const struct usb_endpoint_descriptor *desc); 
 
 61 int (*disable) (struct usb_ep *ep); 
 
 62 
 
 63 struct usb_request *(*alloc_request) (struct usb_ep *ep, 
 
 64 gfp_t gfp_flags); 
 
 65 void (*free_request) (struct usb_ep *ep, struct usb_request *req); 
 
 66



67 int (*queue) (struct usb_ep *ep, struct usb_request *req, 
 
 68 gfp_t gfp_flags);/* 将usb_request提交给endPoint，进行数据传输 */ 
 
 69 int (*dequeue) (struct usb_ep *ep, struct usb_request *req); 
 
 70 
 
 71 int (*set_halt) (struct usb_ep *ep, int value); 
 
 72 int (*set_wedge) (struct usb_ep *ep); 
 
 73 
 
 74 int (*fifo_status) (struct usb_ep *ep); 
 
 75 void (*fifo_flush) (struct usb_ep *ep); 
 
 76 };

在具体的UDC驱动中，需要封装usb_gadget和每个端点usb_ep，实现端点的usb_ep_ops，完成usb_request。另外，usb_gadget_register_driver()、usb_gadget_unregister_driver()这两个API需要由UDC驱动提供，gadget驱动会调用它们，其原型分别为：

int usb_gadget_register_driver(struct usb_gadget_driver *driver); 
 
 int usb_gadget_unregister_driver(struct usb_gadget_driver *driver);

usb_gadget_register_driver()通常在gadget驱动的模块初始化时调用，该函数中通常会调用driver→bind()函数，将该usb_gadget_driver与具体的gadget绑定，该函数最好放在init节内。

usb_gadget_register_driver()通常在gadget驱动的模块卸载时调用，告诉底层的UDC驱动不再投入工作。如果UDC正与USB主机连接，会先调用driver→disconnect()函数，在usb_ gadget_register_driver()函数返回前，也需调用driver→unbind()函数。所以unbind()函数适合放在exit节。

在linux/usb/gadget.h中，还封装了一些常用的API，如下所示。

（1）使能和禁止端点。

static inline int usb_ep_enable(struct usb_ep *ep, 
 
 const struct usb_endpoint_descriptor *desc); 
 
 static inline int usb_ep_disable(struct usb_ep *ep);

它们分别调用了“ep→ops→enable(ep, desc);”和“ep→ops→disable(ep);”。

（2）分配和释放usb_request。

static inline struct usb_request *usb_ep_alloc_request(struct usb_ep *ep, 
 
 gfp_t gfp_flags); 
 
 static inline void usb_ep_free_request(struct usb_ep *ep, 
 
 struct usb_request *req);

它们分别调用了“ep→ops→alloc_request(ep, gfp_flags);”和“ep→ops→free_request(ep, req);”。用于分配和释放一个依附于某端点的usb_request。

（3）提交和取消usb_request。

static inline int usb_ep_queue(struct usb_ep *ep, 
 
 struct usb_request *req, gfp_t gfp_flags); 
 
 static inline int usb_ep_dequeue(struct usb_ep *ep, struct usb_request *req);

它们分别调用“ep→ops→queue(ep, req, gfp_flags) ;”和“ep→ops→dequeue(ep, req);”。usb_ep_queue函数告诉UDC完成usb_request（读写buffer），当请求被完成后，该请求对应的completion函数会被调用。

（4）端点FIFO管理。

static inline int usb_ep_fifo_status(struct usb_ep *ep); 
 
 static inline void usb_ep_fifo_flush(struct usb_ep *ep);

前者调用“ep→ops→fifo_status(ep)”返回目前FIFO中的字节数，后者调用“ep→ops→fifo_flush(ep)”以flush掉FIFO中的数据。

（5）返回目前的帧号。

static inline int usb_gadget_frame_number(struct usb_gadget *gadget);

它调用“gadget→ops→get_frame(gadget)”返回目前的帧号，正常为自SOF以来的一个11位数，如果设备不支持该能力，则返回出错码。

（6）管理配置描述符。

int usb_descriptor_fillbuf(void *, unsigned, 
 
 const struct usb_descriptor_header **); 
 
 int usb_gadget_config_buf(const struct usb_config_descriptor *config, 
 
 void *buf, unsigned buflen, const struct usb_descriptor_header **desc); 
 
 static inline void usb_free_descriptors(struct usb_descriptor_header **v);

其他API还包括usb_gadget_vbus_connect()、usb_gadget_vbus_disconnect()、usb_ep_set_halt()、usb_ep_clear_halt()、usb_gadget_vbus_draw()、usb_gadget_wakeup()、usb_gadget_set_selfpowered()、usb_gadget_clear_selfpowered()、usb_gadget_connect()、usb_gadget_disconnect、usb_ep_set_wedge()等，处理USB总线上的一些电源管理、OTG协议等，详见include/linux/usb/gadget.h。

