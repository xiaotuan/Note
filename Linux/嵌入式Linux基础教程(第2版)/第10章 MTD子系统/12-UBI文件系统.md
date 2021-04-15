### 10.4　UBI文件系统

UBI（Unsorted Block Image）文件系统专门设计用于克服JFFS2文件系统的一些限制。可以将它看做是JFFS2的继任者，虽然JFFS2仍然在那些包含闪存的嵌入式Linux设备中得到广泛使用。UBI文件系统（UBIFS）的层次位于UBI设备之上，而UBI设备又依赖于MTD设备。

UBIFS改进了JFFS2文件系统的一个比较显著的缺陷：挂载时间。JFFS2在系统内存中维护一些索引元数据，每次系统启动时，它都必须读取这个索引以建立一个完整的目录树。这需要读取闪存设备的大部分内容。与此相反，UBIFS是在闪存设备上维护其索引元数据，因此，它不需要在每次挂载时都扫描闪存设备并重新建立索引。所以，挂载UBIFS要比挂载JFFS2快很多。

UBIFS还支持写缓存，这可以显著提升性能。你可以从以下网址了解更多UBIFS的优点：<a class="my_markdown" href="['http://www.linux-mtd.infradead.org/doc/ubifs.html']">www.linux-mtd.infradead.org/doc/ubifs.html</a>。

