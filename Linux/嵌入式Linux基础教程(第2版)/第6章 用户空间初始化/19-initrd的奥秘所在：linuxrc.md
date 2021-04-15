### 6.4.3　 `initrd` 的奥秘所在：linuxrc

当内核引导时，它首先会检测 `initrd` 镜像是否存在。然后，它会将这个压缩的二进制文件从内存中的指定位置复制到一个合适的内核ramdisk中，并挂载它作为根文件系统。 `initrd` 的奥秘来自一个特殊文件的内容，而这个文件就存储在 `initrd` 镜像中。当内核挂载初始的ramdisk时，它会查找一个名为linuxrc的特殊文件。它将这个文件当作是一个脚本文件，并执行其中包含的命令。这种机制允许系统设计者控制 `initrd` 的行为。代码清单6-11显示了一个linuxrc文件的内容。

代码清单6-11　linuxrc文件示例



![108.png](../images/108.png)
实际上，这个文件会包含一些命令，而它们需要在挂载真正的根文件系统之前执行。举例来说，该文件可能会包含一条加载CompactFlash驱动程序的命令，以便从CompactFlash设备上获取一个真正的根文件系统。在代码清单6-6的例子中，仅仅创建一个busybox shell，并且暂停了引导过程以便检查。你可以从代码清单6-10中看到由busybox shell生成的 `#` 命令行提示符。如果在此输入 `exit` 命令，内核会继续其引导过程直至完成。

当内核将ramdisk（ `initrd` 镜像）从物理内存复制到一个内核ramdisk之后，它会将这块物理内存归还到系统的可用内存池中。你可以认为这是将 `initrd` 镜像转移了一下，从物理内存的一个固定地址转移到内核自身的虚拟内存中（形式是一个内核ramdisk设备）。

关于代码清单6-11还有最后一点要注意：挂载/proc文件系统时使用的 `mount` 命令<a class="my_markdown" href="['#anchor069']"><sup class="my_markdown">[9]</sup></a>似乎多用了一个proc。下面这个命令也是有效的：



![109.png](../images/109.png)
<a class="my_markdown" href="['#ac069']">[9]</a>　挂载文件系统所用的 `mount` 命令的格式为： `mount -t type device directory` 。——译者注

注意 `mount` 命令中的 `device` 字段已经被替换成了 `none` 。 `mount` 命令会忽略 `device` 字段，因为没有任何物理设备和proc文件系统相关联。命令中有 `-t proc` 就足够了，这会指示 `mount` 将/proc文件系统挂载到 `/proc` 挂载点（目录）上。使用前一种命令是为了说明我们实际上是将一个内核伪设备（/proc文件系统）挂载到/proc上。mount命令会忽略device参数，你可以选择自己喜欢的方式。使用前一种命令形式挂载成功后，在命令行中输入 `mount` 时<a class="my_markdown" href="['#anchor0610']"><sup class="my_markdown">[10]</sup></a>，输出信息中的 `device` 字段会显示为 `proc` ，而不是 `none` ，这就会提醒你这是一个虚拟文件系统。

<a class="my_markdown" href="['#ac0610']">[10]</a>　如果输入 `mount` 命令时不带任何参数，这个命令会输出所有已挂载的文件系统的信息。——译者注

