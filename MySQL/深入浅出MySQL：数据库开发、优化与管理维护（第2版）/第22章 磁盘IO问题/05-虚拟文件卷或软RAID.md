

最初，RAID 都是由硬件实现的，要使用 RAID，至少需要有一个 RAID 卡。但现在，一些操作系统中提供的软件包，也模拟实现了一些RAID的特性，虽然性能上不如硬RAID，但相比单个磁盘，性能和可靠性都有所改善。比如，Linux下的逻辑卷（Logical Volume）系统 lvm2，支持条带化（Stripe）；Linux下的MD（Multiple Device）驱动，支持RAID 0、RAID 1、RAID 4、RAID 5、RAID 6等。在不具备硬件条件的情况下，可以考虑使用上述虚拟文件卷或软RAID技术，具体配置方法可参见Linux帮助文档。



