### 21.1.2 PCI设备的Linux描述

在Linux系统中，所有种类的PCI设备都可以用pci_dev结构体来描述，由于一个PCI接口卡上可能包含多个功能模块，每个功能被当作一个独立的逻辑设备，因此，每一个PCI功能，即PCI逻辑设备都惟一地对应一个pci_dev设备描述符，该结构体的定义如代码清单21.2所示。

代码清单21.2 pci_dev结构体

1 struct pci_dev { 
 
 2 struct list_head bus_list; 
 
 3 struct pci_bus *bus; /* 这个PCI设备所在的PCI总线的pci_bus结构 */ 
 
 4 struct pci_bus *subordinate; /* 指向这个PCI设备所桥接的下级总线 */ 
 
 5 
 
 6 void *sysdata; /* 指向一片特定于系统的扩展数据 */ 
 
 7 struct proc_dir_entry *procent; /* 该PCI设备在/proc/bus/pci中对应的目录项 */ 
 
 8 struct pci_slot *slot; /* 设备位于的物理插槽 */ 
 
 9 unsigned int devfn; /* 这个PCI设备的设备功能号 */ 
 
 10 unsigned short vendor; /* PCI设备的厂商ID*/ 
 
 11 unsigned short device; /* PCI设备的设备ID */ 
 
 12 unsigned short subsystem_vendor; /* PCI设备的子系统厂商ID */ 
 
 13 unsigned short subsystem_device; /* PCI设备的子系统设备ID */ 
 
 14 unsigned int class ; /* 32位的无符号整数，表示该PCI设备的类别, 
 
 15 bit［7∶0］为编程接口，bit［15∶8］为子类别代码，bit［23∶16］ 
 
 16 为基类别代码，bit［31∶24］无意义 */ 
 
 17 u8 hdr_type; /* PCI配置空间头部的类型 */



18 u8 pcie_type; /* PCI-E 设备/端口类型 */ 
 
 19 u8 rom_base_reg; /* 表示PCI配置空间中的ROM基地址寄存器在PCI配置空间中的位置 */ 
 
 20 u8 pin; /* 中断引脚 */ 
 
 21 struct pci_driver *driver; /* 指向这个PCI设备所对应的驱动pci_driver结构 */ 
 
 22 u64 dma_mask; /* 该设备支持的总线地址位掩码，通常是0xffffffff */ 
 
 23 struct device_dma_parameters dma_parms; 
 
 24 pci_power_t current_state; /* 当前的操作状态 */ 
 
 25 int pm_cap; 
 
 26 unsigned int pme_support:5; 
 
 27 unsigned int d1_support:1; /* 支持low power状态 D1 ? */ 
 
 28 unsigned int d2_support:1; /* 支持low power状态 D2? */ 
 
 29 unsigned int no_d1d2:1; /* 仅允许D0和D3 ? */ 
 
 30 pci_channel_state_t error_state; 
 
 31 struct device dev; /* 通用的设备接口 */ 
 
 32 int cfg_size; /* 配置空间大小 */ 
 
 33 
 
 34 unsigned int irq; 
 
 35 struct resource resource[DEVICE_COUNT_RESOURCE]; 
 
 36 /*表示该设备可能用到的资源，包括： 
 
 37 I/O端口区域、设备内存地址区域以及扩展ROM地址区域 */ 
 
 38 
 
 39 unsigned int transparent: 1; /* 透明PCI桥 ? */ 
 
 40 unsigned int multifunction: 1; /* 多功能设备 ? */ 
 
 41 /* 跟踪设备状态 */ 
 
 42 unsigned int is_added:1; 
 
 43 unsigned int is_busmaster: 1; /* 设备是主设备？ */ 
 
 44 unsigned int no_msi: 1; /* 设备可不使用msi？ */ 
 
 45 unsigned int block_ucfg_access:1; /* 不允许用户空间访问配置空间 ? */ 
 
 46 ... 
 
 47 u32 saved_config_space[16]; /* 挂起时保存的配置空间 */ 
 
 48 struct bin_attribute *rom_attr; /* sysfs ROM入口的属性描述 */ 
 
 49 int rom_attr_enabled; 
 
 50 struct bin_attribute *res_attr[DEVICE_COUNT_RESOURCE];/*资源的sysfs文件*/ 
 
 51 ... 
 
 52 };

