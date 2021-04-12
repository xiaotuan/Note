### 15.2.2　Docker平台安全技术

本节会介绍由Docker平台提供的主要的安全技术。

##### 1．Swarm模式

Swarm模式是Docker未来的趋势。Swarm模式支持用户集群化管理多个Docker主机，同时还能通过声明式的方式部署应用。每个Swarm都由管理者和工作者节点构成，节点可以是Linux或者Windows。管理者节点构成了集群中的控制层，并负责集群配置以及工作负载的分配。工作者节点就是运行应用代码的容器。

正如所预期的，Swarm模式包括很多开箱即用的安全特性，同时还设置了合理的默认值。这些安全特性包括以下几点。

+ 加密节点ID。
+ 基于TLS的认证机制。
+ 安全准入令牌。
+ 支持周期性证书自动更新的CA配置。
+ 加密集群存储（配置DB）。
+ 加密网络。

接下来将详细介绍如何构建安全的Swarm，以及如何进行安全相关的配置。

为了完成下面的内容，读者需要至少3个Docker主机，每个都运行1.13或者更高版本的Docker。示例中3个Docker主机分别叫作“mgr1”“mgr2”“wrk1”。每台主机上都安装Ubuntu 16.04，其上运行了Docker 18.01.0-ce。同时还有一个网络负责联通3台主机，并且主机之间可以通过名称互相ping通。安装完成后如图15.6所示。

![96.png](./images/96.png)
<center class="my_markdown"><b class="my_markdown">图15.6 3个Docker主机</b></center>

（1）配置安全的Swarm集群

读者可以在其Swarm集群管理者节点上运行下面的命令。在本例中，命令运行于“mgr1”节点之上。

```rust
$ docker swarm init
Swarm initialized: current node (7xam...662z) is now a manager.
To add a worker to this swarm, run the following command:
    docker swarm join --token \
     SWMTKN-1-1dmtwu...r17stb-ehp8g...hw738q 172.31.5.251:2377
To add a manager to this swarm, run 'docker swarm join-token manager'
and follow the instructions.
```

上面的命令就是配置安全Swarm集群所要做的全部工作！

“mgr1”被配置为Swarm集群中的第一个管理节点，也是根CA节点。Swarm集群已经被赋予了加密Swarm ID，同时“mgr1”节点为自己发布了一个客户端认证信息，标明自己是Swarm集群管理者。证书的更新周期默认设置为90天，集群配置数据库也已经配置完成并且处于加密状态。安全令牌也已经成功创建，允许新的管理者和工作者节点加入到Swarm集群中。以上全部内容都只需要 **一条命令** ！

实验环境如图15.7所示。

![97.png](./images/97.png)
<center class="my_markdown"><b class="my_markdown">图15.7　实验环境</b></center>

现在将“mgr2”节点加入到集群中，作为额外的管理者节点。

将新的管理者节点加入到Swarm需要两步。第一步，需要提取加入管理者到集群中所需的令牌；第二步，在“mgr2”节点上执行 `docker swarm join` 命令。只要将管理者准入令牌作为 `docker swarm join` 命令的一部分，“mgr2”就作为管理者节点加入Swarm。

在“mgr1”上运行下面的命令获取管理者准入令牌。

```rust
$ docker swarm join-token manager
To add a manager to this swarm, run the following command:
    docker swarm join --token \
    SWMTKN-1-1dmtwu...r17stb-2axi5...8p7glz \
    172.31.5.251:2377
```

命令输出内容给出了管理者加入Swarm所需运行的准确命令。准入令牌和IP地址在读者自己的实验环境中是不一样的。

复制该命令并在“mgr2”节点上运行。

```rust
$ docker swarm join --token SWMTKN-1-1dmtwu...r17stb-2axi5...8p7glz \
> 172.31.5.251:2377
This node joined a swarm as a manager.
```

“mgr2”现在已经作为另一个管理者加入Swarm。

注：

> join命令的格式是 `docker swarm join --token <manager-join-token>`   `<ip-of-existing-manager>:<swarm-port>` 。

可以通过在任意管理者节点上运行 `docker node ls` 命令来确认上述操作。

```rust
$ docker node ls
ID               HOSTNAME  STATUS   AVAILABILITY  MANAGER STATUS
7xamk...ge662z   mgr1      Ready    Active        Leader
i0ue4...zcjm7f * mgr2      Ready    Active        Reachable
```

上述输出内容中显示“mgr1”和“mgr2”都加入了Swarm，并且都是Swarm管理者。最新的配置如图15.8所示。

![98.png](./images/98.png)
<center class="my_markdown"><b class="my_markdown">图15.8 “mgr1”和“mgr2”都加入了Swarm</b></center>

两个管理者这个数量，大概是最糟糕的一种情况了。但是这只是一个实验环境，而不是什么核心业务生产环境，所以糟糕点也无所谓。

向Swarm中加入工作者也只需两步。第一步需要获取新工作者的准入令牌，第二步是在工作者节点上运行 `docker swarm join` 命令。

在任意管理者节点上运行下面的命令，获取工作者准入令牌。

```rust
$ docker swarm join-token worker
To add a worker to this swarm, run the following command:
    docker swarm join --token \
    SWMTKN-1-1dmtw...17stb-ehp8g...w738q \
    172.31.5.251:2377
```

读者可以在指定工作者的节点上运行该命令。准入令牌和IP地址会有所不同。

复制如下所示命令到“wrk1”上并且运行。

```rust
$ docker swarm join --token SWMTKN-1-1dmtw...17stb-ehp8g...w738q \
> 172.31.5.251:2377
This node joined a swarm as a worker.
```

在任意Swarm管理者上运行 `docker node ls` 命令。

```rust
$ docker node ls
ID                HOSTNAME   STATUS   AVAILABILITY  MANAGER STATUS
7xamk...ge662z *  mgr1       Ready    Active        Leader
ailrd...ofzv1u    wrk1       Ready    Active
i0ue4...zcjm7f    mgr2       Ready    Active        Reachable
```

目前读者已经拥有包含两个管理者和一个工作者的Swarm集群。管理者配置为高可用（HA），并且复用集群存储。最新的配置如图15.9所示。

![99.png](./images/99.png)
<center class="my_markdown"><b class="my_markdown">图15.9　将管理者配置为高可用（HA）</b></center>

（2）了解Swarm安全背后的原理

到目前为止，读者已经成功搭建了安全的Swarm集群。接下来一起花费几分钟了解一下这背后涉及的安全技术。

1）Swarm准入令牌

向某个现存的Swarm中加入管理者和工作者所需的唯一凭证就是准入令牌。因此，保证准入令牌的安全十分关键！不要将其发布到公开的Github仓库中。

每个Swarm都包含两种不同准入令牌。

+ 管理者所需准入令牌。
+ 工作者所需准入令牌。

有必要理解Swarm准入令牌的格式。每个准入令牌都由4个不同的字段构成，中间采用虚线（-）连接。

```rust
PREFIX - VERSION - SWARM ID - TOKEN
```

PREFIX永远是“SWMTKN”，这样允许读者通过表达式匹配到该令牌，以避免意外将其发布到公共环境当中；VERSION这一列则展示了Swarm的版本信息；SWARM ID列是Swarm认证信息的一个哈希值；TOKEN这一列的内容决定了该令牌是管理者还是工作者的准入令牌。

如下所示，对于指定Swarm的管理者和工作者准入令牌，除了最后TOKEN字段的内容之外没有任何区别。

+ 管理者：SWMTKN-1-1dmtwusdc...r17stb- **2axi53zjbs45lqxykaw8p7glz** 。
+ 工作者：SWMTKN-1-1dmtwusdc...r17stb- **ehp8gltji64jbl45zl6hw738q** 。

如果用户认为当前准入令牌存在风险，仅用一条命令就可以取消该准入令牌授权，同时发布新的准入令牌。在下面的示例中，取消了已经授权的管理者准入令牌，之后又发布了新的令牌。

```rust
$ docker swarm join-token --rotate manager
Successfully rotated manager join token.
To add a manager to this swarm, run the following command:
    docker swarm join --token \
     SWMTKN-1-1dmtwu...r17stb-1i7txlh6k3hb921z3yjtcjrc7 \
     172.31.5.251:2377
```

需要注意的是，新旧令牌只有最后字段存在区别。SWARM ID还是相同的。

准入令牌保存在集群配置的数据库中，默认是加密的。

2）TLS和双向认证

每个加入Swarm的管理者和工作者节点，都需要发布自己的客户端证书。这个证书用于双向认证。证书中定义了节点相关信息，包括从属的Swarm集群以及该节点在集群中的身份（管理者还是工作者）。

在Linux主机上，读者可以指定使用下面的命令查看指定节点的客户端证书。

```rust
$ sudo openssl x509 \
  -in /var/lib/docker/swarm/certificates/swarm-node.crt \
  -text
  Certificate:
      Data:
          Version: 3 (0x2)
          Serial Number:
              80:2c:a7:b1:28...a8:af:89:a1:2a:51:89
      Signature Algorithm: ecdsa-with-SHA256
          Issuer: CN=swarm-ca
          Validity
              Not Before: Jul 19 07:56:00 2017 GMT
              Not After : Oct 17 08:56:00 2017 GMT
              Subject: O=mfbkgjm2tlametbnfqt2zid8x, OU=swarm-manager,
              CN=7xamk8w3hz9q5kgr7xyge662z
              Subject Public Key Info:
<SNIP>
```

上述输出中， `Subject` 中用到了 `O` 、 `OU` 以及 `CN` 字段分别表示Swarm ID、节点角色以及节点ID信息。

+ 组织字段 `O` 保存的是Swarm ID。
+ 组织单元字段 `OU` 保存的是节点在Swarm中的角色。
+ 规范名称字段 `CN` 保存的是节点的加密ID。

如图15.10所示。

![100.png](./images/100.png)
<center class="my_markdown"><b class="my_markdown">图15.10　 `Subject` 中使用的字段</b></center>

在 `Validity` 中，还可以直接看到证书的更新周期。

上述信息可以在 `docker system info` 命令的输出中得到验证。

```rust
$ docker system info
Swarm: active
 NodeID: 7xamk8w3hz9q5kgr7xyge662z    << Relates to the CN field Is
 Manager: true                        << Relates to the OU field
 ClusterID: mfbkgjm2tlametbnfqt2zid8x << Relates to the O field ...
 ...
 CA Configuration:
  Expiry Duration: 3 months           << Relates to Validity field
 Force Rotate: 0
 Root Rotation In Progress: false

```

3）配置一些CA信息

通过 `docker swarm update` 命令可以配置Swarm证书的更新周期。下面的示例中，将Swarm的证书更新周期修改为30天。

```rust
$ docker swarm update --cert-expiry 720h
```

Swarm允许节点在证书过期前重新创建证书，这样可以保证Swarm中全部节点不会在同一时间尝试更新自己的证书信息。

读者可以在创建Swarm的时候，通过在 `docker swarm init` 命令中增加 `--external-ca` 参数来指定外部的CA。

`docker swarm ca` 命令可以用于管理CA相关配置。可以在运行该命令时指定 `--help` 来查看命令功能。

```rust
$ docker swarm ca --help
Usage: docker swarm ca [OPTIONS]
Manage root CA
Options:
      --ca-cert pem-file               Path to the PEM-formatted root CA
                                       certificate to use for the new cluster Path
      --ca-key pem-file                to the PEM-formatted root CA
                                       key to use for the new cluster
      --cert-expiry duration           Validity period for node certificates
                                       (ns|us|ms|s|m|h) (default 2160h0m0s)
  -d, --detach                         Exit immediately instead of waiting for the
                                       root rotation to converge Specifications of
      --external-ca external-ca        one or more certificate signing endpoints
                                       Print usage
      --help                           Suppress progress output
  -q, --quiet                          Rotate the swarm CA - if no certificate
      --rotate                         or key are provided, new ones will be gene\
```

4）集群存储

集群存储是Swarm的大脑，保存了集群配置和状态数据。

存储目前是基于 `etcd` 的某种实现，并且会在Swarm内所有管理者之间自动复制。存储默认也是加密的。

集群存储正逐渐成为很多Docker平台的关键技术。例如，Docker网络和Docker密钥都用到了集群存储。Docker平台的很多部分都已经用到了集群存储，未来对集群存储的利用会更多，而这也是Swarm模式在Docker规划中占据重要地位的原因之一。这还意味着，如果不使用Swarm模式运行Docker，很多Docker特性就无法使用。

集群存储的日常维护由Docker自动完成。但是，在生产环境中，需要为集群存储提供完整的备份和恢复方案。

Swarm模式安全部分的内容到此为止。

##### 2．Docker安全扫描

快速发现代码缺陷的能力至关重要。Docker安全扫描功能使得对Docker镜像中已知缺陷的检测工作变得简单。

注：

> 在本书编写之时，Docker安全扫描已经可以用于Docker Hub上私有仓库的镜像了。同时该技术还可以作为Docker可信服务本地化部署解决方案的一部分。最后，所有官方Docker镜像都经过了安全扫描，扫描报告在其仓库中可以查阅。

Docker安全扫描对Docker镜像进行二进制代码级别的扫描，对其中的软件根据已知缺陷数据库（CVE数据库）进行检查。在扫描执行完成后，会生成一份详细报告。

打开浏览器访问Docker Hub，并搜索Alpine仓库。图15.11展示了官方Alpine仓库的Tags标签页。

![101.png](./images/101.png)
<center class="my_markdown"><b class="my_markdown">图15.11　官方Alpine仓库的Tags标签页</b></center>

Alpine仓库是官方仓库，这意味着该仓库会自动扫描并生成对应报告。可以看到，镜像标签为 `edge` 、 `latest` 以及 `3.6` 的镜像都通过了已知缺陷的检查。但是 `alpine:3.5` 镜像存在已知缺陷（标红）。

如果打开 `alpine:3.5` 镜像，可以发现如图15.12所示的详细信息。

![102.png](./images/102.png)
<center class="my_markdown"><b class="my_markdown">图15.12　 `alpine:3.5` 镜像的详细信息</b></center>

这是发现自己软件中已知缺陷详情的一种简单方式。

Docker可信镜像仓库服务（Docker Trusted Registry, DTR），属于Docker企业版中本地化镜像仓库服务的一部分内容，提供了相同的Capability，同时还允许用户自行控制其镜像扫描时机以及扫描方式。例如，DTR允许用户选择镜像是在推送时自动触发扫描，还是只能手工触发。同时DTR还允许用户手动更新CVE数据库，这对于DTL无法进行联网来自动更新CVE数据的场景来说，是一种理想的解决方案。

这就是Docker安全扫描，一种深入检测Docker镜像是否存在已知安全缺陷的好方式。当然，能力越大责任越大，当用户发现缺陷后，就需要承担解决相应缺陷的责任了。

##### 3．Docker内容信任

Dockr内容信任（Docker Content Trust，DCT）使得用户很容易就能确认所下载镜像的完整性以及其发布者。在不可信任的网络环境中下载镜像时，这一点很重要。

从更高层面来看，DCT允许开发者对发布到Docker Hub或者Docker可信服务的镜像进行签名。当这些镜像被拉取的时候，会自动确认签名状态。图15.13展示了这一过程。

DCT还可以提供关键上下文，如镜像是否已被签名从而可用于生产环境，镜像是否被新版本取代而过时等。

在本书编写之际，DTC提供的上下文还在初期，配置起来相当复杂。

在Docker主机上启用DCT功能，所要做的只是在环境中将 `DOCKER_CONTENT_TRUST` 变量设置为1。

```rust
$ export DOCKER_CONTENT_TRUST=1
```

![103.png](./images/103.png)
<center class="my_markdown"><b class="my_markdown">图15.13　镜像被拉取时自动确认签名状态</b></center>

在实际环境中，用户可能希望在系统中默认开启该特性。

如果使用Docker统一配置层（Docker企业版的一部分），需要勾选图中15.14所示 `Run Only Signed Images` 复选项。这样会强制所有在UCP集群中的节点只运行已签名镜像。

![104.png](./images/104.png)
<center class="my_markdown"><b class="my_markdown">图15.14 勾选 `Only run signed images` 复选项</b></center>

由图15.14中可知，UCP在DCT的基础上进行进一步封装，提供了已签名镜像的安全首选项信息。例如，用户可能有这样的需求：在生产环境中只能使用由 `secops` 签名的镜像。

一旦DCT功能开启，就不能获取并使用未签名镜像了。图15.15展示了开启DCT之后，如果再次尝试通过Docker CLI或者UCP Web UI界面拉取未签名镜像时所报的错误（两个示例都尝试拉取标签为“unsigned”的镜像）。

![105.png](./images/105.png)
<center class="my_markdown"><b class="my_markdown">图15.15　拉取未签名镜像时报错</b></center>

图15.16展示了DCT是如何阻止Docker客户端拉取一个被篡改的镜像的。图15.17展示了DCT如何阻止客户端拉取旧镜像。

![106.png](./images/106.png)
<center class="my_markdown"><b class="my_markdown">图15.16　拉取被篡改的镜像</b></center>

![107.png](./images/107.png)
<center class="my_markdown"><b class="my_markdown">图15.17　拉取旧镜像</b></center>

Docker内容信任是一种很重要的技术，能帮助用户检查从Docker服务中拉取的镜像。该技术的基础模式配置起来非常简单，但是类似上下文等一些高级特性，现阶段配置起来还是非常复杂的。

##### 4．Docker密钥

很多应用都需要密钥。比如密码、TLS证书、SSH key等。

在Docker1.13版本之前，没有一种标准且安全的方式能让密钥在应用间实现共享。常见的方式是开发人员将密钥以文本的方式写入环境变量（我们都这么做过）。这与理想状态差距甚远。

Docker1.13引入了Docker密钥，将密钥变成Docker生态系统中的一等公民。例如，增加了一个新的子命令 `docker secret` 来管理密钥。在Docker的UCP界面中，也有专门的地方来创建和管理密钥。在后台，密钥在创建后以及传输中都是加密的，使用时被挂载到内存文件系统，并且只对那些已经被授权了的服务开放访问。这确实是一种综合性的端到端解决方案。

图15.18展示了其总体流程。

下面依次介绍图15.18中所示工作流的每一步。

（1）密钥被创建，并且发送到Swarm。

（2）密钥存放在集群存储当中，并且是加密的（每个管理者节点都能访问集群存储）。

（3）B服务被创建，并且使用了该密钥。

（4）密钥传输到B服务的任务节点（容器）的过程是加密的。

（5）B服务的容器将密钥解密并挂载到路径 `/run/secrets` 下。这是一个临时的内存文件系统（在Windows Docker中该步骤有所不同，因为Windows中没有内存文件系统这个概念）。

（6）一旦容器（服务任务）完成，内存文件系统关闭，密钥也随之删除。

（7）A服务中的容器不能访问该密钥。

![108.jpg](./images/108.jpg)
<center class="my_markdown"><b class="my_markdown">图15.18　引入Docker密钥</b></center>

用户可以通过 `docker secret` 子命令来管理密钥，可以通过在运行 `docker service create` 命令时附加 `--secret` ，从而为某个服务指定密钥。

