### 35.3.4　SCHED_RR时间片

通过sched_rr_get_interval()系统调用能够找出SCHED_RR进程在每次被授权使用CPU时分配到的时间片的长度。



![932.png](../images/932.png)
与其他进程调度系统调用一样，pid标识出了需查询信息的进程，当pid为0时表示调用进程。返回的时间片是由tp指向的timespec结构。



![933.png](../images/933.png)
> 在最新的2.6内核中，实时循环时间片是0.1秒。

