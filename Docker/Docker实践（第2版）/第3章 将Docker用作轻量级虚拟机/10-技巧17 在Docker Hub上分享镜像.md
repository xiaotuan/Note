### 技巧17　在Docker Hub上分享镜像

如果能和其他人分享这些名字（和镜像），给镜像打标签的时候用一些带描述的名字可能会更有帮助。为了满足这一需求，Docker提供了轻松将镜像迁移到其他地方的能力，且Docker公司也创建了Docker Hub这一免费服务以鼓励这样的分享。



**注意**

要利用本技巧，用户将需要一个Docker Hub账号，并且它已经在宿主机上通过执行 `docker login` 登录过。如果还没有配置这样的一个账号，可以到Docker Hub上创建一个。只需要照着注册说明的指示去做即可。



#### 问题

想要公开分享一个Docker镜像。

#### 解决方案

使用Docker Hub注册中心（registry）来分享镜像。

当讨论标签时，注册中心相关的各种术语可能容易让人混淆。表3-2应该有助于理解这些术语该如何使用。

<center class="my_markdown"><b class="my_markdown">表3-2　Docker注册中心的术语</b></center>

| 术 语 | 含 义 |
| :-----  | :-----  | :-----  | :-----  |
| 用户名（user name） | Docker注册中心上的用户名 |
| 注册中心（registry） | 注册中心持有镜像。一个注册中心就是一个可以上传镜像或者从这里下载镜像的存储。注册中心可以是公开的，也可以是私有的 |
| 注册中心宿主机（registry host） | 运行Docker注册中心的宿主机 |
| Docker Hub | 托管在官方网站上公开默认的注册中心 |
| 索引（index） | 与注册中心宿主机含义相同，这已经是一个过时的术语 |

正如之前所见，只要喜欢，用户可以给一个镜像打上多个标签。这对复制过来的镜像很有用，如此一来用户便拥有了它的控制权。

我们不妨假设用户在Docker Hub上的用户名是 `adev` 。代码清单3-21给出的3条命令展示了怎样从Docker Hub上将 `debian:wheezy` 镜像复制到自己的账号下。

代码清单3-21　将一个公用镜像复制和推送到adev的Docker Hub账号

```c
docker pull debian:wheezy　　⇽---　从Docker Hub上拉取debian镜像
docker tag debian:wheezy adev/debian:mywheezy1　　⇽---　给wheezy镜像打上自己的用户名（adev）并且指定一个标签（mywheezy1）
docker push adev/debian:mywheezy1　　⇽---　推送新创建的标签
```

至此，用户已经得到了一个下载好的Debian wheezy镜像的引用，可以维护、关联或者以它为基础构建其他镜像。

如果有可以推送的私有仓库，除了必须在标签的前面指定注册中心的地址外，其他流程是完全一致的。假设有一个仓库放在http://mycorp.private.dockerregistry。代码清单3-22中列出的命令将会为镜像打上标签然后推送到该注册中心。

代码清单3-22　将一个公用镜像复制并推送到adev的私有注册中心

```c
docker pull debian　　⇽---　从Docker Hub上拉取Debian镜像
docker tag debian:wheezy \
mycorp.private.dockerregistry/adev/debian:mywheezy1　　⇽---　用注册中心（mycorp.private.dockerregistry）、用户名（adev）和标签（mywheezy1）给wheezy镜像打上标签
docker push mycorp.private.dockerregistry/adev/debian:mywheezy1　　⇽---　将新创建的标签推送到私有注册中心。需要注意的是，在打标签和推送时都必须指定私有注册中心服务器的地址，这样一来Docker才能确保把它推送到正确的位置
```

上述命令将不会把镜像推送到公有的Docker Hub上，而是会把它推送到私有的仓库里，因此任何人只要可以访问该服务上的资源就能够拉取它。

#### 讨论

至此，用户已经具备了和其他人分享镜像的能力。这是一个同其他工程师分享工作成果、想法甚至于遇到的一些问题的绝佳办法。

正如GitHub不是唯一的公开可用的Git服务器一样，Docker Hub也不是唯一的公开可用的Docker注册中心。但是，同GitHub一样，它也是最流行的。

再者，和Git服务器类似，公有的和私有的Docker注册中心可能提供了不同的功能和特性，其中可能有一方或是另外一方吸引到你。你在评估的时候可能会考虑一些东西，如成本（购买、订阅或维护）、遵守的API协议、安全特性和性能等。

在技巧18中，我们将会了解如何引用特定的镜像来帮助避免在未指定使用的镜像时遇到问题。

