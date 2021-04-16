### 20.3.5 实例：USB键盘驱动

在Linux系统中，键盘被认定为标准输入设备，对于一个USB键盘而言，其驱动主要由两部分组成：usb_driver的成员函数以及输入设备驱动的input_event获取和报告。

在USB键盘设备驱动的模块加载和卸载函数中，将分别注册和注销对应于USB键盘的usb_driver结构体usb_kbd_driver，代码清单20.27所示为模块加载与卸载函数以及usb_kbd_driver结构体的定义。

代码清单20.27 USB键盘设备驱动的模块加载与卸载函数及usb_driver结构体

1 static int _ _init usb_kbd_init(void) 
 
 2 { 
 
 3 int result = usb_register(&usb_kbd_driver); 
 
 4 ... 
 
 5 } 
 
 6 
 
 7 static void _ _exit usb_kbd_exit(void) 
 
 8 { 
 
 9 usb_deregister(&usb_kbd_driver); 
 
 10 } 
 
 11 
 
 12 static struct usb_driver usb_kbd_driver = 
 
 13 { 
 
 14 .name = "usbkbd", 
 
 15 .probe = usb_kbd_probe, 
 
 16 .disconnect = usb_kbd_disconnect, 
 
 17 .id_table = usb_kbd_id_table, 
 
 18 }; 
 
 19 
 
 20 static struct usb_device_id usb_kbd_id_table [] = { 
 
 21 { USB_INTERFACE_INFO(USB_INTERFACE_CLASS_HID, USB_INTERFACE_SUBCLASS_BOOT, 
 
 22 USB_INTERFACE_PROTOCOL_KEYBOARD) }, 
 
 23 { } 
 
 24 }; 
 
 25 MODULE_DEVICE_TABLE (usb, usb_kbd_id_table);

在usb_driver的探测函数中，将进行input设备的初始化和注册，USB键盘要使用的中断urb和控制urb的初始化，并设置接口的私有数据，如代码清单20.28所示。



代码清单20.28 USB键盘设备驱动的探测函数

1 static int usb_kbd_probe(struct usb_interface *iface, const struct 
 
 2 usb_device_id *id) 
 
 3 { 
 
 4 ... 
 
 5 pipe = usb_rcvintpipe(dev, endpoint→bEndpointAddress); 
 
 6 maxp = usb_maxpacket(dev, pipe, usb_pipeout(pipe)); 
 
 7 
 
 8 kbd = kzalloc(sizeof(struct usb_kbd), GFP_KERNEL); 
 
 9 input_dev = input_allocate_device();/* 分配input_dev结构体 */ 
 
 10 
 
 11 ... 
 
 12 /* 输入设备初始化 */ 
 
 13 input_dev→name = kbd→name; 
 
 14 input_dev→phys = kbd→phys; 
 
 15 usb_to_input_id(dev, &input_dev→id); 
 
 16 input_dev→cdev.dev = &iface→dev; 
 
 17 input_dev→private = kbd; 
 
 18 
 
 19 input_dev→evbit[0] = BIT(EV_KEY) | BIT(EV_LED) | BIT(EV_REP); 
 
 20 input_dev→ledbit[0] = BIT(LED_NUML) | BIT(LED_CAPSL) | 
 
 21 BIT(LED_SCROLLL) |BIT(LED_COMPOSE) | BIT(LED_KANA); 
 
 22 
 
 23 ... 
 
 24 /* 初始化中断urb */ 
 
 
 25 usb_fill_int_urb(kbd→irq, dev, pipe, kbd→new, (maxp > 8 ? 8 : maxp), 
 
 
 26 usb_kbd_irq, kbd, endpoint→bInterval); 
 
 27 kbd→irq→transfer_dma = kbd→new_dma; 
 
 28 kbd→irq→transfer_flags |= URB_NO_TRANSFER_DMA_MAP; 
 
 29 
 
 30 ... 
 
 31 /* 初始化控制urb */ 
 
 32 usb_fill_control_urb(kbd→led, dev, usb_sndctrlpipe(dev, 0), (void*)kbd→cr, 
 
 33 kbd→leds, 1, usb_kbd_led, kbd); 
 
 34 ... 
 
 35 input_register_device(kbd→dev); /* 注册输入设备 */ 
 
 36 
 
 37 usb_set_intfdata(iface, kbd); /* 设置接口私有数据 */ 
 
 38 return 0; 
 
 39 ... 
 
 40 }

在usb_driver的断开函数中，将设置接口私有数据为NULL、终止已提交的urb并注销输入设备，如代码清单20.29所示。

代码清单20.29 USB键盘设备驱动的断开函数

1 static void usb_kbd_disconnect(struct usb_interface *intf) 
 
 2 { 
 
 3 struct usb_kbd *kbd = usb_get_intfdata(intf); 
 
 4 
 
 5 usb_set_intfdata(intf, NULL);/* 设置接口私有数据为NULL */ 
 
 6 if (kbd) 
 
 7 { 
 
 8 usb_kill_urb(kbd→irq);/* 终止urb */



9 input_unregister_device(kbd→dev); /* 注销输入设备 */ 
 
 10 usb_kbd_free_mem(interface_to_usbdev(intf), kbd); 
 
 11 kfree(kbd); 
 
 12 } 
 
 13 }

键盘主要依赖于中断传输模式，在键盘中断urb的完成函数usb_kbd_irq()中（通过代码清单20.28的第26行可以看出），将会通过input_report_key()报告按键事件，通过input_sync()报告同步事件，如代码清单20.30所示。

代码清单20.30 USB键盘设备驱动的中断urb完成函数

1 static void usb_kbd_irq(struct urb *urb, struct pt_regs *regs) 
 
 2 { 
 
 3 struct usb_kbd *kbd = urb→context; 
 
 4 int i; 
 
 5 
 
 6 switch (urb→status) { 
 
 7 case 0: /* 成功 */ 
 
 8 break; 
 
 9 case - ECONNRESET: /* unlink */ 
 
 10 case - ENOENT: 
 
 11 case - ESHUTDOWN: 
 
 12 return ; 
 
 13 default: /* 错误 */ 
 
 14 goto resubmit; 
 
 15 } 
 
 16 /*获得键盘扫描码并报告按键事件，这里没有列出细节*/ 
 
 17 
 
 18 input_report_key(kbd→dev, usb_kbd_keycode[kbd→old[i]], 0); 
 
 19 ... 
 
 20 input_report_key(kbd→dev, usb_kbd_keycode[kbd→new[i]], 1); 
 
 21 ... 
 
 22 input_sync(kbd→dev); /* 报告同步事件 */ 
 
 23 
 
 24 resubmit: 
 
 25 i = usb_submit_urb (urb, GFP_ATOMIC); 
 
 26 ... 
 
 27 }

从USB键盘驱动的例子中，我们进一步看到了usb_driver本身只是起一个挂接总线的作用，而具体的设备类型的驱动仍然是工作的主体，例如键盘就是input、USB串口就是tty，只是在这些设备底层进行硬件访问的时候，调用的都是URB相关的接口，URB这套USB核心层API的存在，使我们无需关心底层USB主机控制器的具体细节，因此，USB设备驱动也变得与平台无关，同样的驱动可应用于不同的SoC。

