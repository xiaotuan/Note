### 10.4.3　使用UBIFS作为根文件系统

现在，我们已经在/dev/mtd4中放置了一个镜像，我们可以让内核挂载这个文件系统作为其根文件系统。为此，我们可以将下面这些命令行参数传递给内核：



![277.png](../images/277.png)
这组命令行参数会指示内核将设备mtd4附着到ubi0，并且挂载这个UBI设备作为其根文件系统。如果遇到麻烦，请确认在内核命令行中包含了合适的 `rootdelay` 参数<a class="my_markdown" href="['#anchor109']"><sup class="my_markdown">[9]</sup></a>。在这个例子中，我们需要设置 `rootdelay=1` ，以确保内核在挂载UBIFS作为根文件系统时，UBI层和UBIFS层都已经准备就绪。

<a class="my_markdown" href="['#ac109']">[9]</a>　这个参数用于设置挂载根文件系统之前的延时时间，以秒为单位。——译者注

