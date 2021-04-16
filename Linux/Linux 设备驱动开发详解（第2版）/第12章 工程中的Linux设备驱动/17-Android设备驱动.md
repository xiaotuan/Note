### 12.8 Android设备驱动

Android的设备驱动与Linux一样，因为Android本身基于Linux内核，但是Android对内核引入了如下主要补丁。

#### 1．binder IPC系统

binder机制是Android提供的一种进程间通信方法，使一个进程可以以类似远程过程调用的形式调用另一个进程所提供的功能，LDD6410开发板已经将它的代码移植到drivers/android/ binder.h、drivers/android/binder.c下面，从代码清单12.24可知，它就是一种典型的以miscdevice形式实现的字符设备，而且提供了一些/proc结点。本质上，binder用户空间的程序绝大多数情况下在底层是调用了binder驱动的ioctl()函数。

代码清单12.25 Android binder驱动

1 static struct file_operations binder_fops = { 
 
 2 .owner = THIS_MODULE, 
 
 3 .poll = binder_poll, 
 
 4 .unlocked_ioctl = binder_ioctl, 
 
 5 .mmap = binder_mmap, 
 
 6 .open = binder_open,



7 .flush = binder_flush, 
 
 8 .release = binder_release, 
 
 9 }; 
 
 10 
 
 11 static struct miscdevice binder_miscdev = { 
 
 12 .minor = MISC_DYNAMIC_MINOR, 
 
 13 .name = "binder", 
 
 14 .fops = &binder_fops 
 
 15 }; 
 
 16 
 
 17 static int __init binder_init(void) 
 
 18 { 
 
 19 int ret; 
 
 20 
 
 21 binder_proc_dir_entry_root = proc_mkdir("binder", NULL); 
 
 22 if (binder_proc_dir_entry_root) 
 
 23 binder_proc_dir_entry_proc = proc_mkdir("proc", binder_proc_dir_entry_root); 
 
 24 ret = misc_register(&binder_miscdev); 
 
 25 if (binder_proc_dir_entry_root) { 
 
 26 create_proc_read_entry("state", S_IRUGO, binder_proc_dir_entry_root, ...); 
 
 27 create_proc_read_entry("stats", S_IRUGO, binder_proc_dir_entry_root, ...); 
 
 28 create_proc_read_entry("transactions", S_IRUGO, ...); 
 
 29 create_proc_read_entry("transaction_log", S_IRUGO, ...); 
 
 30 create_proc_read_entry("failed_transaction_log", S_IRUGO, ...); 
 
 31 } 
 
 32 return ret; 
 
 33 }

Android中的binder通信基于Service/Client模型，所有需要IBinder通信的进程都必须创建一个IBinder接口。Android虚拟机启动之前系统会先启动Service Manager进程，Service Manager打开binder驱动，并通知binder驱动程序这个进程将作为System Service Manager，然后该进程将进入一个循环，等待处理来自其他进程的数据。

而在用户程序方面，Service端创建一个System Service后，通过defaultServiceManager()可以得到远程ServiceManager的接口，通过这个接口我们可以调用addService()函数将新的System Service添加到Service Manager进程中。对于Client端而言，则可以通过getService()获取到需要连接的目的Service的IBinder对象。对用户程序而言，获得这个对象后就可以通过binder驱动访问Service对象中的方法。

Client与Service在不同的进程中，通过这种方式实现了类似线程间的迁移的通信方式，对用户程序而言当调用Service返回的IBinder接口后，访问Service中的方法就如同调用自己的函数。两个进程间通信就好像是一个进程进入另一个进程执行代码然后带着执行的结果返回。

#### 2．ashemem内存共享机制

ashmem是Android新增的一种内存分配/共享机制，LDD6410开发板已经将它的代码移植到mm/ashmem.c下面。从代码清单12.26可知，它也是一种典型的以miscdevice形式实现的字符设备。

代码清单12.26 Android ashmem驱动

1 static struct file_operations ashmem_fops = { 
 
 2 .owner = THIS_MODULE, 
 
 3 .open = ashmem_open, 
 
 4 .release = ashmem_release,



5 .mmap = ashmem_mmap, 
 
 6 .unlocked_ioctl = ashmem_ioctl, 
 
 7 .compat_ioctl = ashmem_ioctl, 
 
 8 }; 
 
 9 
 
 10 static struct miscdevice ashmem_misc = { 
 
 11 .minor = MISC_DYNAMIC_MINOR, 
 
 12 .name = "ashmem", 
 
 13 .fops = &ashmem_fops, 
 
 14 }; 
 
 15 
 
 16 static int __init ashmem_init(void) 
 
 17 { 
 
 18 ... 
 
 19 
 
 20 ret = misc_register(&ashmem_misc); 
 
 21 if (unlikely(ret)) { 
 
 22 printk(KERN_ERR "ashmem: failed to register misc device!\n"); 
 
 23 return ret; 
 
 24 } 
 
 25 
 
 26 ... 
 
 27 }

在dev目录下对应的设备是/dev/ashmem，相比于传统的内存分配机制，如malloc、匿名/命名mmap，其好处是提供了辅助内核内存回收算法的pin/unpin机制。

ashmem的典型用法是先打开设备文件，然后做mmap映射。

（1）通过调用ashmem_create_region()函数打开和设置ashmem，这个函数的实质工作为：

fd = open("/dev/ashmem", O_RDWR); 
 
 ioctl(fd, ASHMEM_SET_NAME, region_name); 
 
 ioctl(fd, ASHMEM_SET_SIZE, region_size);

（2）应用程序一般会调用mmap来把ashmem分配的空间映射到进程空间：

mapAddr = mmap(NULL, pHdr->mapLength, PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0);

应用程序还可以通过ioctl()来pin（ASHMEM_PIN）和unpin（ASHMEM_UNPIN）某一段映射的空间，以提示内核的page cache算法可以把哪些页面回收，这是一般mmap做不到的。通过ASHMEM_GET_PIN_STATUS这个IOCTL可以查询pin的状态。

#### 3．Android电源管理

Android电源管理针对标准Linux内核的电源管理进行了一些优化，这部分代码LDD6410开发板已经移植到了kernel/power/目录，主要新增了如下文件：

kernel/power/earlysuspend.c 
 
 kernel/power/consoleearlysuspend.c 
 
 kernel/power/fbearlysuspend.c 
 
 kernel/power/wakelock.c 
 
 kernel/power/userwakelock.c

#### 4．Android Low Memory Killer

Linux内核本身提供了OOM（Out Of Memory）机制，它可以在系统内存不够的情况下主动杀死进程腾出内存。不过Android的Low Memory Killer相对于Linux标准OOM机制更加灵活，它可以根据需要杀死进程来释放内存。LDD6410板已将Low Memory Killer移植到drivers/android/lowmemorykiller.c文件。



#### 5．Android RAM console和log设备

为了辅助调试，Android增加了用于将内核打印消息保存起来的RAM console和用户应用程序可以写入、读取log信息的logger设备驱动。这两个驱动分别放置在drivers/android/ ram_console.c 和drivers/android/ logger.c文件。

RAM console通过register_console()被注册，关于这个接口，本书第14章会进行详细介绍，而logger又是一个典型的miscdevice。

#### 6．Android alarm、timed_gpio等。

就Android系统本身而言，在其上编写设备驱动没有什么神秘的，基本完全按照Linux内核本身的框架进行。而Android自身引入的这些补丁，曾经有部分进入过Linux mainline的drivers/staging目录，尔后由于缺少维护的原因，被Greg KH移除。

