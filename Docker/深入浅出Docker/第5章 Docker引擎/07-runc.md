### 5.2.4　runc

如前所述，runc是OCI容器运行时规范的参考实现。Docker公司参与了规范的制定以及runc的开发。

去粗取精，会发现runc实质上是一个轻量级的、针对Libcontainer进行了包装的命令行交互工具（Libcontainer取代了早期Docker架构中的LXC）。

runc生来只有一个作用——创建容器，这一点它非常拿手，速度很快！不过它是一个CLI包装器，实质上就是一个独立的容器运行时工具。因此直接下载它或基于源码编译二进制文件，即可拥有一个全功能的runc。但它只是一个基础工具，并不提供类似Docker引擎所拥有的丰富功能。

有时也将runc所在的那一层称为“OCI层”，如图5.3所示。关于runc的发布信息见GitHub中opencontainers/runc库的release。

