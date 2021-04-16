### 10.5.2 内核中延迟的工作delayed_work

注意，对于这种周期性的任务，Linux内核还提供了一套封装好的快捷机制，其本质利用工作队列和定时器实现，这套快捷机制是就是delayed_work，delayed_work结构体的定义如代码清单10.11所示。

代码清单10.11 delayed_work结构体

1 struct delayed_work { 
 
 2 struct work_struct work; 
 
 3 struct timer_list timer; 
 
 4 };



5 struct work_struct { 
 
 6 atomic_long_t data; 
 
 7 #define WORK_STRUCT_PENDING 0 
 
 8 #define WORK_STRUCT_FLAG_MASK (3UL) 
 
 9 #define WORK_STRUCT_WQ_DATA_MASK (～WORK_STRUCT_FLAG_MASK) 
 
 10 struct list_head entry; 
 
 11 work_func_t func; 
 
 12 #ifdef CONFIG_LOCKDEP 
 
 13 struct lockdep_map lockdep_map; 
 
 14 #endif 
 
 15 };

我们可以通过如下函数调度一个delayed_work在指定的延时后执行：

int schedule_delayed_work(struct delayed_work *work, unsigned long delay);

当指定的delay到来时delayed_work结构体中work成员的work_func_t类型成员func()会被执行。work_func_t类型定义为：

typedef void (*work_func_t)(struct work_struct *work);

其中delay参数的单位是jiffies，因此一种常见的用法如下：

schedule_delayed_work(&work, msecs_to_jiffies(poll_interval));

其中的msecs_to_jiffies()用于将毫秒转化为jiffies。

如果要周期性的执行任务，通常会在delayed_work的工作函数中再次调用schedule_delayed_ work()，周而复始。

如下函数用来取消delayed_work：

int cancel_delayed_work(struct delayed_work *work); 
 
 int cancel_delayed_work_sync(struct delayed_work *work);

