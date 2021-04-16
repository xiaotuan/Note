### 20.2.1 USB主机控制器驱动的整体结构

USB主机控制器有3种规格：OHCI (Open Host Controller Interface)、UHCI (Universal Host Controller Interface) 和EHCI (Enhanced Host Controller Interface)。OHCI驱动程序用来为非PC 系统上以及带有SiS和ALi芯片组的PC主板上的USB芯片提供支持。UHCI驱动程序多用来为大多数其他PC主板（包括Intel和Via）上的USB芯片提供支持。EHCI由USB 2.0规范所提出，它兼容于OHCI和UHCI。UHCI的硬件线路比OHCI简单，所以成本较低，但需要较复杂的驱动程序，CPU负荷稍重。本节将重点介绍嵌入式系统中常用的OHCI主机控制器驱动。

#### 1．主机控制器驱动

在Linux内核中，用usb_hcd结构体描述USB主机控制器驱动，它包含USB主机控制器的“家务”信息、硬件资源、状态描述和用于操作主机控制器的hc_driver等，其定义如代码清单20.6所示。

代码清单20.6 usb_hcd结构体

1 struct usb_hcd { 
 
 2 /* 
 
 3 * housekeeping 
 
 4 */ 
 
 5 struct usb_bus self; /* hcd是一个bus */ 
 
 6 struct kref kref; 
 
 7 
 
 8 const char *product_desc; /* 产品/厂商字符串 */ 
 
 9 char irq_descr[24]; /* driver + bus # */ 
 
 10 
 
 11 struct timer_list rh_timer; /* 驱动根hub的polling */ 
 
 12 struct urb *status_urb; /* 目前的状态urb */ 
 
 13 #ifdef CONFIG_PM 
 
 14 struct work_struct wakeup_work; /* 用于远程唤醒 */ 
 
 15 #endif 
 
 16 
 
 17 /* 
 
 18 * 硬件信息/状态 
 
 19 */ 
 
 
 20 const struct hc_driver*driver; /* 
 硬件特定的钩子函数 
 */ 
 
 21 
 
 22 /* 需要被自动操作的标志 */ 
 
 23 unsigned long flags; 
 
 24 #define HCD_FLAG_HW_ACCESSIBLE 0x00000001 
 
 25 #define HCD_FLAG_SAW_IRQ 0x00000002 
 
 26 
 
 27 unsigned rh_registered:1;/* 根Hub已被注册？ */ 
 
 28 
 
 29 /* 下一个标志的采用只是“权益之计”，当所有HCDs支持新的根Hub轮询机制后将移除 */ 
 
 31 unsigned uses_new_polling:1; 
 
 32 unsigned poll_rh:1; /* 轮询根Hub状态? */ 
 
 33 unsigned poll_pending:1; /* 状态改变了吗? */ 
 
 34 unsigned wireless:1; /* 无线USB HCD? */ 
 
 35 unsigned authorized_default:1; 
 
 36 unsigned has_tt:1; /* 根hub集成了TT? */ 
 
 37 
 
 38 int irq; /* 分配的中断号 */ 
 
 39 void __iomem *regs; /* 设备内存或I/O */ 
 
 40 u64 rsrc_start; /* 内存或I/O资源开始位置 */ 
 
 41 u64 rsrc_len; /* 内存或I/O资源大小 */ 
 
 42 unsigned power_budget; /* in mA, 0 = no limit */



43 
 
 44 #define HCD_BUFFER_POOLS 4 
 
 45 struct dma_pool *pool [HCD_BUFFER_POOLS]; 
 
 46 
 
 47 int state; 
 
 48 
 
 49 /* 主机控制器驱动的私有数据 */ 
 
 52 unsigned long hcd_priv[0] 
 
 53 __attribute__ ((aligned(sizeof(unsigned long)))); 
 
 54 };

usb_hcd中的hc_driver成员非常重要，它包含具体的用于操作主机控制器的钩子函数，其定义如代码清单20.7所示。

代码清单20.7 hc_driver结构体

1 struct hc_driver { 
 
 2 const char *description; /* "ehci-hcd" 等 */ 
 
 3 const char *product_desc; /* 产品/厂商字符串 */ 
 
 4 size_t hcd_priv_size; /* 私有数据的大小 */ 
 
 5 
 
 6 /* 中断处理函数 */ 
 
 7 irqreturn_t(*irq)(struct usb_hcd *hcd); 
 
 8 
 
 9 int flags; 
 
 10 #define HCD_MEMORY 0x0001 /* HC寄存器使用的内存和I/O */ 
 
 11 #define HCD_USB11 0x0010 /* USB 1.1 */ 
 
 12 #define HCD_USB2 0x0020 /* USB 2.0 */ 
 
 13 
 
 14 /* 被调用以初始化HCD和根Hub */ 
 
 15 int(*reset)(struct usb_hcd *hcd); 
 
 16 int(*start)(struct usb_hcd *hcd); 
 
 17 
 
 18 /* 挂起Hub后，进入D3(etc)前被调用 */ 
 
 19 int(*pci_suspend)(struct usb_hcd *hcd, pm_message_t message); 
 
 20 
 
 21 /* 在进入D0(etc)后，恢复Hub前调用 */ 
 
 22 int(*pci_resume)(struct usb_hcd *hcd); 
 
 23 
 
 24 /* 使HCD停止写内存和进行I/O操作 */ 
 
 25 void (*stop)(struct usb_hcd *hcd); 
 
 26 
 
 27 /* 关闭HCD */ 
 
 28 void (*shutdown) (struct usb_hcd *hcd); 
 
 29 
 
 30 /* 返回目前的帧数 */ 
 
 31 int(*get_frame_number)(struct usb_hcd *hcd); 
 
 32 
 
 33 /* 管理I/O请求和设备状态 */ 
 
 34 int (*urb_enqueue)(struct usb_hcd *hcd, struct urb *urb, gfp_t mem_flags); 
 
 35 int (*urb_dequeue)(struct usb_hcd *hcd, struct urb *urb, int status); 
 
 36 
 
 37 /* 释放endpoint资源 */ 
 
 38 void(*endpoint_disable)(struct usb_hcd *hcd, struct usb_host_endpoint *ep); 
 
 39 
 
 40 /* 根Hub支持 */



41 int(*hub_status_data)(struct usb_hcd *hcd, char *buf); 
 
 42 int(*hub_control)(struct usb_hcd *hcd, u16 typeReq, u16 wValue, u16 wIndex, 
 
 43 char *buf, u16 wLength); 
 
 44 int(*bus_suspend)(struct usb_hcd*); 
 
 45 int(*bus_resume)(struct usb_hcd*); 
 
 46 int(*start_port_reset)(struct usb_hcd *, unsigned port_num); 
 
 47 void (*relinquish_port)(struct usb_hcd *, int); 
 
 48 int (*port_handed_over)(struct usb_hcd *, int); 
 
 49 };

在Linux内核中，使用如下函数来创建HCD：

struct usb_hcd *usb_create_hcd (const struct hc_driver *driver, 
 
 struct device *dev, char *bus_name);

如下函数被用来增加和移除HCD：

int usb_add_hcd(struct usb_hcd *hcd, 
 
 unsigned int irqnum, unsigned long irqflags); 
 
 void usb_remove_hcd(struct usb_hcd *hcd);

第34行的urb_enqueue()函数非常关键，实际上，上层通过usb_submit_urb()提交1个USB请求后，该函数调用usb_hcd_submit_urb()，并最终调用至usb_hcd的driver成员（hc_driver类型）的urb_enqueue()。这里可以先建立一点印象，不理解没有关系，后文会看地更加清楚。

#### 2．OHCI主机控制器驱动

OHCI HCD驱动属于HCD驱动的实例，它定义了一个ohci_hcd结构体，作为代码清单20.6给出的usb_hcd结构体的私有数据，这个结构体的定义如代码清单20.8所示。

代码清单20.8 ohci_hcd结构体

1 struct ohci_hcd { 
 
 2 spinlock_t lock; 
 
 3 
 
 4 /* 与主机控制器通信的I/O内存(DMA一致) */ 
 
 5 struct ohci_regs _ _iomem *regs; 
 
 6 
 
 7 /* 与主机控制器通信的主存(DMA一致) */ 
 
 8 struct ohci_hcca *hcca; 
 
 9 dma_addr_t hcca_dma; 
 
 10 
 
 11 struct ed *ed_rm_list; /* 将被移除 */ 
 
 12 struct ed *ed_bulktail; /* 批量队列尾 */ 
 
 13 struct ed *ed_controltail; /* 控制队列尾 */ 
 
 14 struct ed *periodic[NUM_INTS]; /* int_table“影子” */ 
 
 15 
 
 16 /* OTG控制器和收发器需要软件交互，其他的外部收发器应该是软件透明的 */ 
 
 17 struct otg_transceiver *transceiver; 
 
 18 void (*start_hnp)(struct ohci_hcd *ohci); 
 
 19 
 
 20 /* 队列数据的内存管理 */ 
 
 21 struct dma_pool *td_cache; 
 
 22 struct dma_pool *ed_cache; 
 
 23 struct td *td_hash[TD_HASH_SIZE]; 
 
 24 struct list_head pending; 
 
 25 
 
 26 /* driver状态 */ 
 
 27 int num_ports;



28 int load[NUM_INTS]; 
 
 29 u32 hc_control; /* 主机控制器控制寄存器的复制 */ 
 
 30 unsigned long next_statechange; /* 挂起/恢复 */ 
 
 31 u32 fminterval; /* 被保存的寄存器 */ 
 
 32 unsigned autostop:1; 
 
 33 unsigned long flags; 
 
 34 struct work_struct nec_work; 
 
 35 struct timer_list unlink_watchdog; 
 
 36 unsigned eds_scheduled; 
 
 37 struct ed *ed_to_check; 
 
 38 unsigned zf_delay; 
 
 39 };

使用如下内联函数可实现usb_hcd和ohci_hcd的相互转换：

struct ohci_hcd *hcd_to_ohci (struct usb_hcd *hcd); 
 
 struct usb_hcd *ohci_to_hcd (const struct ohci_hcd *ohci);

从usb_hcd得到ohci_hcd只是取得“私有”数据，而从ohci_hcd得到usb_hcd则是通过container_of()从结构体成员获得结构体指针。

使用如下函数可初始化OHCI主机控制器：

int ohci_init (struct ohci_hcd *ohci);

如下函数分别用于开启、停止及复位OHCI控制器：

int ohci_run (struct ohci_hcd *ohci); 
 
 void ohci_stop (struct usb_hcd *hcd); 
 
 void ohci_usb_reset (struct ohci_hcd *ohci);

OHCI主机控制器驱动的主机工作仍然是实现代码清单20.7给出的hc_driver结构体中的成员函数。

