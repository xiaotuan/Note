### 64.2.4　获取从设备名称：ptsname()

函数ptsname()返回伪终端从设备的名称，该从设备同文件描述符 mfd 所代表的伪终端主设备相关联。



![1669.png](../images/1669.png)
在 Linux（以及大多数实现中）上，ptsname()返回形为/dev/pts/nn的字符串，这里的nn由该伪终端从设备专有的唯一标识号所取代。

返回的从设备名称所占用的缓冲区通常是静态分配的。因此后续对ptsname()的调用将覆盖前次的结果。

> GNU C函数库提供了一个可重入版的ptsname()——ptsname_r(mfd, strbuf, buflen)。但是，这个函数不是标准函数，只在几种其他UNIX实现中才存在。必须定义_GNU_SOURCE测试宏才能从<stdlib.h>中得到可重入版的声明。

一旦通过unlockpt()解锁了从设备，我们就可以用传统的系统调用open()来打开它。

> 在采用了STREAMS机制的System V衍生系统上，可能还需要执行一些额外的步骤（将STREAMS模块加载到从设备上，之后再打开）。关于如何执行这些步骤，可以参考[Stevens & Rago, 2005]中的例子。

