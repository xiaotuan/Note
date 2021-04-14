### 技巧79　使用Blockade模拟有问题的网络

对很多应用程序而言，Comcast是一个优秀的工具，不过有一个重要的使用场景它无法解决——如何才能将网络状况应用到全体容器中？手工对几十个容器运行Comcast将是非常痛苦的，上百个更是无法想象！这个问题对容器而言尤为相关，因为它们的启动代价非常低——如果在单台机器上运行上百台虚拟机而不是容器来模拟大型网络，将会遇到更大的问题，如内存不足！

在使用多台机器模拟网络时，有一种特殊类型的网络故障会在这种规模下变得有趣起来——网络分区。当一组网络化的机器被分成两个或更多部分时，这种情况就会出现，同一部分里的所有机器可以相互通信，但不同部分则无法通信。研究表明这种情况的发生比想象中要多得多，尤其是在消费级的云服务上！

遵循经典的Docker微服务线路可大大缓解此类问题，而要理解服务如何对其进行处理，拥有用于做实验的工具就至关重要了。

#### 问题

想要对大量容器进行网络状况编排设置，包括创建网络分区。

#### 解决方案

使用Blockade。Blockade是出自戴尔公司一个团队的开源软件，为“测试网络故障及分区”而生。

Blockade通过读取当前目录中的配置文件（blockade.yml）来工作，该配置文件定义了容器启动的方式以及需要对其应用哪些状况。为了应用这些状况，它可能会下载其他安装了必要工具的镜像。完整的配置细节可从Blockade文档中获得，因此这里只对核心部分进行说明。

首先需要创建一个blockade.yml，如代码清单10-11所示。

代码清单10-11　blockade.yml文件

```c
containers:
  server:
    container_name: server
    image: ubuntu:14.04.2
    command: /bin/sleep infinity
  client1:
    image: ubuntu:14.04.2
    command: sh -c "sleep 5 && ping server"
  client2:
    image: ubuntu:14.04.2
    command: sh -c "sleep 5 && ping server"
network:
  flaky: 50%
  slow: 100ms
  driver: udn
```

上述配置中设置的容器代表由两个客户端连接的一个服务器。在实践中，可能是一个数据库服务器及其客户端应用程序，并且对要建模的组件数量没有任何限制。只要它能在一个compose.yml文件（见技巧76）中表示，就可以在Blockade中对其进行建模。

在此，我们将网络驱动指定为udn——这可以让Blockade模仿技巧77中Docker Compose的行为，创建一个新的虚拟网络以便容器可以通过容器名称相互ping通。为此，我们必须显式地为服务器指定 `container_name` ，因为Blockade默认会自己生成。 `sleep 5` 这条命令是为了保证在客户端启动之前服务器处于运行状态——如果你倾向于在Blockade里使用链接，后者将确保容器以正确顺序启动。这里暂时不用考虑 `network` 小节，稍后会对其进行说明。

与往常一样，使用Blockade的第一步是拉取镜像：

```c
$ IMG=dockerinpractice/blockade
$ docker pull $IMG
latest: Pulling from dockerinpractice/blockade
[...]
Status: Downloaded newer image for dockerinpractice/blockade:latest
$ alias blockade="docker run --rm -v \$PWD:/blockade \
-v /var/run/docker.sock:/var/run/docker.sock $IMG"
```

你可能注意到，相比技巧78，我们遗漏了一些 `docker run` 参数（如 `--privileged` 和 `--pid=host` ）。Blockade使用其他容器来执行网络操控，因此它本身不需要权限。同样需要注意的是将当前目录挂载到容器中的参数，以便Blockade能访问blockade.yml并将状态存储在一个隐藏目录中。



**注意**

如果是运行在网络文件系统之上，第一次启动Blockade可能会遇到奇怪的权限问题，这可能是因为Docker正在尝试以root身份创建该隐藏的状态目录，而网络文件系统不予配合。解决方案是使用本地磁盘。



最后到了关键时刻——运行Blockade。要确保目前位于保存blockade.yml的目录中：

```c
$ blockade up
NODE     CONTAINER ID   STATUS  IP          NETWORK   PARTITION
client1  613b5b1cdb7d   UP      172.17.0.4  NORMAL
client2  2aeb2ed0dd45   UP      172.17.0.5  NORMAL
server   53a7fa4ce884   UP      172.17.0.3  NORMAL
```



**注意**

在启动时，Blockade有时可能会报“/proc”中文件不存在的晦涩错误。首先检查容器是否在启动时马上退出，阻止了Blockade检查其网络状态。此外，请尽量不要使用Blockade的 `-c` 选项来指定自定义配置文件目录——容器内只有当前目录的子目录可用。



所有配置文件中定义的容器已经启动，并显示了已启动容器的一些有用信息。现在来应用一些基本的网络状况。在一个新的终端中持续打印 `client1` 的日志（使用 `docker logs -f 613b5b1cdb7d` ），以便在做修改时可以查看所发生的情况：

```c
$ blockade flaky --all　　⇽---　让所有容器的网络变得不稳定（分组丢失）
$ sleep 5　　⇽---　延后下一条命令，让前一条命令有时间生效并输出一些日志
$ blockade slow client1　　⇽---　让容器client1的网络变慢（为分组增加了延迟）
$ blockade status　　⇽---　检查容器所处的状态
NODE     CONTAINER ID   STATUS  IP          NETWORK   PARTITION
client1  613b5b1cdb7d   UP      172.17.0.4  SLOW
client2  2aeb2ed0dd45   UP      172.17.0.5  FLAKY
server   53a7fa4ce884   UP      172.17.0.3  FLAKY
$ blockade fast --all　　⇽---　将所有容器恢复为正常操作
```

`flaky` 和 `slow` 命令使用了之前配置文件（见代码清单10-10）中 `network` 一节定义的值—— 限定值无法在命令行中指定。如果有需要，可以在容器运行时编辑blockade.yml，然后有选择性地将新的限定值应用到容器上。需要注意的是，一个容器只能处在慢速网络 **或** 不稳定网络中，不能二者皆有。撇开这些限制，对成百上千个容器执行这一命令的便捷性还是相当可观的。

如果回头查看 `client1` 的日志，可以看到不同命令生效的时间：

```c
64 bytes from 172.17.0.3: icmp_seq=638 ttl=64 time=0.054 ms　　⇽---　 icmp_seq是连续的（没有分组丢失），time也比较低（延迟小）
64 bytes from 172.17.0.3: icmp_seq=639 ttl=64 time=0.098 ms
64 bytes from 172.17.0.3: icmp_seq=640 ttl=64 time=0.112 ms
64 bytes from 172.17.0.3: icmp_seq=645 ttl=64 time=0.112 ms　　⇽---　 icmp_seq出现了一个大跳跃——flaky命令生效了
64 bytes from 172.17.0.3: icmp_seq=652 ttl=64 time=0.113 ms
64 bytes from 172.17.0.3: icmp_seq=654 ttl=64 time=0.115 ms
64 bytes from 172.17.0.3: icmp_seq=660 ttl=64 time=100 ms　　⇽---　 time出现了一个大跳跃——slow命令生效了
64 bytes from 172.17.0.3: icmp_seq=661 ttl=64 time=100 ms
64 bytes from 172.17.0.3: icmp_seq=662 ttl=64 time=100 ms
64 bytes from 172.17.0.3: icmp_seq=663 ttl=64 time=100 ms
```

虽然这很有用，不过在Comcast之上使用一些（可能是比较费力的）脚本也能实现，那么来看看Blockade的杀手锏功能——网络分区：

```c
$ blockade partition server client1,client2
$ blockade status
NODE     CONTAINER ID   STATUS  IP          NETWORK  PARTITION
client1  613b5b1cdb7d   UP      172.17.0.4  NORMAL   2
client2  2aeb2ed0dd45   UP      172.17.0.5  NORMAL   2
server   53a7fa4ce884   UP      172.17.0.3  NORMAL   1
```

这会将3个节点划分成2个区域——服务器在其中一个区域，而客户端在另一个区域，它们之间无法进行通信。可以看到 `client1` 的日志停止了，因为所有的ping分组都丢失了！不过，两个客户端依然可以相互通信，这一点可以通过在二者之间发送一些ping分组来验证：

```c
$ docker exec 613b5b1cdb7d ping -qc 3 172.17.0.5
PING 172.17.0.5 (172.17.0.5) 56(84) bytes of data.
--- 172.17.0.5 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2030ms
rtt min/avg/max/mdev = 0.109/0.124/0.150/0.018 ms
```

没有分组丢失，延迟也很低……看起来是个不错的连接。分区及其他网络状况是独立操作的，因此可以在应用分区的同时试验分组丢失。可以定义的分区数量没有限制，因此可以尽情地对复杂场景进行试验。

#### 讨论

如果需要获得比Blockade和Comcast单独提供的能力更强大的能力，可以将Blockade和Comcast组合起来。Blockade擅长创建分区以及完成启动容器的繁杂事务，添加Comcast则能实现每一个容器网络连接的细粒度控制！

Blockade完整的帮助信息同样值得一看——它提供了一些你可能发现有用的东西，比如“混乱”功能可以给随机容器施加各种状况，在命令行添加 `--random` 参数可以（举个例子）查看在容器被随机杀掉时应用程序如何反应。如果你听说过Netflix的Chaos Monkey，这是在较小范围内模拟它的一个方法。

