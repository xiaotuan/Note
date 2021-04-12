### 10.2.2　搭建安全Swarm集群

本节会搭建一套安全Swarm集群，其中包含3个管理节点和3个工作节点。读者也可以自行调整管理节点和工作节点的数量、名称和IP，本书示例将使用图10.2所示的值。

![48.png](./images/48.png)
<center class="my_markdown"><b class="my_markdown">图10.2　Swarm集群</b></center>

每个节点都需要安装Docker，并且能够与Swarm的其他节点通信。如果配置有域名解析就更好了——这样在命令的输出中更容易识别出节点，也更有利于排除故障。

在网络方面，需要在路由器和防火墙中开放如下端口。

+ `2377/tcp` ：用于客户端与Swarm进行安全通信。
+ `7946/tcp` 与 `7946/udp` ：用于控制面gossip分发。
+ `4789/udp` ：用于基于VXLAN的覆盖网络。

如果满足以上前提，就可以着手开始搭建Swarm集群了。

搭建Swarm的过程有时也被称为初始化Swarm，大体流程包括初始化第一个管理节点>加入额外的管理节点>加入工作节点>完成。

##### 1．初始化一个全新的Swarm

不包含在任何Swarm中的Docker节点，称为运行于单引擎（Single-Engine）模式。一旦被加入Swarm集群，则切换为Swarm模式，如图10.3所示。

![49.png](./images/49.png)
<center class="my_markdown"><b class="my_markdown">图10.3　Docker节点加入Swarm集群</b></center>

在单引擎模式下的Docker主机上运行 `docker swarm init` 会将其切换到Swarm模式，并创建一个新的Swarm，将自身设置为Swarm的第一个管理节点。

更多的节点可以作为管理节点或工作节点加入进来。这一操作也会将新加入的节点切换为 Swarm模式。

以下的步骤会将 **mgr1** 切换为Swarm模式，并初始化一个新的Swarm。接下来将 **wrk1** 、 **wrk2** 和 **wrk3** 作为工作节点接入——自动将它们切换为Swarm模式。然后将 **mgr2** 和 **mgr3** 作为额外的管理节点接入，并同样切换为Swarm模式。最终有6个节点切换到Swarm模式，并运行于同一个Swarm中。

本示例会使用图10.2中所示的各节点的IP地址和DNS名称。读者的可以与其不同。

（1）登录到 **mgr1** 并初始化一个新的Swarm（如果在Windows的PowerShell终端执行如下命令的话，不要忘了将反斜杠替换为反引号）。

```rust
$ docker swarm init \
  --advertise-addr 10.0.0.1:2377 \
  --listen-addr 10.0.0.1:2377
Swarm initialized: current node (d21lyz...c79qzkx) is now a manager.
```

将这条命令拆开分析如下。

+ `docker swarm init` 会通知Docker来初始化一个新的Swarm，并将自身设置为第一个管理节点。同时也会使该节点开启Swarm模式。
+ `--advertise-addr` 指定其他节点用来连接到当前管理节点的IP和端口。这一属性是可选的，当节点上有多个IP时，可以用于指定使用哪个IP。此外，还可以用于指定一个节点上没有的IP，比如一个负载均衡的IP。
+ `--listen-addr` 指定用于承载Swarm流量的IP和端口。其设置通常与 `--advertise-addr` 相匹配，但是当节点上有多个IP的时候，可用于指定具体某个IP。并且，如果 `--advertise-addr` 设置了一个远程IP地址（如负载均衡的IP地址），该属性也是需要设置的。建议执行命令时总是使用这两个属性来指定具体IP和端口。

Swarm模式下的操作默认运行于2337端口。虽然它是可配置的，但 `2377/tcp` 是用于客户端与Swarm进行安全（HTTPS）通信的约定俗成的端口配置。

（2）列出Swarm中的节点。

```rust
$ docker node ls
ID            HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
d21...qzkx *  mgr1      Ready   Active        Leader
```

注意到 **mgr1** 是Swarm中唯一的节点，并且作为Leader列出，稍后再探讨这一点。

（3）在mgr1上执行docker swarm join-token命令来获取添加新的工作节点和管理节点到Swarm的命令和Token。

```rust
$ docker swarm join-token worker
To add a manager to this swarm, run the following command:
   docker swarm join \
   --token SWMTKN-1-0uahebax...c87tu8dx2c \
   10.0.0.1:2377
$ docker swarm join-token manager
To add a manager to this swarm, run the following command:
   docker swarm join \
   --token SWMTKN-1-0uahebax...ue4hv6ps3p \
   10.0.0.1:2377
```

请注意，工作节点和管理节点的接入命令中使用的接入Token（ `SWMTKN...` ）是不同的。因此，一个节点是作为工作节点还是管理节点接入，完全依赖于使用了哪个Token。接入Token应该被妥善保管，因为这是将一个节点加入Swarm的唯一所需！

（4）登录到wrk1，并使用包含工作节点接入Token的 `docker swarm join` 命令将其接入Swarm。

```rust
$ docker swarm join \
    --token SWMTKN-1-0uahebax...c87tu8dx2c \
    10.0.0.1:2377 \
    --advertise-addr 10.0.0.4:2377 \
    --listen-addr 10.0.0.4:2377
This node joined a swarm as a worker.
```

`--advertise-addr` 与 `--listen-addr` 属性是可选的。在网络配置方面，请尽量明确指定相关参数，这是一种好的实践。

（5）在 **wrk2** 和 **wrk3** 上重复上一步骤来将这两个节点作为工作节点加入Swarm。确保使用 `--advertise-addr` 与 `--listen-addr` 属性来指定各自的IP地址。

（6）登录到 **mgr2** ，然后使用含有管理节点接入Token的 `docker swarm join` 命令，将该节点作为工作节点接入Swarm。

```rust
$ docker swarm join \
    --token SWMTKN-1-0uahebax...ue4hv6ps3p \
    10.0.0.1:2377 \
    --advertise-addr 10.0.0.2:2377 \
    --listen-addr 10.0.0.1:2377
This node joined a swarm as a manager.
```

（7）在 **mgr3** 上重复以上步骤，记得在 `--advertise-addr` 与 `--listen-addr` 属性中指定 **mgr3** 的IP地址。

（8）在任意一个管理节点上执行 `docker node ls` 命令来列出Swarm节点。

```rust
$ docker node ls
ID                HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
0g4rl...babl8 *   mgr2      Ready   Active        Reachable
2xlti...l0nyp     mgr3      Ready   Active        Reachable
8yv0b...wmr67     wrk1      Ready   Active
9mzwf...e4m4n     wrk3      Ready   Active
d21ly...9qzkx     mgr1      Ready   Active        Leader
e62gf...l5wt6     wrk2      Ready   Active
```

恭喜！想必读者也已经创建了6个节点的Swarm，其中包含3个管理节点和3个工作节点。在这个过程中，每个节点的Docker引擎都被切换到 **Swarm模式** 下。贴心的是， **Swarm** 已经自动启用了TLS以策安全。

观察 `MANAGER STATUS` 一列会发现，3个节点分别显示为“ `Reachable` ”或“ `Leader` ”。关于主节点稍后很快会介绍到。 `MANAGER STATUS` 一列无任何显示的节点是工作节点。注意， **mgr2** 的ID列还显示了一个星号（*），这个星号会告知用户执行 `docker node ls` 命令所在的节点。本例中，命令是在 **mgr2** 节点执行的。

注：

> 每次将节点加入Swarm都指定 `--advertise-addr` 与 `--listen-addr` 属性是痛苦的。然而，一旦Swarm中的网络配置出现问题将会更加痛苦。况且，手动将节点加入Swarm也不是一种日常操作，所以在执行该命令时额外指定这两个属性是值得的。不过选择权在读者手中。对于实验环境，或节点中只有一个IP的情况来说，也许并不需要指定它们。

现在已经有一个运行中的Swarm了，下面看一下如何进行高可用（HA）管理。

##### 2．Swarm管理器高可用性（HA）

至此在Swarm中已经加入了3个管理节点。为什么添加3个，以及它们如何协同工作？ 本节将就此以及更多问题展开介绍。

Swarm的管理节点内置有对HA的支持。这意味着，即使一个或多个节点发生故障，剩余管理节点也会继续保证Swarm的运转。

从技术上来说，Swarm实现了一种主从方式的多管理节点的HA。这意味着，即使你可能——并且应该——有多个管理节点，也总是仅有一个节点处于活动状态。通常处于活动状态的管理节点被称为“主节点”（leader），而主节点也是唯一一个会对Swarm发送控制命令的节点。也就是说，只有主节点才会变更配置，或发送任务到工作节点。如果一个备用（非活动）管理节点接收到了Swarm命令，则它会将其转发给主节点。

这一过程如图10.4所示。步骤①指命令从一个远程的Docker客户端发送给一个管理节点；步骤②指非主节点将命令转发给主节点；步骤③指主节点对Swarm执行命令。

![50.png](./images/50.png)
<center class="my_markdown"><b class="my_markdown">图10.4　10.2.3 Swarm的高可用（HA）管理</b></center>

仔细观察图10.4的读者会发现，管理节点或者是Leader或者是Follower。这是Raft的术语，因为Swarm使用了Raft共识算法的一种具体实现来支持管理节点的HA。关于HA，以下是两条最佳实践原则。

+ 部署奇数个管理节点。
+ 不要部署太多管理节点（建议3个或5个）。

部署奇数个管理节点有利于减少脑裂（Split-Brain）情况的出现机会。假如有4个管理节点，当网络发生分区时，可能会在每个分区有两个管理节点。这种情况被称为脑裂——每个分区都知道曾经有4个节点，但是当前网络中仅有两个节点。糟糕的是，每个分区都无法知道其余两个节点是否运行，也无从得知本分区是否掌握大多数（Quorum）。虽然在脑裂情况下集群依然在运行，但是已经无法变更配置，或增加和管理应用负载了。

不过，如果部署有3个或5个管理节点，并且也发生了网络分区，就不会出现每个分区拥有同样数量的管理节点的情况。这意味着掌握多数管理节点的分区能够继续对集群进行管理。图10.5中右侧的例子，阐释了这种情况，左侧的分区知道自己掌握了多数的管理节点。

对于所有的共识算法来说，更多的参与节点就意味着需要花费更多的时间来达成共识。这就像决定去哪吃饭——只有3个人的时候总是比有33个人的时候能更快确定。考虑到这一点，最佳的实践原则是部署3个或5个节点用于HA。7个节点可以工作，但是通常认为3个或5个是更优的选择。当然绝对不要多于7个，因为需要花费更长的时间来达成共识。

![51.png](./images/51.png)
<center class="my_markdown"><b class="my_markdown">图10.5　多数管理节点的分区继续对集群进行管理</b></center>

关于管理节点的HA再补充一点。显然将管理节点分布到不同的可用域（Availability Zone）中是一种不错的实践方式，但是一定要确保它们之间的网络连接是可靠的，否则由于底层网络分区导致的问题将是令人痛苦的！这意味着，在本书撰写时，将生产环境的应用和基础设置部署在多个不同的公有云（例如AWS和Azure）上的想法仍然是天方夜谭。请一定要确保管理节点之间是有高速可靠的网络连接的!

##### 3．内置的Swarm安全机制

Swarm集群内置有繁多的安全机制，并提供了开箱即用的合理的默认配置——如CA设置、接入Token、公用TLS、加密集群存储、加密网络、加密节点ID等。更多细节请阅读第15章。

##### 4．锁定Swarm

尽管内置有如此多的原生安全机制，重启一个旧的管理节点或进行备份恢复仍有可能对集群造成影响。一个旧的管理节点重新接入Swarm会自动解密并获得Raft数据库中长时间序列的访问权，这会带来安全隐患。进行备份恢复可能会抹掉最新的Swarm配置。

为了规避以上问题，Docker提供了自动锁机制来锁定Swarm，这会强制要求重启的管理节点在提供一个集群解锁码之后才有权从新接入集群。

通过在执行 `docker swarm init` 命令来创建一个新的Swarm集群时传入 `--autolock` 参数可以直接启用锁。然而，前面已经搭建了一个Swarm集群，这时也可以使用 `docker swarm update` 命令来启用锁。

在某个Swarm管理节点上运行如下命令。

```rust
$ docker swarm update --autolock=true
Swarm updated.
To unlock a swarm manager after it restarts, run the
`docker swarm unlock`command and provide the following key:
    SWMKEY-1-5+ICW2kRxPxZrVyBDWzBkzZdSd0Yc7Cl2o4Uuf9NPU4
Please remember to store this key in a password manager, since without
it you will not be able to restart the manager.
```

请确保将解锁码妥善保管在安全的地方！

重启某一个管理节点，以便观察其是否能够自动重新接入集群。读者可以在以下命令前添加sudo执行。

```rust
$ service docker restart
```

尝试列出Swarm中的节点。

```rust
$ docker node ls
Error response from daemon: Swarm is encrypted and needs to be unlocked
before it can be used.
```

尽管Docker服务已经重启，该管理节点仍然未被允许重新接入集群。为了进一步验证，读者可以到其他管理节点执行  `docker node ls` 命令，会发现重启的管理节点会显示 `down` 以及 `unreachable` 。

执行 `docker swarm unlock` 命令来为重启的管理节点解锁Swarm。该命令需要在重启的节点上执行，同时需要提供解锁码。

```rust
$ docker swarm unlock
Please enter unlock key: <enter your key>
```

该节点将被允许重新接入Swarm，并且再次执行 `docker node ls` 命令会显示 `ready` 和 `reachable` 。

至此，Swarm集群已经搭建起来，并且对主节点和管理节点HA有了一定了解，下面开始介绍服务。

