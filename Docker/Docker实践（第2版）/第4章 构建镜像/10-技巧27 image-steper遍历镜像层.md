### 技巧27　image-steper遍历镜像层

如果用户构建了一个包含许多步骤的镜像，往往会发现自己想要知道某个特定的文件是在哪里加进来的，又或者说想知道构建过程中的某个特定时间点该文件处于什么状态。梳理每个镜像层可能很费力，因为用户必须确定层的顺序，检索每个层的ID，然后逐个用ID来启动。

本技巧以一层一行的形式为用户展示了构建过程中按顺序排列每个层对应的镜像标签，这意味着用户处理镜像时只需要增加行号数字便可以找出想要知道的任意内容。

#### 问题

希望可以轻松地引用构建过程中的每一步。

#### 解决方案

使用docker-in-practice/image-stepper镜像来为用户的镜像标签排序。为了说明这一技巧，我们首先将为用户展示一段实现该结果的脚本，这样用户便能理解它的工作原理。

随后，我们将为用户提供一个预设好的镜像，让实现任务变得更加简单。这里有一段简单的脚本，它会给一个指定镜像（myimage）的每个层按照创建顺序打上标签。代码清单4-22给出的是myimage的Dockerfile。

代码清单4-22　带有多个层的镜像的Dockerfile

```c
FROM debian　　⇽---　使用debian作为基础镜像
RUN touch /file1　　⇽---　
RUN touch /file2
RUN touch /file3
RUN touch /file4
RUN touch /file5
RUN touch /file6
RUN touch /file7
RUN touch /file8
RUN touch /file9
RUN touch /file10　　⇽---　在单独的层里分别创建10个文件
CMD ["cat","/file1"]　　⇽---　执行一个定制命令，展示第一个文件的内容
```

这是一份足够简单的Dockerfile，但是它可以清晰地告诉用户现在在构建的哪个阶段。可以通过代码清单4-23所示的命令构建此docker镜像。

代码清单4-23　构建myimage镜像

```c
$ docker build -t myimage -q . 　　⇽---　构建镜像时带上-q（静默）标志，给该镜像打上myimage的标签
 sha256:b21d1e1da994952d8e309281d6a3e3d14c376f9a02b0dd2ecbe6cabffea95288　　⇽---　镜像ID是唯一的输出内容
```

一旦镜像构建成功，用户就可以运行代码清单4-24给出的脚本。

代码清单4-24　按照数字顺序给myimage的每个层打上标签

```c
#!/bin/bash
x=1　　⇽---　将计数器变量（x）初始化为1
 for id in $(docker history -q "myimage:latest" |　　⇽---　运行一个for循环来检索该镜像的历史
➥ grep -vw missing　　⇽---　不考虑远程构建的被标记为missing的镜像层（请参阅下面的注释）
➥ | tac) 　　⇽---　使用tac实用程序来反转docker history命令输出的镜像ID的顺序
 do
    docker tag "${id}" "myimage:latest_step_${x}"　　⇽---　在循环的每次迭代中，使用递增的数字给每个镜像层适当地打上标签
     ((x++))　　⇽---　递增步数计数器
 done
```

如果用户将前面的文件保存为tag.sh然后运行它，该镜像会按照层的顺序逐一打上标签，如代码清单4-25所示。



**注意**

这个打标签方法的技巧仅适用于本地构建的镜像。更多信息参见技巧16中的注释。



代码清单4-25　给层打上标签并展示

```c
 $ ./tag.sh　　⇽---　执行代码清单4-24中的脚本
 $ docker images | grep latest_step　　⇽---　执行一条docker images命令并带上一个简单的grep来查看打上标签的层
 myimage   latest_step_12   1bfca0ef799d   3 minutes ago   123.1 MB　　⇽---　
 myimage   latest_step_11   4d7f66939a4c   3 minutes ago   123.1 MB
 myimage   latest_step_10   78d31766b5cb   3 minutes ago   123.1 MB
 myimage   latest_step_9    f7b4dcbdd74f   3 minutes ago   123.1 MB
 myimage   latest_step_8    69b2fa0ce520   3 minutes ago   123.1 MB
 myimage   latest_step_7    b949d71fb58a   3 minutes ago   123.1 MB
 myimage   latest_step_6    8af3bbf1e7a8   3 minutes ago   123.1 MB
 myimage   latest_step_5    ce3dfbdfed74   3 minutes ago   123.1 MB
 myimage   latest_step_4    598ed62cabb9   3 minutes ago   123.1 MB
 myimage   latest_step_3    6b290f68d4d5   3 minutes ago   123.1 MB
 myimage   latest_step_2    586da987f40f   3 minutes ago   123.1 MB　　⇽---　构建myimage镜像的一系列步骤
 myimage   latest_step_1    19134a8202e7   7 days ago      123.1 MB　　⇽---　最初的（和比较旧的）基础镜像也被打上了latest_step_1的标签
```

如今我们已经了解了这个技巧的工作原理，下面我们将演示该如何将这个一键脚本Docker化，然后使它适用于一般用途。



**注意**

此技巧的源码可以在https://github.com/docker-in-practice/image-stepper找到。



首先，将前面的脚本改成可以接受参数的脚本，如代码清单4-26所示。

代码清单4-26　image-stepper镜像的通用打标签脚本

```c
#!/bin/bash　　⇽---　
 IMAGE_NAME=$1
 IMAGE_TAG=$2
 if [[ $IMAGE_NAME = '' ]]
 then
     echo "Usage: $0 IMAGE_NAME [ TAG ]"
     exit 1
 fi
 if [[ $IMAGE_TAG = '' ]]
 then
     IMAGE_TAG=latest
 fi　　⇽---　定义一个接受两个参数的bash脚本：要处理的镜像名称，以及想要打上标签的某个步骤
 x=1　　⇽---　
 for id in $(docker history -q "${IMAGE_NAME}:${IMAGE_TAG}" |
➥ grep -vw missing | tac)
 do
      docker tag "${id}" "${IMAGE_NAME}:${IMAGE_TAG}_step_$x"
      ((x++))
 done　　⇽---　代码清单4-24里的脚本，其中参数被替换了
```

然后可以将代码清单4-26里的脚本嵌入一个准备好了一份Dockerfile并且运行默认的 `ENTRYPOINT` 的Docker镜像里，如代码清单4-27所示。

代码清单4-27　image-stepper镜像的Dockerfile

```c
 FROM ubuntu:16.04　　⇽---　使用Ubuntu作为基础镜像层
 RUN apt-get update -y && apt-get install -y docker.io　　⇽---　安装docker.io获取Docker客户端程序
 ADD image_stepper /usr/local/bin/image_stepper　　⇽---　将代码清单4-26里的脚本添加到镜像里
 ENTRYPOINT ["/usr/local/bin/image_stepper"]　　⇽---　默认执行image_stepper脚本
```

代码清单4-27里的Dockerfile将会创建一个运行代码清单4-26里的脚本的镜像。代码清单4-28中的命令会将 `myimage` 作为指定参数，运行此镜像。

代码清单4-28　针对其他镜像运行image-stepper

```c
$ docker run --rm　　⇽---　基于image-stepper镜像运行一个容器，然后在完成后删除该容器
➥ -v /var/run/docker.sock:/var/run/docker.sock　　⇽---　将宿主机上的docker套接字挂载到容器里，这样用户便可以使用在代码清单4-27里安装的Docker客户端
➥ dockerinpractice/image-stepper　　⇽---　从Docker Hub下载image-stepper镜像
➥ myimage　　⇽---　给之前创建的myimage打上标签
 Unable to find image 'dockerinpractice/image-stepper:latest' locally　　⇽---　
 latest: Pulling from dockerinpractice/image-stepper
 b3e1c725a85f: Pull complete
 4daad8bdde31: Pull complete
 63fe8c0068a8: Pull complete
 4a70713c436f: Pull complete
 bd842a2105a8: Pull complete
 1a3a96204b4b: Pull complete
 d3959cd7b55e: Pull complete
 Digest: sha256:
➥ 65e22f8a82f2221c846c92f72923927402766b3c1f7d0ca851ad418fb998a753
 Status: Downloaded newer image for dockerinpractice/image-stepper:latest　　⇽---　 docker run命令的输出结果
 $ docker images | grep myimage　　⇽---　执行docker images命令并过滤出刚刚打上标签的那些镜像
 myimage    latest            2c182dabe85c    24 minutes ago    123 MB　　⇽---　
 myimage    latest_step_12    2c182dabe85c    24 minutes ago    123 MB
 myimage    latest_step_11    e0ff97533768    24 minutes ago    123 MB
 myimage    latest_step_10    f46947065166    24 minutes ago    123 MB
 myimage    latest_step_9     8a9805a19984    24 minutes ago    123 MB
 myimage    latest_step_8     88e42bed92ce    24 minutes ago    123 MB
 myimage    latest_step_7     5e638f955e4a    24 minutes ago    123 MB
 myimage    latest_step_6     f66b1d9e9cbd    24 minutes ago    123 MB
 myimage    latest_step_5     bd07d425bd0d    24 minutes ago    123 MB
 myimage    latest_step_4     ba913e75a0b1    24 minutes ago    123 MB
 myimage    latest_step_3     2ebcda8cd503    24 minutes ago    123 MB
 myimage    latest_step_2     58f4ed4fe9dd    24 minutes ago    123 MB
 myimage    latest_step_1     19134a8202e7    2 weeks ago       123 MB　　⇽---　镜像已经被打上标签
$ docker run myimage:latest_step_8 ls / | grep file　　⇽---　随机选择一个步骤并列出根目录下的文件，过滤出代码清单4-27里的Dockerfile创建的文件
file1　　⇽---　
file2
file3
file4
file5
file6
file7　　⇽---　显示的这些文件即是在之前步骤里创建的那些文件
```

当针对宿主机上其他构建好的Docker镜像运行时，这一镜像将会为构建的每一步打上对应的标签，使得用户可以轻松地按顺序查看镜像层。

docker.io软件包安装的客户端程序的版本必须和宿主机上的Docker守护进程的版本兼容，通常这意味着客户端程序不能更新。



**注意**

在一些非Linux操作系统（如Mac和Windows）上，用户可能需要在Docker首选项里将Docker运行目录指定为一个文件共享。



本技巧对于查看构建过程中某个特定文件的添加位置，或者某个特定时间点处文件的状态非常有用。在调试构建问题时，这非常有用！

#### 讨论

在技巧52里我们将使用这项技巧来验证一个已经被删除的密钥文件在镜像的某个层仍然是可以访问的。

