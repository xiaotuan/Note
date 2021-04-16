### 11.4.2 申请与释放设备I/O端口和I/O内存

#### 1．I/O端口申请

Linux内核提供了一组函数用于申请和释放I/O端口。

struct resource *request_region(unsigned long first, unsigned long n, const char *name);

这个函数向内核申请n个端口，这些端口从first开始，name参数为设备的名称。如果分配成功返回值是非NULL，如果返回NULL，则意味着申请端口失败。

当用request_region()申请的I/O端口使用完成后，应当使用release_region()函数将它们归还给系统，这个函数的原型如下：

void release_region(unsigned long start, unsigned long n);

#### 2．I/O内存申请

同样，Linux内核也提供了一组函数用于申请和释放I/O内存的范围。

struct resource *request_mem_region(unsigned long start, unsigned long len, char *name);

这个函数向内核申请n个内存地址，这些地址从first开始，name参数为设备的名称。如果分配成功返回值是非 NULL，如果返回NULL，则意味着申请I/O内存失败。

当用request_mem_region()申请的I/O内存使用完成后，应当使用release_mem_region()函数将它们归还给系统，这个函数的原型如下：

void release_mem_region(unsigned long start, unsigned long len);

上述request_region()和release_mem_region()都不是必须的，但建议使用。其任务是检查申请的资源是否可用，如果可用则申请成功，并标志为已经使用，其他驱动想再次申请该资源时就会失败。

有许多设备驱动程序在没有申请I/O端口和I/O内存之前就直接访问了，这不够安全。

