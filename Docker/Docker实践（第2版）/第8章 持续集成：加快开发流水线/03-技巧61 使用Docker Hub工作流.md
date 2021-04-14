### 技巧61　使用Docker Hub工作流

本技巧将介绍Docker Hub工作流，通过它可触发镜像的重新构建。



**注意**

在本节中，需要一个Docker网站账号，并链接到GitHub或Bitbucket账号。如果读者还未设置及建立链接，可在Github网站和Bitbucket网站的首页找到说明。



#### 问题

想要在代码发生变更时自动测试并将变更推送到镜像中。

#### 解决方案

建立一个Docker Hub仓库并将其链接到代码上。

尽管Docker Hub构建并不复杂，还是需要一些步骤。

（1）在GitHub或Bitbucket上创建仓库。

（2）克隆新的Git仓库。

（3）将代码添加到Git仓库中。

（4）提交源文件。

（5）推送Git仓库。

（6）在Docker Hub上创建一个新仓库。

（7）将Docker Hub仓库链接到Git仓库上。

（8）等待Docker Hub构建完成。

（9）提交并推送一项变更到源文件中。

（10）等待第二次Docker Hub构建完成。



**注意**

Git和Docker都使用“仓库”这个术语来指向一个项目。这可能会对用户造成困扰。即便此处将Git仓库和Docker仓库链接在一起，这两个类型的仓库也并不是一回事。



##### 1．在GitHub或Bitbucket上创建仓库

在GitHub或Bitbucket上创建一个新仓库。可以给它起任何一个想要的名字。

##### 2．克隆新的Git仓库

将这个新的Git仓库克隆到宿主机上。可以在Git项目首页找到执行这一步的命令。

将目录切换到这个仓库里。

##### 3．将代码添加到Git仓库中

现在需要将代码添加到该项目中。

此处可以添加任何所需的Dockerfile，不过代码清单8-1展示的是一个可以工作的示例。它包含两个文件，展示的是一个简单的开发工具环境。它会安装一些首选工具，并打印出当前的bash版本。

代码清单8-1　Dockerfile——简单的开发工具容器Dockerfile

```c
FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y curl　　⇽---　
RUN apt-get install -y nmap
RUN apt-get install -y socat
RUN apt-get install -y openssh-client
RUN apt-get install -y openssl
RUN apt-get install -y iotop
RUN apt-get install -y strace
RUN apt-get install -y tcpdump
RUN apt-get install -y lsof
RUN apt-get install -y inotify-tools
RUN apt-get install -y sysstat
RUN apt-get install -y build-essential　　⇽---　安装有用的软件包
RUN echo "source /root/bash_extra" >> /root/.bashrc　　⇽---　在root的bashrc中添加一行用以加载bash_extra
ADD bash_extra /root/bash_extra　　⇽---　将源文件中的bash_extra添加到容器中
CMD ["/bin/bash"]
```

现在需要创建上面引用的bash_extra文件，其内容如下：

```c
bash --version
```

这个文件只用作演示，展示的是你可以创建一个在启动时读取的bash文件。在本示例中，它显示了shell所使用的bash版本，不过它可以包含用于将shell设置成你偏好状态的所有东西。

##### 4．提交源文件

要提交这些源文件，可使用以下命令：

```c
git commit -am "Initial commit"
```

##### 5．推送Git仓库

现在可以使用以下命令将源文件推送到Git服务器上：

```c
git push origin master
```

##### 6．在Docker Hub上创建一个新仓库

接下来需要在Docker Hub上为这个项目创建一个仓库。打开Docker Hub官方网站并确保已经登录，然后点击“Create”（创建）并选择“Create Automated Build”（创建自动化构建）<sup class="my_markdown">[1]</sup>。

在第一次创建时，你需要经历账户关联的过程。你将看到一个将账户关联到托管Git服务的提示。选择相应服务并遵循提示将其关联到你的账户上。你可以选择是否给予Docker公司完全或更有限的访问权限以便整合。如果你选的是更有限的权限，请阅读一下特定服务的官方文档以确定剩余步骤中可能需要执行哪些额外工作。

##### 7．将Docker Hub仓库链接到Git仓库上

此时将看到一个选择Git服务的界面。选取所使用的源代码服务（GitHub或Bitbucket），然后从所提供的清单中选择新仓库。

接着将看到一个构建配置选项页面。可以保留默认值并点击下面的“Create Repository”（创建仓库）。

##### 8．等待Docker Hub构建完成

这时将看到一个说明链接工作正常的页面。点击“Build Details”（构建详情）链接。

接下来，将看到一个展示构建细节的页面。在“Builds History”（构建历史）下面会有第一次构建的条目。如果什么也没看到，可能需要点击按钮<sup class="my_markdown">[2]</sup>来手工触发构建。构建ID后面的“Status”（状态）字段将显示“Pending”（挂起）<sup>[3]</sup>、“Finished”（完成）<sup>[4]</sup>、“Building”（正在构建）或“Error”（错误）。如果一切顺利，将看到前3个状态之一。如果看到了“Error”，就说明存在问题，需要点击构建ID查看其错误信息。



**注意**

构建启动可能需要花费一段时间，因此有时在等待时看到“Pending”是非常正常的。



可以时不时点击“Refresh”（刷新），直到看到构建完成。一旦构建完成，就可以通过页面顶部列出的 `docker pull` 命令拉取这个镜像。

##### 9．提交并推送一项变更到源文件中

假设现在想要在登录时获取更多的环境信息，如输出正在运行的发行版详情。要实现这一点，可在bash_extra文件中添加这几行，而此时它看起来是这样的：

```c
bash --version
cat /etc/issue
```

然后按第4步和第5步所示进行提交和推送。

##### 10．等待第二次Docker Hub构建完成

如果返回构建页面，新的一行将出现在“Builds History”（构建历史）一节的下面，可以按步骤8所述对此次构建进行跟踪。



**提示**

如果构建出现错误，用户将会收到相关电子邮件（如果一切正常则不会有电子邮件），因此一旦适应了这个工作流，只需要在收到电子邮件时进行检查。



现在，可以使用Docker Hub工作流了。读者将很快适应这个框架，并发现它在保持构建更新和减少手工重新构建Dockerfile的认知负荷这两方面非常有价值。

#### 讨论

因为Docker Hub是镜像的规范源，在CI过程中把镜像推送到这上面可以让事情变得更简单（比如，将镜像分发给第三方）。不必自己运行构建过程更加简单，并能带来额外好处，例如在Docker Hub的列表上显示勾选标记，表示本次构建是在可信服务器上执行的。

对构建拥有额外的信心有助于遵循技巧70中的Docker **契约** ——在技巧113中，我们将看到某些特定的机器有时会影响Docker构建，因此使用完全独立的系统对增加最终结果的信心大有裨益。

