### 技巧92　使用Marathon细粒度管理Mesos

现在读者应该已经意识到了，使用Mesos需要考虑很多细节，即便是对一个极其简单的框架也是如此。能够信赖被正确部署的应用程序这一点非常重要——框架中的bug造成的影响可能会导致部署新应用程序失败，也可能会导致整个服务中断。

随着集群规模的扩展，风险也在上升，除非团队擅长编写可靠的动态部署代码，否则可能需要考虑更多经过验证的方法——Mesos自身是很稳定的，但内部定制的框架可能不是人们想象的那么可靠。

Marathon适用于那些没有内部部署工具开发经验但需要一个良好支持而且易于使用的方案，以便在有些动态的环境中部署容器的公司。

#### 问题

需要一种可靠的方式来利用Mesos的力量，而不会陷入编写自己的框架的困扰。

#### 解决方案

使用Marathon——在Mesos之上的一层，提供更简单的接口，以更快地获得生产力。

Marathon是一款Apache Mesos框架，它是由Mesosphere构建的，用于管理长期运行的应用程序。市场资料将其描述为数据中心（Mesos是其核心）的 `init` 或 `upstart` 守护进程。这个比喻并非没有道理。

Marathon可以让用户启动一个包含了Mesos主节点、Mesos从节点和Marathon自身的单个容器，从而简单快速地上手。这对于演示很有用，但不适用于生产环境下的Marathon部署。要配置一个真实环境的Marathon，用户需要一个Mesos主节点和从节点（出自技巧91）以及一个Zookeeper实例（出自技巧84）。确保这些都在运行之后，我们将开始运行Marathon容器：

```c
$ docker inspect -f '{{.NetworkSettings.IPAddress}}' mesmaster
172.17.0.2
$ docker inspect -f '{{.NetworkSettings.IPAddress}}' messlave
172.17.0.3
$ docker inspect -f '{{.NetworkSettings.IPAddress}}' zookeeper
172.17.0.4
$ docker pull mesosphere/marathon:v0.8.2
[...]
$ docker run -d -h $(hostname) --name marathon -p 8080:8080 \
mesosphere/marathon:v0.8.2 --master 172.17.0.2:5050 --local_port_min 8000 \
--local_port_max 8100 --zk zk://172.17.0.4:2181/marathon
accd6de46cfab65572539ccffa5c2303009be7ec7dbfb49e3ab8f447453f2b93
$ docker logs -f marathon
MESOS_NATIVE_JAVA_LIBRARY is not set. Searching in /usr/lib /usr/local/lib.
MESOS_NATIVE_LIBRARY, MESOS_NATIVE_JAVA_LIBRARY set to >
'/usr/lib/libmesos.so'
[2015-06-23 19:42:14,836] INFO Starting Marathon 0.8.2 >
(mesosphere.marathon.Main$:87)
[2015-06-23 19:42:16,270] INFO Connecting to Zookeeper... >
(mesosphere.marathon.Main$:37)
[...]
[2015-06-30 18:20:07,971] INFO started processing 1 offers, >
launching at most 1 tasks per offer and 1000 tasks in total
➥ (mesosphere.marathon.tasks.IterativeOfferMatcher$:124)
[2015-06-30 18:20:07,972] INFO Launched 0 tasks on 0 offers, >
declining 1 (mesosphere.marathon.tasks.IterativeOfferMatcher$:216)
```

就像Mesos一样，Marathon非常啰唆，不过（也像Mesos）它也会很快停下来。此刻，我们将从编写自己的框架进入一个很熟悉的环节——考虑资源供应并决定用这些资源做些什么。因为还没有启动任何东西，所以自从前面的日志的 `declining 1` 后我们便看不到任何活动。

Marathon有一个漂亮的Web界面，这也是要在宿主机上公开8080端口——在浏览器中访问http://localhost:8080端口来打开页面的原因。

我们直接切换到Marathon的具体操作部分，先创建一个新的应用程序。这里有一些术语要澄清一下——在Marathon的世界里“应用程序”（app）是拥有完全相同定义的一个或多个任务的集合。

点击右上角的“New App”（新建应用程序）按钮，会弹出一个对话框，可以用它来定义要启动的应用程序。我们将继续沿用自己创建的框架，设置ID为“marathon-nc”，设置CPU、内存和磁盘空间为默认值（以符合mesos-nc框架的资源限制），并且设置启动命令为 `echo "hello $MESOS_TASK_ID" | nc -l $PORT0` （使用该任务可用的环境变量，注意就是数字0）。将端口字段值设置为8000，指定我们想要监听的位置。随即，跳过其他的字段设置。点击“Create”（创建）按钮。

用户新定义的应用程序现在将显示在Web界面上。状态会先简要显示为“Deploying”，然后变为“Running”。应用程序现在已经启动了！

如果点击应用程序列表中的“/marathon-nc”条目，将会看到该应用程序的唯一ID。通过REST API可以得到完整的配置，如下面的代码所示，也可以通过对Mesos从节点容器对应的端口执行 `curl` 命令来验证它在运行。用户需要确保保存了REST API返回的完整的配置，因为稍后会派上用场——它被保存在下面例子中的app.json中：

```c
$ curl http://localhost:8080/v2/apps/marathon-nc/versions
{"versions":["2015-06-30T19:52:44.649Z"]}
$ curl -s \
http://localhost:8080/v2/apps/marathon-nc/versions/2015-06-30T19:52:44.649Z \
> app.json
$ cat app.json
{"id":"/marathon-nc", >
"cmd":"echo \"hello $MESOS_TASK_ID\" | nc -l $PORT0",[...]
$ curl http://172.17.0.3:8000
hello marathon-nc.f56f140e-19e9-11e5-a44d-0242ac110012
```

留意一下对应用程序执行 `curl` 命令的输出结果中 `hello` 后面的文本——它应该和界面中的唯一ID是匹配的。检查要快速，因为执行 `curl` 命令会终止该应用程序，Marathon会重新启动它，界面中的唯一ID会改变。一旦验证了这些，继续点击“Destroy App”（销毁应用程序）按钮来删除 `marathon-nc` 。

一切工作正常，但是读者可能已经注意到，我们没有达成使用Marathon的目的——编排Docker容器。尽管应用程序在容器中，但它在Mesos从节点容器中启动，而不是在自己的容器中启动。阅读Marathon文档说明，在Docker容器中创建任务还需要做更多的配置（就像编写自己的框架时一样）。

幸好，之前启动的Mesos从节点都有所需的设置，所以只需要修改一些Marathon选项——特别是应用程序方面的选项。通过获取之前Marathon API的响应信息（存放在app.json中），我们可以专注于添加Marathon的设置信息，从而启用Docker。我们将使用 `jq` 工具执行操作，尽管通过文本编辑器来做也同样简单：

```c
$ JQ=https://github.com/stedolan/jq/releases/download/jq-1.3/jq-linux-x86_64
$ curl -Os $JQ && mv jq-linux-x86_64 jq && chmod +x jq
$ cat >container.json <<EOF
{
  "container": {
    "type": "DOCKER",
    "docker": {
      "image": "ubuntu:14.04.2",
      "network": "BRIDGE",
      "portMappings": [{"hostPort": 8000, "containerPort": 8000}]
    }
  }
}
$ # merge the app and container details
$ cat app.json container.json | ./jq -s add > newapp.json
```

现在，我们可以将新的应用程序定义发送给API，然后见证Marathon启动它：

```c
$ curl -X POST -H 'Content-Type: application/json; charset=utf-8' \
--data-binary @newapp.json http://localhost:8080/v2/apps
{"id":"/marathon-nc", >
"cmd":"echo \"hello $MESOS_TASK_ID\" | nc -l $PORT0",[...]
$ sleep 10
$ docker ps --since=marathon
CONTAINER ID  IMAGE         COMMAND              CREATED              >
STATUS             PORTS                   NAMES
284ced88246c  ubuntu:14.04  "\"/bin/sh -c 'echo  About a minute ago   >
Up About a minute  0.0.0.0:8000->8000/tcp  mesos- >
1da85151-59c0-4469-9c50-2bfc34f1a987
$ curl localhost:8000
hello mesos-nc.675b2dc9-1f88-11e5-bc4d-0242ac11000e
$ docker ps --since=marathon
CONTAINER ID  IMAGE         COMMAND              CREATED         >
STATUS                     PORTS                   NAMES
851279a9292f  ubuntu:14.04  "\"/bin/sh -c 'echo  44 seconds ago  >
Up 43 seconds              0.0.0.0:8000->8000/tcp  mesos- >
37d84e5e-3908-405b-aa04-9524b59ba4f6
284ced88246c  ubuntu:14.04  "\"/bin/sh -c 'echo  24 minutes ago   >
Exited (0) 45 seconds ago                          mesos-1da85151-59c0-
➥ 4469-9c50-2bfc34f1a987
```

和我们在技巧91中的自定义框架一样，Mesos 已经启动了一个Docker容器，应用程序就运行在里面。执行 `curl` 命令会终止应用程序和容器，然后自动启动一个新的容器。

#### 讨论

技巧91中的自定义框架与Marathon框架之间有一些显著的差异。例如，在那个自定义框架里，我们可以对资源供给的接受进行非常细粒度的控制，我们可以选定单个要监听的端口。为了在Marathon中也能做类似的事情，则需要给每一个从节点强加一些额外的设置。

相比之下，Marathon拥有很多内置的功能，包括健康检查、事件通知系统和REST API。这并不是微不足道的实现细节，使用Marathon可以确保的一点是在操作它时你并不是第一个吃螃蟹的人。如果没有别的需求，获取Marathon的支持比定制框架要容易得多。我们发现Marathon的文档比Mesos的文档更加通俗易懂。

我们已经介绍了设置和使用Marathon的一些基础知识，但是这里面还有更多的事情要做。我们看到的更有趣的一个建议便是使Marathon启动其他的Mesos框架，可能包括你自己的定制框架！我们鼓励读者去积极探索——Mesos是一个专注于编排领域的高品质工具，而Marathon在其上提供了一个可用的应用层。

