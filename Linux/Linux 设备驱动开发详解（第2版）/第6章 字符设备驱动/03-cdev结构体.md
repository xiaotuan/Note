### 6.1.1 cdev结构体

在Linux 2.6内核中，使用cdev结构体描述一个字符设备，cdev结构体的定义如代码清单6.1。

代码清单6.1 cdev结构体

1 struct cdev { 
 
 2 struct kobject kobj; /* 内嵌的kobject对象 */ 
 
 3 struct module *owner; /*所属模块*/ 
 
 4 struct file_operations *ops; /*文件操作结构体*/ 
 
 5 struct list_head list; 
 
 6 dev_t dev; /*设备号*/ 
 
 7 unsigned int count; 
 
 8 };

cdev结构体的dev_t成员定义了设备号，为32位，其中12位主设备号，20位次设备号。使用下列宏可以从dev_t获得主设备号和次设备号：

MAJOR(dev_t dev) 
 
 MINOR(dev_t dev)

而使用下列宏则可以通过主设备号和次设备号生成dev_t：

MKDEV(int major, int minor)

cdev结构体的另一个重要成员file_operations定义了字符设备驱动提供给虚拟文件系统的接口函数。

Linux 2.6内核提供了一组函数用于操作cdev结构体：

void cdev_init(struct cdev *, struct file_operations *); 
 
 struct cdev *cdev_alloc(void); 
 
 void cdev_put(struct cdev *p); 
 
 int cdev_add(struct cdev *, dev_t, unsigned); 
 
 void cdev_del(struct cdev *);

cdev_init()函数用于初始化cdev的成员，并建立cdev和file_operations之间的连接，其源代码如代码清单6.2所示。

代码清单6.2 cdev_init()函数

1 void cdev_init(struct cdev *cdev, struct file_operations *fops) 
 
 2 { 
 
 3 memset(cdev, 0, sizeof *cdev); 
 
 4 INIT_LIST_HEAD(&cdev->list); 
 
 5 kobject_init(&cdev->kobj, &ktype_cdev_default); 
 
 6 cdev->ops = fops; /*将传入的文件操作结构体指针赋值给cdev的ops*/ 
 
 7 }

cdev_alloc()函数用于动态申请一个cdev内存，其源代码如代码清单6.3所示。

代码清单6.3 cdev_alloc()函数

1 struct cdev *cdev_alloc(void) 
 
 2 {



3 struct cdev *p = kzalloc(sizeof(struct cdev), GFP_KERNEL); 
 
 4 if (p) { 
 
 5 INIT_LIST_HEAD(&p->list); 
 
 6 kobject_init(&p->kobj, &ktype_cdev_dynamic); 
 
 7 } 
 
 8 return p; 
 
 9 }

cdev_add()函数和cdev_del()函数分别向系统添加和删除一个cdev，完成字符设备的注册和注销。对cdev_add()的调用通常发生在字符设备驱动模块加载函数中，而对cdev_del()函数的调用则通常发生在字符设备驱动模块卸载函数中。

