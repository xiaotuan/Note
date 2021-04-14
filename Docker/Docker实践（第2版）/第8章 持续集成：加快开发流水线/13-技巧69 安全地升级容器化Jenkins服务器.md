### 技巧69　安全地升级容器化Jenkins服务器

如果你已经在生产环境中使用了Jenkins一段时间，你会注意到Jenkins会频繁地给服务器发布安全性和功能性变动更新。

在一台专用的、非Docker化的宿主机上，这通常是由包管理器来管理的。使用Docker的话，升级的原因就稍微有点复杂，因为服务器环境与数据可能是分离的。

#### 问题

要可靠地升级Jenkins服务器。

#### 解决方案

运行一个能处理Jenkins服务器升级的Jenkins升级器镜像。

本技巧以一个Docker镜像形式交付，该镜像由多个部分组成。首先我们将说明构建该镜像的Dockerfile。这个Dockerfile以官方Docker镜像（包含Docker客户端）为基础，添加了一个管理升级的脚本。

这个镜像将执行一个Docker命令，挂载宿主机上的Docker项目，使其能管理所有必需的Jenkins升级。

##### 1．Dockerfile

我们从Dockerfile开始看起，如代码清单8-15所示。

代码清单8-15　Jenkins升级器Dockerfile

```c
FROM docker　　⇽---　使用Docker官方标准镜像
ADD jenkins_updater.sh /jenkins_updater.sh　　⇽---　添加jenkins_updater.sh脚本（稍后讨论）
RUN chmod +x /jenkins_updater.sh　　⇽---　确保jenkins_updater.sh脚本可运行
ENTRYPOINT /jenkins_updater.sh　　⇽---　将jenkins_updater.sh脚本设置为镜像默认的入口点
```

上述Dockerfile将备份Jenkins的需求封装在一个可运行的Docker镜像里。它使用docker官方标准镜像以获得一个运行在容器内的Docker客户端。该容器将运行代码清单8-16里的脚本，用于管理宿主机上所有必需的Jenkins升级。



**注意**

如果你的Docker守护进程的版本与docker Docker镜像里的版本不同，可能会碰到问题。请尽量使用相同版本。



##### 2．jenkins_updater.sh

代码清单8-16中给出的是在容器内管理升级的shell脚本。

代码清单8-16　备份并重启Jenkins的shell脚本

```c
#!/bin/sh　　⇽---　这个脚本使用的是sh shell（而不是/bin/bash），因为Docker镜像里只有sh
 set -e　　⇽---　确保脚本里的任何命令失败时脚本也会失败
 set -x　　⇽---　将脚本里运行的所有命令都记录到标准输出中
 if ! docker pull jenkins | grep up.to.date　　⇽---　只在dockers pull jenkins不输出up to date时触发
 then
    docker stop jenkins　　⇽---　在升级时，首先停止jenkins容器
     docker rename jenkins jenkins.bak.$(date +%Y%m%d%H%M) 　　⇽---　一旦停止，将jenkins容器重命名为jenkins.bak跟着到分钟的时间
     cp -r /var/docker/mounts/jenkins_home \　　⇽---　
           /var/docker/mounts/jenkins_home.bak.$(date +%Y%m%d%H%M) 　　⇽---　将Jenkins容器镜像状态目录复制到备份目录中
     docker run -d \　　⇽---　运行Docker命令以守护进程方式启动Jenkins
         --restart always \　　⇽---　设置Jenkins容器总是重启
         -v /var/docker/mounts/jenkins_home:/var/jenkins_home \　　⇽---　将jenkins状态卷挂载到宿主机目录中
         --name jenkins \　　⇽---　将容器命名为jenkins以防止多个此类容器不小心同时运行
         -p 8080:8080 \　　⇽---　将容器的8080端口发布到宿主机的8080端口上
         jenkins　　⇽---　最后，给出用于执行docker命令的jenkins镜像名称
 fi
```

上述脚本将尝试使用 `docker pull` 命令从Docker Hub拉取 `jenkins` 。如果输出包含 `up to date` ， `docker pull | grep ...` 命令返回 `true` 。不过我们只想在输出里看不到 `up to date` 时才做升级。这也是在 `if` 后面放了个感叹号 `!` 用于否定 `if` 语句的原因。

其结果是 `if` 块里的代码只会在下载了新的“latest”Jenkins镜像版本后才会触发。在这个代码块里，运行中的Jenkins容器将停止并被重命名。使用重命名而非删除是为了在升级不起作用时可以恢复以前的版本。考虑到这个回滚策略，同样对宿主机上包含Jenkins状态的挂载目录作了备份。

最后，使用 `docker run` 命令启动最新下载的Jenkins镜像。



**注意**

你可以根据个人偏好修改宿主机挂载目录或所运行的Jenkins容器名称。



你可能好奇这个Jenkins镜像是如何与宿主机的Docker守护进程进行连接的。为了实现这一点，我们用到了在技巧66中见过的方法来运行镜像。

##### 3．jenkins-updater镜像调用

代码清单8-17中的命令将使用早前创建的镜像（内部包含了shell脚本）来执行Jenkins升级：

代码清单8-17　用于运行Jenkins升级器的Docker命令

```c
docker run　　⇽---　 docker run命令
     --rm \　　⇽---　在容器完成作业后删除它
     -d \　　⇽---　在后台运行该容器
     -v /var/lib/docker:/var/lib/docker \　　⇽---　将宿主机的docker守护进程目录挂载到容器中
     -v /var/run/docker.sock:/var/run/docker.sock \　　⇽---　将宿主机的docker套接字挂载到容器中，这样docker命令就可以在容器中起作用
     -v /var/docker/mounts:/var/docker/mounts　　⇽---　挂载宿主机中Jenkins数据所存储的挂载目录，以便jenkins_updater.sh脚本可以复制这些文件
         dockerinpractice/jenkins-updater　　⇽---　指定运行的镜像为dockerinpractice/ jenkins-updater镜像
```

##### 4．自动化升级

以下这一行代码可以很容易地在crontab里运行。这将运行在我们的主服务器上。

```c
0 * * * * docker run --rm -d -v /var/lib/docker:/var/lib/docker -v
➥ /var/run/docker.sock:/var/run/docker.sock -v
➥ /var/docker/mounts:/var/docker/mounts dockerinpractice/jenkins-updater
```



**注意**

上述命令全部都在一行里，因为crontab无法像shell脚本那样在末尾放置一个反斜杠来忽略换行。



最终的结果是，单一的crontab条目即可安全地管理Jenkins实例的升级，而无须担心。

自动化清除旧容器和数据卷挂载的任务作为一个练习留给读者。

#### 讨论

本技巧举例说明了一些贯穿全书的事情，可以应用在与Jenkins环境类似的情况中。

首先，使用docker镜像与宿主机上的Docker守护进程通信。其他可移植脚本可能会以其他方式编写来管理Docker守护进程。比如，你可能会写个脚本来删除旧的数据卷，或者报告守护进程上的活动。

更具体地说， `if` 块模式可用于在镜像有新版本时更新和重启镜像。因为安全原因或进行小升级而更新镜像并不是什么罕见的事。

如果你担心在升级版本时遇到困难，同样需要指出的是，你不一定需要使用“latest”的镜像标签（本技巧是这么做的）。很多镜像使用了不同的标签，用于跟踪不同的版本号。比如，一个 `exampleimage` 可能会有一个 `exampleimage:latest` 标签，以及 `exampleimage:v1.1` 和 `exampleimage:v1` 标签。所有标签随时都可能更新，但相比 `:latest` 标签， `:v1.1` 标签不太可能变成新版本。 `:latest` 标签可能会变成与新的 `:v1.2` 标签（可能需要升级步骤）一样的版本，也可能变成 `:v2.1` 标签，后者的大版本 `2` 表示极有可能会打乱升级过程。

本技巧也简要概述了Docker升级的一个回滚策略。容器与数据（使用数据卷挂载）的分离可能会对升级稳定性造成困难。通过保留服务可工作时旧的容器和旧的数据副本，可以更容易地从失败中恢复。

#### 数据库升级与Docker

数据库升级是一个特殊的场景，其中的稳定性受到密切关注。如果你要升级数据库到新的版本，你需要考虑此次升级是否要求修改数据结构和数据库数据的存储。将镜像新版本运行成容器并指望它能起作用是远远不够的。如果数据库足够聪明，能够知道所看到的数据是哪个版本，并且能够相应地执行升级，则情况会变得更加复杂。在这些情况下，使用升级可能会更合适。

很多因素都会影响到你的升级策略。你的应用程序可能会采用乐观的方式（如在此Jenkins示例中看到的那样），假定所有东西都是好的，并在失败发生时（没有如果）做好准备。另一方面，你可能要求100%的正常运行时间，无法容忍任何形式的失败。在这种情况下，（不论有或没有Docker参与）通常都需要一个经过充分测试的升级计划以及比执行 `docker pull` 更深入的平台知识。

尽管Docker没有消除升级问题，版本化镜像的不可变性可以简化需要考虑的因素。Docker还可以通过两种方式帮助你为失败做好准备：备份宿主机数据卷中的状态，以及让测试可预测状态变得更容易。在管理和理解Docker所做的工作中经历困难，可以让你对升级过程有更多的控制和把握。

