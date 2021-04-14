### 技巧28　ONBUILD指令和golang

`ONBUILD` 指令可能会给一些Docker新手带来很多困惑。本技巧会通过一个两行代码的Dockerfile构建和运行一个Go应用，演示该指令在真实环境中的使用。

#### 问题

用户想要减少构建一个应用镜像所需的步骤。

#### 解决方案

使用 `ONBUILD` 指令自动化及封装一个镜像的构建。用户首先将完成整个过程，然后我们再来解释这中间发生了什么。我们将要用到的示例是outyet项目，这是golang GitHub仓库里的一个例子。它所做的就是建立一个Web服务，然后返回一个页面，告诉用户Go 1.4是否已经可用。

按照代码清单4-29所示的方式构建镜像。

代码清单4-29　构建outyet镜像

```c
 $ git clone https://github.com/golang/example　　⇽---　克隆Git仓库
 $ cd example/outyet　　⇽---　切换到outyet目录
 $ docker build -t outyet . 　　⇽---　构建outyet镜像
```

基于生成的镜像运行一个容器，然后检索该容器提供的网页，如代码清单4-30所示。

代码清单4-30　运行并验证outyet镜像

```c
$ docker run　　⇽---　--publish标志告诉Docker将容器的8080端口映射到宿主机的8080端口
➥ --publish 8080:8080　　⇽---　--name标志为容器提供了一个可预测的名称，使其更易于使用
➥ --name outyet1 -d outyet　　⇽---　以后台模式运行容器
$ curl localhost:8080　　⇽---　调用curl访问容器端口服务获取输出
 <!DOCTYPE html><html><body><center>　　⇽---　
     <h2>Is Go 1.4 out yet?</h2>
     <h1>
         <a href="https://go.googlesource.com/go/+/go1.4">YES!</a>
     </h1>
 </center></body></html>　　⇽---　容器提供的网站内容
```

就是这样—— 一个简单的应用程序，它会返回一个网页，告诉用户Go 1.4是否可用。

如果仔细看一下克隆下来的仓库，不难发现它的Dockerfile只有两行代码（见代码清单4-31）！

代码清单4-31　outyet的Dockerfile

```c
 FROM golang:onbuild　　⇽---　基于golang:onbuild镜像开始构建
 EXPOSE 8080　　⇽---　对外公开8080端口
```

有点儿困惑，对吧？没事，看看 `golang:onbuild` 镜像的Dockerfile，它可能更有意义，如代码清单4-32所示。

代码清单4-32　golang:onbuild 的Dockerfile

```c
 FROM golang:1.7　　⇽---　使用golang:1.7作为基础镜像
 RUN mkdir -p /go/src/app　　⇽---　创建一个存放应用程序的目录
 WORKDIR /go/src/app　　⇽---　挪到该目录下
 CMD ["go-wrapper", "run"]　　⇽---　将生成的镜像的执行命令设置为调用go-wrapper来运行go应用
 ONBUILD COPY . /go/src/app　　⇽---　第一个ONBUILD指令将Dockerfile上下文的代码拷贝到镜像里
 ONBUILD RUN go-wrapper download　　⇽---　第二个ONBUILD指令再次使用go-wrapper指令下载任意的软件依赖
 ONBUILD RUN go-wrapper install　　⇽---　第三个ONBUILD指令
```

`golang:onbuild` 镜像定义了在任何其他Dockerfile里的 `FROM` 指令引用该镜像时会发生什么。结果便是当一个Dockerfile使用此镜像作为基础镜像时， `ONBUILD` 指令将会在 `FROM` 的镜像下载完成后立即触发，并且（如果没有被覆盖）将生成的镜像作为容器运行时， `CMD` 命令将会被执行。

现在，下面代码里的 `dockerbuild` 命令的输出内容可能更有意义。

```c
 Step 1 : FROM golang:onbuild　　⇽---　
  onbuild: Pulling from library/golang
  6d827a3ef358: Pull complete
  2726297beaf1: Pull complete
  7d27bd3d7fec: Pull complete
  62ace0d726fe: Pull complete
  af8d7704cf0d: Pull complete
  6d8851391f39: Pull complete
  988b98d9451c: Pull complete
  5bbc96f59ddc: Pull complete
  Digest: sha256:
➥ 886a63b8de95d5767e779dee4ce5ce3c0437fa48524aedd93199fb12526f15e0
 Status: Downloaded newer image for golang:onbuild　　⇽---　执行FROM指令，拉取的镜像正是golang:onbuild
 # Executing 3 build triggers... 　　⇽---　 Docker构建程序表明它想要执行ONBUILD指令的意图
 Step 1 : COPY . /go/src/app　　⇽---　第一条ONBUILD指令将Dockerfile上下文里的Go代码拷贝到构建目录
 Step 1 : RUN go-wrapper download　　⇽---　在下载完成后，第二条ONBUILD指令被触发
  ---> Running in c51f9b0c4da8
+ exec go get -v -d　　⇽---　调用go-wrapper触发一个shell命令调用go get
 Step 1 : RUN go-wrapper install　　⇽---　触发第三条ONBUILD指令，它将会去安装应用程序
  ---> Running in adaa8f561320
+ exec go install -v　　⇽---　调用go-wrapper触发一个shell命令调用go install
 app
  ---> 6bdbbeb8360f
 Removing intermediate container 47c446aa70e3　　⇽---　
 Removing intermediate container c51f9b0c4da8
 Removing intermediate container adaa8f561320　　⇽---　删除3个因为ONBUILD指令构建产生的中间容器
 Step 2 : EXPOSE 8080　　⇽---　执行Dockerfile里面第二行的EXPOSE指令
  ---> Running in 564d4a34a34b
  ---> 5bf1767318e5
 Removing intermediate container 564d4a34a34b
 Successfully built 5bf1767318e5
```

本技巧的结果就是让用户可以轻松地构建一个只包含运行它所需的代码的镜像，而无须其他太多的冗余内容。把构建工具留在镜像里不仅会让镜像变得比原来更大，还增加了运行容器的安全攻击范围。

#### 讨论

由于Docker和Go是目前常见的流行技术，因此我们用它来演示如何使用 `ONBUILD` 构建Go应用的二进制文件。

市面上也存在一些其他的有关 `ONBUILD` 的例子。比如在Docker Hub上可以找到 `node:onbuild` 以及 `python:onbuild` 这些镜像。

这也许可以激发用户的灵感去构建自己的 `ONBUILD` 镜像，从而帮助用户所在的组织建立一套通用的构建模式。这种标准化有助于进一步减少不同团队之间的对抗和不匹配。

