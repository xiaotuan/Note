### 7.2.10　Web服务器示例

到目前为止，已经介绍了如何启动一个简单的容器，并与其进行交互。同时也知道了如何停止、重启以及删除一个容器。现在来看一个Linux Web服务器示例。

在该示例中，会使用到我用于Pluralsight视频教程网站中的一个镜像。这个镜像会在8080端口启动一个相当简单的Web服务。

使用 `docker container stop` 以及 `docker container rm` 命令清理当前系统中的全部容器，然后运行下面的 `docker container run` 命令。

```rust
$ docker container run -d --name webserver -p 80:8080 \
  nigelpoulton/pluralsight-docker-ci
Unable to find image 'nigelpoulton/pluralsight-docker-ci:latest' locally
latest: Pulling from nigelpoulton/pluralsight-docker-ci
a3ed95caeb02: Pull complete
3b231ed5aa2f:  Pull complete
7e4f9cd54d46:  Pull complete
929432235e51:  Pull complete
6899ef41c594:  Pull complete
0b38fccd0dab:  Pull complete
Digest: sha256:7a6b0125fe7893e70dc63b2...9b12a28e2c38bd8d3d
Status: Downloaded newer image for nigelpoulton/plur...docker-ci:latest
6efa1838cd51b92a4817e0e7483d103bf72a7ba7ffb5855080128d85043fef21
```

注意，当前Shell提示符并未发生变化。这是因为使用了 `-d` 参数启动容器，并在后台运行。这种后台启动的方式不会将当前终端连接到容器当中。

该示例在 `docker container run` 命令中抛出了一些额外的参数，一起来快速了解一下。

已经知道 `docker container run` 会启动一个新容器，但是这次使用 `-d` 参数替换了 `-it` 。 `-d` 表示后台模式，告知容器在后台运行。

然后为容器命名，并且指定了 `-p 80:8080` 。 `-p` 参数将Docker主机的端口映射到容器内。本例中，将Docker主机的80端口映射到了容器内的8080端口。这意味着当有流量访问主机的80端口的时候，流量会直接映射到容器内的8080端口。之所以如此是因为当前使用的镜像，其Web服务监听了8080端口。这意味着容器启动时会运行一个Web服务，监听8080端口。

最终，命令中还指定Docker所使用的镜像： `nigelpoulton/pluralsight-docker-ci` 。这个镜像不一定保持更新，并且可能存在缺陷。

使用 `docker container ls` 命令可以查看当前运行的容器以及端口的映射情况。端口信息按照 `host-port:container-port` 的格式显示，明确这一点很重要。

```rust
$ docker container ls
CONTAINER ID  COMMAND         STATUS       PORTS               NAMES
6efa1838cd51  /bin/sh -c...   Up 2 mins  0.0.0.0:80->8080/tcp  webserver
```

注：

> 为了提高可读性，上面输出中的部分列并未展示。

现在容器已经运行，端口也映射成功，可以通过浏览器来访问该容器，需要在浏览器中指定 **Docker主机** 的IP地址或DNS名称，端口号是80。图7.4展示了由容器服务提供的网页。

![35.png](./images/35.png)
<center class="my_markdown"><b class="my_markdown">图7.4　由容器服务提供的网页</b></center>

`docker container stop` 、 `docker container pause` 、 `docker container start` 和 `docker container rm` 命令同样适用于容器。同时，持久性的规则也适用于容器——停止或暂停容器并不会导致容器销毁，或者内部存储的数据丢失。

