### 技巧89　在pod内访问Kubernetes API

通常，pod有可能彼此完全独立地运行，甚至可以不知道它们是作为Kubernetes集群的一部分运行的。但是，Kubernetes确实提供了丰富的API，并且使容器能够访问它，这为自检和适应性行为以及容器自行管理Kubernetes集群的能力打开了大门。

#### 问题

想要在pod内访问Kubernetes API。

#### 解决方案

使用 `curl` 从pod中的容器中访问Kubernetes API，使用可用于容器的授权信息。

这是本书中较为简短的技巧之一，但其中包含很多要学习的内容。这是它成为要学习的一种有用的技巧的原因之一。除此之外，我们将介绍：

+ `kubectl` 命令；
+ 启动Kubernetes pod；
+ 访问Kubernetes pod；
+ 一个Kubernetes反模式；
+ 不记名令牌（bearer token）；
+ Kubernetes密文；
+ Kubernetes“向下的API”。

##### 1．没有Kubenetes集群？

如果无权访问Kubernetes集群，可以有几个选择。有许多云提供商提供按需付费的Kubernetes集群。不过，为了使依赖性降到最低，我们建议使用Minikube（技巧88中已提到），它不需要信用卡。

有关如何安装Minikube的信息，参见Kubernetes官方网站上的文档。

##### 2．创建pod

首先，我们将使用 `kubectl` 命令在新的 `ubuntu pod` 中创建一个容器，然后在命令行上访问该容器中的shell，如代码清单12-2所示。（ `kubectl run` 目前在pod和容器之间是一对一的关系，尽管pod通常比容器更灵活。）

代码清单12-2　创建并设置容器

```c
$ kubectl run -it ubuntu --image=ubuntu:16.04 --restart=Never　　⇽---　使用-ti标志来运行kubectl命令，给pod命名为“ubuntu”，使用当前还算熟悉的ubuntu:16.04镜像，并且告知Kubernetes在pod/容器已经存在的时候不要重启
 If you don't see a command prompt, try pressing enter. 　　⇽---　 Kubectl告知你终端在你没有按回车键之前可能没有展示提示符
 root@ubuntu:/# apt-get update -y && apt-get install -y curl　　⇽---　在你按回车键后，这是容器内的提示符，我们会升级容器的打包系统，安装curl
 [...]
root@ubuntu:/ 　　⇽---　一旦安装完成，提示符会返回
```

现在，我们位于由 `kubectl` 命令创建的容器中，并确保已安装curl。从pod访问Kubenetes API的方法如代码清单12-3所示。



**警告**

从shell访问和修改pod被视为Kubernetes反模式。我们在这里使用它来演示在pod内可能发生的事情，而不是如何使用pod。



代码清单12-3　从pod访问Kubenetes API

```c
root@ubuntu:/# $ curl -k -X GET \　　⇽---　使用curl命令来获取Kubernetes API。-k标志允许curl无须在客户端部署的证书即可工作，和API交互的HTTP方法通过-X标志指定为GET
   -H "Authorization: Bearer \　　⇽---　-H标志给请求添加了HTTP协议头。这个是简短讨论过的授权令牌
   $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" <3> \
  https://${KUBERNETES_PORT_443_TCP_ADDR}:${KUBERNETES_SERVICE_PORT_HTTPS}　　⇽---　访问的URL地址通过pod内的环境变量构建而成
 {
  "paths": [　　⇽---　 API的默认返回值列出了可供消费的路径
    "/api",
    "/api/v1",
    "/apis",
    "/apis/apps",
    "/apis/apps/v1beta1",
    "/apis/authentication.k8s.io",
    "/apis/authentication.k8s.io/v1",
    "/apis/authentication.k8s.io/v1beta1",
    "/apis/authorization.k8s.io",
    "/apis/authorization.k8s.io/v1",
    "/apis/authorization.k8s.io/v1beta1",
    "/apis/autoscaling",
    "/apis/autoscaling/v1",
    "/apis/autoscaling/v2alpha1",
    "/apis/batch",
    "/apis/batch/v1",
    "/apis/batch/v2alpha1",
    "/apis/certificates.k8s.io",
    "/apis/certificates.k8s.io/v1beta1",
    "/apis/extensions",
    "/apis/extensions/v1beta1",
    "/apis/policy",
    "/apis/policy/v1beta1",
    "/apis/rbac.authorization.k8s.io",
    "/apis/rbac.authorization.k8s.io/v1alpha1",
    "/apis/rbac.authorization.k8s.io/v1beta1",
    "/apis/settings.k8s.io",
    "/apis/settings.k8s.io/v1alpha1",
    "/apis/storage.k8s.io",
    "/apis/storage.k8s.io/v1",
    "/apis/storage.k8s.io/v1beta1",
    "/healthz",
    "/healthz/ping",
    "/healthz/poststarthook/bootstrap-controller",
    "/healthz/poststarthook/ca-registration",
    "/healthz/poststarthook/extensions/third-party-resources",
    "/logs",
    "/metrics",
    "/swaggerapi/",
    "/ui/",
    "/version"
  ]
}
root@ubuntu:/# curl -k -X GET -H "Authorization: Bearer $(cat　　⇽---　
➥ /var/run/secrets/kubernetes.io/serviceaccount/token)"
➥ https://${KUBERNETES_PORT_443_TCP_ADDR}:
➥ ${KUBERNETES_SERVICE_ORT_HTTPS}/version　　⇽---　发起了另一个请求，这次是/version路径
 {
  "major": "1",
  "minor": "6",　　⇽---　/version请求的返回值指定了正在运行的Kubernetes的版本
  "gitVersion": "v1.6.4",
  "gitCommit": "d6f433224538d4f9ca2f7ae19b252e6fcb66a3ae",
  "gitTreeState": "dirty",
  "buildDate": "2017-06-22T04:31:09Z",
  "goVersion": "go1.7.5",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```

代码清单12-3中涵盖了许多新材料，但我们希望它给人一种无须任何设置即可动态地在Kubernetes pod中完成工作的感觉。

从代码清单12-3中获取的关键点是，该信息对pod内的用户可用，使pod可以与Kubernetes API联系。这些信息项统称为“向下的API”。目前，向下的API包括两类数据：环境变量和公开给pod的文件。

前面的示例中使用了一个文件来向Kubernetes API提供身份验证令牌。该令牌在/var/run/secrets/kubernetes.io/serviceaccount/token文件中可用。在代码清单12-3中，这一文件通过 `cat` 运行，并且 `cat` 命令的输出被作为 `Authorization` 的一部分——HTTP首部提供。这一首部指定所使用的授权属于 `Bearer` （不记名）类型，并且不记名令牌是 `cat` 的输出，因此 `curl` 的 `-H` 参数如下所示：

```c
-H "Authorization: Bearer
➥ $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)"
```



**注意**

不记名令牌是仅需要给予特定令牌而不需要其他认证（如用户名/密码）的验证方式。不记名股票的操作遵循类似的原则，即股票的持有者是有权出售股票的人。



向下的API项是Kubernetes“密文”的一种形式。可以使用Kubernetes API创建任何密文，并通过pod中的文件公开。这种机制允许将密文与Docker镜像和Kubernetes pod或部署配置分开，这意味着可以将权限与那些更开放的项目分开处理。

#### 讨论

本技巧值得关注，因为它涉及很多背景知识。要掌握的关键点是，Kubernetes pod提供了允许它们与Kubernetes API进行交互的信息。这使应用程序可以在Kubernetes中运行，以监视集群中发生的活动并对其进行操作。例如，你可能有一个基础设施pod，可以监视新涌现的pod的API，调查其活动并在其他地方记录数据。

尽管基于角色的访问控制（role based access control，RBAC）不在本书的讨论范围内，但是值得一提的是，这对安全性是有影响的，因为你不一定希望集群中的任何用户都具有这种访问级别。因此，API的某些部分将不仅仅需要不记名令牌来获得访问权限。

这些与安全性相关的考虑因素使本技巧一半与Kubernetes相关，一半与安全相关。无论哪种方式，对于希望“真正”使用Kubernetes的人来说，这都是一项重要的技巧，可以帮助他们了解API的工作方式以及它可能如何被滥用。

