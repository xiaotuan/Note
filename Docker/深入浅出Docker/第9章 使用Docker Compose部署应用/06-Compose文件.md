### 9.2.3　Compose文件

Docker Compose使用YAML文件来定义多服务的应用。YAML是JSON的一个子集，因此也可以使用JSON。不过本章中的例子将全部采用YAML。

Docker Compose默认使用文件名 `docker-compose.yml` 。当然，用户也可以使用 `-f` 参数指定具体文件。

如下是一个简单的Compose文件的示例，它定义了一个包含两个服务（ `web-fe` 和 `redis` ）的小型Flask应用。这是一个能够对访问者进行计数并将其保存到Redis的简单的Web服务。本书中将其命名为 `counter-app` ，并将其作为后续章节的示例应用程序。

```rust
version: "3.5"
services:
  web-fe:
    build: .
    command: python app.py
    ports:
      - target: 5000
        published: 5000
    networks:
      - counter-net
    volumes:
      - type: volume
        source: counter-vol
        target: /code
  redis:
    image: "redis:alpine"
    networks:
      counter-net:
networks:
  counter-net:
volumes:
  counter-vol:
```

在深入研究之前粗略观察文件的基本结构，首先可以注意到，它包含4个一级key： `version` 、 `services` 、 `networks` 、 `volumes` 。

除此之外的其他key，这里暂时不展开讨论。

`version` 是必须指定的，而且总是位于文件的第一行。它定义了Compose文件格式（主要是API）的版本。建议使用最新版本。

注意， `version` 并非定义Docker Compose或Docker引擎的版本号。如果希望了解关于Docker引擎、Docker Compose以及Compose文件之间的版本兼容性信息，请搜索“Compose file versions and upgrading”。

本章中Compose文件将使用版本3及以上的版本。

`services` 用于定义不同的应用服务。上边的例子定义了两个服务：一个名为 `web-fe` 的Web前端服务以及一个名为 `redis` 的内存数据库服务。Docker Compose会将每个服务部署在各自的容器中。

`networks` 用于指引Docker创建新的网络。默认情况下，Docker Compose会创建 `bridge` 网络。这是一种单主机网络，只能够实现同一主机上容器的连接。当然，也可以使用 `driver` 属性来指定不同的网络类型。

下面的代码可以用来创建一个名为 `over-net` 的Overlay网络，允许独立的容器（standalone container）连接（ `attachable` ）到该网络上。

```rust
networks:
  over-net:
  driver: overlay
  attachable: true
```

`volumes` 用于指引Docker来创建新的卷。

##### 分析示例中的Compose文件

上面例子中的 Compose 文件使用的是 v3.5 版本的格式，定义了两个服务，一个名为 `counter-net` 的网络和一个名为 `counter-vol` 的卷。

更多的信息在 `services` 中，下面仔细分析一下。

Compose文件中的 `services` 部分定义了两个二级key： `web-fe` 和 `redis` 。

它们各自定义了一个应用程序服务。需要明确的是，Docker Compose会将每个服务部署为一个容器，并且会使用key作为容器名字的一部分。本例中定义了两个key： `web-fe` 和 `redis` 。因此Docker Compose会部署两个容器，一个容器的名字中会包含 `web-fe` ，而另一个会包含 `redis` 。

`web-fe` 的服务定义中，包含如下指令。

+ `build` ： `.` 指定Docker基于当前目录（ `.` ）下Dockerfile中定义的指令来构建一个新镜像。该镜像会被用于启动该服务的容器。
+ `command` ： `python app.py` 指定Docker在容器中执行名为 `app.py` 的Python脚本作为主程序。因此镜像中必须包含 `app.py` 文件以及Python，这一点在Dockerfile中可以得到满足。
+ `ports` ：指定Docker将容器内（ `-target` ）的5000端口映射到主机（ `published` ）的5000端口。这意味着发送到Docker主机5000端口的流量会被转发到容器的5000端口。容器中的应用监听端口5000。
+ `networks` ：使得Docker可以将服务连接到指定的网络上。这个网络应该是已经存在的，或者是在 `networks` 一级key中定义的网络。对于Overlay网络来说，它还需要定义一个 `attachable` 标志，这样独立的容器才可以连接上它（这时Docker Compose会部署独立的容器而不是Docker服务）。
+ `volumes` ：指定Docker将 `counter-vol` 卷（ `source:` ）挂载到容器内的 `/code` （ `target:` ）。 `counter-vol` 卷应该是已存在的，或者是在文件下方的 `volumes` 一级key中定义的。

综上，Docker Compose会调用Docker来为 `web-fe` 服务部署一个独立的容器。该容器基于与Compose文件位于同一目录下的Dockerfile构建的镜像。基于该镜像启动的容器会运行 `app.py` 作为其主程序，将5000端口暴露给宿主机，连接到 `counter-net` 网络上，并挂载一个卷到 `/code` 。

注：

> 从技术上讲，本例并不需要配置 `command: python app.py` 。因为镜像的Dockerfile 已经将 `python app.py` 定义为了默认的启动程序。但是，本例主要是为了展示其如何执行，因此也可用于覆盖Dockerfile中配置的 `CMD` 指令。

`redis` 服务的定义相对比较简单。

+ `image: redis:alpine` 使得Docker可以基于 `redis:alpine` 镜像启动一个独立的名为 `redis` 的容器。这个镜像会被从Docker Hub上拉取下来。
+ `networks` ：配置 `redis` 容器连接到 `counter-net` 网络。

由于两个服务都连接到 `counter-net` 网络，因此它们可以通过名称解析到对方的地址。了解这一点很重要，本例中上层应用被配置为通过名称与Redis服务通信。

既然理解了Compose文件的工作原理，下面开始部署实战吧！

