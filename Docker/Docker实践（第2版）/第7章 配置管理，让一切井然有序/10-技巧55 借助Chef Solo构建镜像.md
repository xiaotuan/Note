### 技巧55　借助Chef Solo构建镜像

Docker新手们常常疑惑的一件事情便是，Dockerfile是否是唯一被支持的配置管理工具，以及现有配置管理工具是否应该移植到Dockerfile。这些观点都是不对的。

尽管Dockerfile被设计成是一种简单、可移植的镜像置备手段，但是它也足够灵活，允许任何其他的配置管理工具接管。简而言之，如果可以在终端里运行它，便可以在Dockerfile中运行它。

这里作为演示，我们将展示如何在Dockerfile中启动并运行Chef（Chef可能是Dockerfile中最成熟的配置管理工具）。使用像Chef这样的工具可以减少配置镜像的工作量。



**注意**

尽管使用本技巧并不要求用户熟悉Chef，但是如果你想要第一次就能快速掌握它，仍需对Chef有一定程度的熟练度。完整介绍一款配置管理工具需要一本专门的书才能办到，不过仔细学习本技巧再加上一些研究，就可以对Chef有一个基本的了解。



#### 问题

想要通过使用Chef来减少配置工作。

#### 解决方案

使用Dockerfile在容器里安装Chef，然后在这个容器里使用Chef Solo运行recipe来置备它。

在这个示例里，我们将使用Chef置备一个简单的“Hello World！”Apache网站。这个例子可以给读者直观的感受，即Chef在配置管理方面能做些什么。

Chef Solo不需要配置外部的Chef服务器。如果你对Chef很熟悉，这个例子可以很容易适配现有脚本，如果你需要，也可以和Chef服务器交互。

我们将演示这一Chef示例的创建过程，但如果想要得到可执行代码，这里有一个Git仓库可供下载。要下载它，执行下面这条命令：

```c
git clone https://github.com/docker-in-practice/docker-chef-solo-example.git
```

我们将从一个小目标做起，利用Apache设置一个一访问它便输出“Hello World!”的Web服务器。该站点工作在mysite.com下，而且在镜像上会设置一个 `mysiteuser` 用户。

首先，创建一个目录并设定好Chef配置所需的文件，如代码清单7-11所示。

代码清单7-11　为Chef配置文件创建必要的文件

```c
$ mkdir chef_example
$ cd chef_example
$ touch attributes.json　　⇽---　 Chef的属性文件，它定义了这个镜像（或者用Chef的说法是节点）的一些变量，包含这个镜像的执行列表里的recipe，以及其他的一些信息
$ touch config.rb　　⇽---　 Chef的配置文件，它设置一些Chef配置相关的基础变量
$ touch Dockerfile　　⇽---　将用来构建镜像的Dockerfile
$ mkdir -p cookbooks/mysite/recipes　　⇽---　创建默认的recipe文件夹，在这里面保存构建该镜像的Chef指令
$ touch cookbooks/mysite/recipes/default.rb
$ mkdir -p cookbooks/mysite/templates/default　　⇽---　针对动态配置的内容创建一些模板
$ touch cookbooks/mysite/templates/default/message.erb
```

attributes.json的内容如代码清单7-12所示。

代码清单7-12　attributes.json

```c
{
        "run_list": [
                "recipe[apache2::default]",
                "recipe[mysite::default]"
        ]
}
```

上述文件列出了要运行的recipe。apache2 recipe将会从一个公共仓库获取，而mysite recipe则在本地编写。

接下来，config.rb里放了一些基础信息，如代码清单7-13所示。

代码清单7-13　config.rb

```c
base_dir        "/chef/"
file_cache_path base_dir + "cache/"
cookbook_path   base_dir + "cookbooks/"
verify_api_cert true
```

上述文件设置了相关位置的一些基础信息，并添加了配置参数 `verify_api_cert` 来去掉不相干的错误。

至此，我们终于收获了劳动成果——该镜像的Chef recipe。代码块里每一个由 `end` 结尾的小节定义了一个Chef资源，如代码清单7-14所示。

代码清单7-14　cookbooks/mysite/recipes/default.rb

```c
user "mysiteuser" do　　⇽---　创建一个用户
     comment "mysite user"
    home "/home/mysiteuser"
    shell "/bin/bash"
end
directory "/var/www/html/mysite" do　　⇽---　创建一个目录来放置Web内容
     owner "mysiteuser"
    group "mysiteuser"
    mode 0755
    action :create
end
template "/var/www/html/mysite/index.html" do　　⇽---　定义了一个将会放到 Web 文件夹下的文件。根据source属性中定义的模板创建该文件
     source "message.erb"
    variables(
        :message => "Hello World!"
    )
    user "mysiteuser"
    group "mysiteuser"
    mode 0755
end
web_app "mysite" do　　⇽---　为apache2定义一个Web应用
     server_name "mysite.com"
    server_aliases ["www.mysite.com","mysite.com"]　　⇽---　在真实场景里，用户必须将这些引用从mysite改成自己的站点名称。如果用户是在自己的宿主机上访问或测试那就没问题了
    docroot "/var/www/html/mysite"
    cookbook 'apache2'
end
```

网站的内容包含在模板文件里。Chef会去读取其中一行，如代码清单7-15所示，将其替换成来自config.rb的“Hello World!”消息，然后再将替换后的文件写到模板目标（/var/www/html/ mysite/index.html）。这个例子中用到的模板语言在这里不做详细介绍。

代码清单7-15　cookbooks/mysite/templates/default/message.erb

```c
<%= @message %>
```

最后，将所有内容和Dockerfile放到一起，它会设置Chef的前置要求然后运行Chef来配置镜像，如代码清单7-16所示。

代码清单7-16　Dockerfile

```c
FROM ubuntu:14.04
RUN apt-get update && apt-get install -y git curl
RUN curl -L \
https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64
➥/chefdk_0.3.5-1_amd64.deb\
-o chef.deb
RUN dpkg -i chef.deb && rm chef.deb　　⇽---　下载并安装Chef。如果这一下载方式不起作用，可以检查之前在这一技巧的讨论中提到的docker-chef-solo-　example的最新代码，因为这里可能需要更新的版本
COPY . /chef　　⇽---　将所在文件夹下的内容复制到镜像上的/chef文件夹
WORKDIR /chef/cookbooks　　⇽---　
 RUN knife cookbook site download apache2
 RUN knife cookbook site download iptables
 RUN knife cookbook site download logrotate　　⇽---　切换到cookbooks文件夹然后使用Chef的knife工具下载apache2 cookbook及相关依赖的压缩包
RUN /bin/bash -c 'for f in $(ls *gz); do tar -zxf $f; rm $f; done'　　⇽---　解压下载完的压缩包然后删除它们
RUN chef-solo -c /chef/config.rb -j /chef/attributes.json　　⇽---　执行chef命令配置镜像，把事先创建好的属性和配置文件传给它
CMD /usr/sbin/service apache2 start && sleep infinity　　⇽---　定义镜像默认的启动命令。sleep infinity命令可以确保容器不会在service命令完成任务后立刻退出
```

现在可以构建并运行镜像：

```c
docker build -t chef-example .
docker run -ti -p 8080:80 chef-example
```

如果你现在浏览http://localhost:8080，应该能看到“Hello World!”的字样。



**警告**

如果Chef构建需要很长时间，而且用的是Docker Hub工作流，构建可能会出现超时。如果发生这种情况，用户可以在一台受自己控制的机器上完成构建，为支持的服务买单，或者把构建步骤拆分成更小的单元，这样一来Dockerfile里每个单独步骤返回的时间便会更短。



这个例子虽然很简单，但是使用这一方案的好处是显而易见的。通过一些相对明了的配置文件，将镜像转换成所需状态的具体细节交由配置管理工具处理。这并不意味着可以忘记配置的细节，更改变量值还是要求理解其语义的，这样可以确保不会把事情搞砸。但是，这种方法的确可以节省很多的时间和精力，特别是那些不需要了解太多细节的项目。

#### 讨论

本技巧的目的在于纠正一些关于Dockerfile概念的错误观念，尤其是Dockerfile是其他配置管理工具（如Chef和Ansible）的竞争对手这一观点。

Docker本质上（就如同我们在本书其他地方说的）是一个 **打包** 工具。它允许你以一种可预测的，包形式的方式得到构建过程的结果。你可以自行决定如何构建它，可以使用Chef、Puppet、Ansible、Makefiles和shell脚本，或者将它们整合在一起使用。

大多数人之所以不使用Chef、Puppet或其他工具来构建镜像，主要是因为Docker镜像更倾向于被构建为单一目的和单一过程的工具。不过如果你手上已经有配置脚本，为何不复用它们呢？

