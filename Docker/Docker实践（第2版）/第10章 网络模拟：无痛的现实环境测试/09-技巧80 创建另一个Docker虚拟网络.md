### 技巧80　创建另一个Docker虚拟网络

在人们首次了解创建自有虚拟网络的能力时，一个常见的反应是询问如何创建默认Docker网桥的副本，以便一组容器进行通信，但又是与其他容器隔离。

Docker公司意识到这将是一个大众化要求，因此在最初的实验性版本就将其作为虚拟网络首批功能之一实现了。

#### 问题

想要一个Docker公司支持的用于创建虚拟网络的解决方案。

#### 解决方案

使用嵌套在 `docker network` 下面的Docker子命令集来创建自己的虚拟网络。

内建的“网桥”驱动可能是最常用的驱动，它受到官方支持，允许你创建默认的内建网桥的新副本。但在本技巧的后面我们会看到两者的一个重要区别：在非默认的网桥里，你可以通过名称来ping容器。

使用 `docker network ls` 命令可以看到内建的网络列表：

```c
$ docker network ls
NETWORK ID          NAME           DRIVER             SCOPE
100ce06cd9a8        bridge         bridge             local
d53919a3bfa1        host           host               local
2d7fcd86306c        none           null               local
```

在此可以看到，我的机器上有3个网络可供容器加入。 `bridge` 网络是容器默认具有的，使其可与网桥上的其他容器对话。 `host` 网络指定了在启动容器时使用 `--net=host` 会发生什么（容器可以像机器上的其他正常程序那样看到这个网络），而 `none` 对应的是 `--net=none` ，容器将只有回送网卡。

我们来增加一个新的 `bridge` 网络，为容器提供一个可自由通信的新的扁平网络：

```c
$ docker network create --driver=bridge mynet
770ffbc81166d54811ecf9839331ab10c586329e72cea2eb53a0229e53e8a37f
$ docker network ls | grep mynet
770ffbc81166        mynet               bridge              local
$ ip addr | grep br-
522: br-91b29e0d29d5: <NO-
     CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group
➥ default
     inet 172.18.0.1/16 scope global br-91b29e0d29d5
$ ip addr | grep docker
5: docker0: <NO-
     CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group
➥ default
     inet 172.17.0.1/16 scope global docker0
```

这将创建一个新的网卡，使用与正常Docker网桥不同的IP地址范围。对于网桥，目前新的网卡名称将以 `br-` 开头，不过这点未来可能会有变化。

现在我们来启动两个附加到该网络的容器：

```c
$ docker run -it -d --name c1 ubuntu:14.04.2 bash　　⇽---　启动一个名为c1的容器（在默认网桥上）
 87c67f4fb376f559976e4a975e3661148d622ae635fae4695747170c00513165
$ docker network connect mynet c1　　⇽---　使用mynet网络连接c1容器
$ docker run -it -d --name c2 \
--net=mynet ubuntu:14.04.2 bash　　⇽---　在mynet网络里创建一个名为c2的容器
 0ee74a3e3444f27df9c2aa973a156f2827bcdd0852c6fd4ecfd5b152846dea5b
$ docker run -it -d --name c3 ubuntu:14.04.2 bash　　⇽---　启动一个名为c3的容器（在默认网桥上）
```

前面的命令演示了将容器连接到网络两种不同的方法——启动容器然后附加到服务上，以及在一个步骤里创建并附加。

两者之间有一个差异。前者会在启动时加入默认网络（通常是Docker网桥，不过这个可以通过Docker守护进程的参数自定义），然后添加一个新的网卡以便同时访问 `mynet` 。后者将只会加入 `mynet` ——普通Docker网桥上的任何容器都无法访问它。

我们来做些连通性检查。首先，看一下容器的IP地址：

```c
$ docker exec c1 ip addr | grep 'inet.*eth'　　⇽---　列出c1的网卡及IP地址—— 一个在默认网桥上，一个在mynet上
    inet 172.17.0.2/16 scope global eth0
    inet 172.18.0.2/16 scope global eth1
$ docker exec c2 ip addr | grep 'inet.*eth'　　⇽---　列出c2的网卡和IP地址——在mynet内部
   inet 172.18.0.3/16 scope global eth0
$ docker exec c3 ip addr | grep 'inet.*eth'
    inet 172.17.0.3/16 scope global eth0　　⇽---　列出c3的网卡及IP地址—— 在默认网桥上
```

现在我们可以做一些连通性测试：

```c
$ docker exec c2 ping -qc1 c1　　⇽---　尝试从容器2 ping容器1的名称（成功）
 PING c1 (172.18.0.2) 56(84) bytes of data.
--- c1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.041/0.041/0.041/0.000 ms
$ docker exec c2 ping -qc1 c3　　⇽---　
 ping: unknown host c3
$ docker exec c2 ping -qc1 172.17.0.3　　⇽---　尝试从容器2 ping容器3的名称和IP地址（失败）
 PING 172.17.0.3 (172.17.0.3) 56(84) bytes of data.
--- 172.17.0.3 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms
$ docker exec c1 ping -qc1 c2　　⇽---　尝试从容器1 ping容器2的名称（成功）
 PING c2 (172.18.0.3) 56(84) bytes of data.
--- c2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.047/0.047/0.047/0.000 ms
$ docker exec c1 ping -qc1 c3　　⇽---　
 ping: unknown host c3
$ docker exec c1 ping -qc1 172.17.0.3　　⇽---　尝试从容器1 ping容器3的名称和IP地址（失败，成功）
 PING 172.17.0.3 (172.17.0.3) 56(84) bytes of data.
--- 172.17.0.3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.095/0.095/0.095/0.000 ms
```

这里东西很多！以下是主要的收获。

+ 在新的网桥上，容器可以通过IP地址和名称ping通彼此。
+ 在默认网桥上，容器只能通过IP地址ping通彼此。
+ 跨多网桥的容器可以访问它们所属的任意网络上的容器。
+ 容器无法跨网桥相互访问，即便使用IP地址也不行。

#### 讨论

这个新的网桥创建功能曾与技巧77中的Docker Compose及技巧79中的Blockade一同使用来为容器提供通过名称相互ping的能力。不过你也看到了，这是一个高度灵活的功能，具备建立相当复杂的网络模型的潜力。

举个例子，你可能想在一台 **堡垒机** （提供对另一个更高价值网络的访问的一台锁定机器）做实验。通过将应用程序服务放在一个新的网桥中，然后仅通过同时连接默认网桥和新网桥的容器公开这些服务，你就可以在自己的机器上开始运行一些比较真实的渗透测试，同时保持隔离。

