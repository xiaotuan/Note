### 技巧78　使用Comcast模拟有问题的网络

尽管用户在进行跨多主机分发应用程序时希望网络状况尽可能好，但现实却是残酷的——分组（packet，也称数据包）丢失（也称丢包）、连接中断、网络分区比比皆是，尤其是在商用云服务供应商上。

在技术栈遭遇现实世界的这些情况之前对其进行测试以确认其行为是非常明智的—— 一个为高可用设计的应用程序不应在外部服务开始出现显著的额外延迟时陷入停顿。

#### 问题

想要为单个容器应用不同的网络状况。

#### 解决方案

使用Comcast（指的是网络工具，而非ISP）。

#### 讨论

Comcast是一个娱乐化命名的工具，用于修改Linux机器的网络接口，以便对其应用某些不同寻常的（或者，对不走运的人而言是典型的）状况。

在Docker创建容器时，它会同时创建几个虚拟的网络接口——这也是容器具有不同IP地址并且可以相互通信的原因。因为这些都是标准网络接口，只要能查找出其网络接口名称，就可以在其上使用Comcast。这说起来容易做起来难。

代码清单10-10展示了包含Comcast及其前置要求以及一些优化的Docker镜像。

代码清单10-10　为运行comcast镜像做准备

```c
$ IMG=dockerinpractice/comcast
$ docker pull $IMG
latest: Pulling from dockerinpractice/comcast
[...]
Status: Downloaded newer image for dockerinpractice/comcast:latest
$ alias comcast="docker run --rm --pid=host --privileged \
-v /var/run/docker.sock:/var/run/docker.sock $IMG"
$ comcast -help
Usage of comcast:
  -cont string
        Container ID or name to get virtual interface of
  -default-bw int
        Default bandwidth limit in kbit/s (fast-lane) (default -1)
  -device string
        Interface (device) to use (defaults to eth0 where applicable)
  -dry-run
        Specifies whether or not to actually commit the rule changes
  -latency int
        Latency to add in ms (default -1)
  -packet-loss string
        Packet loss percentage (e.g. 0.1%)
  -stop
        Stop packet controls
  -target-addr string
        Target addresses, (e.g. 10.0.0.1 or 10.0.0.0/24 or >
10.0.0.1,192.168.0.0/24 or 2001:db8:a::123)
  -target-bw int
        Target bandwidth limit in kbit/s (slow-lane) (default -1)
  -target-port string
        Target port(s) (e.g. 80 or 1:65535 or 22,80,443,1000:1010)
  -target-proto string
        Target protocol TCP/UDP (e.g. tcp or tcp,udp or icmp) (default >
"tcp,udp,icmp")
  -version
        Print Comcast's version
```

这里新增的优化提供了 `-cont` 选项，可以指向一个容器而无须查找虚拟网络接口的名称。请注意，为了赋予容器更多权限， `docker run` 命令中增加了一些特殊的标志，这样Comcast就可以自由地对网络接口进行检查并应用变更。

为了展示Comcast可以带来的变化，先来看一下一个正常的网络连接是什么样的。打开一个新的终端，并执行以下命令来设置基准网络性能的预期：

```c
$ docker run -it --name c1 ubuntu:14.04.2 bash
root@0749a2e74a68:/# apt-get update && apt-get install -y wget
[...]
root@0749a2e74a68:/# ping -q -c 5 www.example.com
PING www.example.com (93.184.216.34) 56(84) bytes of data.
--- www.example.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, >
time 4006ms　　⇽---　这台机器与www. example.com的连接看起来是可靠的，没有分组丢失
 rtt min/avg/max/mdev = 86.397/86.804/88.229/0.805 ms　　⇽---　到www.example.com的平均往返时间在100毫秒左右
 root@0749a2e74a68:/# time wget -o /dev/null https://www.example.com
real    0m0.379s　　⇽---　下载www. example.com的HTML首页总共花费时间大概是0.7秒
 user    0m0.008s
sys     0m0.008s
root@0749a2e74a68:/#
```

完成上述步骤后，保持该容器处于运行状态，然后对其应用一些网络状况：

```c
$ comcast -cont c1 -default-bw 50 -latency 100 -packet-loss 20%
Found interface veth62cc8bf for container 'c1'
sudo tc qdisc show | grep "netem"
sudo tc qdisc add dev veth62cc8bf handle 10: root htb default 1
sudo tc class add dev veth62cc8bf parent 10: classid 10:1 htb rate 50kbit
sudo tc class add dev veth62cc8bf parent 10: classid 10:10 htb rate 1000000kb
➥ it
sudo tc qdisc add dev veth62cc8bf parent 10:10 handle 100: netem delay 100ms
➥ loss 20.00%
sudo iptables -A POSTROUTING -t mangle -j CLASSIFY --set-class 10:10 -p tcp
sudo iptables -A POSTROUTING -t mangle -j CLASSIFY --set-class 10:10 -p udp
sudo iptables -A POSTROUTING -t mangle -j CLASSIFY --set-class 10:10 -p icmp
sudo ip6tables -A POSTROUTING -t mangle -j CLASSIFY --set-class 10:10 -p tcp
sudo ip6tables -A POSTROUTING -t mangle -j CLASSIFY --set-class 10:10 -p udp
sudo ip6tables -A POSTROUTING -t mangle -j CLASSIFY --set-class 10:10 -p icmp
Packet rules setup...
Run 'sudo tc -s qdisc' to double check
Run 'comcast --device veth62cc8bf --stop' to reset
```

上述命令应用了3种不同的状况：针对所有目标设置50 KB/s的带宽上限（唤起了对拨号的回忆），（在所有固定延迟之上）添加100毫秒的延迟，以及20%的分组丢失率。

Comcast首先确定容器正确的虚拟网络接口，然后调用一些标准的Linux命令行网络工具来应用流量规则，并在执行过程中列出其所做的动作。来看一下容器是如何对此进行回应的：

```c
root@0749a2e74a68:/# ping -q -c 5 www.example.com
PING www.example.com (93.184.216.34) 56(84) bytes of data.
--- www.example.com ping statistics ---
5 packets transmitted, 2 received, 60% packet loss, time 4001ms
rtt min/avg/max/mdev = 186.425/189.429/195.008/3.509 ms
root@0749a2e74a68:/# time wget -o /dev/null https://www.example.com
real    0m1.993s
user    0m0.011s
sys     0m0.011s
```

成功了！ping报告的延迟增加了100毫秒，而对 `wget` 的计时展示了略大于5倍的降速，与预期相当（带宽上限、额外的延迟及分组丢失同时产生了影响）。但是分组丢失有点儿奇怪——它似乎比预期大了3倍。需要注意的很重要的一点是，ping只发送了少量的分组，而分组丢失不是精确的“五分之一”计数器——如果将ping次数提高到50，将会发现分组丢失结果与预期要接近得多。

注意，上面应用的规则对通过该网络接口的 **所有** 网络连接都有效，包括与宿主机及其他容器的连接。

现在告诉Comcast删除这些规则。Comcast还无法对单个状况进行添加或删除，因此修改某个网络接口上的任何东西都意味着要完全删除或重新添加该网络接口上的规则。如果要恢复正常的容器网络操作，也必须删除这些规则。不过，在退出容器时无须考虑这些规则的删除——它们会在Docker删除虚拟网络接口时被自动删除：

```c
$ comcast -cont c1 -stop
Found interface veth62cc8bf for container 'c1'
[...]
Packet rules stopped...
Run 'sudo tc -s qdisc' to double check
Run 'comcast' to start
```

如果读者有兴趣动手实践，可以深入挖掘Linux的流量控制工具，以 `-dry-run` 使用Comcast来生成要使用的命令示例集合。其可能性的完整性论述已经超出本技巧的范围，不过请记住，只要能将其放到容器内并连接到网络，就能使用它来做试验。

#### 讨论

只要做些实现上的努力，没理由不能将Comcast用于手动控制容器带宽之外。举个例子，假设你正在使用类似btsync（见技巧35）的工具，不过想限制其可用宽带以免它把连接占满——下载Comcast，将它放置在容器里，然后使用 `ENTRYPOINT` （见技巧49）作为容器启动的一部分来设置带宽限制。

要这么做，你需要安装Comcast的依赖项（针对alpine镜像，我们的Dockerfile列出了这些依赖项：https://github.com/docker-in-practice/docker-comcast/blob/master/Dockerfile），并至少赋予容器网络管理的能力——你可以在技巧93中获取有关能力的更多信息。

