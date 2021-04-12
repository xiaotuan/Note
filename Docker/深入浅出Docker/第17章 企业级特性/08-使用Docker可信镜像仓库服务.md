### 17.2.5　使用Docker可信镜像仓库服务

Docker可信镜像服务是一种安全的、自行配置和管理的私有镜像库。它被集成在UCP以达到良好的开箱即用的使用体验。

本节将会介绍如何从DTR推送和拉取镜像，以及如何使用DTR Web界面来查看和管理镜像库。

##### 1．登录到DTR界面并创建镜像库及权限

下面登录到DTR，并创建一个新的镜像库，该库对所有的 `technology/devs` 团队的成员开放推送和拉取镜像的权限。

登录到DTR。DTR的URL可以在UCP Web界面的 `Admin > Admin Settings > Docker Trusted Registry` 下找到。注意，DTR Web界面可以通过端口443的HTTPS访问。

创建一个新的组织和团队，然后添加一个用户。本例将创建一个名为 `technology` 的组织、一个名为 `devs`  的团队和一个名为 `nigelpoulton` 的用户。读者请根据具体情况自行调整。

（1）单击左侧导航栏的 `Organizations` （组织）。

（2）单击 `New Organization` （新建组织）并命名为 `technology` 。

（3）选择新创建的 `technology` 组织，并单击 `TEAMS` （组织）旁的+按钮，如图17.11所示。

![133.png](./images/133.png)
<center class="my_markdown"><b class="my_markdown">图17.11　单击 `TEAMS` （组织）旁的+按钮</b></center>

（4）在选择 `devs` 团队的情况下，添加一个用户。

本例会添加名为 `nigelpoulton` 的用户，读者环境中的用户名会有不同。

DTR中对组织和团队的修改也会反映在UCP中，因为它们共享账号数据库。

接下来创建一个新的镜像库，并添加 `technology/devs` 团队的读/写权限。

在DTR Web界面中进行如下操作。

+ 进入 `Organizations > technology > devs` 。
+ 选择 `Repositories` （库）页签，并创建一个新的镜像库。
+ 对镜像库进行如下配置。

在 **technology** 组织下创建的 **新** 镜像库命名为 **test** 。将其配置为 **公开（Public）** ，开启 **推送时扫描（SCAN ON PUSH）** ，并分配 **读/写（Read-write）** 权限。具体配置如图17.12所示。

![134.png](./images/134.png)
<center class="my_markdown"><b class="my_markdown">图17.12　创建一个新的DTR镜像库</b></center>

（4）保存修改。

恭喜！读者在DTR上已经有一个名为 `<dtr-url>/technology` 的镜像库了， `technology/devs`  团队对其有读/写权限，因此他们可以对其进行 `push` 和 `pull` 操作。

##### 2．推送镜像到DTR库

本节将演示如何推送一个新镜像到刚刚创建的镜像库。具体通过以下几个步骤来完成。

（1）拉取一个镜像并从新打标签。

（2）为客户端配置一组证书。

（3）推送打了新标签的镜像到DTR库。

（4）在DTR Web界面中检查操作过程。

首先拉取一个镜像，并为其打标签，以便能够推送到DTR仓库。拉取什么镜像并不重要。本例使用的是 `alpine:latest` 镜像，因为它很小。

```rust
$ docker pull alpine:latest
latest: Pulling from library/alpine
ff3a5c916c92: Pull complete
Digest: sha256:7df6...b1c0
Status: Downloaded newer image for alpine:latest
```

为了推送一个镜像到一个具体的仓库，需要将镜像用库的名称打标签。本例中，DTR库的全限定名为 `dtr.mydns.com/technology/test` 。这个名字是由DTR的DNS域名与镜像库的名称组合得到的。读者的会有差异。

为该镜像打标签，以便能够推送到DTR库。

```rust
$ docker image tag alpine:latest dtr.mydns.com/technology/test:v1
```

下一步就是要配置Docker客户端，使其用对该库有读/写权限的组内的用户来认证。总体来说就是为该用户创建一组证书，并配置Docker客户端使用这些证书。

（1）以管理员身份登录UCP，或使用有读/写权限的用户登录。

（2）导航到目标用户账号，然后创建一个 `client bundle` 。

（3）复制Bundle文件到需要进行配置的Docker客户端。

（4）登录到Docker客户端，并执行以下命令。

（5）解压Bundle，并执行Shell脚本来进行配置。

以下命令可用于Mac和Linux。

```rust
$ eval "$(<env.sh)"
```

（6）执行 `docker version` 命令以确定环境配置和证书配置是否正确。

如果输出内容的 `Server` 部分显示 `Version` 为 `ucp/x.x.x` ，则表示已经正确配置。这是因为Shell脚本对Docker客户端进行了配置，使其连接到UCP Manager上的一个远端daemon。并且还会令Docker客户端使用证书对所有的命令进行签名。

接下来登录到DTR。读者的DTR URL和用户名会有差异。

```rust
$ docker login dtr.mydns.com
Username: nigelpoulton
Password:
Login Succeeded
```

现在可以推送打标签的镜像到DTR了。

```rust
$ docker image push dtr.mydns.com/technology/test:v1
The push refers to a repository [dtr.mydns.com/technology/test]
cd7100a72410: Pushed
v1: digest: sha256:8c03...acbc size: 528
```

可见推送操作是成功的，下面在DTR的Web界面中进行确认。

（1）先登录到DTR的Web界面。

（2）单击左侧导航栏中的 `Repositories` 。

（3）单击 `technology/test` 库的 `View Details` （查看细节）。

（4）单击 `IMAGES` （镜像）页签。

DTR库中的镜像如图17.13所示。可见图中镜像为基于Linux的镜像，它有3个主要缺陷。缺陷信息的出现是由于之前对镜像库中新推送的镜像开启了缺陷扫描。

![135.png](./images/135.png)
<center class="my_markdown"><b class="my_markdown">图17.13　DTR库中的镜像</b></center>

恭喜。读者现在已经成功地将镜像推送到DTR上的新镜像库中。这时可以通过勾选镜像左侧的复选框来删除它。由于删除操作是不可逆的，因此一定要谨慎操作。

