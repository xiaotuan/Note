### 5.2.5　containerd

在对Docker daemon的功能进行拆解后，所有的容器执行逻辑被重构到一个新的名为containerd（发音为container-dee）的工具中。它的主要任务是容器的生命周期管理—— `start`  |  `stop`  |  `pause`  |  `rm` ....

containerd在Linux和Windows中以daemon的方式运行，从1.11版本之后Docker就开始在Linux上使用它。Docker引擎技术栈中，containerd位于daemon和runc所在的OCI层之间。Kubernetes也可以通过cri-containerd使用containerd。

如前所述，containerd最初被设计为轻量级的小型工具，仅用于容器的生命周期管理。然而，随着时间的推移，它被赋予了更多的功能，比如镜像管理。

其原因之一在于，这样便于在其他项目中使用它。比如，在Kubernetes中，containerd就是一个很受欢迎的容器运行时。然而在Kubernetes这样的项目中，如果containerd能够完成一些诸如push和pull镜像这样的操作就更好了。因此，如今containerd还能够完成一些除容器生命周期管理之外的操作。不过，所有的额外功能都是模块化的、可选的，便于自行选择所需功能。所以，Kubernetes这样的项目在使用containerd时，可以仅包含所需的功能。

containerd是由Docker公司开发的，并捐献给了云原生计算基金会（Cloud Native Computing Foundation, CNCF）。2017年12月发布了1.0版本，具体的发布信息见GitHub中的containerd/ containerd库的releases。

