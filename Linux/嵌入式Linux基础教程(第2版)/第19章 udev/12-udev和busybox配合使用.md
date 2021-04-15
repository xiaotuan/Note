### 19.8　udev和busybox配合使用

回顾一下代码清单19-4中的第一条规则。这条规则在执行 `modprobe` 命令时使用了 `-b` 标志，这个标志用于检查模块黑名单。目前，这和busybox中的modprobe是不兼容的<a class="my_markdown" href="['#anchor198']"><sup class="my_markdown">[8]</sup></a>。如果不对 `modprobe` 作修改，任何驱动都不会被加载。但是这个错误不容易发现，因为udev守护进程在执行程序（比如modprobe）时会接收它打印到stdout和stderr中的消息。因此，错误消息不会显示在控制台上。

<a class="my_markdown" href="['#ac198']">[8]</a>　在busybox v1.41.1中测试。

解决这个问题的最简单方法是使用modprobe的真实版本——也就是在你的嵌入式系统中使用module-init-tools软件包。这个软件包中包含了完整版本的 `modprobe` 、 `lsmod` 和 `insmod` 。此外，还需要在编译busybox时禁用其中的 `depmod` ，或者至少是将那些指向busybox以实现module-init-tools功能的符号链接都删除掉。根据busybox的具体配置，你可能会使用链接或scriptlet（简单的脚本包裹程序）为每种支持的功能执行busybox。请参考第11章，以了解更多有关安装选项的详细信息。

