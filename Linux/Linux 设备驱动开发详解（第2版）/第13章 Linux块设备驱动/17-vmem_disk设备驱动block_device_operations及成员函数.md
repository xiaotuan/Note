### 13.7.3 vmem_disk设备驱动block_device_operations及成员函数

vmem_disk提供block_device_operations结构体中open()、release()、getgeo()、media_changed()、revalidate_disk()这些成员函数，代码清单13.18给出了vmem_disk设备驱动的block_device_ operations结构体定义及其成员函数的实现。

代码清单13.18 vmem.disk设备驱动block.device.operations结构体及成员函数

1 /* 
 
 2 * Open和close. 
 
 3 */ 
 
 4 
 
 5 static int vmem_disk_open(struct block_device *bdev, fmode_t mode) 
 
 6 { 
 
 7 struct vmem_disk_dev *dev = bdev->bd_disk->private_data; 
 
 8 
 
 9 del_timer_sync(&dev->timer); 
 
 10 spin_lock(&dev->lock); 
 
 11 dev->users++; 
 
 12 spin_unlock(&dev->lock); 
 
 13 
 
 14 return 0; 
 
 15 } 
 
 16 
 
 17 static int vmem_disk_release(struct gendisk *disk, fmode_t mode) 
 
 18 { 
 
 19 struct vmem_disk_dev *dev = disk->private_data; 
 
 20 
 
 21 spin_lock(&dev->lock); 
 
 22 dev->users--; 
 
 23 
 
 24 if (!dev->users) { 
 
 25 dev->timer.expires = jiffies + INVALIDATE_DELAY;



26 add_timer(&dev->timer); 
 
 27 } 
 
 28 spin_unlock(&dev->lock); 
 
 29 
 
 30 return 0; 
 
 31 } 
 
 32 
 
 33 int vmem_disk_media_changed(struct gendisk *gd) 
 
 34 { 
 
 35 struct vmem_disk_dev *dev = gd->private_data; 
 
 36 
 
 37 return dev->media_change; 
 
 38 } 
 
 39 
 
 40 int vmem_disk_revalidate(struct gendisk *gd) 
 
 41 { 
 
 42 struct vmem_disk_dev *dev = gd->private_data; 
 
 43 
 
 44 if (dev->media_change) { 
 
 45 dev->media_change = 0; 
 
 46 memset (dev->data, 0, dev->size); 
 
 47 } 
 
 48 return 0; 
 
 49 } 
 
 50 
 
 51 /* 
 
 52 * invalidate()在定时器到期时执行，设置一个标志来模拟磁盘的移除 
 
 53 */ 
 
 54 void vmem_disk_invalidate(unsigned long ldev) 
 
 55 { 
 
 56 struct vmem_disk_dev *dev = (struct vmem_disk_dev *) ldev; 
 
 57 
 
 58 spin_lock(&dev->lock); 
 
 59 if (dev->users || !dev->data) 
 
 60 printk (KERN_WARNING "vmem_disk: timer sanity check failed\n"); 
 
 61 else 
 
 62 dev->media_change = 1; 
 
 63 spin_unlock(&dev->lock); 
 
 64 } 
 
 65 
 
 66 /* 
 
 67 * getgeo() 实现 
 
 68 */ 
 
 69 
 
 70 static int vmem_disk_getgeo(struct block_device *bdev, struct hd_geometry *geo) 
 
 71 { 
 
 72 long size; 
 
 73 struct vmem_disk_dev *dev = bdev->bd_disk->private_data; 
 
 74 
 
 75 size = dev->size*(hardsect_size/KERNEL_SECTOR_SIZE); 
 
 76 geo->cylinders = (size & ~0x3f) >> 6; 
 
 77 geo->heads = 4; 
 
 78 geo->sectors = 16; 
 
 79 geo->start = 4; 
 
 80



81 return 0; 
 
 82 } 
 
 83 
 
 84 /* 
 
 85 * block_device_operations结构体 
 
 86 */ 
 
 87 static struct block_device_operations vmem_disk_ops = { 
 
 88 .owner = THIS_MODULE, 
 
 89 .open = vmem_disk_open, 
 
 90 .release = vmem_disk_release, 
 
 91 .media_changed = vmem_disk_media_changed, 
 
 92 .revalidate_disk = vmem_disk_revalidate, 
 
 93 .getgeo = vmem_disk_getgeo, 
 
 94 };

