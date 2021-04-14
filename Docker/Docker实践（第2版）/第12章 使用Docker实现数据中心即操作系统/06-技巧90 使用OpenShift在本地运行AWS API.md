### 技巧90　使用OpenShift在本地运行AWS API

本地开发最大的挑战之一是针对其他服务测试应用程序。如果可以将服务放在容器中，则Docker可以提供帮助，但在外部第三方服务的庞大世界中这是尚未解决的问题。

常见的解决方案是拥有测试API实例，但是这些实例通常会提供假响应——如果围绕服务构建应用程序，则无法进行更完整的功能测试。例如，假设你想将AWS S3用作应用程序的上传位置，然后在该位置上处理应用程序——对此进行测试会花钱。

#### 问题

想要在本地使用类似AWS的API进行开发。

#### 解决方案

设置LocalStack并使用可用的AWS服务替代物。

在本演练中，我们将使用Minishift设置OpenShift系统，然后在其pod中运行LocalStack。OpenShift是由RedHat赞助的对Kubernetes的包装，它提供了更适合Kubernetes企业生产环境部署的额外功能。

在本技巧中，我们将介绍：

+ OpenShift中路由的创建；
+ 安全上下文约束；
+ OpenShift和Kubernetes之间的区别；
+ 使用公共Docker镜像测试AWS服务。



**注意**

要学习本技巧，需要安装Minishift。Minishift和在技巧89中所见的Minikube类似。不同之处在于，它包含了对OpenShift的安装（在技巧99中详细解释）。



##### 1．LocalStack

LocalStack是一个旨在为开发者提供尽可能完整的一组AWS API的项目，依赖这些API开发不会产生任何费用。这对于在真正花费时间和金钱之前针对AWS进行测试或尝试编码非常有用。

LocalStack在本地机器上启动以下核心Cloud API：

+ API Gateway，位于http://localhost:4567；
+ Kinesis，位于http://localhost:4568；
+ DynamoDB，位于http://localhost:4569；
+ DynamoDB Streams，位于http://localhost:4570；
+ Elasticsearch，位于http://localhost:4571；
+ S3，位于http://localhost:4572；
+ Firehose，位于http://localhost:4573；
+ Lambda，位于http://localhost:4574；
+ SNS，位于http://localhost:4575；
+ SQS，位于http://localhost:4576；
+ Redshift，在http://localhost:4577；
+ ES（Elasticsearch Service），位于http://localhost:4578；
+ SES，位于http://localhost:4579；
+ Route53，位于http://localhost:4580；
+ CloudFormation，位于http://localhost:4581；
+ CloudWatch，位于http://localhost:4582。

LocalStack支持在Docker容器中或本机上运行。它是基于Moto构建的，而Moto是基于Boto构建的模拟框架，而Boto又是Python AWS开发工具包。

在OpenShift集群中运行使我们能够运行许多AWS API环境。然后，我们就可以为每组服务创建不同的端点，并将它们彼此隔离。另外，我们可以减少对资源使用的担心，因为集群调度程序将解决这一问题。但是，LocalStack并不是开箱即用的，因此我们将指导读者完成需要完成的操作。

##### 2．确保Minishift安装好了

至此，我们假设读者已经设置好了Minishift（读者可以查看其有关入门的官方文档）。检查Minishift是否安装正确的方法如代码清单12-4所示。

代码清单12-4　检查Minishift安装正确

```c
$ eval $(minishift oc-env)
$ oc get all
No resources found.
```

##### 3．更改默认安全上下文约束

安全上下文约束（security context constraints，SCC）是OpenShift概念，允许对Docker容器的功能进行更细粒度的控制。安全上下文约束控制SELinux上下文（见技巧100），可以从正在运行的容器中删除功能（见技巧93），可以确定pod可以作为哪个用户运行，等等。

为了使它运行，我们需要更改默认的 `restricted` （受限的）SCC。读者也可以创建一个单独的SCC，并将其应用于特定项目，读者可以自己尝试。

要更改“受限的”SCC，我们需要成为集群管理员：

```c
$ oc login -u system:admin
```

然后可以通过下列命令编辑“受限的”SCC：

```c
$ oc edit scc restricted
```

我们会看到 `restricted` SCC的定义。

此时我们必须要做的两件事情是：

+ 允许容器作为任意用户运行（本例中是 `root` ）；
+ 防止SCC把我们的能力限制在 `setuid` 和 `setgid` 。

##### 4．允许作为任意用户运行

默认情况下，LocalStack容器以root身份运行，但是出于安全原因，OpenShift不允许容器默认以root身份运行。相反，它会在非常高的范围内选择一个UID，并以此UID身份运行。注意，UID是数字，与用户名不同，用户名是映射到UID的字符串。

为了简化问题，并允许LocalStack容器以root身份运行，将

```c
runAsUser:
 type: MustRunAsRange
```

改为

```c
runAsUser:
 type: RunAsAny
```

这让容器可以作为 **任意** 用户运行，而不是作为UID范围内的一个用户运行。

##### 5．允许SETUID和SETGID的能力

当LocalStack启动时，它需要成为另一个用户才能启动ElastiCache。ElastiCache服务无法以root用户身份启动。

为了解决这个问题，使用LocalStack的 `su` 命令作为向容器中的LocalStack用户发送的启动命令。由于受限的SCC明确禁止更改用户ID或组ID的操作，因此我们需要删除这些限制。为此，要删除以下几行：

```c
- SETUID
- SETGID
```

##### 6．保存文件

完成了前面两步，就该保存文件了。

记下宿主机。如果执行下面的命令，可以获得本地机器可访问的Minishift实例：

```c
$ minishift console --machine-readable | grep HOST | sed 's/^HOST=\(.*\)/\1/'
```

记下这一宿主机，后面需要替换。

##### 7．部署pod

部署LocalStack只需要简单执行下面的命令：

```c
$ oc new-app localstack/localstack --name="localstack"
```

这将获取localstack/localstack镜像并围绕它创建一个OpenShift应用程序，设置内部服务（基于LocalStack Docker镜像的Dockerfile中公开的端口），在pod中运行该容器，并执行其他各种管理任务。

##### 8．创建路由

如果要从外部访问服务，则需要创建OpenShift路由，该路由会创建用于访问OpenShift网络中的服务的外部地址。例如，要为SQS服务创建路由，就要创建代码清单12-5所示的文件，称为route.yaml。

代码清单12-5　route.yaml

```c
apiVersion: v1　　⇽---　在yaml文件的顶部指定了Kubernetes API版本
 kind: Route　　⇽---　创建的对象类型指定为Route
 metadata: 　　⇽---　元数据部分包含有关路由的信息，而不是路由本身的规范
   name: sqs　　⇽---　在此为路由命名
 spec: 　　⇽---　 spec部分指定路线的详细信息
   host: sqs-test.HOST.nip.io　　⇽---　 host是路由将被映射到的URL，即客户端访问的URL
   port: 　　⇽---　
     targetPort: 4576-tcp　　⇽---　 port部分在to部分中指定的服务上标识路由将到达的端口
   to: 　　⇽---　 to部分标识将请求路由到的位置
     kind: Service　　⇽---　
     name: localstack　　⇽---　在本例中，它起源于LocalStack服务
```

通过执行下面的命令创建路由：

```c
$ oc create -f route.yaml
```

这会创建刚才创建的yaml文件描述的路由。然后对每个想要设置的服务重复这一过程。

然后执行 `oc get all` 来查看刚才在OpenShift项目里创建了什么：

```c
$ oc get all　　⇽---　返回OpenShift项目中最重要的项目
 NAME DOCKER REPO TAGS UPDATED　　⇽---　
 is/localstack 172.30.1.1:5000/myproject/localstack latest 15 hours ago　　⇽---　首先列出的是镜像流。这些是跟踪本地或远程镜像状态的对象
 NAME REVISION DESIRED CURRENT TRIGGERED BY　　⇽---　
 dc/localstack 1 1 1 config,image(localstack:latest) 　　⇽---　接下来列出部署配置，这些配置指定了将pod部署到集群的方式
 NAME DESIRED CURRENT READY AGE　　⇽---　
 rc/localstack-1 1 1 1 15　　⇽---　第三类是复制配置，它指定正在运行的Pod的复制特征
 NAME HOST/PORT PATH SERVICES PORT TERMINATION WILDCARD　　⇽---　第四类是在项目中设置的路由
 routes/sqs sqs-test.192.168.64.2.nip.io localstack 4576-tcp None
 NAME CLUSTER-IP EXTERNAL-IP PORT(S) AGE　　⇽---　
 svc/localstack 172.30.187.65 4567/TCP,4568/TCP,4569/TCP,4570/TCP,4571/TCP,
➥ 4572/TCP,4573/TCP,4574/TCP,4575/TCP,4576/TCP,4577/TCP,4578/TCP, 
➥ 4579/TCP,4580/TCP,4581/TCP,4582/TCP,8080/TCP 15h　　⇽---　列出的下一类是服务。在这里，可以看到Dockerfile中公开的端口会使得该服务公开端口
 NAME READY STATUS RESTARTS AGE　　⇽---　
 po/localstack-1-hnvpw 1/1 Running 0 15h　　⇽---　最后，列出了项目中的pod
```

尽管从技术上来讲， `oc get all` 命令显示的并不是项目中可用的 **所有** 对象，但是它显示了对运行应用程序最重要的项目。

现在就可以将类似于SQS的AWS服务作为URL端点进行访问，以对我们的代码进行测试了。

##### 9．访问服务

现在，我们可以从宿主机上访问这一服务。下面是创建SQS流的示例：

```c
 $ aws --endpoint-url=http://kinesis-test.192.168.64.2.nip.io kinesis
➥ list-streams　　⇽---　 aws客户端应用程序用于访问新创建的网络接口，并要求kinesis列出其流
 {　　⇽---　
  "StreamNames": []
 }　　⇽---　 JSON输出显示不存在流
 $ aws --endpoint-url=http://kinesis-test.192.168.64.2.nip.io kinesis
➥ create-stream --stream-name teststream --shard-count 2　　⇽---　再次调用aws客户端以创建名为teststream的SQS流，其分片计数为2
 $ aws --endpoint-url=http://kinesis-test.192.168.64.2.nip.io kinesis
➥ list-streams　　⇽---　同样，您要求提供kinesis流列表
 {　　⇽---　
  "StreamNames": [
  "teststream"
  ]
 }　　⇽---　 JSON输出表明存在一个称为teststream的流
```



**注意**

我们需要安装 `aws` 客户端。另外，可以直接对API端点执行 `curl` 命令，但是我们不建议这样做。这样做还需要你已经执行 `aws configure` 并指定了你的AWS密钥和默认区域。指定的实际值与LocalStack无关，因为它不进行身份验证。



这里我们只介绍了一种服务，但是这一技巧很容易扩展到本技巧开头列举的其他项目中。

#### 讨论

本技巧使我们了解了OpenShift（以及OpenShift所基于的Kubernetes）的强大功能。要使用可用端点启动有用的应用，并处理所有内部连接，在很多方面都是实现Docker提供的可移植性承诺，并将其纵向拓展到数据中心。

例如，可以更进一步，可以在同一OpenShift集群上部署多个LocalStack实例。可以并行进行针对AWS API的测试，而不必花费更多的资源（当然，这取决于OpenShift集群的大小和测试的需求）。因为这就是全部代码，所以可以设置持续集成以动态启动和关闭LocalStack实例，以便在每次AWS代码库提交的时候与之对话。

除指出了Kubernetes的各个方面之外，这一特殊技巧还证明了OpenShift之类的产品正在Kubernetes之上构建以扩展其功能。例如，安全上下文约束是一个OpenShift概念（尽管安全上下文也存在于Kubernetes中），“路由”是一个在Kubernetes之上创建的OpenShift概念，这一概念最终直接用于Kubernetes中的实现。随着时间的流逝，为OpenShift开发的功能已被Kubernetes所采用，并已成为其产品的一部分。

在技巧99中我们将再次看到OpenShift，到时候我们将研究如何将其用作平台，安全地让用户运行容器。

