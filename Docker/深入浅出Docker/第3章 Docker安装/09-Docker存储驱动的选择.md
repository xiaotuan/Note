## 3.6　Docker存储驱动的选择

每个Docker容器都有一个本地存储空间，用于保存层叠的镜像层（Image Layer）以及挂载的容器文件系统。默认情况下，容器的所有读写操作都发生在其镜像层上或挂载的文件系统中，所以存储是每个容器的性能和稳定性不可或缺的一个环节。

以往，本地存储是通过存储驱动（Storage Driver）进行管理的，有时候也被称为Graph Driver或者 GraphDriver。虽然存储驱动在上层抽象设计中都采用了栈式镜像层存储和写时复制（Copy-on-Write）的设计思想，但是Docker在Linux底层支持几种不同的存储驱动的具体实现，每一种实现方式都采用不同方法实现了镜像层和写时复制。虽然底层实现的差异不影响用户与Docker之间的交互，但是对Docker的性能和稳定性至关重要。

在Linux上，Docker可选择的一些存储驱动包括AUFS（最原始也是最老的）、Overlay2（可能是未来的最佳选择）、Device Mapper、Btrfs和ZFS。

Docker在Windows操作系统上只支持一种存储驱动，即 `Windows Filter` 。

存储驱动的选择是节点级别的。这意味着每个Docker主机只能选择一种存储驱动，而不能为每个容器选择不同的存储驱动。在Linux上，读者可以通过修改 `/etc/docker/daemon.json` 文件来修改存储引擎配置，修改完成之后需要重启Docker才能够生效。下面的代码片段展示了如何将存储驱动设置为 `overlay2` 。

```rust
{
  "storage-driver": "overlay2"
}
```

注：

> 如果配置所在行不是文件的最后一行，则需要在行尾处增加逗号。

如果读者修改了正在运行Docker主机的存储引擎类型，则现有的镜像和容器在重启之后将不可用，这是因为每种存储驱动在主机上存储镜像层的位置是不同的（通常在 `/var/lib/docker/ <storage-driver>/...` 目录下）。修改了存储驱动的类型，Docker就无法找到原有的镜像和容器了。切换到原来的存储驱动，之前的镜像和容器就可以继续使用了。

如果读者希望在切换存储引擎之后还能够继续使用之前的镜像和容器，需要将镜像保存为Docker格式，上传到某个镜像仓库，修改本地Docker存储引擎并重启，之后从镜像仓库将镜像拉取到本地，最后重启容器。

通过下面的命令来检查Docker当前的存储驱动类型。

```rust
$ docker system info
<Snip>
Storage Driver: overlay2
  Backing Filesystem: xfs
  Supports d_type: true
  Native Overlay Diff: true
<Snip>
```

选择存储驱动并正确地配置在Docker环境中是一件重要的事情，特别是在生产环境中。下面的清单可以作为一个 **参考指南** ，帮助读者选择合适的存储驱动。但是，本书仍建议读者参阅Docker官网上由Linux发行商提供的最新文档来做出选择。

+ Red Hat Enterprise Linux：4.x版本内核或更高版本 + Docker 17.06版本或更高版本，建议使用Overlay2。
+ Red Hat Enterprise Linux：低版本内核或低版本的Docker，建议使用Device Mapper。
+ Ubuntu Linux：4.x版本内核或更高版本，建议使用Overlay2。
+ Ubuntu Linux：更早的版本建议使用AUFS。
+ SUSE Linux Enterprise Server：Btrfs。

再次强调，上面的清单内容只是一个参考建议。读者需要时刻关注Docker文档中关于存储驱动的最新支持和版本兼容列表。尤其当读者正在使用Docker企业版（EE），并且有售后支持合同的情况下，更有必要查阅最新文档。

