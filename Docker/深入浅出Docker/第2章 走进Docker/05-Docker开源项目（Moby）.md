## 2.4　Docker开源项目（Moby）

“Docker”一词也会用于指代开源Docker项目。其中包含一系列可以从Docker官网下载和安装的工具，比如Docker服务端和Docker客户端。不过，该项目在2017年于Austin举办的DockerCon上正式命名为Moby项目。由于这次改名，GitHub上的docker/docker库也被转移到了moby/moby，并且拥有了项目自己的Logo，如图2.3所示。

![11.png](./images/11.png)
<center class="my_markdown"><b class="my_markdown">图2.3　Moby的Logo</b></center>

Moby项目的目标是基于开源的方式，发展成为Docker上游，并将Docker拆分为更多的模块化组件。Moby项目托管于GitHub的Moby代码库，包括子项目和工具列表。核心的Docker引擎项目位于GitHub的moby/moby，但是引擎中的代码正持续被拆分和模块化。

作为一个开源项目，其源码是公开可得的，在遵循Apache协议2.0的情况下，任何人都可以自由地下载、贡献、调整和使用。

如果查看项目的提交历史，可以发现其中包含来自如下公司的基础技术：红帽、微软、IBM、思科，以及HPE。此外，还可以看到一些并非来自大公司的贡献者。

多数项目及其工具都是基于Golang编写的，这是谷歌推出的一种新的系统级编程语言，又叫Go语言。使用Go语言的读者，将更容易为该项目贡献代码。

Mody/Docker作为开源项目的好处在于其所有的设计和开发都是开放的，并摒弃了私有代码闭源开发模式下的陈旧方法。因此发布过程也是公开进行的，不会再出现某个秘密的版本提前几个月就宣布要召开发布会和庆功会的荒唐情况。Moby/Docker不是这样运作的，项目中多数内容都是开放并欢迎任何人查看和作出贡献的。

Moby项目以及更广泛的Docker运动一时间掀起了一波热潮。GitHub上已经有数以千计的提交请求（pull request），以及数以万计的基于容器化技术的项目了，更不用说Docker Hub上数十亿的镜像下载。Moby项目已经给软件产业带来了翻天覆地的变化。

这并非妄想，Docker已经得到了广泛的应用！

