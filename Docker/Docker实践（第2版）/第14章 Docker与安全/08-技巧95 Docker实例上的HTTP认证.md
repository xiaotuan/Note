### 技巧95　Docker实例上的HTTP认证



在技巧1中我们看到了如何给守护进程打开网络访问权限，在技巧4中我们了解了如何使用socat来监听Docker API。

本技巧把二者结合起来：我们将能远程访问自己的守护进程并查看其反应。访问仅限于那些拥有用户名/密码组合的人，所以稍微安全些。除此之外还有好处，不用通过重启Docker守护进程来达到这个目的——启动一个容器守护进程吧！

#### 问题

想要一些对Docker守护进程上可用的网络访问的基本身份验证。

#### 解决方案

使用HTTP身份验证把自己的Docker守护进程临时分享给其他人。

图14-1给出了本技巧的整体架构的最终布局。

![64.png](../images/64.png)
<center class="my_markdown"><b class="my_markdown">图14-1　一个带有基本身份验证的Docker守护进程架构</b></center>



**注意**

本讨论假设用户的Docker守护进程使用的是位于/var/run/docker.sock中的Docker默认的Unix套接字接入方法。



本技巧中的代码可以在https://github.com/docker-in-practice/docker-authenticate找到。代码清单14-1展示了这个仓库中的用来创建本技巧中的镜像的Dockerfile。

代码清单14-1　Dockerfile

```c
FROM debian
RUN apt-get update && apt-get install -y \
 nginx apache2-utils　　⇽---　确保需要的软件都安装并且更新好了
RUN htpasswd -c /etc/nginx/.htpasswd username　　⇽---　为名为username的用户创建密码文件
RUN htpasswd -b /etc/nginx/.htpasswd username password　　⇽---　为名为username的用户创建密码为password
RUN sed -i 's/user .*;/user root;/' \
 /etc/nginx/nginx.conf　　⇽---　 nginx 需要以 root 权限运行以获取Docker Unix套接字，因此我们把用户那一行替换为了root用户的信息
ADD etc/nginx/sites-enabled/docker \
 /etc/nginx/sites-enabled/docker　　⇽---　在Docker的nginx site文件中复制（见代码清单14-8）
CMD service nginx start && sleep infinity　　⇽---　默认开启nginx服务并且无限等待
```

用 `htpasswd` 命令建立的.htpasswd文件包含在允许（或禁止）连接到Docker套接字之前的凭证。如果用户在自己创建此镜像，可能想改变这两步中的 `username` 和 `password` 来定制对Docker套接字权限的凭证。



**警告**

小心不要共享此镜像，因为它包含你设置的密码！



Docker中的nginx site文件如代码清单14-2所示。

代码清单14-2　/etc/nginx/sites-enabled/docker

```c
upstream docker {
  server unix:/var/run/docker.sock; 　　⇽---　定义指向Docker的域套接字时nginx中“docker”的位置
 }
server {
  listen 2375 default_server; 　　⇽---　监听2375端口（标准的Docker端口）
  location / {
   proxy_pass http://docker; 　　⇽---　将发往和来自之前定义的“docker”地址的请求代理
    auth_basic_user_file /etc/nginx/.htpasswd; 　　⇽---　定义要用到的密码文件
    auth_basic "Access restricted";　　⇽---　通过密码限制权限
   }
}
```

现在把这个镜像作为守护进程容器运行起来，将需要的宿主机上的资源映射进来：

```c
$ docker run -d --name docker-authenticate -p 2375:2375 \
  -v /var/run:/var/run dockerinpractice/docker-authenticate
```

这条命令会在后台以 `docker-authenticate` 为名执行，之后可以引用。在宿主机上公开了容器的2375端口，而且这个容器挂载了默认的含有作为卷的Docker套接字的目录，从而能够访问Docker守护进程。如果读者用的是自己定制的镜像，有自己的用户名和密码，在这里需要把镜像名替换成自己的。

网络服务现在应该就启动运行起来了。如果读者使用自己设立的用户名和密码来对这个服务执行 `curt` 命令，应该能看到一个API响应：

```c
$ curl http://username:password@localhost:2375/info　　⇽---　在要对其执行curl命令的URL中写上username:password，地址放在@符号后。本请求是访问Docker守护进程API的/info端点
 {"Containers":115,"Debug":0, >　　⇽---　从Docker守护进程返回的JSON
  "DockerRootDir":"/var/lib/docker","Driver":"aufs", >
  "DriverStatus":[["Root Dir","/var/lib/docker/aufs"], >
  ["Backing Filesystem","extfs"],["Dirs","1033"]], >
  "ExecutionDriver":"native-0.2", >
  "ID":"QSCJ:NLPA:CRS7:WCOI:K23J:6Y2V:G35M:BF55:OA2W:MV3E:RG47:DG23", >
  "IPv4Forwarding":1,"Images":792, >
  "IndexServerAddress":"https://index.docker.io/v1/", >
  "InitPath":"/usr/bin/docker","InitSha1":"", >
  "KernelVersion":"3.13.0-45-generic", >
  "Labels":null,"MemTotal":5939630080,"MemoryLimit":1, >
  "NCPU":4,"NEventsListener":0,"NFd":31,"NGoroutines":30, >
  "Name":"rothko","OperatingSystem":"Ubuntu 14.04.2 LTS", >
  "RegistryConfig":{"IndexConfigs":{"docker.io": >
  {"Mirrors":null,"Name":"docker.io", >
  "Official":true,"Secure":true}}, >
  "InsecureRegistryCIDRs":["127.0.0.0/8"]},"SwapLimit":0}
```

完成之后，通过下面的命令移除容器：

```c
$ docker rm -f docker-authenticate
```

权限现在被收回了。

##### 使用docker命令？

读者可能想知道其他用户能否通过 `docker` 命令来连接。例如，类似于：

```c
docker -H tcp://username:password@localhost:2375 ps
```

在编写本书时，身份验证功能尚未被内置到Docker本身。但是我们已经创建了可以处理身份验证信息并且允许Docker连接到守护进程的镜像。简单地使用此镜像如下：

```c
$ docker run -d --name docker-authenticate-client \　　⇽---　在该背景下运行客户端容器，并给它一个名字
 -p 127.0.0.1:12375:12375 \　　⇽---　公开一个端口用来让Docker连接到守护进程，但是仅允许来自本地机器的连接
 dockerinpractice/docker-authenticate-client \　　⇽---　使用我们创建的镜像以允许和Docker建立身份验证连接
 192.168.1.74:2375 username:password　　⇽---　镜像的两个参数：指定验证连接的另一端以及用户名和密码（应当替换为你自己设立的合适的值）
```

注意，对于指定身份验证连接的另一端来说， `localhost` 或 `127.0.0.1` 是不起作用的，如果想要在一台宿主机上试用，必须使用 `ip addr` 来为机器指定外部IP地址。

现在可以用下列命令来使用身份验证连接：

```c
docker -H localhost:12375 ps
```

注意，由于一些实现上的限制，交互式的Docker命令（带有 `-i` 参数的 `run` 、 `exec` ）不能使用。

#### 讨论

在本技巧中，我们展示了如何在受信网络给Docker服务创建基本的身份验证。在技巧96中，我们会着眼于加密流量，以使嗅探器无法刺探你的流量，甚至注入恶意数据或代码。

**警告**

这一技巧提供了基本的身份验证，但是这并不能提供真正意义上的安全（尤其能够监听你的网络流量的人可以拦截你的用户名和密码）。更加需要的是创建一个用TLS保护的服务器，技巧96中会介绍。



