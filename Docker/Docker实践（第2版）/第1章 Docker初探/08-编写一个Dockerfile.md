### 1.2.2　编写一个Dockerfile

Dockerfile是一个包含一系列命令的文本文件。本示例中我们将使用的Dockerfile如代码清单1-1所示。创建一个新目录，移动到这个目录里，然后使用这些内容创建一个名为“Dockerfile”的文件。

代码清单1-1　todoapp Dockerfile

```c
FROM node　　⇽---　定义基础镜像
LABEL maintainer ian.miell@gmail.com　　⇽---　声明维护人员
RUN git clone -q https://github.com/docker-in-practice/todo.git　　⇽---　克隆todoapp代码
WORKDIR todo　　⇽---　移动到新的克隆目录
RUN npm install > /dev/null　　⇽---　执行node包管理器的安装命令（npm）
EXPOSE 8000　　⇽---　指定从所构建的镜像启动的容器需要监听这个端口
CMD ["npm","start"]　　⇽---　指定在启动时需要执行的命令
```

Dockerfile的开始部分是使用 `FROM` 命令定义基础镜像。本示例使用了一个Node.js镜像以便访问Node.js程序。官方的Node.js镜像名为 `node` 。

接下来，使用 `LABEL` 命令声明维护人员。在这里，我们使用的是其中一个人的电子邮件地址，读者也可以替换成自己的，因为现在它是你的Dockerfile了。这一行不是创建可工作的Docker镜像所必需的，不过将其包含进来是一个很好的做法。到这个时候，构建已经继承了node容器的状态，读者可以在它上面做操作了。

接下来，使用 `RUN` 命令克隆todoapp代码。这里使用指定的命令获取应用程序的代码：在容器内运行 `git` 。在这个示例中，Git是安装在基础node镜像里的，不过读者不能对这类事情做假定。

现在使用 `WORKDIR` 命令移动到新克隆的目录中。这不仅会改变构建环境中的目录，最后一条 `WORKDIR` 命令还决定了从所构建镜像启动容器时用户所处的默认目录。

接下来，执行node包管理器的安装命令（ `npm` ）。这将为应用程序设置依赖。我们对输出的信息不感兴趣，所以将其重定向到/dev/null上。

由于应用程序使用了8000端口，使用 `EXPOSE` 命令告诉Docker从所构建镜像启动的容器应该监听这个端口。

最后，使用 `CMD` 命令告诉Docker在容器启动时将执行哪条命令。

这个简单的示例演示了Docker及Dockerfile的几个核心功能。Dockerfile是一组严格按顺序执行的有限的命令集的简单序列。它影响了最终镜像的文件和元数据。这里的 `RUN` 命令通过签出并安装应用程序影响了文件系统，而 `EXPOSE` 、 `CMD` 和 `WORKDIR` 命令影响了镜像的元数据。

