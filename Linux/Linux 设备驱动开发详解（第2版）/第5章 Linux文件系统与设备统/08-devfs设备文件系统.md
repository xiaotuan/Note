### 5.3 devfs设备文件系统

devfs（设备文件系统）是由Linux 2.4内核引入的，引入时被许多工程师给予了高度评价，它的出现使得设备驱动程序能自主地管理它自己的设备文件。具体来说，devfs具有如下优点。

（1）可以通过程序在设备初始化时在/dev 目录下创建设备文件，卸载设备时将它删除。

（2）设备驱动程序可以指定设备名、所有者和权限位，用户空间程序仍可以修改所有者和权限位。

（3）不再需要为设备驱动程序分配主设备号以及处理次设备号，在程序中可以直接给register_ chrdev()传递0主设备号以获得可用的主设备号，并在devfs_register()中指定次设备号。

驱动程序应调用下面这些函数来进行设备文件的创建和删除工作。

/*创建设备目录*/ 
 
 devfs_handle_t devfs_mk_dir(devfs_handle_t dir, const char *name, void *info); 
 
 /*创建设备文件*/ 
 
 devfs_handle_t devfs_register(devfs_handle_t dir, const char *name, unsigned 
 
 int flags, unsigned int major, unsigned int minor, umode_t mode, void *ops, 
 
 void *info); 
 
 /*撤销设备文件*/ 
 
 void devfs_unregister(devfs_handle_t de);

在Linux 2.4的设备驱动编程中，分别在模块加载和卸载函数中创建和撤销设备文件是被普遍采用并值得大力推荐的好方法。代码清单5.5给出了一个使用devfs的例子。



代码清单5.5 devfs的使用范例

1 static devfs_handle_t devfs_handle; 
 
 2 static int _ _init xxx_init(void) 
 
 3 { 
 
 4 int ret; 
 
 5 int i; 
 
 6 /*在内核中注册设备*/ 
 
 7 ret = register_chrdev(XXX_MAJOR, DEVICE_NAME, &xxx_fops); 
 
 8 if (ret < 0) { 
 
 9 printk(DEVICE_NAME " can't register major number\n"); 
 
 10 return ret; 
 
 11 } 
 
 12 /*创建设备文件*/ 
 
 13 devfs_handle =devfs_register(NULL, DEVICE_NAME, DEVFS_FL_DEFAULT, 
 
 14 XXX_MAJOR, 0, S_IFCHR | S_IRUSR | S_IWUSR, &xxx_fops, NULL); 
 
 15 ... 
 
 16 printk(DEVICE_NAME " initialized\n"); 
 
 17 return 0; 
 
 18 } 
 
 19 
 
 20 static void _ _exit xxx_exit(void) 
 
 21 { 
 
 22 devfs_unregister(devfs_handle); /*撤销设备文件*/ 
 
 23 unregister_chrdev(XXX_MAJOR, DEVICE_NAME); /*注销设备*/ 
 
 24 } 
 
 25 
 
 26 module_init(xxx_init); 
 
 27 module_exit(xxx_exit);

代码中第7行和第23行分别用于注册和注销字符设备，使用的register_chrdev()和unregister_chrdev()在Linux 2.6内核中虽然仍然被支持，但这是过时的做法。第13和22行分别用于创建和删除devfs文件节点。

