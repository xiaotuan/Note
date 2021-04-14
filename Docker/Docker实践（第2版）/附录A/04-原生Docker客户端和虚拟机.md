### A.3　原生Docker客户端和虚拟机

一个常用的（且官方推荐的）方式是，拥有一台运行着Linux和Docker的最小虚拟机，再安装一个和虚拟机上的Docker通信的Docker客户端。

目前实现这一点支持并且推荐的做法有两种。

+ Mac用户安装Docker Mac版，参见官方文档。
+ Windows用户安装Docker Windows版，参见官方文档。

和A.1节讨论过的虚拟机的方式不同，由Docker为Mac/Windows创建的虚拟机是非常轻量的，因为它只运行Docker，但是值得注意的是，如果运行资源消耗大的程序，仍然要在设置中调整虚拟机的内存。

请不要将Windows上的Docker和Windows容器混淆（尽管可以在安装完Docker Windows版后可以使用Windows容器）。注意，由于依赖新版的Hyper-V功能，Docker Windows版需要运行在Windows 10上（但是 **不** 支持Windows 10家庭版）。

如果读者使用的是Windows 10家庭版或者更旧的Windows版本，那么可能还想尝试安装Docker Toolbox，这是之前的旧办法。Docker公司将其描述为遗留版本，因此，我们强烈建议只要能使用其他办法使用Docker就用其他办法，否则可能会遇到下面这些情况。

+ 在卷的开头需要双斜杠。
+ 因为容器是在并没有集成到系统中的虚拟机内运行的，如果想要从宿主机上访问公开的端口，就需要在shell中使用 `docker-machine ip default` 找到虚拟的IP来访问它。
+ 如果要将端口公开到宿主机外，就需要使用socat之类的工具来做端口转发。

如果之前用过Docker Toolbox，并希望升级到更新版本的工具，可以在Docker网站上找到针对Mac和Windows的迁移说明。

这里提到的Docker Toolbox只是作为一种备选方案。

