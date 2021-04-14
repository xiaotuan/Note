### 技巧66　在一个Docker容器里运行Jenkins主服务器

将 Jenkins 主服务器放到一个容器里不像从节点那样有很多好处（见技巧67），不过确实可以带来Docker的不可变镜像的常规优势。我们发现，能对有效的主服务器配置和插件进行提交，可以极大地减轻实验负担。

#### 问题

想要一个可移植的Jenkins服务器。

#### 解决方案

使用官方的Jenkins Docker镜像来运行服务器。

相比直接在宿主机上安装，在一个Docker容器里运行Jenkins具有一定的优势。办公室里时常出现这样的叫喊：“不要动我的Jenkins服务器配置！”甚至是更糟的：“谁动了我的Jenkins服务器？”对正在运行的容器执行 `docker export` 可以克隆出Jenkins服务器的状态，以此进行升级和修改尝试将有助于消除这些抱怨。同样，备份和移植也变得更加容易。

在本技巧中，将采用官方的Jenkins Docker镜像并做一些修改，以满足后续一些技巧对访问Docker套接字的需要，例如，在Jenkins里进行Docker构建。



**注意**

本书中与Jenkins相关的示例都可以在GitHub中找到，地址是https://github.com/docker-in- practice/jenkins.git。





**注意**

该Jenkins镜像及其 `run` 命令在本书与Jenkins相关的技巧中都将作为服务器来使用。



##### 1．构建服务器

首先准备一个所需的服务器插件清单，并将其放置在一个名为jenkins_plugins.txt的文件中：

```c
swarm:3.4
```

这个简短的清单包括了Jenkins Swarm插件（与Docker Swarm无关），这个插件在后续技巧中将会用到。

代码清单8-11展示的是构建Jenkins服务器的Dockerfile。

代码清单8-11　Jenkins服务器构建

```c
FROM jenkins　　⇽---　使用官方的 Jenkins镜像作为基础
COPY jenkins_plugins.txt /tmp/jenkins_plugins.txt　　⇽---　复制要安装的插件清单
RUN /usr/local/bin/plugins.sh /tmp/jenkins_plugins.txt　　⇽---　将插件安装到服务器中
USER root　　⇽---　
RUN rm /tmp/jenkins_plugins.txt　　⇽---　切换到 root 用户并删除插件文件
RUN groupadd -g 999 docker　　⇽---　
RUN addgroup -a jenkins docker　　⇽---　使用与宿主机相同的用户组 ID 将Docker组添加到容器中（此数字可能与读者的有所不同）
USER jenkins　　⇽---　切换回容器里的Jenkins用户
```

这里没有 `CMD` 或 `ENTRYPOINT` 指令，是因为要继承官方Jenkins镜像中定义的启动命令。

读者的宿主机上的Docker的用户组ID可能会不一样。要想查看这个ID，可执行下面这条命令来查看本地用户组ID：

```c
$ grep -w ^docker /etc/group
docker:x:999:imiell
```

如果这个值不是999，则使用相应值来替换它。



**警告**

如果打算在 Jenkins Docker 容器中运行 Docker，Jenkins 服务器环境及Jenkins从节点环境中的用户组ID必须一致。在迁移服务器时还可能会出现移植问题（读者应该已经在原生服务器安装中遇到过同样的问题）。环境变量本身在这里无法起作用，因为用户组是在构建期设置的，无法进行动态配置。



执行下面这条命令来构建这个场景中的镜像：

```c
docker build -t jenkins_server .
```

##### 2．运行服务器

现在可以使用这个命令在Docker下运行服务器：

```c
docker run --name jenkins_server -p 8080:8080 \　　⇽---　将Jenkins服务器端口映射到宿主机的8080端口上
 -p 50000:50000 \　　⇽---　如果想附加构建从节点服务器，容器的50000端口需要打开
 -v /var/run/docker.sock:/var/run/docker.sock \　　⇽---　挂载Docker套接字，以便能在容器里与Docker守护进程互动
 -v /tmp:/var/jenkins_home \　　⇽---　将 Jenkins 应用程序数据挂载到宿主机的/tmp上，这样就不会出现文件权限错误。如果要投入实际使用，可将其挂载到一个任何人都可写的目录上
 -d \　　⇽---　以守护进程来运行该服务器
 jenkins_server
```

如果访问http://localhost:8080，你将看到Jenkins配置界面——按照链接的流程，可能会需要使用 `docker exec` （在技巧12中说明）获取第一步提示输入的密码。

一旦完成，Jenkins服务器就准备好了，并安装了相应插件（安装的插件取决于在设置过程中你所选择的选项）。要确认这一点，打开Manage Jenkins（系统管理）> Manage Plugins（管理插件）> Installed（已安装），查找Swarm即可验证它已经安装好了。

#### 讨论

可以看到，我们像技巧45那样将Docker套接字挂载到这个Jenkins主服务器中，以此提供对Docker守护进程的访问权限。这让你可以通过在宿主机上运行容器使用内建的主从节点执行Docker构建。



**注意**

本技巧及其相关内容的代码可从GitHub获取，地址是 https://github.com/docker-in-practice/ jenkins。



