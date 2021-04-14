### 技巧82　使用systemd管理宿主机上的容器

在本技巧中，我们将使用systemd配置一个简单的Docker服务。如果读者熟悉systemd，跟进本章内容将会相对容易些，但我们假设读者之前对此工具并不了解。

对于一个拥有运维团队的成熟公司来说，使用systemd控制Docker是很有用的，因为他们更喜欢沿用自己已经了解并且已经工具化的经过生产验证的技术。

#### 问题

想要管理宿主机上Docker容器服务的运行。

#### 解决方案

使用systemd管理容器服务。

systemd是一个系统管理的守护进程，它在前段时间取代了Fedora的SysV init脚本。它可以通过独立“单元”的形式管理系统上的所有服务——从挂载点到进程，甚至到一次性脚本。它在被推广到其他发行版和操作系统后变得愈加受欢迎，虽然在一些系统上安装和启用它可能还有问题（编写本书时Gentoo就是一个例子）。设置systemd时，别人使用systemd过程中遇到类似问题的处理经验值得借鉴。

在本技巧里，我们将通过运行第1章中的to-do应用程序来演示如何使用systemd管理容器的启动。

##### 1. 安装systemd

如果用户的宿主机系统上还没有安装systemd（可以通过执行 `systemctl status` 命令来检查，查看是否能得到正确的响应），可以使用标准包管理工具将其直接安装到宿主机的操作系统上。

如果不太习惯以这种方式与宿主机系统交互，推荐使用Vagrant来部署一个已经安装好systemd的虚拟机，如代码清单11-1所示。这里我们只做简要介绍，有关安装Vagrant的更多建议参见附录C。

代码清单11-1　设置Vagrant

```c
$ mkdir centos7_docker　　⇽---　
$ cd centos7_docker　　⇽---　创建并进入一个新的目录
$ vagrant init jdiprizio/centos-docker-io　　⇽---　将目录初始化成一个Vagrant环境，指定Vagrant镜像
$ vagrant up) 　　⇽---　启动虚拟机
$ vagrant ssh　　⇽---　采用SSH的方式登入虚拟机
```



**注意**

在编写本书时，jdiprizio/centos-docker-io是一个合适并可用的虚拟机镜像。如果读者阅读本书时发现它已经失效，可以使用另一个镜像名称来替换代码清单11-1中的这一字符串。读者可以在HashiCorp的“Discover Vagrant Boxes”页面上搜索一个镜像（box是一个Vagrant用来指代虚拟机镜像的术语）。要查找该镜像，我们可以搜索“docker centos”。在启动新的虚拟机之前，读者可能需要查看 `vagrant box add` 命令行的帮助文档，了解如何下载该虚拟机。



##### 2．用systemd设置一个简单的Docker应用程序

现在机器上安装好了systemd和Docker，接下来将使用该机器运行第1章中讲到的to-do应用程序。

systemd通过读取INI格式的配置文件来工作。



**提示**

INI文件是一种简单的文本文件，其基本结构由节、属性和值组成。



首先需要以root身份创建一个服务文件/etc/systemd/system/todo.service，如代码清单11-2所示。在这个文件里告诉systemd在宿主机的8000端口上运行一个名为“todo”的Docker容器。

代码清单11-2　/etc/systemd/system/todo.service

```c
[Unit] 　　⇽---　 Unit小节定义了systemd对象的通用信息
 Description=Simple ToDo Application
 After=docker.service　　⇽---　 Docker服务启动之后立即启动这个单元
 Requires=docker.service　　⇽---　该单元成功运行的前提是运行Docker服务
[Service] 　　⇽---　 Service小节定义了与systemd服务单元类型相关的配置信息
 Restart=always　　⇽---　如果服务终止了，总是重启它
 ExecStartPre=/bin/bash \
 -c '/usr/bin/docker rm -f todo || /bin/true'　　⇽---　 ExecStartPre定义了一个命令。该命令会在该单元启动前执行。要确保启动该单元前容器已经删掉，可以在这里删除它
 ExecStartPre=/usr/bin/docker pull dockerinpractice/todo　　⇽---　确保运行容器之前已经下载了该镜像
 ExecStart=/usr/bin/docker run --name todo \
 -p 8000:8000 dockerinpractice/todo　　⇽---　 ExecStart定义了服务启动时要执行的命令
 ExecStop=/usr/bin/docker rm -f todo　　⇽---　 ExecStop定义了服务停止时要执行的命令
[Install] 　　⇽---　 Install 小节包含了启用该单元时systemd所需的信息
 WantedBy=multi-user.target　　⇽---　告知systemd当进入多用户目标环境的时候希望启动该服务单元
```

从该配置文件可以非常清楚地看出，systemd为进程的管理提供了一种简单的声明式模式，将依赖管理的细节交给systemd服务去处理。但这并不意味着用户可以忽视这些细节，只是它确实为用户提供了很多方便的工具来管理Docker（和其他）进程。



**注意**

默认情况下，Docker不会设置任何重启策略，但值得注意的是，一旦有所设置，它都会和大多数的进程管理器冲突。因此，如果使用了进程管理器就不要设置重启策略。



启动一个新的服务单元即是调用 `systemctl enable` 命令。如果希望系统启动的时候该服务单元能够自动启动，也可以在systemd的multi-user.target.wants目录下创建一个符号链接。一旦完成，就可以使用 `systemctl start` 来启动该单元了：

```c
$ systemctl enable /etc/systemd/system/todo.service
$ ln -s '/etc/systemd/system/todo.service' \
'/etc/systemd/system/multi-user.target.wants/todo.service'
$ systemctl start todo.service
```

然后只要等它启动。如果出现问题会有相应的提示。

可以使用 `systemctl status` 命令来检查是否一切正常。它会打印一些关于该服务单元的通用信息，如进程运行的时间以及相应的进程 ID，紧随其后的是该进程的日志信息。通过以下例子可以看出Swarm服务器在8000端口下正常启动：

```c
[root@centos system]# systemctl status todo.service
todo.service - Simple ToDo Application
   Loaded: loaded (/etc/systemd/system/todo.service; enabled)
   Active: active (running) since Wed 2015-03-04 19:57:19 UTC; 2min 13s ago
  Process: 21266 ExecStartPre=/usr/bin/docker pull dockerinpractice/todo \
(code=exited, status=0/SUCCESS)
  Process: 21255 ExecStartPre=/bin/bash -c /usr/bin/docker rm -f todo || \
/bin/true (code=exited, status=0/SUCCESS)
  Process: 21246 ExecStartPre=/bin/bash -c /usr/bin/docker kill todo ||  \
/bin/true (code=exited, status=0/SUCCESS)
 Main PID: 21275 (docker)
   CGroup: /system.slice/todo.service
           ??21275 /usr/bin/docker run --name todo
➥ -p 8000:8000 dockerinpractice/todo
Mar 04 19:57:24 centos docker[21275]: TodoApp.js:117:                 \
// TODO scroll into view
Mar 04 19:57:24 centos docker[21275]: TodoApp.js:176:                 \
if (i>=list.length()) { i=list.length()-1; } // TODO .length
Mar 04 19:57:24 centos docker[21275]: local.html:30:                  \
<!-- TODO 2-split, 3-split -->
Mar 04 19:57:24 centos docker[21275]: model/TodoList.js:29:           \
// TODO one op - repeated spec? long spec?
Mar 04 19:57:24 centos docker[21275]: view/Footer.jsx:61:             \
// TODO: show the entry's metadata
Mar 04 19:57:24 centos docker[21275]: view/Footer.jsx:80:             \
todoList.addObject(new TodoItem()); // TODO create default
Mar 04 19:57:24 centos docker[21275]: view/Header.jsx:25:             \
// TODO list some meaningful header (apart from the id)
Mar 04 19:57:24 centos docker[21275]: > todomvc-swarm@0.0.1 start /todo
Mar 04 19:57:24 centos docker[21275]: > node TodoAppServer.js
Mar 04 19:57:25 centos docker[21275]: Swarm server started port 8000
```

现在可以在端口8000访问服务器了。

#### 讨论

本技巧中介绍的一些原理不只适用于systemd，大部分进程管理器，包括其他的init系统，都可以采用类似的方式来配置。若你有兴趣，可以把系统上现存的已经运行的服务（比如PostgreSQL数据库）用容器化的服务来代替。

在技巧83里，我们会更进一步，使用systemd来实现在技巧77中创建的SQLite服务器。

