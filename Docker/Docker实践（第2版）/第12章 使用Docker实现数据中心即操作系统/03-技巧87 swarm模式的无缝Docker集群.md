### 技巧87　swarm模式的无缝Docker集群

能够完全控制集群当然很好，但是有时候对集群进行太细微的管理是没有必要的。实际上，如果用户的应用程序没有很复杂的需求，完全可以充分利用Docker可以在任何地方运行的承诺——实在没有任何理由不把容器丢到集群里，让集群决定在哪里运行它们。

swarm模式在研究型的实验室环境中很有用处，如果实验室能够将计算密集型的问题分解为一系列的小块，将可以在机器集群里非常轻松地处理问题。

#### 问题

有一组安装了Docker的宿主机，想要启动容器并且不需要很细地管理它们的运行位置。

#### 解决方案

使用Docker的swarm模式——Docker内置的处理编排的特性。

Docker的swarm模式是Docker公司的官方解决方案，将宿主机集群视为单个Docker守护程序并为其部署服务。它的命令行与我们在 `docker run` 中熟悉的命令行非常相似。swarm模式是从与Docker一起使用的官方Docker工具演变而来的，它已被集成到Docker守护程序本身中。如果读者在任何地方看到对“Docker Swarm”的旧引用，它们可能是指旧的工具。

Docker swarm由多个节点组成。每个节点可以是管理节点或工作节点，这些角色是灵活的，可以随时在集群中更改。管理节点负责将服务部署到可用节点，而工作节点将只运行容器。默认情况下，管理节点也可以运行容器，但我们还将了解如何更改该设定。

当管理节点被启动时，它将初始化swarm的某些状态，然后监听来自其他节点的连接以添加到swarm中。



**注意**

swarm中使用的所有Docker版本都必须至少是1.12.0。理想的情况是，应该尽量让所有版本都保持一致，否则可能遇到版本不兼容问题。



首先，让我们创建一个新的swarm：

```c
h1 $ ip addr show | grep 'inet ' | grep -v 'lo$\|docker0$' # get external IP
    inet 192.168.11.67/23 brd 192.168.11.255 scope global eth0
h1 $ docker swarm init --advertise-addr 192.168.11.67
Swarm initialized: current node (i5vtd3romfl9jg9g4bxtg0kis) is now a
manager.
To add a worker to this swarm, run the following command:
    docker swarm join \
    --token SWMTKN-1-4blo74l0m2bu5p8synq3w4239vxr1pyoa29cgkrjonx0tuid68
➥ -dhl9o1b62vrhhi0m817r6sxp2 \
    192.168.11.67:2377
To add a manager to this swarm, run 'docker swarm join-token manager' and
follow the instructions.
```

这样就成功创建了一个新的swarm，并且把宿主机 `h1` 上的Docker守护进程设置为管理节点。

现在我们可以检查新创建的swarm：

```c
h1 $ docker info
[...]
Swarm: active
 NodeID: i5vtd3romfl9jg9g4bxtg0kis
 Is Manager: true
 ClusterID: sg6sfmsa96nir1fbwcf939us1
 Managers: 1
 Nodes: 1
 Orchestration:
  Task History Retention Limit: 5
 Raft:
  Snapshot Interval: 10000
  Number of Old Snapshots to Retain: 0
  Heartbeat Tick: 1
  Election Tick: 3
 Dispatcher:
  Heartbeat Period: 5 seconds
 CA Configuration:
  Expiry Duration: 3 months
 Node Address: 192.168.11.67
 Manager Addresses:
  192.168.11.67:2377
[...]
h1 $ docker node ls
$ docker node ls
ID                          HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
i5vtd3romfl9jg9g4bxtg0kis * h1        Ready   Active        Leader
```

在管理节点启动后，可以在另一台宿主机上执行特定命令使Docker守护进程作为工作节点加入：

```c
h2 $ docker swarm join \
     --token SWMTKN-1-4blo74l0m2bu5p8synq3w4239vxr1pyoa29cgkrjonx0tuid68
➥ -dhl9o1b62vrhhi0m817r6sxp2 \
     192.168.11.67:2377
This node joined a swarm as a worker.
```

`h2` 现在作为工作节点加入了我们的swarm。在任意一台宿主机上执行 `docker info` 都可显示出节点数已经增长为2， `docker node ls` 命令也会把两个节点都列出。

最后，让我们启动一个容器。在swarm模式下，这被称为部署服务，因为有些附加功能对容器没有意义。在部署服务之前，我们将标记管理节点的可用性为 `drain` （耗尽）——默认情况下，所有管理节点都可用于运行容器，但是在本技巧中，我们要演示远程机器调度功能，因此我们将采取一些措施来避免管理节点。耗尽将导致节点上已有的所有容器被重新部署到其他位置，并且不会在该节点上调度任何新服务。

```c
h1 $ docker node update --availability drain i5vtd3romfl9jg9g4bxtg0kis
h1 $ docker service create --name server -d -p 8000:8000 ubuntu:14.04 \
        python3 -m http.server 8000
vp0fj8p9khzh72eheoye0y4bn
h1 $ docker service ls
ID            NAME    MODE        REPLICAS  IMAGE         PORTS
vp0fj8p9khzh  server  replicated  1/1       ubuntu:14.04  *:8000->8000/tcp
```

这里有几件事要注意。最重要的是，swarm已自动选择一台机器来启动容器，如果你有多个工作节点，管理节点将根据负载均衡选择一个。读者可能也会发现，有些 `docker service create` 的参数和 `docker run` 的参数相似——许多参数是共享的，但是仍然值得读一读文档。例如， `docker run` 的 `--volume` 参数在 `--mount` 参数中具有不同的格式，你应该读一下文档。

现在是时候检查一下我们的服务是否已经启动并正在运行了：

```c
h1 $ docker service ps server
ID            NAME      IMAGE         NODE  DESIRED STATE  CURRENT STATE
➥          ERROR  PORTS
mixc9w3frple  server.1  ubuntu:14.04  h2    Running        Running 4
minutes ago
h1 $ docker node inspect --pretty h2 | grep Addr
 Address:               192.168.11.50
h1 $ curl -sSL 192.168.11.50:8000 | head -n4
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
➥ "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ascii">
```

swarm模式具有默认启用的一项附加功能，称为 **路由网格** （routing mesh）。这使swarm中的每个节点看起来都好像可以服务于swarm中已发布端口的所有服务的请求一样——任何传入的连接都被转发到适当的节点。

例如，如果再次回到 `h1` 管理节点（我们知道它没有运行该服务，因为它的可用性为 `drain` ），它将仍然在端口8000上响应任何请求：

```c
h1 $ curl -sSL localhost:8000 | head -n4
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
➥ "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ascii">
```

这对于一种简单的服务发现特别有用——只要知道一个节点的地址，就可以非常轻松地访问所有服务。

swarm使用完毕后，就可以关闭所有服务并删除集群了。

```c
$ docker service rm server
server
$ docker swarm leave
Error response from daemon: You are attempting to leave the swarm on a >
node that is participating as a manager. Removing the last manager erases >
all current state of the swarm. Use '--force' to ignore this message.
$ docker swarm leave --force
Node left the swarm.
```

正如我们在此处所见，如果我们正在节点中关闭最后一个管理节点，则swarm模式将发出警告，因为该swarm中的所有信息都将丢失。你可以使用 `--force` 覆盖此警告。你还需要在所有工作节点上执行 `docker swarm leave` 。

#### 讨论

这是对Docker中的swarm模式的简要介绍，这里没有涉及很多内容。例如，读者可能已经注意到了，在初始化swarm后的帮助文本中提到了将其他主服务器连接到swarm的功能，这对于恢复能力很有用。另一些有趣的主题是部分内置功能，它们存储服务配置信息（如在技巧74中用etcd所做的那样），使用约束来指导容器的放置以及有关如何在发生故障时回滚的情况下升级容器的信息。我们建议读者参考Dockers网站上的官方文档来获取更多信息。

