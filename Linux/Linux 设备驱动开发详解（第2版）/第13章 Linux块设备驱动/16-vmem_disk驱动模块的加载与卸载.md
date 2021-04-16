### 13.7.2 vmem_disk驱动模块的加载与卸载

vmem_disk驱动的模块加载函数完成的工作与13.3节给出的模板完全一致，它支持“制造请求”（对应代码清单13.9）、请求队列（对应代码清单13.10）两种模式（留意在请求队列方面又支持简、繁两种模式），使用模块参数request_mode进行区分。代码清单13.16给出了vmem_disk设备驱动的模块加载与卸载函数。

代码清单13.17 vmem.disk设备驱动的模块加载与卸载函数

1 static int __init vmem_disk_init(void) 
 
 2 { 
 
 3 int i; 
 
 4 /* 
 
 5 * 注册块设备 
 
 6 */ 
 
 7 vmem_disk_major = register_blkdev(vmem_disk_major, "vmem_disk"); 
 
 8 if (vmem_disk_major <= 0) { 
 
 9 printk(KERN_WARNING "vmem_disk: unable to get major number\n"); 
 
 10 return -EBUSY; 
 
 11 } 
 
 12 /* 
 
 13 * 分配设备数组，初始化它们 
 
 14 */ 
 
 15 Devices = kmalloc(ndevices*sizeof (struct vmem_disk_dev), GFP_KERNEL); 
 
 16 if (Devices == NULL) 
 
 17 goto out_unregister; 
 
 18 for (i = 0; i < ndevices; i++) 
 
 19 setup_device(Devices + i, i); 
 
 20 
 
 21 return 0;



22 
 
 23 out_unregister: 
 
 24 unregister_blkdev(vmem_disk_major, "sbd"); 
 
 25 return -ENOMEM; 
 
 26 } 
 
 27 
 
 28 static void vmem_disk_exit(void) 
 
 29 { 
 
 30 int i; 
 
 31 
 
 32 for (i = 0; i < ndevices; i++) { 
 
 33 struct vmem_disk_dev *dev = Devices + i; 
 
 34 
 
 35 del_timer_sync(&dev->timer); 
 
 36 if (dev->gd) { 
 
 37 del_gendisk(dev->gd); 
 
 38 put_disk(dev->gd); 
 
 39 } 
 
 40 if (dev->queue) { 
 
 41 if (request_mode == RM_NOQUEUE) 
 
 42 kobject_put (&dev->queue->kobj); 
 
 43 else 
 
 44 blk_cleanup_queue(dev->queue); 
 
 45 } 
 
 46 if (dev->data) 
 
 47 vfree(dev->data); 
 
 48 } 
 
 49 unregister_blkdev(vmem_disk_major, "vmem_disk"); 
 
 50 kfree(Devices); 
 
 51 } 
 
 52 
 
 53 /* 
 
 54 * 设置设备 
 
 55 */ 
 
 56 static void setup_device(struct vmem_disk_dev *dev, int which) 
 
 57 { 
 
 58 /* 
 
 59 * 分配globalmem的内存 
 
 60 */ 
 
 61 memset (dev, 0, sizeof (struct vmem_disk_dev)); 
 
 62 dev->size = nsectors*hardsect_size; 
 
 63 dev->data = vmalloc(dev->size); 
 
 64 if (dev->data == NULL) { 
 
 65 printk (KERN_NOTICE "vmalloc failure.\n"); 
 
 66 return; 
 
 67 } 
 
 68 spin_lock_init(&dev->lock); 
 
 69 
 
 70 /* 
 
 71 * 使用一个timer来模拟设备invalidate 
 
 72 */ 
 
 73 init_timer(&dev->timer); 
 
 74 dev->timer.data = (unsigned long) dev; 
 
 75 dev->timer.function = vmem_disk_invalidate; 
 
 76



77 /* 
 
 78 * I/O队列，具体实现依赖于我们是否使用make_request函数 
 
 79 */ 
 
 80 switch (request_mode) { 
 
 81 case RM_NOQUEUE: 
 
 82 dev->queue = blk_alloc_queue(GFP_KERNEL); 
 
 83 if (dev->queue == NULL) 
 
 84 goto out_vfree; 
 
 85 blk_queue_make_request(dev->queue, vmem_disk_make_request); 
 
 86 break; 
 
 87 
 
 88 case RM_FULL: 
 
 89 dev->queue = blk_init_queue(vmem_disk_full_request, &dev->lock); 
 
 90 if (dev->queue == NULL) 
 
 91 goto out_vfree; 
 
 92 break; 
 
 93 
 
 94 default: 
 
 95 printk(KERN_NOTICE "Bad request mode %d, using simple\n", request_mode); 
 
 96 
 
 97 case RM_SIMPLE: 
 
 98 dev->queue = blk_init_queue(vmem_disk_request, &dev->lock); 
 
 99 if (dev->queue == NULL) 
 
 100 goto out_vfree; 
 
 101 break; 
 
 102 } 
 
 103 blk_queue_hardsect_size(dev->queue, hardsect_size); 
 
 104 dev->queue->queuedata = dev; 
 
 105 /* 
 
 106 * gendisk分配与初始化 
 
 107 */ 
 
 108 dev->gd = alloc_disk(vmem_disk_MINORS); 
 
 109 if (! dev->gd) { 
 
 110 printk (KERN_NOTICE "alloc_disk failure\n"); 
 
 111 goto out_vfree; 
 
 112 } 
 
 113 dev->gd->major = vmem_disk_major; 
 
 114 dev->gd->first_minor = which*vmem_disk_MINORS; 
 
 115 dev->gd->fops = &vmem_disk_ops; 
 
 116 dev->gd->queue = dev->queue; 
 
 117 dev->gd->private_data = dev; 
 
 118 snprintf (dev->gd->disk_name, 32, "vmem_disk%c", which + 'a'); 
 
 119 set_capacity(dev->gd, nsectors*(hardsect_size/KERNEL_SECTOR_SIZE)); 
 
 120 add_disk(dev->gd); 
 
 121 return; 
 
 122 
 
 123 out_vfree: 
 
 124 if (dev->data) 
 
 125 vfree(dev->data); 
 
 126 }

上述代码中引用的vmem_disk_major、ndevices、nsectors、hardsect_size都是模块参数，其默认值定义如下：

static int vmem_disk_major = 0; 
 
 module_param(vmem_disk_major, int, 0);



static int hardsect_size = 512; 
 
 module_param(hardsect_size, int, 0); 
 
 static int nsectors = 1024; /* 该驱动器的大小 */ 
 
 module_param(nsectors, int, 0); 
 
 static int ndevices = 4; 
 
 module_param(ndevices, int, 0); 
 
 /* 
 
 * 我们能使用的不同request模式 
 
 */ 
 
 enum { 
 
 RM_SIMPLE = 0, /* 简单请求函数(对应代码清单13.13) */ 
 
 RM_FULL = 1, /* 复杂的请求函数(对应代码清单13.15) */ 
 
 RM_NOQUEUE = 2, /* 使用make_request(对应代码清单13.16) */ 
 
 }; 
 
 static int request_mode = RM_SIMPLE; 
 
 module_param(request_mode, int, 0);

在模块加载时我们可以更改这些参数。尤其值得注意的是，request_mode等于RM_SIMPLE、RM_FULL、RM_NOQUEUE分别对应于代码清单13.13、13.15和13.16这三种不同的请求处理方式。

