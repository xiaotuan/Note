### 技巧86　使用Registrator进行自动化服务注册

到目前为止，Consul（以及任何服务发现工具）最明显的缺点是必须管理服务条目的创建和删除。如果将它集成到应用程序中，将会存在多种实现方案以及多个可能出错的地方。

对于没有完全控制权的应用程序，集成也不起作用，因此在启动数据库之类的应用时最终还得编写包装脚本。

#### 问题

不想在Consul中手动管理服务条目和健康检查。

#### 解决方案

使用Registrator。

本技巧是构建在之前的技巧之上的，并假设有一个两部分的 Consul 集群可用，如前文所描述的那样。我们还假设集群中没有服务，所以可能需要从头开始重新创建容器。

Registrator消除了管理Consul服务的复杂性，它监视容器的启动和停止，根据公开的端口和容器环境变量注册服务。了解该行为的最简单方法便是亲自去试试。

我们所做的一切都将在客户端代理机器上。如前所述，除服务器代理之外，我们不应该在其他机器上运行任何容器。

需要根据以下命令启动Registrator：

```c
$ IMG=gliderlabs/registrator:v6
$ docker pull $IMG
[...]
$ ip addr | grep 'inet ' | grep -v 'lo$\|docker0$'
    inet 192.168.1.80/24 brd 192.168.1.255 scope global wlan0
$ EXTIP=192.168.1.80
$ ip addr | grep docker0 | grep inet
    inet 172.17.42.1/16 scope global docker0
$ BRIDGEIP=172.17.42.1
$ docker run -d --name registrator -h $(hostname)-reg \
-v /var/run/docker.sock:/tmp/docker.sock $IMG -ip $EXTIP -resync \
60 consul://$BRIDGEIP:8500 # if this fails, $EXTIP is an alternative
b3c8a04b9dfaf588e46a255ddf4e35f14a9d51199fc6f39d47340df31b019b90
$ docker logs registrator
2015/08/14 20:05:57 Starting registrator v6 ...
2015/08/14 20:05:57 Forcing host IP to 192.168.1.80
2015/08/14 20:05:58 consul: current leader 192.168.1.87:8300
2015/08/14 20:05:58 Using consul adapter: consul://172.17.42.1:8500
2015/08/14 20:05:58 Listening for Docker events ...
2015/08/14 20:05:58 Syncing services on 2 containers
2015/08/14 20:05:58 ignored: b3c8a04b9dfa no published ports
2015/08/14 20:05:58 ignored: a633e58c66b3 no published ports
```

这里的第一个命令（用于拉动镜像和查找外部IP地址）应该看上去很熟悉。该IP地址会传给Registrator，这样一来它便知道使用哪个IP地址来广播服务。Docker套接字已挂载，以便容器启动和停止时随时自动通知Registrator。我们也告诉了Registrator该如何连接到Consul代理，我们希望所有的容器每60秒刷新一次。容器的变化会自动通知Registrator，因此最终的配置有助于减轻Registrator可能错过更新时带来的影响。

现在Registrator正在运行，注册第一个服务非常简单：

```c
$ curl -sSL 172.17.42.1:8500/v1/catalog/services | python -m json.tool
{
    "consul": []
}
$ docker run -d -e "SERVICE_NAME=files" -p 8000:80 ubuntu:14.04.2 python3 \
 -m http.server 80
3126a8668d7a058333d613f7995954f1919b314705589a9cd8b4e367d4092c9b
$ docker inspect 3126a8668d7a | grep 'Name.*/'
    "Name": "/evil_hopper",
$ curl -sSL 172.17.42.1:8500/v1/catalog/services | python -m json.tool
{
    "consul": [],
    "files": []
}
$ curl -sSL 172.17.42.1:8500/v1/catalog/service/files | python -m json.tool
[
    {
        "Address": "192.168.1.80",
        "Node": "mylaptop2",
        "ServiceAddress": "192.168.1.80",
        "ServiceID": "mylaptop2-reg:evil_hopper:80",
        "ServiceName": "files",
        "ServicePort": 8000,
        "ServiceTags": null
    }
]
```

在注册服务时，要做的唯一一件事情便是传递一个环境变量给Registrator，告诉它要使用的服务的名称。在默认情况下，Registrator使用的名称基于斜杠之后和标签之前的容器名称组件，mycorp.com/myteam/myimage:0.5 的名称为 myimage。用户可以使用该命名约定，也可以根据自己的命名约定手动指定名称。

其余的值也正如预期的那样。Registrator已经发现正在侦听的端口，将其添加到Consul，并为之配置了一个服务ID，用于指示哪里可以找到容器。（这就是为什么主机名配置在了Registrator容器里。）

#### 讨论

如果在不断变化的环境中拥有一大波容器，那么Registrator会表现得很优秀，它可以确保用户不必再担心创建服务时是否创建好了健康检查的问题。

如果环境里有其他的详细信息，Registrator也会获取一些信息，包括标签、每个端口的服务名称（如果有多个）以及所使用的健康检查（如果使用Consul作为数据存储）。可以在JSON中指定环境中检查的细节来启用所有3种类型的Consul健康检查。读者可以重读一下技巧85来获取对Consul健康检查本身的简单介绍。

