### 技巧10　查找并运行一个Docker镜像

Docker注册中心造就的是与GitHub相似的社交编码文化。如果读者有兴趣尝试一个新的软件应用程序，或正在找寻服务于某个特定用途的新的应用程序，那么Docker镜像将是一个简单的实验手段，它不会对宿主机造成干扰，不需要配备一台虚拟机，也不必担心安装步骤。

#### 问题

想要查找一个Docker镜像形式的应用程序或工具，并进行尝试。

#### 解决方案

使用 `docker search` 命令来查找要拉取的镜像，然后运行它。

假设读者对Node.js有兴趣。在下面的示例中，我们使用 `docker search` 命令搜索出匹配“node”的镜像：

```c
$ docker search node
NAME　　　　　　　　　　　DESCRIPTION
➥ STARS　　 OFFICIAL　 AUTOMATED
node　　　　　　　　　　　Node.js is a JavaScript-based platform for...
➥　 3935　　　[OK] 　　⇽---　docker search的输出是按评星数量排序的
 nodered/node-red-docker　 Node-RED Docker images.
➥　 57　　　　　　　　　 [OK] 　　⇽---　描述是上传者对镜像用途的解释
 strongloop/node　　　　　 StrongLoop, Node.js, and tools.
➥　 38　　　　　　　　　 [OK] 　　⇽---　官方镜像是指受Docker Hub信任的镜像
 kkarczmarczyk/node-yarn　 Node docker image with yarn package manage...
➥　 25　　　　　　　　　 [OK] 　　⇽---　自动化镜像是指使用Docker Hub自动化构建功能构建的镜像
 bitnami/node　　　　　　　Bitnami Node.js Docker Image
➥　 19　　　　　　　　　 [OK]
siomiz/node-opencv　　　　_/node + node-opencv
➥　 10　　　　　　　　　 [OK]
dahlb/alpine-node　　　　 small node for gitlab ci runner
➥　 8　　　　　　　　　　[OK]
cusspvz/node　　　　　　　Super small Node.js container (~15MB) ba...
➥　 7　　　　　　　　　　[OK]
anigeo/node-forever　　　 Daily build node.js with forever
➥　 4　　　　　　　　　　[OK]
seegno/node　　　　　　　 A node docker base image.
➥　 3　　　　　　　　　　[OK]
starefossen/ruby-node　　 Docker Image with Ruby and Node.js installed
➥　 3　　　　　　　　　　[OK]
urbanmassage/node　　　　 Some handy (read, better) docker node images
➥　 1　　　　　　　　　　[OK]
xataz/node　　　　　　　　very light node image
➥　 1　　　　　　　　　　[OK]
centralping/node　　　　　Bare bones CentOS 7 NodeJS container.
➥　 1　　　　　　　　　　[OK]
joxit/node　　　　　　　　Slim node docker with some utils for dev
➥　 1　　　　　　　　　　[OK]
bigtruedata/node　　　　　Docker image providing Node.js & NPM
➥　 1　　　　　　　　　　[OK]
1science/node　　　　　　 Node.js Docker images based on Alpine Linux
➥　 1　　　　　　　　　　[OK]
domandtom/node　　　　　　Docker image for Node.js including Yarn an...
➥　 0　　　　　　　　　　[OK]
makeomatic/node　　　　　 various alpine + node based containers
➥　 0　　　　　　　　　　[OK]
c4tech/node　　　　　　　 NodeJS images, aimed at generated single-p...
➥　 0　　　　　　　　　　[OK]
instructure/node　　　　　Instructure node images
➥　 0　　　　　　　　　　[OK]
octoblu/node　　　　　　　Docker images for node
➥　 0　　　　　　　　　　[OK]
edvisor/node　　　　　　　Automated build of Node.js with commonly u...
➥　 0　　　　　　　　　　[OK]
watsco/node　　　　　　　 node:7
➥　 0　　　　　　　　　　[OK]
codexsystems/node　　　　 Node.js for Development and Production
➥　 0　　　　　　　　　　[OK]
```

一旦选择了一个镜像，就可以通过对其名称执行 `docker pull` 命令来下载它：

```c
$ docker pull node　　⇽---　从Docker Hub拉取名为node的镜像
 Using default tag: latest
latest: Pulling from library/node
5040bd298390: Already exists
fce5728aad85: Pull complete
76610ec20bf5: Pull complete
9c1bc3c30371: Pull complete
33d67d70af20: Pull complete
da053401c2b1: Pull complete
05b24114aa8d: Pull complete
Digest:
➥ sha256:ea65cf88ed7d97f0b43bcc5deed67cfd13c70e20a66f8b2b4fd4b7955de92297
Status: Downloaded newer image for node:latest　　⇽---　如果Docker拉取了一个新的镜像（与之相对的是说明没有比已有镜像更新的版本），会显示这条信息。读者看到的输出可能会有所不同
```

接着，可以使用 `-t` 和 `-i` 标志以交互方式运行它。 `-t` 标志指明创建一个TTY设备（一个终端），而 `-i` 标志指明该Docker会话是交互式的：

```c
$ docker run -t -i node /bin/bash
root@c267ae999646:/# node
> process.version
'v7.6.0'
>
```



**提示**

可以在上述 `docker run` 调用中用 `-ti` 或 `-it` 取代 `-t -i` 来减少输入。从这里开始，本书将使用这种用法。



镜像维护人员经常会提供一些有关如何运行镜像的建议。在Docker Hub官方网站上搜索镜像将引导到该镜像的页面。其描述标签页可提供更多信息。



**警告**

如果用户下载并运行了一个镜像，运行的将是自己无法充分验证的代码。虽然使用受信任的镜像具有相对的安全性，但是通过互联网下载和运行软件时，没有什么是能保证100%安全的。



有了这方面的知识和经验，现在可以对Docker Hub提供的大量资源进行挖掘了。毫不夸张地说，要试用这成千上万的镜像，有很多东西要学。请慢慢享受！

#### 讨论

Docker Hub是一项极佳的资源，不过有时会很慢——这时值得暂停一下，决定如何最好地构建搜索命令以获取最佳结果。在不打开浏览器的情况下进行搜索的能力让你可以快速了解生态系统中可能感兴趣的项目，因此你可以更好地定位到满足需求的镜像文档上。

当你在重建镜像时，最好能不时运行一次搜索，看看评星数量是否表明Docker社区已经开始向一个不同于你当前所使用的镜像聚集。

