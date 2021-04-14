### 7.1　配置管理和Dockerfile

Dockerfile是构建Docker镜像的标准方式。人们常常会疑惑Dockerfile对于配置管理意味着什么。你也可能会有许多疑问（尤其是在对一些其他配置管理工具有些经验的时候），例如下面3个问题。

+ 如果基础镜像更改会发生什么？
+ 如果更改要安装的包然后重新构建会发生什么？
+ Dockerfile会取代Chef/Puppet/Ansible吗？

事实上，Dockerfile很简单：从给定的镜像开始，Dockerfile为Docker指定一系列的shell命令和元指令，从而产出最终所需的镜像。

Dockerfile提供了一个普通、简单和通用的语言来配置Docker镜像。使用Dockerfile，用户可以使用任何偏好的方式来达到所期望的最终状态。用户可以调用Puppet，可以从其他脚本里复制，甚至可以从一个完整的文件系统复制！

让我们先一起考虑一下如何处理Dockerfile带来的一些小挑战，然后再来讨论我们刚提到的那些更棘手的问题。

