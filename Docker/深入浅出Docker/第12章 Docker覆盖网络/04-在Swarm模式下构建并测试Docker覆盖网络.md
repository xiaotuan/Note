### 12.2.1　在Swarm模式下构建并测试Docker覆盖网络

要完成下面的示例，需要两台Docker主机，并通过一个路由器上两个独立的二层网络连接在一起。如图12.1所示，注意节点位于不同网络之上。

![76.png](./images/76.png)
<center class="my_markdown"><b class="my_markdown">图12.1　连接网络</b></center>

读者可以选择Linux容器主机或者Windows容器主机。Linux内核版本不能低于4.4（高版本更好），Windows需要Windows Server 2016版本，并且应安装最新的补丁。

##### 1．构建Swarm

首先需要将两台主机配置为包含两个节点的Swarm集群。接下来会在node1节点上运行 `docker swarm init` 命令使其成为管理节点，然后在node2节点上运行 `docker swarm join` 命令来使其成为工作节点。

注：

> 如果读者需要在自己的环境中继续下面的示例，则需要先将环境中的IP地址、容器ID和Token等替换为正确的值。

在 **node1** 节点上运行下面的命令。

```rust
$ docker swarm init \
  --advertise-addr=172.31.1.5 \
  --listen-addr=172.31.1.5:2377
Swarm initialized: current node (1ex3...o3px) is now a manager.
```

在 **node2** 上运行下面的命令。如果需要在Windows环境下生效，则需要修改Windows防火墙规则，打开 `2377/tcp` 、 `7946/tcp` 以及 `7946/udp` 等几个端口。

```rust
$ docker swarm join \
  --token SWMTKN-1-0hz2ec...2vye \
  172.31.1.5:2377
This node joined a swarm as a worker.
```

现在读者已经拥有了包含管理节点 **node1** 和工作节点 **node2** 两个节点的Swarm集群了。

##### 2．创建新的覆盖网络

现在创建一个名为 `uber-net` 的覆盖网络。

在 **node1** （管理节点）节点上运行下面的命令。若要这些命令在Windows上也能运行，需要在Windows Docker节点上添加 `4789/udp` 规则。

```rust
$ docker network create -d overlay uber-net
c740ydi1lm89khn5kd52skrd9
```

刚刚创建了一个崭新的覆盖网络，能连接Swarm集群内的所有主机，并且该网络还包括一个TLS加密的控制层！如果还想对数据层加密的话，只需在命令中增加 `-o encrypted` 参数。

可以通过docker network ls命令列出每个节点上的全部网络。

```rust
$ docker network ls
NETWORK ID        NAME                  DRIVER     SCOPE
ddac4ff813b7      bridge            bridge     local
389a7e7e8607      docker_gwbridge   bridge     local
a09f7e6b2ac6      host              host       local
ehw16ycy980s      ingress           overlay    swarm
2b26c11d3469      none              null       local
c740ydi1lm89      uber-net          overlay    swarm
```

在Windows Docker主机上输出内容如下。

```rust
NETWORK ID        NAME              DRIVER     SCOPE
8iltzv6sbtgc      ingress           overlay    swarm
6545b2a61b6f      nat               nat        local
96d0d737c2ee      none              null       local
nil5ouh44qco      uber-net          overlay    swarm
```

列表的最下方就是刚刚创建的网络uber-net。其他的网络是在安装Docker以及初始化Swarm集群的时候创建的。

如果在 **node2** 节点上运行 `docker network ls` 命令，就会发现无法看到 **uber-net** 网络。这是因为只有当运行中的容器连接到覆盖网络的时候，该网络才变为可用状态。这种延迟生效策略通过减少网络梳理，提升了网络的扩展性。

##### 3．将服务连接到覆盖网络

现在覆盖网络已经就绪，接下来新建一个Docker服务并连接到该网络。Docker服务会包含两个副本（容器），一个运行在 **node1** 节点上，一个运行在 **node2** 节点上。这样会自动将 **node2** 节点接入 **uber-net** 网络。

在node1节点上运行下面的命令。

Linux示例如下。

```rust
$ docker service create --name test \
  --network uber-net \
  --replicas 2 \
  ubuntu sleep infinity
```

Windows示例如下。

```rust
> docker service create --name test `
  --network uber-net `
  --replicas 2 `
  microsoft\powershell:nanoserver Start-Sleep 3600
```

注：

> Windows示例使用反引号的方式将单条命令分为多行，以提高命令的可读性。PowerShell中使用反引号来转义换行字符。

该命令创建了名为 **test** 的新服务，连接到了 **uber-net** 这个覆盖网络，并且还基于指定的镜像创建了两个副本（容器）。在两个示例中，均在容器中采用sleep命令来保持容器运行，并在休眠结束后退出该容器。

由于运行了两个副本（容器），而Swarm包含两个节点，因此每个节点上都会运行一个副本。

可以通过 `docker service ps` 命令来确认上面的操作。

```rust
$ docker service ps test
ID          NAME    IMAGE    NODE   DESIRED STATE  CURRENT STATE
77q...rkx   test.1  ubuntu   node1  Running        Running
97v...pa5   test.2  ubuntu   node2  Running        Running
```

当Swarm在覆盖网络之上启动容器时，会自动将容器运行所在节点加入到网络当中。这意味着此时在 **node2** 节点上就可以看到 **uber-net** 网络了。

恭喜！目前已经成功在两个由物理网络连接的节点上创建了新的覆盖网络。同时，还将两个容器连接到了该网络当中。多么简单！

##### 4．测试覆盖网络

现在使用ping命令来测试覆盖网络。

如图12.2所示，在两个独立的网络中分别有一台Docker主机，并且两者都接入了同一个覆盖网络。目前在每个节点上都有一个容器接入了覆盖网络。测试一下两个容器之间是否可以ping通。

![77.png](./images/77.png)
<center class="my_markdown"><b class="my_markdown">图12.2　节点上的容器接入覆盖网络</b></center>

为了执行该测试，需要知道每个容器的IP地址（为了测试，暂时忽略相同覆盖网络上的容器可以通过名称来互相ping通的事实）。

运行 `docker network inspect` 查看被分配给覆盖网络的 **Subnet** 。

```rust
$ docker network inspect uber-net
[
    {
        "Name": "uber-net",
        "Id": "c740ydi1lm89khn5kd52skrd9",
        "Scope": "swarm",
        "Driver": "overlay",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "10.0.0.0/24",
                    "Gateway": "10.0.0.1"
                }
<Snip>
```

由以上输出可见， **uber-net** 的子网是 `10.0.0.0/24` 。注意，这与两个节点的任意底层物理网络IP均不相符（ `172.31.1.0/24` 和 `192.168.1.0/24` ）。

在 **node1** 和 **node2** 节点上运行下面两条命令。这两条命令可以获取到容器ID和IP地址。在第二条命令中一定要使用读者自己的环境中的容器ID。

```rust
$ docker container ls
CONTAINER  ID  IMAGE          COMMAND           CREATED       STATUS
396c8b142a85   ubuntu:latest  "sleep infinity"  2 hours ago   Up 2 hrs
$ docker container inspect \
  --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
  396c8b142a85
10.0.0.3
```

读者需要在两台节点上分别运行上述命令，获取两个容器的ID和IP地址。

图12.3展示了配置现状。在读者的环境中，子网和IP地址信息可能不同。

![78.png](./images/78.png)
<center class="my_markdown"><b class="my_markdown">图12.3　配置现状</b></center>

由图可知，一个二层覆盖网络横跨两台主机，并且每个容器在覆盖网络中都有自己的IP地址。这意味着 **node1** 节点上的容器可以通过 **node2** 节点上容器的IP地址 `10.0.0.4` 来ping通，该IP地址属于覆盖网络。尽管两个节点分属于不同的二层网络，还是可以直接ping通。接下来验证这一点。

登录到 **node1** 的容器，并ping另一个的容器。

在Linux Ubuntu容器中执行该操作的话，需要安装 `ping` 工具包。如果读者使用Windows PowerShell示例， `ping` 工具已默认安装。

注意，读者自己本地环境中的容器ID会不同。

Linux示例如下。

```rust
$ docker container exec -it 396c8b142a85 bash
root@396c8b142a85:/# apt-get update
root@396c8b142a85:/# apt-get install iputils-ping
Reading package lists... Done
Building dependency tree
Reading state information... Done
Setting up iputils-ping (3:20121221-5ubuntu2) ...
Processing triggers for libc-bin (2.23-0ubuntu3) ...
root@396c8b142a85:/# ping 10.0.0.4
PING 10.0.0.4 (10.0.0.4) 56(84) bytes of data.
64 bytes from 10.0.0.4: icmp_seq=1 ttl=64 time=1.06 ms
64 bytes from 10.0.0.4: icmp_seq=2 ttl=64 time=1.07 ms
64 bytes from 10.0.0.4: icmp_seq=3 ttl=64 time=1.03 ms
64 bytes from 10.0.0.4: icmp_seq=4 ttl=64 time=1.26 ms
^C
root@396c8b142a85:/#
```

Windows示例如下。

```rust
> docker container exec -it 1a4f29e5a4b6 pwsh.exe
Windows PowerShell
Copyright (C) 2016 Microsoft Corporation. All rights reserved.
PS C:\> ping 10.0.0.4
Pinging 10.0.0.4 with 32 bytes of data:
Reply from 10.0.0.4: bytes=32 time=1ms TTL=128
Reply from 10.0.0.4: bytes=32 time<1ms TTL=128
Reply from 10.0.0.4: bytes=32 time=2ms TTL=128
Reply from 10.0.0.4: bytes=32 time=2ms TTL=12
PS C:\>
```

恭喜。 **node1** 上的容器可以通过覆盖网络ping通 **node2** 之上的容器了。

读者还可以在容器内部跟踪ping命令的路由信息。路由信息只有一跳，证明容器间通信确实通过覆盖网络直连——无须关心底层网络，这太省心了。

注：

> 如果希望Linux示例中的traceroute可执行，读者需要安装traceroute包。

Linux示例如下。

```rust
$ root@396c8b142a85:/# traceroute 10.0.0.4
traceroute to 10.0.0.4 (10.0.0.4), 30 hops max, 60 byte packets
 1 test-svc.2.97v...a5.uber-net (10.0.0.4) 1.110ms 1.034ms 1.073ms
```

Windows示例如下。

```rust
PS C:\> tracert 10.0.0.3
Tracing route to test.2.ttcpiv3p...7o4.uber-net [10.0.0.4]
over a maximum of 30 hops:
  1 <1 ms <1 ms <1 ms test.2.ttcpiv3p...7o4.uber-net [10.0.0.4]
Trace complete.
```

到目前为止，读者已经通过单条命令创建了覆盖网络，并向该网络中接入了容器。这些容器分布在两个不同的主机上，两台主机分属于不同的二层网络。在找出两台容器的IP之后，验证了容器可以通过覆盖网络完成直连。

