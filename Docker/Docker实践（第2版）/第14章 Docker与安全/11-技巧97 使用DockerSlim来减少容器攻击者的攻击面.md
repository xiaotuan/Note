### 技巧97　使用DockerSlim来减少容器攻击者的攻击面

在7.3节中我们讨论了为了防止需要通过网络传输大量数据，从而创建一种小型的镜像的方式。但是这样做还有其他的理由——如果镜像中的内容越少，攻击者下手的地方就越少。举个具体的例子，如果容器中没有shell，那么攻击者就无法获得shell。

为容器构建一个“符合预期”的配置描述文件，然后在运行时强制指定，意味着预期外的行为有相当机会可以被检测到并且进行预防。

#### 问题

试图把镜像缩小到刚好可用的程度，来减少攻击面。

#### 解决方案

使用DockerSlim工具来分析镜像，修改之以减少攻击面。

该工具接受一个Docker镜像，将其减少到刚好可用的程度。

DockerSlim以至少两种不同的方式来减少Docker镜像的体积。首先，它仅保留必须的文件并且将它们放置在单一层中。结果就是镜像会比臃肿的原版本显著瘦身。

第二点，它提供了一个seccomp配置描述文件。它通过动态分析运行中的镜像来达成该目标。简单说，它会把镜像运行起来，追踪使用到的文件和系统调用。当DockerSlim正在分析运行中的容器的时候，你要尽量地按照典型用户的使用方法来使用它，保证必须的文件和系统调用被选取到了。



**警告**

如果你像这样用动态分析工具来减少镜像体积，请保证你在分析阶段已经充分地使用了自己的镜像。本示例用了一个简单的镜像，但是你的镜像可能很复杂，难以完全地分析。



本技巧会使用一个简单的网络应用示例来展示本技巧，你将会：

+ 安装DockerSlim；
+ 构建镜像；
+ 用DockerSlim把该镜像作为容器运行起来；
+ 访问该应用的网络端点；
+ 使用创建好的seccomp配置描述文件来运行瘦身后的镜像。



**注意**

seccomp配置描述文件主要是一个何种系统调用可以使用的白名单。当运行容器的时候，你可以根据应用需求，使用降低的权限或提升的权限来指定seccomp配置描述文件。默认的seccomp配置在300余种系统调用中禁用了45种。大多数应用需要的比这少得多。



##### 1．设置DockerSlim

用代码清单14-5中的命令来获取docker-slim二进制文件并且安装。

代码清单14-5　下载docker-slim文件并且安装到指定文件夹

```c
$ mkdir -p docker-slim/bin && cd docker-slim/bin　　⇽---　创建docker-slim文件夹以及bin子文件夹
 $ wget https://github.com/docker-slim/docker-slim/releases/download/1.18
➥ /dist_linux.zip　　⇽---　从DockerSlim发行文件夹中获取其zip文件
 $ unzip dist_linux.zip　　⇽---　解压zip文件夹
 $ cd .. 　　⇽---　移动到父目录docker-slim中
```



**注意**

本技巧是依据之前版本的docker-slim来测试的。该项目并非处在急速发展中，所以更新应该不是很重要。



现在在bin子文件夹中安装好了docker-slim二进制文件。

##### 2．构建臃肿镜像

接下来我们会使用NodeJS来构建一个示例应用。该应用只是在8000端口提供一段JSON的简单应用。代码清单14-6中的命令克隆docker-slim仓库，移动到示例应用代码，然后把其Dockerfile以 `sample-node-app` 的名字构建到一个镜像里了。

代码清单14-6　构建一个docker-slim应用

```c
$ git clone https://github.com/docker-slim/docker-slim.git　　⇽---　克隆该仓库，仓库中包含示例应用
$ cd docker-slim && git checkout 1.18　　⇽---　从docker-slim仓库中签出一个可工作的版本
$ cd sample/apps/node　　⇽---　移动到NodeJS示例应用文件夹
$ docker build -t sample-node-app . 　　⇽---　构建镜像，命名为sample-node-app
$ cd -　　⇽---　返回到之前的目录，docker-slim二进制文件在此目录中
```

##### 3．运行臃肿的镜像

现在臃肿镜像已经创建好了，下一步就是使用docker-slim来把它运行为容器。一旦应用初始化完成，你需要访问网络端点来执行其代码。最后，把后台运行的docker-slim应用放到前台来，等待其结束。

```c
$ ./docker-slim build --http-probe sample-node-app &　　⇽---　以sample-node-app来运行docker-slim二进制文件。将其进程放在后台。http-probe会在所有公开的端口调用应用
 $ sleep 10 && curl localhost:32770　　⇽---　休眠10秒以让sample-node-app进程运行，然后访问应用运行的端口
 {"status":"success","info":"yes!!!","service":"node"}　　⇽---　把应用的JSON响应送到终端中
 $ fg　　⇽---　把docker-slim放到前台，等待其完成
 ./docker-slim build --http-probe sample-node-app　　⇽---　
 INFO[0014] docker-slim: HTTP probe started...
 INFO[0014] docker-slim: http probe - GET http://127.0.0.1:32770/ => 200
 INFO[0014] docker-slim: HTTP probe done.
 INFO[0015] docker-slim: shutting down 'fat' container...
 INFO[0015] docker-slim: processing instrumented 'fat' container info...
 INFO[0015] docker-slim: generating AppArmor profile...
 INFO[0015] docker-slim: building 'slim' image... 　　⇽---　 docker-slim输出的第一部分展示了工作日志
 Step 1 : FROM scratch　　⇽---　
  --->
 Step 2 : COPY files /
  ---> 0953a87c8e4f
 Removing intermediate container 51e4e625017e
 Step 3 : WORKDIR /opt/my/service
  ---> Running in a2851dce6df7
  ---> 2d82f368c130
 Removing intermediate container a2851dce6df7
 Step 4 : ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:
➥ /bin"
  ---> Running in ae1d211f118e
  ---> 4ef6d57d3230　　⇽---　 docker-slim构建“瘦身”容器
 Removing intermediate container ae1d211f118e　　⇽---　
 Step 5 : EXPOSE 8000/tcp
  ---> Running in 36e2ced2a1b6
  ---> 2616067ec78d
 Removing intermediate container 36e2ced2a1b6
 Step 6 : ENTRYPOINT node /opt/my/service/server.js
  ---> Running in 16a35fd2fb1c
  ---> 7451554aa807
 Removing intermediate container 16a35fd2fb1c
 Successfully built 7451554aa807
 INFO[0016] docker-slim: created new image: sample-node-app.slim　　⇽---　 docker-slim构建“瘦身”容器
 $　　⇽---　当其完成，请按回车键以获取终端提示符
 $
```

在本例中所谓的“执行代码”仅仅是访问一个URL然后获取返回值。更复杂的应用可能要更多样的测试来充分执行。

注意根据文档，我们无须手动访问32770端口，因为我们使用了 `http-probe` 参数。如果你启用了 `HTTP probe` ，对于所有指定的端口默认它会在根URL（“/”）发起HTTP和HTTPS的GET请求。我们手动使用 `curl` 仅仅是为了文档展示。

此时，已经创建好了sample-node-app的瘦身版。如果检视 `docker images` 的输出，你会发现镜像已经急剧缩小。

```c
$ docker images
REPOSITORY             TAG      IMAGE ID       CREATED             SIZE
sample-node-app.slim   latest   7451554aa807   About an hour ago   14.02 MB　　⇽---　 sample-node-app瘦身版仅14 MB
sample-node-app        latest   78776db92c2a   About an hour ago   418.5 MB　　⇽---　原版sample-node-app镜像有400 MB
```

如果通过 `docker history` 的输出检查臃肿版和瘦身版，会发现二者的结构大有不同。

```c
$ docker history sample-node-app　　⇽---　 docker history命令在sample-node-app镜像上执行
 IMAGE         CREATED       CREATED BY                              SIZE　　⇽---　
 78776db92c2a  42 hours ago  /bin/sh -c #(nop)  ENTRYPOINT ["node"   0 B
 0f044b6540cd  42 hours ago  /bin/sh -c #(nop)  EXPOSE 8000/tcp      0 B
 555cf79f13e8  42 hours ago  /bin/sh -c npm install                  14.71 MB
 6c62e6b40d47  42 hours ago  /bin/sh -c #(nop)  WORKDIR /opt/my/ser  0 B
 7871fb6df03b  42 hours ago  /bin/sh -c #(nop) COPY dir:298f558c6f2  656 B
 618020744734  42 hours ago  /bin/sh -c apt-get update &&   apt-get  215.8 MB
 dea1945146b9  7 weeks ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]    0 B
 <missing>     7 weeks ago   /bin/sh -c mkdir -p /run/systemd && ec  7 B
 <missing>     7 weeks ago   /bin/sh -c sed -i 's/^#\s*\(deb.*unive  2.753 kB
 <missing>     7 weeks ago   /bin/sh -c rm -rf /var/lib/apt/lists/*  0 B
 <missing>     7 weeks ago   /bin/sh -c set -xe   && echo '#!/bin/s  194.6 kB
 <missing>     7 weeks ago   /bin/sh -c #(nop) ADD file:8f997234193  187.8 MB　　⇽---　镜像的历史展示了它最初创建的所有命令
 $ docker history sample-node-app.slim　　⇽---　 docker history命令在sample-node-app瘦身版镜像上运行
 IMAGE         CREATED       CREATED BY                              SIZE　　⇽---　
 7451554aa807  42 hours ago  /bin/sh -c #(nop)  ENTRYPOINT ["node"   0 B
 2616067ec78d  42 hours ago  /bin/sh -c #(nop)  EXPOSE 8000/tcp      0 B
 4ef6d57d3230  42 hours ago  /bin/sh -c #(nop)  ENV PATH=/usr/local  0 B
 2d82f368c130  42 hours ago  /bin/sh -c #(nop)  WORKDIR /opt/my/ser  0 B
 0953a87c8e4f  42 hours ago  /bin/sh -c #(nop) COPY dir:36323da1e97  14.02 MB　　⇽---　瘦身版的历史由更少的命令组成，包括最初的臃肿版中不存在的COPY命令
```

上面的输出给出了DockerSlim做了什么的提示。它采用了最终的文件系统状态，把它复制为镜像的最终层，从而（高效地）把镜像减少为一个14MB的单一层。

正如本技巧最开始提到的，DockerSlim就其第二点目的产生了一个制品。一个seccomp.json文件被创建（本例中是sample-node-app-seccomp.json），它可用来限定运行中的容器的行为。

让我们看看该文件的内容（此处编辑过，因为它比较长），如代码清单14-7所示。

代码清单14-7　seccomp配置描述文件

```c
$ SECCOMPFILE=$(ls $(pwd)/.images/*/artifacts/sample-node-app-seccomp.json) 　　⇽---　从变量SECCOMPFILE中获取seccomp文件的位置
 $ cat ${SECCOMPFILE}　　⇽---　用cat来查看文件
 {
"defaultAction": "SCMP_ACT_ERRNO",　　⇽---　指定试图调用任何禁止的系统调用的进程的退出码
   "architectures": [　　⇽---　
   "SCMP_ARCH_X86_64"
   ], 　　⇽---　指定该配置描述文件应当应用在何种硬件架构上
   "syscalls": [　　⇽---　
     {
       "name": "capset",
       "action": "SCMP_ACT_ALLOW"
     },
     {
       "name": "rt_sigaction",
       "action": "SCMP_ACT_ALLOW"
     },
     {
       "name": "write",
       "action": "SCMP_ACT_ALLOW"
     },
 [...]
    {
     "name": "execve",
       "action": "SCMP_ACT_ALLOW"
     },
     {
       "name": "getcwd",
       "action": "SCMP_ACT_ALLOW"
     }　　⇽---　通过指定SCMP_ACT_ALLOW来把一些系统调用加入白名单
   ] 
}
```

最后，使用seccomp配置描述文件把瘦身版镜像运行起来，检查一下是否如预期般运行。

```c
$ docker run -p32770:8000 -d \
--security-opt seccomp=/root/docker-slim-bin/.images/${IMAGEID}/artifacts
➥ /sample-node-app-seccomp.json sample-node-app.slim　　⇽---　将该瘦身版镜像运行为守护进程，公开之前在分析阶段同样的端口，然后把seccomp配置描述文件应用在上面
 4107409b61a03c3422e07973248e564f11c6dc248a6a5753a1db8b4c2902df55　　⇽---　把容器ID输出到终端
 $ sleep 10 && curl localhost:3277l　　⇽---　重新执行curl命令，确认该应用是否和之前一样运行
 {"status":"success","info":"yes!!!","service":"node"}　　⇽---　输出和之前的臃肿镜像是一致的
```

#### 讨论

这个简单的例子展示了镜像不止体积上可以减少，可以施展的行为也可以减少。这是通过删除不重要的文件（也在技巧59中谈论过）实现的，而且可以限制仅提供运行应用必须的系统调用。

这里“使用“应用的方法很简单（只是一个对默认端点的 `curl` 请求）。对于真实的应用来说，有很多种方式来保证已经覆盖了所有可能性。一种办法是对已知的网络端点开发一套测试，另一种方法是使用”漏洞检查工具“自动向应用程序灌入大量输入（这是一种用来发现软件中的bug和安全漏洞的办法）。最简单的办法就是运行应用足够长的时间，期望所有必需的文件和系统调用都有被引用到。

许多企业版的Docker安全工具都是以这种原则工作的，但是工作起来更加自动化。一般他们会让程序运行一段时间，然后追踪哪些系统调用被调用了，哪些文件被访问了，还有（也许）哪些操作系统能力被用到了。基于此——还有一个可配置的学习过程——他们可以决定对于应用来说什么是预期行为，然后报告所有似乎越线的行为。举例来说，如果一个攻击者获取了权限来运行容器、启动bash二进制文件或者打开预期外的端口，这可能会引发系统警报。DockerSlim允许你预先控制该流程，减少攻击者在获取了权限的情况下可以做的事情。

另外一种可以减少应用的受攻击面的方法是限制其能力。在技巧93中有所介绍。

