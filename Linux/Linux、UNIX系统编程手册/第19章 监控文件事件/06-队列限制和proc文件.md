### 19.5　队列限制和/proc文件

对inotify事件做排队处理，需要消耗内核内存。正因如此，内核会对inotify机制的操作施以各种限制。超级用户可配置/proc/sys/fs/inotify路径中的3个文件来调整这些限制：

##### max_queued_events

调用inotify_init()时，使用该值来为新inotify实例队列中的事件数量设置上限。一旦超出这一上限，系统将生成IN_Q_OVERFLOW事件，并丢弃多余的事件。溢出事件的wd字段值为−1。

##### max_user_instances

对由每个真实用户ID创建的inotify实例数的限制值。

##### max_user_watches

对由每个真实用户ID创建的监控项数量的限制值。

这3个文件的典型默认值分别为16384、128和8192。

