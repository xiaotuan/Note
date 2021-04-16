### 20.5 USB OTG驱动

USB OTG标准在完全兼容USB 2.0标准的基础上，它允许设备既可作为主机，也可作为外设操作，OTG新增了主机通令协议（HNP）和对话请求协议（SRP）。

在OTG中，初始主机设备称为A设备，外设称为B设备。可用电缆的连接方式来决定初始角色。两用设备使用新型mini-AB插座，从而使mini-A插头、mini-B插头和mini-AB插座增添了第5个引脚（ID），以用于识别不同的电缆端点。mini-A插头中的ID引脚接地，mini-B插头中的ID引脚浮空。当OTG设备检测到接地的ID引脚时，表示默认的是A设备（主机），而检测到ID引脚浮空的设备则认为是B设备（外设）。系统一旦连接后，OTG的角色还可以更换，采用新的HNP协议。而SRP允许B设备请求A设备打开VBUS电源并启动一次对话。一次OTG对话可通过A设备提供VBUS电源的时间来确定。

自从Linux 2.6.9开始，OTG相关源代码已经被包含在内核中，新增的主要内容包括：

（1）UDC驱动端添加的OTG相关属性和函数。

struct usb_gadget { 
 
 ... 
 
 unsigned is_otg:1; 
 
 unsigned is_a_peripheral:1; 
 
 unsigned b_hnp_enable:1; 
 
 unsigned a_hnp_support:1; 
 
 unsigned a_alt_hnp_support:1; 
 
 ... 
 
 };

int usb_gadget_vbus_connect(struct usb_gadget *gadget); 
 
 int usb_gadget_vbus_disconnect(struct usb_gadget *gadget); 
 
 int usb_gadget_vbus_draw(struct usb_gadget *gadget, unsigned mA);

/* 控制 USB D+的pullup */ 
 
 int usb_gadget_connect(struct usb_gadget *gadget); 
 
 int usb_gadget_disconnect(struct usb_gadget *gadget);

int usb_gadget_wakeup(struct usb_gadget *gadget);

（2）gadget驱动端添加的OTG相关属性和函数。

如果gadget→is_otg字段为真，则增加一个OTG描述符；通过printk()、LED等方式报告HNP可用；当suspend开始时，通过用户界面报告HNP切换开始（B-Peripheral 到 B-Host或A-Peripheral to A-Host）。

（3）主机侧添加的OTG相关属性和函数。

USB核心中新增了关于OTG设备枚举的信息：



struct usb_bus { 
 
 ... 
 
 u8 otg_port; /* 0, or index of OTG/HNP port */ 
 
 unsigned is_b_host:1; /* true during some HNP roleswitches */ 
 
 unsigned b_hnp_enable:1; /* OTG: did A-Host enable HNP? */ 
 
 ... 
 
 };

为了实现HNP需要的suspend/resume，新增如下通用接口：

int usb_suspend_device(struct usb_device *dev, u32 state); 
 
 int usb_resume_device(struct usb_device *dev);

（4）新增OTG控制器otg_transceiver。

struct otg_transceiver { 
 
 struct device *dev; 
 
 const char *label;

u8 default_a; 
 
 enum usb_otg_state state; 
 
 struct usb_bus *host; 
 
 struct usb_gadget *gadget; 
 
 /* to pass extra port status to the root hub */ 
 
 u16 port_status; 
 
 u16 port_change; 
 
 /* bind/unbind主机控制器 */ 
 
 int (*set_host)(struct otg_transceiver *otg, 
 
 struct usb_bus *host); 
 
 /* bind/unbind设备控制器 */ 
 
 int (*set_peripheral)(struct otg_transceiver *otg, 
 
 struct usb_gadget *gadget); 
 
 /* 对B设备有效 */ 
 
 int (*set_power)(struct otg_transceiver *otg, 
 
 unsigned mA); 
 
 /* 针对B设备: 与A-Host进入一个session */ 
 
 int (*start_srp)(struct otg_transceiver *otg); 
 
 /* 开始/继续HNP角色切换 */ 
 
 int (*start_hnp)(struct otg_transceiver *otg); 
 
 };

目前，完整实现OTG支持的驱动非常少，例如目前S3C6410的USB 2.0控制器驱动就没有完整实现OTG，因此，我们无法在运行时动态切换S3C6410的身份，而TI OMAP处理器的OTG支持比较完整。而真正支持完整OTG功能的产品也非常少，Nokia N810 internet Tablet是其中之一，它使用的SoC是OMAP 2420。其他大多号称支持OTG的产品实际上并未完整实现HNP和SRP。

