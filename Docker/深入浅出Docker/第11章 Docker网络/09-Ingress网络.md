### 11.2.6　Ingress网络

Swarm支持两种服务发布模式，两种模式均保证服务从集群外可访问。

+ Ingress模式（默认）。
+ Host模式。

通过Ingress模式发布的服务，可以保证从Swarm集群内任一节点（即使 **没有** 运行服务的副本）都能访问该服务；以Host模式发布的服务只能通过运行服务副本的节点来访问。图11.20展示了两种模式的区别。

Ingress模式是默认方式，这意味着任何时候读者通过 `-p` 或者 `--publish` 发布服务的时候，默认都是Ingress模式；如果需要以Host模式发布服务，则读者需要使用 `--publish` 参数的完整格式，并添加 `mode=host` 。下面一起来看Host模式的例子。

```rust
$ docker service create -d --name svc1 \
  --publish published=5000,target=80,mode=host \
  nginx
```

关于该命令的一些说明。 `docker service mode` 允许读者使用完整格式语法或者简单格式语法来发布服务。简单格式如 `-p 5000:80` ，前面已经多次出现。但是，读者不能使用简单格式发布Host模式下的服务。

![73.png](./images/73.png)
<center class="my_markdown"><b class="my_markdown">图11.20　Ingress模式与Host模式</b></center>

完整格式如 `--publish published=5000,target=80,mode=host` 。该方式采用逗号分隔多个参数，并且逗号前后不允许有空格。具体选项说明如下。

+ `published=5000`  表示服务通过端口5000提供外部服务。
+ `target=80` 表示发送到published端口5000的请求，会映射到服务副本的80端口之上。
+ `mode=host` 表示只有外部请求发送到运行了服务副本的节点才可以访问该服务。

通常使用Ingress模式。

在底层，Ingress模式采用名为 **Service Mesh** 或者 **Swarm Mode Service Mesh** 的四层路由网络来实现。图11.21展示了Ingress模式下一个外部请求是如何流转，最终访问到服务的。

简要介绍图11.21的内容。

+ 图中最上方命令部署了一个名为“svc1”的Swarm服务。该服务连接到了 `overnet` 网络，并发布到5000端口。
+ 按上述方式发布Swarm服务（ `--publish published=5000,target=80` ）会在Ingress网络的5000端口进行发布。因为Swarm全部节点都接入了Ingress网络，所以这个端口被发布到了Swarm范围内。
+ 集群确保到达Ingress网络中 **任意节点** 的5000端口的流量，都会被路由到80端口的“svc1”服务。

![74.png](./images/74.png)
<center class="my_markdown"><b class="my_markdown">图11.21　Ingress模式下访问服务</b></center>

+ 当前“svc1”服务只部署了一个副本，集群中有一条映射规则：“所有访问Ingress网络5000端口的流量都需要路由到运行了“svc1”服务副本的节点之上”。
+ 红线展示了访问Node的15000端口的流量，通过Ingress网络，被路由到了Node2节点正在运行的服务副本之上。

入站流量可能访问4个Swarm节点中的任意一个，但是结果都是一样的，了解这一点很重要。这是因为服务通过Ingress网络实现了Swarm范围内的发布。

此外，还有一点很重要：如果存在多个运行中的副本，流量会平均到每个副本之上，如图11.22中展示的一样。

![75.png](./images/75.png)
<center class="my_markdown"><b class="my_markdown">图11.22　流量平均到每个副本之上</b></center>

