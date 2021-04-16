### 13.2.2 gendisk结构体

在Linux内核中，使用gendisk（通用磁盘）结构体来表示一个独立的磁盘设备（或分区），这个结构体的定义如代码清单13.2所示。

代码清单13.2 gendisk结构体

1 struct gendisk { 
 
 2 int major; /* 主设备号 */ 
 
 3 int first_minor; 
 
 4 int minors; /* 最大的次设备数，如果不能分区，则为1*/



5 
 
 6 char disk_name[DISK_NAME_LEN]; /* 设备名称 */ 
 
 7 
 
 8 /* 由partno索引的分区指针的数组 
 
 9 */ 
 
 10 struct disk_part_tbl *part_tbl; 
 
 11 struct hd_struct part0; 
 
 12 
 
 13 struct block_device_operations *fops; /* 块设备操作集合 */ 
 
 14 struct request_queue *queue; 
 
 15 void *private_data; 
 
 16 
 
 17 int flags; 
 
 18 struct device *driverfs_dev; // FIXME: remove 
 
 19 struct kobject *slave_dir; 
 
 20 
 
 21 struct timer_rand_state *random; 
 
 22 
 
 23 atomic_t sync_io; /* RAID */ 
 
 24 struct work_struct async_notify; 
 
 25 #ifdef CONFIG_BLK_DEV_INTEGRITY 
 
 26 struct blk_integrity *integrity; 
 
 27 #endif 
 
 28 int node_id; 
 
 29 };

major、first_minor和minors共同表征了磁盘的主、次设备号，同一个磁盘的各个分区共享一个主设备号，而次设备号则不同。fops为block_device_operations，即上节描述的块设备操作集合。queue是内核用来管理这个设备的I/O请求队列的指针。private_data可用于指向磁盘的任何私有数据，用法与字符设备驱动file结构体的private_data类似。hd_struct成员表示一个分区，而disk_part_tbl成员用于容纳分区表，part0和part_tbl二者的关系在于：

disk->part_tbl->part[0] = &disk->part0;

Linux内核提供了一组函数来操作gendisk，如下所示。

#### 1．分配gendisk

gendisk结构体是一个动态分配的结构体，它需要特别的内核操作来初始化，驱动不能自己分配这个结构体，而应该使用下列函数来分配gendisk：

struct gendisk *alloc_disk(int minors);

minors参数是这个磁盘使用的次设备号的数量，一般也就是磁盘分区的数量，此后minors不能被修改。

#### 2．增加gendisk

gendisk结构体被分配之后，系统还不能使用这个磁盘，需要调用如下函数来注册这个磁盘设备。

void add_disk(struct gendisk *disk);

特别要注意的是对add_disk()的调用必须发生在驱动程序的初始化工作完成并能响应磁盘的请求之后。

#### 3．释放gendisk

当不再需要一个磁盘时，应当使用如下函数释放gendisk。

void del_gendisk(struct gendisk *gp);



#### 4．gendisk引用计数

通过get_disk()和put_disk()函数可用来操作gendisk的引用计数，这个工作一般不需要驱动亲自做。这两个函数的原型分别为：

struct kobject *get_disk(struct gendisk *disk); 
 
 void put_disk(struct gendisk *disk);

前者最终会调用“kobject_get(&disk_to_dev(disk)->kobj);”，而后者则会调用“kobject_put (&disk_to_dev(disk)->kobj);”。

