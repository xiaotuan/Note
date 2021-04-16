### 13.3 Linux块设备驱动的模块加载与卸载

在块设备驱动的模块加载函数中通常需要完成如下工作。

① 分配、初始化请求队列，绑定请求队列和请求函数。

② 分配、初始化gendisk，给gendisk的major、fops、queue等成员赋值，最后添加gendisk。

③ 注册块设备驱动。

代码清单13.9和13.10分别给出了使用blk_alloc_queue()分配请求队列并使用blk_queue_ make_request()绑定“请求队列”和“制造请求”的函数，以及使用blk_init_queue()初始化请求队列并绑定请求队列与请求处理函数两种不同情况下的块设备驱动模块加载函数模板。

代码清单13.9 块设备驱动的模块加载函数模板（使用blk.alloc.queue）

1 static int _ _init xxx_init(void) 
 
 2 { 
 
 3 /* 分配gendisk */ 
 
 4 xxx_disks = alloc_disk(1); 
 
 5 if (!xxx_disks) 
 
 6 goto out; 
 
 7 
 
 8 /* 块设备驱动注册 */ 
 
 9 if (register_blkdev(XXX_MAJOR, "xxx")) { 
 
 10 err = - EIO; 
 
 11 goto out; 
 
 12 } 
 
 13 
 
 14 /* “请求队列”分配 */ 
 
 
 15 xxx_ 
 queue = blk_ 
 alloc_ 
 queue(GFP_ 
 KERNEL); 
 
 16 if (!xxx_queue) 
 
 17 goto out_queue; 
 
 18 
 
 
 19 blk_ 
 queue_ 
 make_ 
 request(xxx_ 
 queue, &xxx_ 
 make_ 
 request); /* 绑定“制造请求”函数 
 */ 
 
 20 blk_queue_hardsect_size(xxx_queue, xxx_blocksize); /* 硬件扇区尺寸设置 */ 
 
 21 
 
 22 /* gendisk初始化 */ 
 
 23 xxx_disks->major = XXX_MAJOR; 
 
 24 xxx_disks->first_minor = 0; 
 
 25 xxx_disks->fops = &xxx_op; 
 
 26 xxx_disks->queue = xxx_queue; 
 
 27 sprintf(xxx_disks->disk_name, "xxx%d", i); 
 
 28 add_disk(xxx_disks); /* 添加gendisk */ 
 
 29



30 return 0; 
 
 31 out_queue: unregister_blkdev(XXX_MAJOR, "xxx"); 
 
 32 out: put_disk(xxx_disks); 
 
 33 blk_cleanup_queue(xxx_queue); 
 
 34 
 
 35 return -ENOMEM; 
 
 36 }

代码清单13.10 块设备驱动的模块加载函数模板（使用blk.init.queue）

1 static int _ _init xxx_init(void) 
 
 2 { 
 
 3 /* 块设备驱动注册 */ 
 
 4 if (register_blkdev(XXX_MAJOR, "xxx")) { 
 
 5 err = - EIO; 
 
 6 goto out; 
 
 7 } 
 
 8 
 
 9 /* 请求队列初始化 */ 
 
 
 10 xxx_ 
 queue = blk_ 
 init_ 
 queue(xxx_ 
 request, xxx_ 
 lock); 
 
 11 if (!xxx_queue) 
 
 12 goto out_queue; 
 
 13 
 
 14 blk_queue_hardsect_size(xxx_queue, xxx_blocksize); /* 硬件扇区尺寸设置 */ 
 
 15 
 
 16 /* gendisk初始化 */ 
 
 17 xxx_disks->major = XXX_MAJOR; 
 
 18 xxx_disks->first_minor = 0; 
 
 19 xxx_disks->fops = &xxx_op; 
 
 20 xxx_disks->queue = xxx_queue; 
 
 21 sprintf(xxx_disks->disk_name, "xxx%d", i); 
 
 22 set_capacity(xxx_disks, xxx_size *2); 
 
 23 add_disk(xxx_disks); //添加gendisk 
 
 24 
 
 25 return 0; 
 
 26 out_queue: unregister_blkdev(XXX_MAJOR, "xxx"); 
 
 27 out: put_disk(xxx_disks); 
 
 28 blk_cleanup_queue(xxx_queue); 
 
 29 
 
 30 return - ENOMEM; 
 
 31 }

在块设备驱动的模块卸载函数中完成与模块加载函数相反的工作。

① 清除请求队列。

② 删除gendisk和对gendisk的引用。

③ 删除对块设备的引用，注销块设备驱动。

代码清单13.11给出了块设备驱动的模块卸载函数的模板。

代码清单13.11 块设备驱动的模块卸载函数模板

1 static void _ _exit xxx_exit(void) 
 
 2 { 
 
 3 if (bdev) { 
 
 4 invalidate_bdev(xxx_bdev, 1); 
 
 5 blkdev_put(xxx_bdev);



6 } 
 
 7 del_gendisk(xxx_disks); /* 删除gendisk */ 
 
 8 put_disk(xxx_disks); 
 
 9 blk_cleanup_queue(xxx_queue[i]); /* 清除请求队列 */ 
 
 10 unregister_blkdev(XXX_MAJOR, "xxx"); 
 
 11 }

