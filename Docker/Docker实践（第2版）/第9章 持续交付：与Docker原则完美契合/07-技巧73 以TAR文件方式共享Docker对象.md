### 技巧73　以TAR文件方式共享Docker对象

TAR文件是Linux上移动文件的一种传统方法。在没有注册中心或者没必要设立注册中心的情况下，Docker允许手工创建TAR文件然后进行移动。下面展示这些命令的详细内容。

#### 问题

想要在没有注册中心的情况下与其他人共享镜像和容器。

#### 解决方案

使用 `docker export` 或 `docker save` 创建 TAR 文件，然后经由 SSH 使用 `docker import` 或 `docker load` 来使用它们。

如果只是随意地使用这些命令，它们之间的区别将难于掌握，因此下面花点儿时间快速看一下它们都做了什么。表9-1概述了这些命令的输入与输出。

<center class="my_markdown"><b class="my_markdown">表9-1　 `export` 和 `import` 与 `save` 和 `load` 的对比</b></center>

| 命令 | 创建了 | 目标类型 | 来源 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| `export` | TAR文件 | 容器文件系统 | 容器 |
| `import` | Docker镜像 | 平面文件系统 | TAR文件 |
| `save` | TAR文件 | Docker镜像（带历史记录） | 镜像 |
| `load` | Docker镜像 | Docker镜像（带历史记录） | TAR文件 |

前两个命令使用平面文件系统。 `docker export` 命令输出一个TAR文件，这个TAR文件包含了组成容器状态的文件。在Docker中，正在运行进程的状态不会被保存——只有文件。 `docker import` 命令从TAR文件创建Docker镜像——没有历史也没有元数据。

这些命令不是对称的——无法仅使用 `import` 和 `export` 从现有容器创建一个容器。这种不对称非常有用，因为可以使用 `docker export` 将一个镜像导出成一个TAR文件，然后使用 `docker import` 导入从而“丢弃”所有的层历史及元数据。这就是技巧52中描述的镜像扁平化方法。

在导出或保存成TAR文件时，文件会被默认发送到标准输出（ `stdout` ）中，因此需要像下面这样确保将其保存到文件中：

```c
docker pull debian:7:3
[...]
docker save debian:7.3 > debian7_3.tar
```

类似刚创建的TAR文件可以安全地在网络中传播（不过你可能会想先用gzip做一下压缩），其他人可以使用它们导入完整镜像。你可以通过邮件或 `scp` 来发送它们：

```c
$ scp debian7_3.tar example.com:/tmp/debian7_3.tar
```

如果拥有相应权限，还可以更进一步，直接将镜像发送给其他用户的Docker守护进程，如代码清单9-5所示。

代码清单9-5　通过SSH直接发送镜像

```c
docker save debian:7.3 | \　　⇽---　 docker save命令将7.3版本的Debian提取出来，并通过管道发送给ssh命令
 ssh example.com \　　⇽---　 ssh命令在远程机器example.com上运行命令
docker load -　　⇽---　 docker load命令从赋予它的TAR文件创建所有历史的镜像，-表示TAR文件是通过标准输入获取的
```

如果要舍弃镜像的历史，可以使用 `import` 而不是 `load` ，如代码清单9-6所示。

代码清单9-6　通过SSH直接传输镜像，并舍弃层

```c
docker export $(docker run -d debian:7.3 true) | \
    ssh example.com docker import
```



**注意**

与 `docker import` 不同， `docker load` 不需要在最后使用一个 `-` 来表示TAR文件是通过标准输入获取的。



#### 讨论

你可能还记得技巧52中的导出和导入过程，在那里你看到了如何通过扁平化镜像来移除隐藏在较低层中的机密信息。在传输镜像给其他人时需要牢记一个事实：机密信息可能能从较低层中获取——如果你在镜像上层删除了公共密钥，但它还存在于较低层中，这将是一个真正的麻烦事，因为你需要将其视为威胁，并在所有地方做修改。

如果你发现自己大量使用本技巧来传输镜像，可能还是值得投入点时间到技巧9中设置自己的注册中心，让事情变得正式一些。

