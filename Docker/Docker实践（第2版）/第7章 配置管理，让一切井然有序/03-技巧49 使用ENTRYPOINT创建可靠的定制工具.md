### 技巧49　使用ENTRYPOINT创建可靠的定制工具

Docker允许在 **任何地方** 执行命令的潜质意味着在命令行上执行的一些复杂的定制指令或脚本可以预先配置然后包装到一个打包好的工具中。

容易被曲解的 `ENTRYPOINT` 指令便是这其中的一个重要部分。用户将能看到它是怎样帮助我们创建出一些作为工具的镜像的，这些工具镜像封装良好，定义清晰，并且具备十分有用的灵活性。

#### 问题

想要定义容器将会执行的命令，但是将命令的具体参数留给用户。

#### 解决方案

使用Dockerfile的 `ENTRYPOINT` 指令。

作为演示，不妨试想一下企业里有一个这样的简单场景：有一个常规的管理任务是要清理旧的日志文件。通常这很容易出错，人们可能会意外删错东西，因此我们打算使用一个Docker镜像来降低出现问题的风险。

代码清单7-1中给出的脚本（用户应该在保存的时候将其命名为 `clean_log` ）会删除超过特定天数的日志，其中具体天数作为一个命令行选项传入。在任意地方创建一个任意名字的目录，进入该目录，然后将 `clean_log` 脚本放入该目录：

代码清单7-1　clean_log shell脚本

```c
#!/bin/bash
echo "Cleaning logs over $1 days old"
find /log_dir -ctime "$1" -name '*log' -exec rm {} \;
```

注意，这一脚本清理的是/log_dir文件夹下的日志。此文件夹只有在运行时挂载了它才会存在。你可能还会注意到，这里没有检查是否有参数传给该脚本。这样做的原因我们会在后面介绍这一技巧时披露。

现在，让我们在同一目录下新建一个Dockerfile来创建一个镜像，这个Dockerfile包含代码清单7-2中给出的脚本作为定义好的命令来执行，或者叫 **入口点** （entrypoint）。

代码清单7-2　创建一个使用clean_log脚本的镜像

```c
FROM ubuntu:17.04
ADD clean_log /usr/bin/clean_log　　⇽---　将之前组织好的clean_log脚本添加到镜像里
RUN chmod +x /usr/bin/clean_log
ENTRYPOINT ["/usr/bin/clean_log"]　　⇽---　将此镜像的入口点定义为clean_log脚本
CMD ["7"]　　⇽---　设置ENTRYPOINT命令的默认参数（7天）
```



**提示**

你可能会发现，相比于shell形式（ `CMD /usr/bin/command` ），我们更喜欢用 `CMD` 和 `ENTRYPOINT` 的数组形式（如 `CMD ["/usr/bin/command"]` ）。这是因为，如果是shell形式，它会自动在用户提供的命令前面加上一个 `/bin/bash -c` 的命令，这可能会导致难以预料的行为。然而，在某些时候shell形式反而会更有用些（见技巧55）。



人们常常费解 `ENTRYPOINT` 和 `CMD` 之间到底有什么区别。要理解的关键点是，入口点总会在镜像启动之后运行，即使命令被提供给 `docker run` 调用。如果用户尝试传入一条命令，它将会作为参数被传给入口点，然后取代在 `CMD` 指令部分定义的默认值。用户只能通过显式地传入一个 `--entrypoint` 标志给 `docker run` 命令来覆盖入口点。

这就意味着，通过/bin/bash命令运行镜像将不会提供一个shell，而会将/bin/bash作为 `clean_log` 脚本的参数。

通过 `CMD` 指令定义好默认参数，就意味着不需要再检查是否有传入参数。下列命令展示了该如何构建和调用此工具：

```c
docker build -t log-cleaner .
docker run -v /var/log/myapplogs:/log_dir log-cleaner 365
```

在构建完该镜像后，通过将/var/log/myapplogs挂载到脚本将用到的目录，并传入 `365` 以删除过去一年（而不是一周）的日志文件。

如果有人尝试以不指定天数这样的不正确方式使用镜像，将会得到一条报错消息：

```c
$ docker run -ti log-cleaner /bin/bash
Cleaning logs over /bin/bash days old
find: invalid argument '-name' to '-ctime'
```

#### 讨论

这个例子的确相当简单，不过试想一下，一家企业便可以借此跨资源集中管理脚本，以便可以通过一个私有的注册中心维护和安全地分发脚本。

读者可以在Docker Hub上的dockerinpractice/log-cleaner查看并使用我们在本技巧中创建的镜像。

