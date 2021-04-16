### 5.4.3 udev的组成

udev的主页位于：http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html，上面包含了关于udev的详细介绍，从http://www.us.kernel.org/pub/linux/utils/kernel/hotplug/上可以下载最新的udev包。udev的设计目标如下。

● 在用户空间中执行。

（1）动态建立/删除设备文件。

（2）允许每个人都不用关心主/次设备号。

（3）提供LSB标准名称。

（4）如果需要，可提供固定的名称。

为了提供这些功能，udev以3个分割的子计划发展：namedev、libsysfs和udev。namedev为设备命名子系统，libsysfs提供访问sysfs文件系统从中获取信息的标准接口，udev提供/dev设备节点文件的动态创建和删除策略。udev程序背负与namedev和libsysfs库交互的任务，当/sbin/hotplug程序被内核调用时，udev将被运行。udev的工作过程如下。

（1）当内核检测到在系统中出现了新设备后，内核会在sysfs文件系统中为该新设备生成新的记录并导出一些设备特定的信息及所发生的事件。

（2）udev获取内核导出的信息，它调用namedev决定应该给该设备指定的名称，如果是新插入设备，udev将调用libsysfs决定应该为该设备的设备文件指定的主/次设备号，并用分析获得的设备名称和主/次设备号创建/dev中的设备文件；如果是设备移除，则之前已经被创建的/dev文件将被删除。

在namedev中使用5步序列来决定指定设备的命名。

（1）标签（label）/序号（serial）：这一步检查设备是否有惟一的识别记号，例如USB设备有惟一的USB序号，SCSI 有惟一的UUID。如果namedev找到与这种惟一编号相对应的规则，它将使用该规则提供的名称。

（2）设备总线号：这一步会检查总线设备编号，对于不可热插拔的环境，这一步足以辨别设备。例如，PCI总线编号在系统的使用期间内很少变更。如果namedev找到相对应的规则，规则中的名称就会被使用。

（3）总线上的拓扑：当设备在总线上的位置匹配用户指定的规则时，就会使用该规则指定的名称。

（4）替换名称：当内核提供的名称匹配指定的替代字符串时，就会使用替代字符串指定的名称。

（5）内核提供的名称：这一步“包罗万象”，如果以前的几个步骤都没有被提供，默认的内核将被指定给该设备。

代码清单5.8给出了一个namedev命名规则的例子，第2、4行定义的是符合第1步的规则，第6、8行定义的是符合第2步的规则，第11、14行定义的是符合第3步的规则，第16行定义的是符合第4步的规则。

代码清单5.8 namedev命名规则

1 # USB Epson printer to be called lp_epson 
 
 2 LABEL, BUS="usb", serial="HXOLL0012202323480", NAME="lp_epson" 
 
 3 # USB HP printer to be called lp_hp, 
 
 4 LABEL, BUS="usb", serial="W09090207101241330", NAME="lp_hp" 
 
 5 # sound card with PCI bus id 00:0b.0 to be the first sound card 
 
 6 NUMBER, BUS="pci", id="00:0b.0", NAME="dsp" 
 
 7 # sound card with PCI bus id 00:07.1 to be the second sound card 
 
 8 NUMBER, BUS="pci", id="00:07.1", NAME="dsp1" 
 
 9 # USB mouse plugged into the third port of the first hub to be 
 
 10 # called mouse0 
 
 11 TOPOLOGY, BUS="usb", place="1.3", NAME="mouse0" 
 
 12 # USB tablet plugged into the second port of the second hub to be 
 
 13 # called mouse1 
 
 14 TOPOLOGY, BUS="usb", place="2.2", NAME="mouse1" 
 
 15 # ttyUSB1 should always be called visor 
 
 16 REPLACE, KERNEL="ttyUSB1", NAME="visor"

