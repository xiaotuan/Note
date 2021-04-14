### 13.3.1　云原生计算基金会（CNCF）

云原生计算基金会（CNCF）与众不同之处在于它不是一家公司，但它可能是这个领域中最具影响力的参与者。CNCF成立于2015年，旨在推广容器技术的通用标准。其创始成员包括谷歌、Twitter、英特尔、思科、IBM、Docker和VMWare。它的创建与Kubernetes 1.0的发布同时进行，该版本由谷歌捐赠给CNCF（尽管它早已由谷歌开源了）。

CNCF在容器领域的影响力非常大。由于所涉及的各个参与者的集体力量是如此之大，因此，当CNCF支持一项技术时，你就知道了：它将有投资和支持，而另一家供应商不太可能会受到青睐。后一个因素对Docker平台使用者特别重要，因为这意味着你的技术选择在可预见的将来不太可能被淘汰。

CNCF认可的技术清单很长（而且还在不断增长）。我们将介绍一些最重要的，如Kubernetes、CNI、Containerd、Envoy、Notary和Prometheus。

##### 1．Kubernetes

Kubernetes是CNCF的创始和最重要的技术。它是由谷歌捐赠给社区的，首先是作为开源软件，然后是归CNCF所有。

尽管它是开源的，但对社区的捐赠却是谷歌进行云技术商品化战略的一部分，由此使消费者更容易脱离其他云提供方，其中最主要的是AWS。

Kubernetes是大多数Docker平台（最著名的是OpenShift）、Rancher甚至是Docker公司自己的Docker Datacenter的基础技术，因为这些平台除了支持Swarm外，还支持Kubernetes。

##### 2．CNI

CNI（Container Network Interface）表示容器网络接口。该项目提供了用于管理容器网络接口的标准接口。正如你在第10章中所看到的那样，网络可能是容器管理的一个复杂领域，而该项目旨在帮助简化其管理。

这是一个（非常）简单的示例，它定义了一个回送接口：

```c
{
    "cniVersion": "0.2.0",
    "type": "loopback"
}
```

该文件可以放在/etc/cni/net.d/99-loopback.conf中，并用于配置回送网络接口。

##### 3．Containerd

Containerd是Docker守护程序的社区版本。它管理容器的生命周期。Runc是它的姊妹项目，它是负责运行容器本身的运行时。

##### 4．Envoy

Envoy最初是在Lyft上构建的，目的是将其架构从单体架构转变为微服务架构，它是一种高性能的开源边缘和服务代理，使网络对应用程序透明。

它允许直接管理关键网络和集成挑战，如负载平衡、代理和分布式跟踪。

##### 5．Notary

Notary最初是由Docker公司设计和构建的工具，用于签名和验证容器镜像的完整性（见13.2.1节）。

##### 6．Prometheus

Prometheus是一款监视工具，可以很好地与容器配合使用。它在社区中获得越来越多的认可，例如Red Hat在其OpenShift平台上从Hawkular更换到Prometheus。

