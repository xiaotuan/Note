### 49.6　其他mmap()标记

除了MAP_PRIVATE和MAP_SHARED之外，Linux允许在mmap() flags参数中包含其他一些值（取OR）。表49-3对这些值进行了总结。除了MAP_PRIVATE和MAP_SHARED之外，在SUSv3中仅规定了MAP_FIXED标记。

<center class="my_markdown"><b class="my_markdown">表49-3：mmap() flags参数的位掩码值</b></center>

| 值 | 描 述 | SUSv3 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| MAP_ANONYMOUS | 创建一个匿名映射 |
| MAP_FIXED | 原样解释addr参数（49.10节） | ● |
| MAP_LOCKED | 将映射分页锁进内存（自Linux 2.6起） |
| MAP_HUGETLB | 创建一个使用巨页的映射（自Linux 2.6.32起） |
| MAP_NORESERVE | 控制交换空间的预留（49.9节） |
| MAP_NORESERVE | 对映射数据的修改是私有的 | ● |
| MAP_POPULATE | 填充一个映射的分页（自Linux 2.6起） |
| MAP_SHARED | 发生在映射数据上的变更对其他进程可见并会被反映到底层文件上（与MAP_PRIVATE相反） | ● |
| MAP_UNINITIALIZED | 不清除匿名映射（自Linux 2.6.33起） |

下面提供了与表49-3中列出的flags值有关的更多细节信息（不包含MAP_PRIVATE和MAP_SHARED，因为之前已经介绍过这两个标记了）。

##### MAP_ANONYMOUS

创建一个匿名映射，即没有底层文件对应的映射。在49.7节中将会对这个标记进行深入介绍。

##### MAP_FIXED

在49.10节中将会对这个标记进行介绍。

##### MAP_HUGETLB（自Linux 2.6.32起）

这个标记在mmap()所起的作用与SHM_HUGETLB标记在System V共享内存段中所起的作用一样。参见48.2节。

##### MAP_LOCKED（自Linux 2.6起）

按照mlock()的方式预加载映射分页并将映射分页锁进内存。在50.2节中将会对使用这个标记所需的特权以及管理其操作的限制进行介绍。

##### MAP_NORESERVE

这个标记用来控制是否提前为映射的交换空间执行预留操作。细节信息请参见49.9节。

##### MAP_POPULATE（自Linux 2.6起）

填充一个映射的分页。对于文件映射来讲，这将会在文件上执行一个超前读取。这意味着后续对映射内容的访问不会因分页故障而发生阻塞（假设此时不会因内存压力而导致分页被交换出去）。

##### MAP_UNINITIALIZED（自Linux 2.6.33起）

指定这个标记会防止一个匿名映射被清零。它能够带来性能上的提升，但同时也带来了安全风险，因为已分配的分页中可能会包含上一个进程留下来的敏感信息。因此这个标记一般只供嵌入式系统使用，因为在这种系统中性能是一个至关重要的因素，并且整个系统都处于嵌入式应用程序的控制之下。这个标记只有在使用CONFIG_MMAP_ALLOW_UNINITIALIZED选项配置内核时才会生效。

