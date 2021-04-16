### 5.4.4 udev规则文件

udev的规则文件以行为单位，以“#”开头的行代表注释行。其余的每一行代表一个规则。每个规则分成一个或多个匹配和赋值部分。匹配部分用匹配专用的关键字来表示，相应的赋值部分用赋值专用的关键字来表示。匹配关键字包括：ACTION（行为）、KERNEL（匹配内核设备名）、BUS（匹配总线类型）、SYSFS（匹配从sysfs得到的信息，比如label、vendor、USB序列号）、SUBSYSTEM（匹配子系统名）等，赋值关键字包括：NAME（创建的设备文件名）、SYMLINK（符号创建链接名）、OWNER（设置设备的所有者）、GROUP（设置设备的组）、IMPORT（调用外部程序）等。

例如，如下规则：

SUBSYSTEM=="net", ACTION=="add", SYSFS{address}=="00:0d:87:f6:59:f3", IMPORT="/sbin/ 
 
 rename_netiface %k eth0"

其中的“匹配”部分有3项，分别是SUBSYSTEM、ACTION和SYSFS。而“赋值”部分有一项，是IMPORT。这个规则的意思是：当系统中出现的新硬件属于net子系统范畴，系统对该硬件采取的动作是加入这个硬件，且这个硬件在sysfs文件系统中的“address”信息等于“00:0d:87:f6:59:f3”时，对这个硬件在udev层次施行的动作是调用外部程序/sbin/rename_netiface，并传递给该程序两个参数，一个是“%k”，代表内核对该新设备定义的名称，另一个是“eth0”。

通过一个简单的例子可以看出udev和devfs在命名方面的差异。如果系统中有两个USB打印机，一个可能被称为/dev/usb/lp0，另外一个便是/dev/usb/lp1。但是到底哪个文件对应哪个打印机是无法确定的，lp0、lp1和实际的设备没有一一对应的关系，映射关系会因为设备发现的顺序，打印机本身关闭等原因而不确定。因此，理想的方式是两个打印机应该采用基于它们的序列号或者其他标识信息的办法来进行确定的映射，devfs无法做到这一点，udev却可以做到。使用如下规则：

BUS="usb", SYSFS{serial}="HXOLL0012202323480", NAME="lp_epson", SYMLINK="printers/ 
 
 epson_stylus"

该规则中的匹配项目有BUS和SYSFS，赋值项目为NAME和SYMLINK，它意味着当一台USB打印机的序列号为“HXOLL0012202323480”时，创建/dev/lp_epson文件，并同时创建一个符号链接/dev/printers/epson_styles。序列号为“HXOLL0012202323480”的USB打印机不管何时被插入，对应的设备名都是/dev/lp_epson，而devfs显然无法实现设备的这种固定命名。

udev规则的写法非常灵活，在匹配部分，可以通过“*”、“?”、[a～c]、[1～9]等shell通配符来灵活匹配多个项目。*类似于shell中的*通配符，代替任意长度的任意字符串，?代替一个字符，[x～y]是访问定义。此外，%k就是KERNEL，%n则是设备的KERNEL序号（如存储设备的分区号）。

可以借助udev中的udevinfo工具查找规则文件可以利用的信息，如运行“udevinfo -a -p/ sys/block/sda”命令将得到：

Udevinfo starts with the device specified by the devpath and then 
 
 walks up the chain of parent devices. It prints for every device 
 
 found, all possible attributes in the udev rules key format. 
 
 A rule to match, can be composed by the attributes of the device 
 
 and the attributes from one single parent device.

looking at device '/block/sda': 
 
 KERNEL=="sda" 
 
 SUBSYSTEM=="block" 
 
 DRIVER=="" 
 
 ATTR{stat}==" 1 689 3 169 85 746 24 000 2 017 2 095 32 896 
 
 47 292 0 23 188 71 292"

ATTR{size}=="6 291 456" 
 
 ATTR{removable}=="0" 
 
 ATTR{range}=="16" 
 
 ATTR{dev}=="8:0"

looking at parent device '/devices/platform/host0/target0:0:0/0:0:0:0': 
 
 KERNELS=="0:0:0:0" 
 
 SUBSYSTEMS=="scsi" 
 
 DRIVERS=="sd" 
 
 ATTRS{ioerr_cnt}=="0x5" 
 
 ATTRS{iodone_cnt}=="0xe86" 
 
 ATTRS{iorequest_cnt}=="0xe86" 
 
 ATTRS{iocounterbits}=="32" 
 
 ATTRS{timeout}=="30" 
 
 ATTRS{state}=="running" 
 
 ATTRS{rev}=="1.0 " 
 
 ATTRS{model}=="VMware Virtual S" 
 
 ATTRS{vendor}=="VMware, " 
 
 ATTRS{scsi_level}=="3" 
 
 ATTRS{type}=="0" 
 
 ATTRS{queue_type}=="none" 
 
 ATTRS{queue_depth}=="3" 
 
 ATTRS{device_blocked}=="0"

looking at parent device '/devices/platform/host0/target0:0:0': 
 
 KERNELS=="target0:0:0" 
 
 SUBSYSTEMS=="" 
 
 DRIVERS==""



looking at parent device '/devices/platform/host0': 
 
 KERNELS=="host0" 
 
 SUBSYSTEMS=="" 
 
 DRIVERS==""

looking at parent device '/devices/platform': 
 
 KERNELS=="platform" 
 
 SUBSYSTEMS=="" 
 
 DRIVERS==""

