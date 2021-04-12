### 16.2.2　Docker通用控制平面（UCP）

本节接下来使用 **UCP** 代指Docker通用控制平面。

UCP是企业级的容器即服务平台的图形化操作界面。UCP使用Docker引擎，并添加了各种企业喜欢以及需要的功能。例如RBAC、可配置、认证、高可用控制平面以及简单界面。在UCP内部，是一个容器化的微服务应用，以多个容器的形式运行。

架构层面上讲，UCP是基于Swarm模式下的Docker EE构建的。如图16.4所示，UCP控制平面运行在Swarm管理节点上，应用则部署在Swarm工作节点上。

![112.png](./images/112.png)
<center class="my_markdown"><b class="my_markdown">图16.4　UCP结构</b></center>

截至本书编写时，UCP管理节点必须是Linux。工作节点既可以Windows，也可以是Linux。

##### 1．规划UCP安装

在规划UCP安装的时候，合理设置集群大小和规格十分重要。下面介绍该过程中需要考虑的一些方面。

集群中全部节点的时钟需要同步（例如NTP）。如果没有同步，可能导致一些很难定位的问题。

全部节点都要有自己的静态IP地址和固定的DNS名称。

默认情况下，UCP管理节点不运行用户工作负载。推荐使用这种最佳实践，并建议用户在生产环境中强制使用。该方式使得管理节点只需关注控制平面职责。同时也能简化问题定位。

用户需要保证管理节点数量为奇数。这样就能避免出现脑裂等类似场景时，会导致管理节点不可用，或者与集群割裂的现象。理想数量为3、5或者7，3或者5是较常用的。多于7的话，可能导致后台Raft算法或者集群一致性的问题。如果不能提供3个管理节点，1个要好于2个！

如果配置了后台计划（用户应当配置）并进行日常备份，可能需要部署5个管理节点。这是因为Swarm和UCP的备份操作需要停止Docker和UCP服务。5个管理节点可以保证在执行类似操作时集群的弹性。

管理节点应当根据数据中心可用域进行部署。用户最不想见到的场景，就是全部UCP管理节点所在的域都不可用。但是，管理节点之间的通信必须经由高速可靠的网络完成。因此如果数据中心可用域之间网络状况不佳，最好还是将所有管理节点部署在相同域之中。有件事已经约定成俗，即在公有云上部署时，需要将管理节点部署在同区域内的可用域中。跨区域通常会受到低可靠性和高延迟网络的影响。

工作节点的数量可以根据需求设置，因为它们并不会参与到集群Raft操作当中，所以就不会影响控制平面操作。

规划工作节点的规格和数量，需要理解计划部署在集群上的应用需求。例如，理解之后能帮助用户确定需要多少Windows节点和Linux节点。同时还需要知道应用是否有特殊需求，需要工作节点的定制化来支持，例如PCI类工作负载。

此外，虽然Docker引擎是轻量级的，但其上运行的容器化应用不一定也是。出于这样的考虑，根据应用的CPU、RAM、网络以及磁盘I/O需求规划节点数目就很重要了。

确定合理的节点配置并不是什么好玩的事儿，这完全取决于工作负载。但是，Docker网站上对Linux Docker UCP 2.2.4的最低配置有如下建议。

+ UCP管理节点运行DTR：8GB RAM，3GB磁盘空间。
+ UCP工作节点：4GB RAM，3GB空闲磁盘空间。

推荐配置如下。

+ 运行DTR的UCP管理节点：8GB RAM，4核CPU，100GB磁盘。
+ UCP工作节点：4GB RAM，25-100GB空闲磁盘空间。

该建议仅供参考，用户在确定配置时需要自己多加练习。

有一点是确认的：Window镜像会比Linux镜像 **稍大一些** 。所以规划时务必考虑该因素。

关于需求规划最后多说一点。Docker Swarm和Docker UCP简化了管理节点和工作节点的添加/删除工作。新加入的管理节点被自动加入到HA控制平面，新加入的工作节点马上就能参与到工作负载调度当中。类似的，删除管理节点和工作节点也非常简单。只要拥有多个管理节点，就可以在不影响集群操作的情况下移除其中一个。移除工作节点时，需要清理该节点上的工作负载，然后从运行中的集群移除。上述特点使得UCP对管理节点和工作节点的变更做到不感知。

记住前面的内容后，就可以开始安装UCP了。

##### 2．安装Docker UCP

本节主要介绍在新集群的第一个管理节点上安装Docker UCP的完整过程。

（1）在某个Linux Docker EE节点上运行下面的命令，该节点应是计划中作为UCP集群的第一个管理节点。

关于命令需要补充说明，示例在安装UCP时，使用了 `docker/ucp:2.2.5` 镜像，用户需要替换为适合自己的版本。 `--host-address` 设置了Web界面访问地址。如果用户在AWS上完成安装，并且计划通过互联网访问公司的网络，这里就需要设置AWS的公共IP地址。

```rust
$ docker container run --rm -it --name ucp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker/ucp:2.2.5 install \
  --host-address <node-ip-address> \
  --interactive
```

（2）配置管理员账号。安装过程会提示用户输入用户名和密码，作为UCP管理员账号。这是一个本地账号，建议遵守公司规范来创建用户名和密码。创建后千万不要忘记。

（3）主体别名（Subject Alternative Name，SAN）。安装程序会提示输入能访问UCP的IP地址和名称列表。列表内容可以是私有IP地址以及DNS名称，并且会加入到账号当中。

安装过程还需注意以下的一些内容。

UCP基于Docker Swarm，这意味着UCP管理节点需要运行在Swarm管理节点上。如果在某个节点上以单引擎模式（Single-Engine Mode）安装UCP，则该节点会默认切换为Swarm模式。

安装程序拉取UCP服务所需的全部镜像，并完成相应容器的启动。下面列举了部分由安装程序拉取的镜像。

```rust
INFO[0008] Pulling required images... (this may take a while)
INFO[0008] Pulling docker/ucp-auth-store:2.2.5
INFO[0013] Pulling docker/ucp-hrm:2.2.5
INFO[0015] Pulling docker/ucp-metrics:2.2.5
INFO[0020] Pulling docker/ucp-swarm:2.2.5
INFO[0023] Pulling docker/ucp-auth:2.2.5
INFO[0026] Pulling docker/ucp-etcd:2.2.5
INFO[0028] Pulling docker/ucp-agent:2.2.5
INFO[0030] Pulling docker/ucp-cfssl:2.2.5
INFO[0032] Pulling docker/ucp-dsinfo:2.2.5
INFO[0080] Pulling docker/ucp-controller:2.2.5
INFO[0084] Pulling docker/ucp-proxy:2.2.5
```

部分比较值得关注的镜像包括以下几点。

+ `ucp-agent` 这是UCP核心代理。该代理会部署到集群的全部节点上，用于确保UCP所需容器全部启动并运行。
+ `ucp-etcd` 集群持久化键值对存储。
+ `ucp-auth`  共享鉴权服务（在DTR的单点登录中也用到了）。
+ `ucp-proxy`  控制对本地Docker Socket端口的访问，这样未认证的客户端就不能擅自篡改集群了。
+ `ucp-swarm`  提供对底层Swarm的适配。

最终，安装程序创建了一对根CA：一个用于集群内部通信，另一个用于外部访问。CA使用自签名证书，这对于实验和测试环境来说很好，但是不适用于生产环境。

为了完成可信CA证书的UCP安装，需要使用下面3个文件完成证书绑定。

+ `ca.pem` ：可信CA证书（通常是公司内部CA）。
+ `cert.pem` ：UCP的公开证书。该证书包含了全部被授权访问集群的IP地址和DNS名称，包括位于集群之前的负载均衡器。
+ `key.pem` ：UCP的私钥。

如果已经有了上述文件，则需要将其挂载到Dockerucp-controller-server-certs卷下，并且使用 `--external-ca` 参数指定卷。用户也可以在安装完成后，通过Web界面中的 `管理员设置（Admin Setting）` 页面来修改证书。

UCP安装程序输出中的最后一段内容，就是访问所用的URL。

```rust
<Snip>
INFO[0049] Login to UCP at https://<IP or DNS>:443
```

通过Web浏览器访问该地址并且登录。如果使用自签名证书，则需要确认浏览器的告警信息。同时还需要指定许可证文件，该文件可以从Docker商店的 `My Content` 中下载。

登录后即可访问UCP管理面板，如图16.5所示。

到目前为止，一个单点登录UCP集群已经就绪。

可以通过管理面板底部的 `Add Nodes` 链接为集群添加更多的管理节点和工作节点。

图16.6展示了添加节点的界面。用户可以选择添加管理节点或者工作节点，然后界面中就会给出对应的命令，在待添加节点上运行即可。示例中选择添加Linux工作节点。注意，这是一个 `docker swarm` 命令。

添加的节点会加入Swarm集群，并且配置所需的UCP服务。如果添加的是管理节点，推荐在连续添加之间稍作等待。这样可以给Docker留出下载并运行所需UCP容器的机会，同时也允许集群注册新的管理节点并达到法定人数。

新加入的管理节点会自动配置到高可用（HA）的一致性Raft组当中，并且被授权可以访问集群存储。此外，虽然外部负载均衡器通常不被认作UCP HA的核心部分，但其本身对外提供了稳定的DNS名称，屏蔽了一些后端场景，如某个节点挂掉。

![113.png](./images/113.png)
<center class="my_markdown"><b class="my_markdown">图16.5　UCP管理面板</b></center>

![114.png](./images/114.png)
<center class="my_markdown"><b class="my_markdown">图16.6　添加节点的界面</b></center>

用户需要为443端口的TCP透传配置外部的负载均衡器，通过自定义的HTTPS心跳检查 `https://<ucp_man-ager>/_ping` 确认UCP管理节点的状态。

现在一个工作状态的UCP已经搭建完成，可以通过 `Admin Settings` 页面查看相关选项，如图16.7所示。

![115.png](./images/115.png)
<center class="my_markdown"><b class="my_markdown">图16.7　通过 `Admin Settings` 页面查看相关选项</b></center>

本页面的配置信息包含了大部分的UCP后台配置信息。

##### 3．UCP的访问控制

所有对UCP的访问，都经由身份管理子系统。这意味着用户在集群上执行任何操作前，首先需要通过用户名和密码进行认证。这些操作包括集群的管理，以及服务的部署和管理。

用户使用UI界面的时候已经体验过了，必须使用用户名和密码才能登录。在CLI中也是一样的，用户不能在未登录的情况下通过UCP执行命令！这是因为UCP集群中本地Docker Socket受到 `ucp-proxy` 服务的保护，不会接受未认证命令。

##### 4．客户端绑定

每个运行Docker CLI的节点，都能部署并管理UCP集群的工作负载， **只要该节点存在一个有效UCP用户认证** 。

本节中会创建一个新UCP用户，新建并下载该用户的绑定证书，接着创建一个Docker客户端并使用该证书。在完成上述步骤后，会解释其工作原理。

（1）如果还没就绪，则以管理员身份登录UCP。

（2）单击 `User Management > Users` ，创建一个新用户。因为还未讨论角色和权限相关的内容，所以将用户设置为Docker EE管理员。

（3）在新用户选中状态下，单击 `Configure` 下拉框，然后选择 `Client Bundle` ，如图16.8所示。

![116.png](./images/116.png)
<center class="my_markdown"><b class="my_markdown">图16.8 选择 `Client Bundle`</b></center>

（4）单击 `Client Bundle +` 链接，生成并下载该用户的客户端Bundle。

此时需要注意，客户端Bundle是与用户相关的。因此，该Bundle能够使得配置好的Docker客户端在UCP集群上以该Bundle所属用户的身份执行命令。

（5）复制下载内容到Docker客户端，该客户端是用户配置用于管理UCP的。

（6）登录客户端节点，执行下面的全部命令。

（7）解压缩客户端绑定内容。

```rust
$ unzip ucp-bundle-nigelpoulton.zip
Archive: ucp-bundle-nigelpoulton.zip
extracting: ca.pem
extracting: cert.pem
extracting: key.pem
extracting: cert.pub
extracting: env.sh
extracting: env.ps1
extracting: env.cmd
```

示例使用Linux的unzip包将客户端绑定解压缩到当前目录。需要将命令中客户端绑定的名称替换为自己环境中的名称。

（8）使用恰当的脚本配置Docker客户端。env.sh可以在Linux和Mac上使用，env.ps和env.cmd可以在Windows上使用。

运行脚本需要管理员/root权限。

示例在Windows和Linux上均可以执行。

```rust
$ eval "$(<env.sh)"
```

此时，客户端节点配置已经完成。

（9）测试权限。

```rust
$ docker version
 <Snip>
Server:
 Version:      ucp/2.2.5
 API version:  1.30 (minimum version 1.20)
 Go version:   go1.8.3
 Git commit:   42d28d140
 Built:        Wed Jan 17 04:44:14 UTC 2018
 OS/Arch:      linux/amd64
 Experimental: false
```

注意到输出中的 `Server` 部分显示其版本为ucp/2.2.5，这就说明Docker客户端已经成功连接到UCP节点的daemon了。

实际上，脚本共配置了3个环境变量： `DOCKER_HOST` 、 `DOCKER_TLS_VERIFY` 和 `DOCKER_CERT_PATH` 。

DOCKER_HOST将客户端指向了远端位于UCP控制层中的Docker daemon。比如 `DOCKER_HOST=tcp://34.242.196.63:443` ，可以看到，是通过443端口访问的。

DOCKER_TLS_VERIFY设置为1，告诉客户端使用TLS认证的客户端模式。

DOCKER_CERT_PATH告诉Docker客户端绑定证书的具体位置。

最终结果就是所有 `Docker` 命令都会在客户端使用用户证书签名，然后经由网络发送到远端的UCP管理节点，如图16.9所示。

![117.png](./images/117.png)
<center class="my_markdown"><b class="my_markdown">图16.9　用户证书签名被发送到远端的UCP管理节点</b></center>

下面来了解一下如何备份并恢复UCP。

##### 5．UCP备份

首先并且最重要的是，高可用（HA）并不等价于备份！

思考下面的例子。有一个包含5个管理节点的UCP集群。所有管理节点都处于健康状态，并且控制平面开启了复制功能。某个心怀怨恨的员工对集群进行破坏（或者删除了全部用户账户）。破坏操作会复制到全部5个管理节点，导致集群被破坏。这种场景下HA没有丝毫帮助。此时需要的，是备份！

一个UCP集群主要由3个部分构成，也是需要分别备份的内容：Swarm、UCP和Docker可信镜像仓库服务（DTR）。

接下来会展示如何完成Swarm和UCP的备份，有关DTR备份的内容本章会在稍后进行介绍。

虽然UCP位于Swarm上层，但是它们是互相独立的。Swarm维护了全部节点关系、网络以及服务定义。UCP在其上层构建，维护自己的数据库和卷存储来记录用户、组、授权、Bundle、许可证文件、认证等信息。

一起来看一下如何进行 **Swarm备份** 。

Swarm配置和状态保存在 `/var/lib/docker/swarm` 中，其中包含了Raft日志密钥，并且会复制到每个管理节点。Swarm备份就是复制该目录下的所有文件。

因为该信息会复制到每个管理节点，所以用户可以在任何管理节点上进行备份。

备份时需要在待执行备份操作的节点上停止Docker。这意味着在主管理节点上执行备份操作不是一个好的选择，因为这样会导致重新选主。执行备份时最好选择在业务的低峰期进行，虽然对于拥有多管理节点的Swarm来说，停止某个管理节点并不会出现问题，但这种操作还是会增加集群在另一管理节点宕机时出现高可用有效节点数不足的情况。

在执行备份前，创建一些Swarm对象可以验证备份和回滚操作是否确实生效了。示例中待备份的Swarm，拥有一个名为 `vantage-net` 的覆盖网络，以及名为 `vantage-svc` 的Swarm服务。

（1）停止待备份Swarm管理节点上的Docker。这样会停止该节点上的全部UCP容器。如果UCP配置了HA，则其他管理节点会保证控制平面处于可用状态。

```rust
$ service docker stop
```

（2）备份Swarm配置。示例使用Linux tar工具来执行文件复制。可随意选择其他工具。

```rust
$ tar -czvf swarm.bkp /var/lib/docker/swarm/
tar: Removing leading `/' from member names
/var/lib/docker/swarm/
/var/lib/docker/swarm/docker-state.json
/var/lib/docker/swarm/state.json
<Snip>
```

（3）确认备份文件存在。

```rust
$ ls -l
-rw-r--r-- 1 root root 450727 Jan 29 14:06 swarm.bkp
```

备份文件的保存周期需要视公司具体的备份策略而定。

（4）重启Docker。

```rust
$ service docker restart
```

现在Swarm备份完成，是时候 **备份UCP** 了。

在开始UCP备份前，需要注意如下几点。

因为UCP备份任务以容器方式运行，所以如果想进行备份，需要Docker保持运行状态。

可以在集群中的任意一台UCP管理节点上运行备份，并且只需要在一个节点上运行即可（UCP复制功能会将配置信息复制到全部管理节点，所以没有必要备份多节点）。

对UCP进行备份会停止所在管理节点上的全部UCP容器。在该前提下，备份操作需要运行在一个高可用UCP集群上，并且最好是在业务低峰期运行。

自始至终，执行备份的管理节点上的用户工作负载并不会停止。但是，并不建议在UCP管理节点上执行用户工作负载。

下面开始备份UCP。

在某个UCP管理节点上执行下面的命令。该节点的Docker需要保持运行状态。

```rust
$ docker container run --log-driver none --rm -i --name ucp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker/ucp:2.2.5 backup --interactive \
  --passphrase "Password123" > ucp.bkp
```

该命令很长，一起来看一下每个步骤的内容。

第一行是标准的 `docker container run` 命令，让Docker运行某个容器，运行时不开启日志，在运行结束后进行删除，同时调用 `ucp` ；第二行将Docker socket挂载到容器中，这样容器可以通过访问Docker API来停止运行；第三行是告诉Docker在容器内基于 `docker/ ucp:2.2.5` 镜像运行 `backup --interactive` 命令；最后一行创建了名为 `ucp.bkp` 的加密文件，并且用密码进行安全保护。

下面是值得注意的几点。

指定具体的UCP镜像版本（标签）是一个好办法，示例中指定为 `docker/ucp:2.2.5` 。这样做是因为进行备份和恢复操作的时候，建议使用相同版本的镜像。如果没有显示指定镜像版本，Docker会默认使用标签为 `latest` 的镜像，这可能导致执行备份和恢复操作时镜像版本存在差异。

每次备份都应当使用 `--passphrase` 来保护备份内容，此外可以改进示例中的密码，使其对用户更加友好。

建议根据用户的备份要求对备份文件进行目录化管理，并保存一个离线备份。此外建议配置备份计划和对应的检查任务。

现在已经完成了Swarm和UCP的备份，可以在灾难性事件发生后安全地进行恢复了。

##### 6．恢复UCP

在介绍恢复UCP之前，有句话不得不提前说明：从备份进行恢复是最后的手段，只能在整个集群都宕机或者全部管理节点都丢失的情况下使用！

**如果HA集群下仅丢失某个管理节点，并不需要从备份进行恢复。** 该情况下，很容易就能创建新管理节点并加入集群。

下面会先介绍如何从备份恢复Swarm，然后是UCP。

在欲恢复的Swarm/UCP管理节点上执行下面的任务。

（1）停止Docker。

```rust
$ service docker stop
```

（2）删除全部已存在的Swarm配置。

```rust
$ rm -r /var/lib/docker/swarm
```

（3）从Swarm备份中恢复配置信息。

示例中使用了名为 `swarm.bkp` 的压缩文件，格式为 `tar` 。该命令需要指定恢复到根目录下，因为备份文件解压为原始文件的操作中会包含全路径信息。读者环境可能略有不同。

```rust
$ tar -zxvf swarm.bkp -C /
```

（4）初始化新的Swarm集群。

切记，当前执行的操作并不是恢复某个节点然后重新加入集群。该操作是恢复一个不可用的Swarm集群，其中不包含任何存活的管理节点。-- `force-new-cluster` 参数告诉Docker创建新集群，使用的配置保存在当前节点/var/lib/docker/swarm目录下。

```rust
$ docker swarm init --force-new-cluster
Swarm initialized: current node (jhsg...3l9h) is now a manager.
```

（5）检查网络和服务是恢复操作中的一部分。

```rust
$ docker network ls
NETWORK ID        NAME          DRIVER       SCOPE
snkqjy0chtd5      vantage-net   overlay      swarm
$ docker service ls
ID              NAME          MODE        REPLICAS   IMAGE
w9dimu8jfrze    vantage-svc   replicated  5/5        alpine:latest
```

恭喜。Swarm集群完成恢复。

（6）为Swarm集群增加新的管理节点和工作节点，并刷新备份。

在恢复Swarm之后，可以 **恢复UCP** 。

在示例中，UCP备份到了当前目录下名为ucp.bkp的文件中。虽然文件名是备份文件，但其本质是一个Linux打包工具。

在欲恢复UCP的节点上执行下面的命令。该节点可以是刚刚执行Swarm恢复操作的节点。

（1）删除已经存在并且可能崩溃的UCP安装。

```rust
$ docker container run --rm -it --name ucp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker/ucp:2.2.5 uninstall-ucp --interactive
INFO[0000] Your engine version 17.06.2-ee-6, build e75fdb8 is compatible
INFO[0000] We're about to uninstall from this swarm cluster.
Do you want to proceed with the uninstall? (y/n): y
INFO[0000] Uninstalling UCP on each node...
INFO[0009] UCP has been removed from this cluster successfully.
INFO[0011] Removing UCP Services
```

（2）从备份中恢复UCP。

```rust
$ docker container run --rm -i --name ucp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker/ucp:2.2.5 restore --passphrase "Password123" < ucp.bkp
INFO[0000] Your engine version 17.06.2-ee-6, build e75fdb8 is compatible
<Snip>
time="2018-01-30T10:16:29Z" level=info msg="Parsing backup file"
time="2018-01-30T10:16:38Z" level=info msg="Deploying UCP Agent Service"
time="2018-01-30T10:17:18Z" level=info msg="Cluster successfully restored.
```

（3）登录UCP Web界面，确认之前创建的用户还存在（或者是任何之前环境中存在的UCP对象）。

恭喜。现在已经知道了如何备份并恢复Docker Swarm以及Docker UCP。

接下来将目光转移到Docker可信镜像仓库服务。

