### 13.5.4　objcopy

objcopy用于将一个二进制目标文件的内容复制到另一个文件中（对其进行格式化），而且在这个过程中可能会转换目标文件的格式。当我们需要为存储在ROM或闪存中的镜像生成代码时，这个工具特别有用。我们在第7章中介绍过U-Boot引导加载程序，它会使用objcopy将最终的ELF文件转换成binary或s-record格式<a class="my_markdown" href="['#anchor1310']"><sup class="my_markdown">[10]</sup></a>的输出文件。下面是一个objcopy的例子，这里使用它来构建一个闪存镜像。



![374.png](../images/374.png)
<a class="my_markdown" href="['#ac1310']">[10]</a>　s-record格式的文件是以ASCII码表示的二进制文件，很多设备烧写器和二进制实用程序都使用了这种格式。

这条命令显示了如何为闪存创建一个镜像。输入文件（在这个例子中是u-boot）是一个完整的ELF格式的U-Boot镜像，其中包括符号和重定位信息。objcopy只提取包含了程序代码和数据的相关段，并将它们放置到输出文件中，也就是命令行中指定的u-boot.bin<a class="my_markdown" href="['#anchor1311']"><sup class="my_markdown">[11]</sup></a>。

<a class="my_markdown" href="['#ac1311']">[11]</a>　输入文件u-boot的格式是ELF，而命令行中的 `-O binary` 指定了输出文件的格式是binary。——译者注

闪存块在被擦除后其内容为全1。因此，将二进制镜像中的间隙都填充为全1能够提高烧写的效率并延长闪存寿命，毕竟闪存的写寿命是有限的。这是通过objcopy的命令行参数 `--gap-fill` 来完成的。

这只是一个使用objcopy的简单例子。它可以生成s-record格式的文件，而且能够转换文件格式。请参考它的帮助手册以了解完整的细节。

