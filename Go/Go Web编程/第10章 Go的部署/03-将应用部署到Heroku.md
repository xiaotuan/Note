### 10.2　将应用部署到Heroku

在上一节中，我们学习了如何将一个简单的Go Web服务部署到独立的服务器上面，以及如何通过 `init` 守护进程管理Web服务。在本节中，我们将要学习如何将同样的Web服务部署到PaaS供应商Heroku上面，这种部署方式跟上一节介绍的部署方式一样简单。

Heroku允许用户部署、运行和管理使用包括Go在内的几种编程语言开发的应用。根据Heroku的定义，一个应用就是由Heroku支持的某一种编程语言编写的一系列源代码，以及与这些源代码相关联的依赖关系。

Heroku的预设条件非常简单，它只要求用户提供以下几样东西：

+ 定义依赖关系的配置文件或者相关机制，如Ruby的 `Gemfile` 文件、Node.js的 `package.json` 文件或者Java的 `pom.xml` 文件；
+ 定义可执行文件的 `Procfile` 文件，其中可执行文件可以有不止一个。

Heroku大量地使用命令行，并因此提供了一个名为toolbelt的命令行工具，用于部署、运行和管理应用。此外，Heroku还需要通过Git将被部署的源码推送至服务器。当Heroku平台接收到Git推送的代码时，它会构建代码并获取指定的依赖关系，然后将构建的结果以及相应的依赖关系组装到一个slug里面，最后在Heroku的dynos上运行这个slug（dynos是Heroku对隔离式、轻量级、虚拟化的Unix容器的称呼）。

尽管某些管理和配置工作可以在之后通过Web界面来完成，但Heroku最主要的操作界面还是它的命令行工具toolbelt，因此我们在注册完Heroku之后的第一件事，就是访问https:// toolbelt.heroku.com下载toolbelt。

Heroku是一个非典型的PaaS供应商，人们想要使用PaaS来部署Web应用的原因有很多，对Web应用的开发者来说，最主要的原因莫过于PaaS可以让基础设施和系统层变得抽象，并且不再需要人工的管理和干预。尽管PaaS在企业级IT基础设施这样的大规模生产环境中并不少见，但它们对小型公司和创业公司来说却能够提供极大的方便，并且能够有效地减少这些公司在基础设施方面的前期投入。

在下载完toolbelt之后，用户需要使用注册账号时获得的凭据登入Heroku：

```go
heroku login
Enter your Heroku credentials.
Email: <your email>
Password (typing will be hidden):
Authentication successful.
```

图10-1展示了将简单Web服务部署到Heroku的具体步骤。

为了将简单Web应用部署到Heroku，我们需要对这个应用的代码做一些细微的修改：在当前的代码中，应用使用的是8080端口，但是在把应用部署到Heroku的时候，用户是无法控制应用使用哪个端口的，程序必须通过读取环境变量 `PORT` 来获知自己能够使用的端口号。为此，我们需要将 `server.go文件` 中 `main` 函数的代码从现在的：

```go
func main() {
　server := http.Server{
　　Addr: ":8080",
　}
　http.HandleFunc("/post/", handlePost)
　server.ListenAndServe()
}
```

修改为：

```go
func main() {
 server := http.Server{
　　Addr: ":" + os.Getenv("PORT"),//　❶
　}
　http.HandleFunc("/post/", handlePost)
　server.ListenAndServe()
}
```

❶ 从环境变量中获取端口号

![61.png](../images/61.png)
<center class="my_markdown"><b class="my_markdown">图10-1　将Web应用部署到Heroku的具体步骤</b></center>

以上就是将简单Web应用部署到Heroku所需要做的全部代码修改，其他代码只要保留原样即可。在修改完代码之后，我们接下来要做的就是将简单Web应用所需的依赖关系告知Heroku。Heroku使用godep（https://github.com/tools/godep）来管理Go的依赖关系，godep可以通过执行以下命令来安装：

```go
go get github.com/tools/godep
```

在godep安装完毕之后，我们需要使用它来引入简单Web服务的依赖关系。为此，我们需要在简单Web服务的根目录中执行以下命令：

```go
godep save
```

这条命令不仅会创建一个名为 `Godeps` 的目录，它还会获取代码中的全部依赖关系，并将这些依赖关系的源代码复制到 `Godeps/_workspace` 目录中。除此之外，这个命令还会创建一个名为 `Godeps.json` 的文件，并在该文件中列出代码中的全部依赖关系。作为例子，代码清单10-4展示了godep为简单Web服务创建的 `Godeps.json` 文件。

代码清单10-4　 `Godeps.json` 文件

```go
{
　"ImportPath": "github.com/sausheong/ws-h",
　"GoVersion": "go1.4.2",
　"Deps": [
　　{
　　　"ImportPath": "github.com/lib/pq",
　　　"Comment": "go1.0-cutoff-31-ga33d605",
　　　"Rev": "a33d6053e025943d5dc89dfa1f35fe5500618df7"
　　}
　]
}
```

因为我们的简单Web服务只需要依赖Postgres数据库驱动，所以文件中只出现了关于该驱动的依赖信息。

在Heroku上实施部署需要做的最后一件事，就是定义一个 `Procfile` 文件，并使用该文件去描述需要被执行的可执行文件或者主函数。代码清单10-5展示了简单Web服务的 `Procfile` 文件。

代码清单10-5　 `Procfile` 文件

```go
web: ws-h
```

整个文件非常简单，只有短短的一行。这个文件定义了Web进程与 `ws-h` 可执行二进制文件之间的关联，Heroku在完成应用的构建工作之后，就会执行 `ws-h` 文件。

准备工作一切就绪之后，我们接下来要做的就是将简单Web服务的代码推送至Heroku。Heroku允许用户通过GitHub集成、Dropbox同步、Heroku官方提供的API以及标准的Git操作等多种不同的手段来推送代码。作为例子，本节接下来将展示如何使用标准的Git操作将简单Web服务推送至Heroku。

在推送代码之前，用户首先需要创建一个Heroku应用：

```go
heroku create ws-h
```

这条命令将创建一个名为 `ws-h` 的Heroku应用，该应用最终将在地址https://ws-h.herokuapp.com上展示。需要注意的是，因为本书在这里已经使用了 `ws-h` 作为应用的名字，所以读者将无法创建相同名字的应用。为此，读者在创建应用的时候可以使用其他名字，或者在创建应用时去掉名字参数，让Heroku为应用自动生成一个随机的名字：

```go
heroku create
```

`heroku create` 命令将为我们的简单Web服务创建一个本地的Git代码库（repository），并在代码库中添加远程Heroku代码库的地址。因此，用户在创建完Heroku应用之后，就可以通过以下命令使用Git将应用代码推送至Heroku：

```go
git push heroku master
```

因为Heroku在接收到用户推送的代码之后就会自动触发相应的构建以及部署操作，所以将应用部署到Heroku的工作到此就可以告一段落了。除上面提到的工具之外，Heroku还提供了一系列非常棒的应用管理工具，这些工具可以对应用进行性能扩展以及版本管理，并且在需要时，用户也可以使用Heroku提供的配置工具添加新的服务，有兴趣的读者可以自行查阅Heroku提供的相关文档。

