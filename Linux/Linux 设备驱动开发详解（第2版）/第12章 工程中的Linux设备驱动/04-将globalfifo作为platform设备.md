### 12.1.2 将globalfifo作为platform设备

现在我们将前面章节的globalfifo驱动挂接到platform总线上，要完成两个工作。

（1）将globalfifo移植为platform驱动。

（2）在板文件中添加globalfifo这个platform设备。

为完成将globalfifo移植到platform驱动的工作，需要在原始的globalfifo字符设备驱动中套一层platform_driver的外壳，如代码清单12.5。注意进行这一工作后，并没有改变globalfifo是字符设备的本质，只是将其挂接到了platform总线。

代码清单12.5 为globalfifo添加platform.driver

1 static int __devinit globalfifo_probe(struct platform_device *pdev) 
 
 2 { 
 
 3 int ret; 
 
 4 dev_t devno = MKDEV(globalfifo_major, 0); 
 
 5 
 
 6 /* 申请设备号*/ 
 
 7 if (globalfifo_major) 
 
 8 ret = register_chrdev_region(devno, 1, "globalfifo"); 
 
 9 else { /* 动态申请设备号 */ 
 
 10 ret = alloc_chrdev_region(&devno, 0, 1, "globalfifo"); 
 
 11 globalfifo_major = MAJOR(devno); 
 
 12 } 
 
 13 if (ret < 0) 
 
 14 return ret;



15 /* 动态申请设备结构体的内存*/ 
 
 16 globalfifo_devp = kmalloc(sizeof(struct globalfifo_dev), GFP_KERNEL); 
 
 17 if (!globalfifo_devp) { /*申请失败*/ 
 
 18 ret = - ENOMEM; 
 
 19 goto fail_malloc; 
 
 20 } 
 
 21 
 
 22 memset(globalfifo_devp, 0, sizeof(struct globalfifo_dev)); 
 
 23 
 
 24 globalfifo_setup_cdev(globalfifo_devp, 0); 
 
 25 
 
 26 init_MUTEX(&globalfifo_devp->sem); /*初始化信号量*/ 
 
 27 init_waitqueue_head(&globalfifo_devp->r_wait); /*初始化读等待队列头*/ 
 
 28 init_waitqueue_head(&globalfifo_devp->w_wait); /*初始化写等待队列头*/ 
 
 29 
 
 30 return 0; 
 
 31 
 
 32 fail_malloc: unregister_chrdev_region(devno, 1); 
 
 33 return ret; 
 
 34 } 
 
 35 
 
 36 static int __devexit globalfifo_remove(struct platform_device *pdev) 
 
 37 { 
 
 38 cdev_del(&globalfifo_devp->cdev); /*注销cdev*/ 
 
 39 kfree(globalfifo_devp); /*释放设备结构体内存*/ 
 
 40 unregister_chrdev_region(MKDEV(globalfifo_major, 0), 1); /*释放设备号*/ 
 
 41 return 0; 
 
 42 } 
 
 43 
 
 44 static struct platform_driver globalfifo_device_driver = { 
 
 45 .probe = globalfifo_probe, 
 
 46 .remove = __devexit_p(globalfifo_remove), 
 
 47 .driver = { 
 
 
 48 .name = "globalfifo", 
 
 49 .owner = THIS_MODULE, 
 
 50 } 
 
 51 }; 
 
 52 
 
 53 static int __init globalfifo_init(void) 
 
 54 { 
 
 
 55 return platform_ 
 driver_ 
 register(&globalfifo_ 
 device_ 
 driver); 
 
 56 } 
 
 57 
 
 58 static void __exit globalfifo_exit(void) 
 
 59 { 
 
 
 60 platform_ 
 driver_ 
 unregister(&globalfifo_ 
 device_ 
 driver); 
 
 61 } 
 
 62 
 
 63 module_init(globalfifo_init); 
 
 64 module_exit(globalfifo_exit);

在代码清单12.5中，模块加载和卸载函数仅仅通过platform_driver_register()、platform_driver_ unregister()函数进行platform_driver的注册与注销，而原先注册和注销字符设备的工作已经被移交到platform_driver的probe()和remove()成员函数中。

代码清单12.5未列出的部分与原始的globalfifo驱动相同，都是实现作为字符设备驱动核心的file_operations的成员函数。

为了完成在板文件中添加globalfifo这个platform设备的工作，需要在板文件（对于LDD6410而言，为arch/arm/mach-s3c6410/ mach-ldd6410.c）中添加相应的代码，如代码清单12.6所示。

代码清单12.6 globalfifo对应的platform.device

1 static struct platform_device globalfifo_device = { 
 
 
 2 .name = "globalfifo", 
 
 3 .id = -1, 
 
 4 };

对于LDD6410开发板而言，为了完成上述globalfifo_device这一platform_device的注册，只需要将其地址放入arch/arm/mach-s3c6410/ mach-ldd6410.c中定义的ldd6410_devices数组，如：

static struct platform_device *ldd6410_devices[]__initdata = { 
 
 + & globalfifo_device, 
 
 #ifdef CONFIG_FB_S3C_V2 
 
 &s3c_device_fb, 
 
 #endif 
 
 &s3c_device_hsmmc0, 
 
 ... 
 
 }

在加载LDD6410驱动后，在sysfs中会发现如下结点：

/sys/bus/platform/devices/globalfifo/ 
 
 /sys/devices/platform/globalfifo/

留意一下代码清单12.5的第48行和代码清单12.6的第2行，platform_device和platform_driver 的name一致，这是两者得以匹配的前提。

