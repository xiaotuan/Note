### 1.6.2 Linux下的LED驱动

在Linux下，可以使用字符设备驱动的框架来编写对应于代码清单1.3的LED设备驱动（这里仅仅是为了讲解的方便，到后文我们会发现，内核中实际实现了一个提供sysfs结点的GPIO LED驱动，位于drivers/leds/leds-gpio.c），操作硬件的LightInit()、LightOn()、LightOff()函数仍然需要，但是，遵循Linux编程的命名习惯，重新将其命名为light_init()、light_on()、light_off()。这些函数将被LED设备驱动中独立于设备的针对内核的接口进行调用，代码清单1.4给出了Linux下LED的驱动，此时读者并不需要能读懂这些代码。

代码清单1.4 Linux操作系统下LED的驱动

1 #include .../*包含内核中的多个头文件*/

2 /*设备结构体*/ 
 
 3 struct light_dev { 
 
 4 struct cdev cdev; /*字符设备cdev结构体*/



5 unsigned char vaule; /*LED亮时为1，熄灭时为0，用户可读写此值*/ 
 
 6 };

7 struct light_dev *light_devp; 
 
 8 int light_major = LIGHT_MAJOR;

9 MODULE_AUTHOR("Barry Song <21cnbao@gmail.com>"); 
 
 10 MODULE_LICENSE("Dual BSD/GPL"); 
 
 11 /*打开和关闭函数*/ 
 
 12 int light_open(struct inode *inode, struct file *filp) 
 
 13 { 
 
 14 struct light_dev *dev; 
 
 15 /* 获得设备结构体指针 */ 
 
 16 dev = container_of(inode->i_cdev, struct light_dev, cdev); 
 
 17 /* 让设备结构体作为设备的私有信息 */ 
 
 18 filp->private_data = dev; 
 
 19 return 0; 
 
 20 }

21 int light_release(struct inode *inode, struct file *filp) 
 
 22 { 
 
 23 return 0; 
 
 24 } 
 
 25 /*读写设备:可以不需要 */ 
 
 26 ssize_t light_read(struct file *filp, char __user *buf, size_t count, 
 
 27 loff_t *f_pos) 
 
 28 { 
 
 29 struct light_dev *dev = filp->private_data; /*获得设备结构体 */ 
 
 30 if (copy_to_user(buf, &(dev->value), 1)) 
 
 31 return -EFAULT;

32 return 1; 
 
 33 } 
 
 34 ssize_t light_write(struct file *filp, const char __user *buf, size_t count, 
 
 35 loff_t *f_pos) 
 
 36 { 
 
 37 struct light_dev *dev = filp->private_data;

38 if (copy_from_user(&(dev->value), buf, 1)) 
 
 39 return -EFAULT;

40 /*根据写入的值点亮和熄灭LED*/ 
 
 41 if (dev->value == 1) 
 
 42 light_on(); 
 
 43 else 
 
 44 light_off(); 
 
 45 return 1; 
 
 46 }

47 /* ioctl函数 */ 
 
 48 int light_ioctl(struct inode *inode, struct file *filp, unsigned int cmd, 
 
 49 unsigned long arg)



50 { 
 
 51 struct light_dev *dev = filp->private_data;

52 switch (cmd) { 
 
 53 case LIGHT_ON: 
 
 54 dev->value = 1; 
 
 55 light_on(); 
 
 56 break; 
 
 57 case LIGHT_OFF: 
 
 58 dev->value = 0; 
 
 59 light_off(); 
 
 60 break; 
 
 61 default: 
 
 62 /* 不能支持的命令 */ 
 
 63 return -ENOTTY; 
 
 64 }

65 return 0; 
 
 66 }

67 struct file_operations light_fops = { 
 
 68 .owner = THIS_MODULE, 
 
 69 .read = light_read, 
 
 70 .write = light_write, 
 
 71 .ioctl = light_ioctl, 
 
 72 .open = light_open, 
 
 73 .release = light_release, 
 
 74 };

75 /*设置字符设备cdev结构体*/ 
 
 76 static void light_setup_cdev(struct light_dev *dev, int index) 
 
 77 { 
 
 78 int err, devno = MKDEV(light_major, index); 
 
 79 cdev_init(&dev->cdev, &light_fops); 
 
 80 dev->cdev.owner = THIS_MODULE; 
 
 81 dev->cdev.ops = &light_fops; 
 
 82 err = cdev_add(&dev->cdev, devno, 1); 
 
 83 if (err) 
 
 84 printk(KERN_NOTICE "Error %d adding LED%d", err, index); 
 
 85 }

86 /*模块加载函数*/ 
 
 87 int light_init(void) 
 
 88 { 
 
 89 int result; 
 
 90 dev_t dev = MKDEV(light_major, 0); 
 
 91 /* 申请字符设备号*/ 
 
 92 if (light_major) 
 
 93 result = register_chrdev_region(dev, 1, "LED"); 
 
 94 else { 
 
 95 result = alloc_chrdev_region(&dev, 0, 1, "LED"); 
 
 96 light_major = MAJOR(dev); 
 
 97 } 
 
 98 if (result < 0) 
 
 99 return result;



100 /* 分配设备结构体的内存 */ 
 
 101 light_devp = kmalloc(sizeof(struct light_dev), GFP_KERNEL); 
 
 102 if (!light_devp) { 
 
 103 result = -ENOMEM; 
 
 104 goto fail_malloc; 
 
 105 } 
 
 106 memset(light_devp, 0, sizeof(struct light_dev)); 
 
 107 light_setup_cdev(light_devp, 0); 
 
 108 light_gpio_init(); 
 
 109 return 0;

110 fail_malloc: 
 
 111 unregister_chrdev_region(dev, light_devp); 
 
 112 return result; 
 
 113 }

114 /*模块卸载函数*/ 
 
 115 void light_cleanup(void) 
 
 116 { 
 
 117 cdev_del(&light_devp->cdev); /*删除字符设备结构体*/ 
 
 118 kfree(light_devp); /*释放在light_init中分配的内存*/ 
 
 119 unregister_chrdev_region(MKDEV(light_major, 0), 1); /*删除字符设备*/ 
 
 120 }

121 module_init(light_init); 
 
 122 module_exit(light_cleanup);

上述代码的行数与代码清单1.3已经不能比拟，除了代码清单1.3中的硬件操作函数仍然需要外，代码清单1.4中还包含了大量对我们暂时陌生的元素，如结构体file_operations、cdev，Linux内核模块声明用的MODULE_AUTHOR、MODULE_LICENSE、module_init、module_exit，以及用于字符设备注册、分配和注销用的函数register_chrdev_region()、alloc_chrdev_region()、unregister_chrdev_region()等。我们也不能理解为什么驱动中要包含light_init ()、light_cleanup ()、light_read()、light_write()等函数。

此时，我们只需要有一个感性认识，那就是，上述暂时陌生的元素都是Linux内核给字符设备定义的为实现驱动与内核接口而定义的。Linux对各类设备的驱动都定义了类似的数据结构和函数。

