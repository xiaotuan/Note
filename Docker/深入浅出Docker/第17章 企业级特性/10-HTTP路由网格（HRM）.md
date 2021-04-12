### 17.2.7　HTTP路由网格（HRM）

Docker Swarm内置有四层路由网格的功能，称为Swarm路由网格（Swarm Routing Mesh）。这一功能可以使Swarm服务暴露给集群中的所有节点，并且能够在服务的各个副本之间实现对入站流量的负载均衡。其效果就是可以基本实现流量均衡到达服务的所有副本。不过，该负载均衡并不作用于应用层。例如，它无法根据HTTP头部数据进行七层路由。为了弥补这一点，UCP实现了七层路由网格，称为HTTP路由网格（HTTP Routing Mesh，HRM）。这一功能以Swarm路由网格为基础。

HRM使得多个Swarm服务可以发布在同一个Swarm端口上，并根据HTTP请求头中的主机名将流量路由到正确的服务中。

图17.20展示的是包含两个服务的简单示例。

![142.png](./images/142.png)
<center class="my_markdown"><b class="my_markdown">图17.20　包含两个服务的HRM操作</b></center>

在图17.20中，笔记本客户端向 `mustang.internal` 的80端口发出了一个HTTP请求。UCP集群中有两个监听80端口的服务。 `mustang` 服务在80端口监听发送给 `mustang.internal` 主机的流量。 `camero` 服务也监听80端口，不过它被配置为接收到达 `camero.internal` 的流量。

其实还有第三个称为 `HRM` 的服务，用来维护主机名与UCP服务之间的映射关系。HRM会接收所有到达80端口的流量，查看HTTP请求头，并决定将其路由到哪个服务。

下面举例予以说明，并对一些细节进行解释。

这里就采用图17.20所示的例子。过程为首先开启HRM的80端口。接着使用 `nigelpoulton/dockerbook:mustang` 镜像部署一个名为“mustang”的服务，并为该服务创建一个主机路由，从而所有对“mustang.internal”的请求都会被路由到该服务。然后使用 `nigelpoulton/dockerbook:camero` 镜像创建一个名为“camero”的服务，并为该服务创建一个主机路由，实现该服务与“mustang.internal”的映射。

读者也可以使用可解析的DNS域名，比如“mustang.mycompany.com”，只需要配置好域名解析，使得所有发向这些地址的请求都能够解析到UCP集群前的负载均衡器即可。如果没有负载均衡器，那么可以将流量指向集群中任一个节点的IP。下面具体操作一下。

（1）登录到UCP Web界面。

（2）进入 `Admin > Admin Settings > Routing Mesh` （路由网格）。

（3）勾选 `Enable Routing Mesh` （启用路由网格）复选框，确保 `HTTP Port` 配置为 `80` 。

（4）单击 `Save` 。

这样就完成了UCP集群开启HRM的配置。这一操作，其底层会部署一个名为 `ucp-hrm` 的系统服务，以及一个名为ucp-hrm的覆盖网络。

如果查看 `ucp-hrm` 系统服务，会发现它是以入站模式（Ingress Mode）发布在 `80` 端口的。也就是说 `ucp-hrm` 是部署在集群上的，并且会在集群中的所有节点上绑定 `80` 端口。因此，到达集群 `80` 端口的 **所有流量** 都会被该服务处理。当 `Mustang` 和 `Camero` 服务部署之后， `ucp-hrm` 服务的主机映射会被更新，它也就知道如何来进行流量的路由。

现在HRM已经部署好了，下面部署服务。

（1）选择左侧导航栏中的 `Services` ，并单击 `Create Service` 。

（2）按照如下步骤部署“mustang”。

+ **Details/Name** : mustang。
+ **Details/Image** : nigelpoulton/dockerbook:mustang。
+ **Network/Ports/Publish Port** : 单击 `Publish Port +` 选项。
+ **Network/Ports/Internal Port** : 8080。
+ **Network/Ports/Add Hostname Based Routes** : 单击选项添加一个基于主机名的路由。
+ **Network/Ports/External Scheme** : Http://。
+ **Network/Ports/Routing Mesh Host** : mustang.internal。
+ **Network/Ports/Networks** : 确保服务接入ucp-hrm网络。

（3）单击Create来部署服务。

（4）部署“camero”服务。

部署该服务的过程与部署“mustang”服务类似，不同之处来自于以下几点。

+ **Details/Name** : camero。
+ **Details/Image** : nigelpoulton/dockerbook:camero。
+ **Network/Ports/Routing Mesh Host** : camero.internal。

（5）单击Create。

每个服务的部署会花费几秒时间，一旦完成，就可以在网页浏览器中进行测试了，输入 `mustang.internal` 可以访问Mustang服务（见图17.21），而 `camero.internal` 可以访问camero服务。

注：

> 为了使 `mustang.internal` 和 `camero.internal` 能够被解析到UCP集群，读者显然需要进行域名解析的配置。解析的地址即为集群前的一个负载均衡器，从而可以将流量转发到集群的80端口。不过如果读者手中为测试环境，并没有负载均衡器，则可以通过编辑 `hosts` 文件的方式，配置域名到集群中某个节点IP的映射。

下面回顾一下其工作过程。

HTTP路由网格是运行于Swarm路由网格传输层基础之上的一个Docker UCP特性。具体来说，HRM增加了基于主机名规则的应用层路由。

![143.png](./images/143.png)
<center class="my_markdown"><b class="my_markdown">图17.21　访问mustang服务</b></center>

启用HRM的时候会部署一个名为 `ucp-hrm` 的UCP系统服务。该服务是Swarm范围的，监听80或443端口。这意味着所有到达集群这两个端口之一的流量都会被发送到 `ucp-hrm` 服务。而 `ucp-hrm` 服务会接收、解析，并路由所有到达集群中的流量。

到此已经完成了两个用户服务的部署。在部署服务时，需要创建基于主机名的映射，该映射会被加入 `ucp-hrm` 服务。“mustang”服务创建的映射，使得它能够收到所有到达80端口的，HTTP头指向“mustang.internal”的流量。“camero”服务与之类似，接收所有到达80端口的，HTTP头指向“camero.internal”的流量。总体来说， `ucp-hrm` 服务将完成如下两个任务。

+ 所有发往“mustang.internal”的80端口的流量都会被转发至“mustang”服务。
+ 所有发往“camero.internal”的80端口的流量都会被转发至“camero”服务。

让我们再次回顾图17.20。希望到此已经解释清楚了！

