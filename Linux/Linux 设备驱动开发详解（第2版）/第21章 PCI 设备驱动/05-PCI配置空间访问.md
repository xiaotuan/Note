### 21.1.3 PCI配置空间访问

PCI有3种地址空间：PCI I/O空间、PCI内存地址空间和PCI配置空间。CPU可以访问所有的地址空间，其中PCI I/O空间和PCI内存地址空间由设备驱动程序使用。PCI支持自动配置设备，与旧的ISA驱动程序不一样，PCI驱动程序不需要实现复杂的检测逻辑。启动时，BIOS或内核自身会遍历PCI总线并分配资源，如中断优先级和I/O基址。设备驱动程序通过PCI配置空间来找到资源分配情况。

PCI规范定义了3种类型的PCI配置空间头部，其中type 0用于标准的PCI设备，type 1用于PCI桥，type 2用于PCI CardBus桥。如图2.17所示，不管是哪一种类型的配置空间头部，其前16个字节的格式都是相同的，/include/linux/pci_regs.h文件中定义了PCI配置空间头部，如代码清单21.3所示。

代码清单21.3 PCI配置空间头部寄存器定义

1 #define PCI_VENDOR_ID 0x00 /* 16位厂商ID */ 
 
 2 #define PCI_DEVICE_ID 0x02 /* 16位设备ID */ 
 
 3 
 
 4 /* PCI命令寄存器 */



5 #define PCI_COMMAND 0x04 /* 16位 */ 
 
 6 #define PCI_COMMAND_IO 0x1 /* 使能设备响应对I/O空间的访问 */ 
 
 7 #define PCI_COMMAND_MEMORY 0x2 /* 使能设备响应对存储空间的访问 */ 
 
 8 #define PCI_COMMAND_MASTER 0x4 /* 使能总线主模式 */ 
 
 9 #define PCI_COMMAND_SPECIAL 0x8 /* 使能设备响应特殊周期 */ 
 
 10 #define PCI_COMMAND_INVALIDATE 0x10 /*使用PCI内存写无效事务 */ 
 
 11 #define PCI_COMMAND_VGA_PALETTE 0x20 /* 使能VGA调色板侦测 */ 
 
 12 #define PCI_COMMAND_PARITY 0x40 /* 使能奇偶校验 */ 
 
 13 #define PCI_COMMAND_WAIT 0x80 /* 使能地址/数据步进 */ 
 
 14 #define PCI_COMMAND_SERR 0x100 /* 使能SERR */ 
 
 15 #define PCI_COMMAND_FAST_BACK 0x200 /* 使能背靠背写 */ 
 
 16 #define PCI_COMMAND_INTX_DISABLE 0x400 /* 禁止中断竞争*/ 
 
 17 
 
 18 /* PCI状态寄存器 */ 
 
 19 #define PCI_STATUS 0x06 /* 16位 */ 
 
 20 #define PCI_STATUS_CAP_LIST 0x10 /* 支持的能力列表 */ 
 
 21 #define PCI_STATUS_66MHz 0x20 /* 支持PCI 2.1 66MHz */ 
 
 22 #define PCI_STATUS_UDF 0x40 /* 支持用户定义的特征 */ 
 
 23 #define PCI_STATUS_FAST_BACK 0x80 /* 快速背靠背操作 */ 
 
 24 #define PCI_STATUS_PARITY 0x100 /* 侦测到奇偶校验错 */ 
 
 25 #define PCI_STATUS_DEVSEL_MASK 0x600 /* DEVSEL定时 */ 
 
 26 #define PCI_STATUS_DEVSEL_FAST 0x000 
 
 27 #define PCI_STATUS_DEVSEL_MEDIUM 0x200 
 
 28 #define PCI_STATUS_DEVSEL_SLOW 0x400 
 
 29 #define PCI_STATUS_SIG_TARGET_ABORT 0x800 /* 目标设备异常 */ 
 
 30 #define PCI_STATUS_REC_TARGET_ABORT 0x1000 /* 主设备确认 */ 
 
 31 #define PCI_STATUS_REC_MASTER_ABORT 0x2000 /* 主设备异常 */ 
 
 32 #define PCI_STATUS_SIG_SYSTEM_ERROR 0x4000 /* 驱动了SERR */ 
 
 33 #define PCI_STATUS_DETECTED_PARITY 0x8000 /* 奇偶校验错 */ 
 
 34 
 
 35 /* 类代码寄存器和修订版本寄存器 */ 
 
 36 #define PCI_CLASS_REVISION 0x08 /* 高24位为类码，低8位为修订版本 */ 
 
 37 #define PCI_REVISION_ID 0x08 /* 修订号 */ 
 
 38 #define PCI_CLASS_PROG 0x09 /* 编程接口 */ 
 
 39 #define PCI_CLASS_DEVICE 0x0a /* 设备类 */ 
 
 40 #define PCI_CACHE_LINE_SIZE 0x0c /* 8位 */ 
 
 41 #define PCI_LATENCY_TIMER 0x0d /* 8位 */ 
 
 42 
 
 43 /* PCI头类型 */ 
 
 44 #define PCI_HEADER_TYPE 0x0e /* 8位头类型 */ 
 
 45 #define PCI_HEADER_TYPE_NORMAL 0 
 
 46 #define PCI_HEADER_TYPE_BRIDGE 1 
 
 47 #define PCI_HEADER_TYPE_CARDBUS 2 
 
 48 
 
 49 /* 表示配置空间头部中的Built-In Self-Test寄存器在配置空间中的字节地址索引 */ 
 
 50 #define PCI_BIST 0x0f /* 8 位 */ 
 
 51 #define PCI_BIST_CODE_MASK 0x0f /* 完成代码 */ 
 
 52 #define PCI_BIST_START 0x40 /* 用于启动BIST*/ 
 
 53 #define PCI_BIST_CAPABLE 0x80 /* 设备是否支持BIST？ */

紧接着前16个字节的寄存器为基地址寄存器0～基地址寄存器5，其中，PCI_BASE_ADDRESS_ 2～5仅对标准PCI设备的0类型配置空间头部有意义，而PCI_BASE_ADDRESS_0～1则适用于0类型和1类型配置空间头部。

基地址寄存器中的bit［0］的值决定了这个基地址寄存器所指定的地址范围是在I/O空间还是在内存映射空间内进行译码。当基地址寄存器所指定的地址范围位于内存映射空间中时，其bit ［2∶1］表示内存地址的类型，bit［3］表示内存范围是否为可预取（Prefetchable）的内存。

1类型配置空间头部适用于PCI-PCI桥设备，其基地址寄存器0与基地址寄存器1可以用来指定桥设备本身可能要用到的地址范围，而后40个字节（0x18～0x39）则被用来配置桥设备的主、次编号以及地址过滤窗口等信息。

pci_bus结构体中的pci_ops类型成员指针ops指向该PCI总线所使用的配置空间访问操作的具体实现，pci_ops 结构体的定义如代码清单21.4所示。

代码清单21.4 pci_ops结构体

1 struct pci_ops { 
 
 2 int(*read)(struct pci_bus *bus, unsigned int devfn, int where, int size, u32 
 
 3 *val);/* 读配置空间 */ 
 
 4 int(*write)(struct pci_bus *bus, unsigned int devfn, int where, int size, u32 
 
 5 val); /* 写配置空间 */ 
 
 6 };

read()和write()成员函数中的size表示访问的是字节、2字节还是4字节，对于write()而言，val是要写入的值；对于read()而言，val是要返回的读取到的值的指针。通过bus参数的成员以及devfn可以定位相应PCI总线上相应PCI逻辑设备的配置空间。在Linux设备驱动中，可用如下一组函数来访问配置空间：

inline int pci_read_config_byte(struct pci_dev *dev, int where, u8 *val); 
 
 inline int pci_read_config_word(struct pci_dev *dev, int where, u16 *val); 
 
 inline int pci_read_config_dword(struct pci_dev *dev, int where, u32 *val); 
 
 inline int pci_write_config_byte(struct pci_dev *dev, int where, u8 val); 
 
 inline int pci_write_config_word(struct pci_dev *dev, int where, u16 val); 
 
 inline int pci_write_config_dword(struct pci_dev *dev, int where, u32 val);

上述函数只是对如下函数进行调用：

int pci_bus_read_config_byte (struct pci_bus *bus, unsigned int devfn, int where, u8 *val); 
 
 /* 读字节 */ 
 
 int pci_bus_read_config_word (struct pci_bus *bus, unsigned int devfn, int where, u16 
 
 *val); /* 读字 */ 
 
 int pci_bus_read_config_dword (struct pci_bus *bus, unsigned int devfn, int where, u32 
 
 *val); /* 读双字 */ 
 
 int pci_bus_write_config_byte (struct pci_bus *bus, unsigned int devfn, int where, u8 
 
 val); /* 写字节 */ 
 
 int pci_bus_write_config_word (struct pci_bus *bus, unsigned int devfn, int where, u16 
 
 val); /* 写字 */ 
 
 int pci_bus_write_config_dword (struct pci_bus *bus, unsigned int devfn, int where, u32 
 
 val); /* 写双字 */

最后，我们来看一下PCI总线、设备与驱动在/proc和/sysfs文件系统中的描述。首先，通过查看/proc/bus/pci中的文件，可以获得系统连接的PCI设备的基本信息描述。在本书配套虚拟机Linux上的/proc/bus/pci目录下的树型结构如下：

/proc/bus/pci 
 
 |-- 00 
 
 | |-- 00.0 
 
 | |-- 01.0 
 
 | |-- 01.1 
 
 | |-- 02.0 
 
 | |-- 03.0



| |-- 04.0 
 
 | |-- 05.0 
 
 | |-- 06.0 
 
 | |-- 07.0 
 
 | `-- 0b.0 
 
 `-- devices

1 directory, 11 files

sysfs文件系统/sys/bus/pci目录中也给出了系统中总线上挂接的设备及驱动信息，该目录下的树型结构如下：

/sys/bus/pci 
 
 |-- devices 
 
 | |-- 0000:00:00.0 → ../../../devices/pci0000:00/0000:00:00.0 
 
 | |-- 0000:00:01.0 → ../../../devices/pci0000:00/0000:00:01.0 
 
 | |-- 0000:00:01.1 → ../../../devices/pci0000:00/0000:00:01.1 
 
 | |-- 0000:00:02.0 → ../../../devices/pci0000:00/0000:00:02.0 
 
 | |-- 0000:00:03.0 → ../../../devices/pci0000:00/0000:00:03.0 
 
 | |-- 0000:00:04.0 → ../../../devices/pci0000:00/0000:00:04.0 
 
 | |-- 0000:00:05.0 → ../../../devices/pci0000:00/0000:00:05.0 
 
 | |-- 0000:00:06.0 → ../../../devices/pci0000:00/0000:00:06.0 
 
 | |-- 0000:00:07.0 → ../../../devices/pci0000:00/0000:00:07.0 
 
 | `-- 0000:00:0b.0 → ../../../devices/pci0000:00/0000:00:0b.0 
 
 |-- drivers 
 
 | |-- Intel ICH 
 
 | | |-- 0000:00:05.0 → ../../../../devices/pci0000:00/0000:00:05.0 
 
 | | |-- bind 
 
 | | |-- module → ../../../../module/snd_intel8x0 
 
 | | |-- new_id 
 
 | | |-- uevent 
 
 | | `-- unbind 
 
 | ... 
 
 | |-- pcnet32 
 
 | | |-- 0000:00:03.0 → ../../../../devices/pci0000:00/0000:00:03.0 
 
 | | |-- bind 
 
 | | |-- module → ../../../../module/pcnet32 
 
 | | |-- new_id 
 
 | | |-- uevent 
 
 | | `-- unbind 
 
 | 
 
 |-- drivers_autoprobe 
 
 |-- drivers_probe 
 
 |-- slots 
 
 `-- uevent

89 directories, 239 files

此外，pciutils（PCI工具）中的lspci工具会分析/proc/bus/pci中的文件，从而可被用户用于查看系统中PCI设备的描述信息，例如在本书配套虚拟机上运行lspci的结果为：

00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02) 
 
 00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II] 
 
 00:01.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01) 
 
 00:02.0 VGA compatible controller: InnoTek Systemberatung GmbH VirtualBox Graphics 
 
 Adapter 
 
 00:03.0 Ethernet controller: Advanced Micro Devices [AMD] 79c970 [PCnet32 LANCE] (rev



40)

00:04.0 System peripheral: InnoTek Systemberatung GmbH VirtualBox Guest Service 
 
 00:05.0 Multimedia audio controller: Intel Corporation 82801AA AC'97 Audio Controller 
 
 (rev 01) 
 
 00:06.0 USB Controller: Apple Computer Inc. KeyLargo/Intrepid USB 
 
 00:07.0 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08) 
 
 00:0b.0 USB Controller: Intel Corporation 82801FB/FBM/FR/FW/FRW (ICH6 Family) USB2 EHCI 
 
 Controller

