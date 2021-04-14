### 技巧54　传统方式：搭配make和Docker

有时候，用户可能会发现有些Dockerfile限制了自己的构建流程。举个例子，如果限制自己执行 `dockerbuild` 命令，就无法产出任何输出 **文件** ，并且无法在Dockerfile里定义变量。

这种附加的工具化需求可以通过一些工具（包括纯shell脚本）来实现。在本技巧里，我们将一起来看看可以怎样结合老牌的make工具与Docker一起工作。

#### 问题

想要在 `dockerbuild` 执行过程中增加额外的任务。

#### 解决方案

使用一个古老的（计算机术语中）工具make。

为了避免用户之前没有make使用经验，我们在这里对它先做一些简单的介绍，make是一款工具，它需要一个或多个输入文件并且会产出一个输出文件，但是它也可以用作一个任务执行器。代码清单7-4给出的是一个简单的示例（注意所有缩进都必须是制表符）。

代码清单7-4　一个简单的Makefile

```c
.PHONY: default createfile catfile　　⇽---　默认情况下，make会假定所有目标均是将被任务创建的文件名，使用.PHONY表明这不是任务的真正名称
default: createfile　　⇽---　按照惯例，Makefile中的第一个目标是default。如果在运行的时候没有指定一个明确的目标，make将会选取文件中的第一个目标。可以看到，因为createfile是default的唯一依赖，default将会执行它
createfile: x.y.z　　⇽---　 createfile是一个伪任务，它依赖x.y.z任务
catfile: 　　⇽---　 catfile是一个伪任务，它执行单条命令
     cat x.y.z
x.y.z: 　　⇽---　 x.y.z是一个文件任务，会执行两条命令并创建目标x.y.z文件
     echo "About to create the file x.y.z"
    echo abc > x.y.z
```



**警告**

一个Makefile里的所有缩进都必须是制表符，并且目标里的每条命令都是在不同的shell里执行的（所以环境变量不会被传递过去）。



一旦在名为Makefile的文件中定义了上述内容，便可以使用像 `make createfile` 这样的命令去调用任意目标。

现在我们可以在Makefile中查看一些有用的模式——接下来要讨论的目标都将是伪任务，因为它很难（尽管可以）通过追踪文件的变动来自动触发Docker构建。Dockerfile会对镜像层进行缓存，因此构建往往会很快。

第一步就是运行一个Dockerfile。因为Makefile是由shell命令组成的，所以这一点很容易办到，如代码清单7-5所示。

代码清单7-5　创建一个镜像的Dockerfile

```c
base:
    docker build -t corp/base .
```

上述命令做的工作带来的一些正常变动正是用户所期许的结果（例如，将文件通过管道传递给 `docker build` 以删除上下文，或是用 `-f` 指定采用不同命名的Dockerfile），而且用户可以使用 `make` 的依赖功能，在必要时自动构建基础镜像（在 `FROM` 中使用的那个）。例如，如果用户在一个叫repos的子目录下迁出几个仓库（这样也容易做 `make` ），用户可以像代码清单7-6所示这样添加一个目标。

代码清单7-6　在子目录里构建镜像的Makefile

```c
app1: base
    cd repos/app1 && docker build -t corp/app1 .
```

这样做的缺点是，每当基础镜像需要重新构建时，Docker就需要上传一个包含所有依赖仓库的构建上下文。可以通过显式地传入一个作为构建上下文的TAR文件给Docker来解决这一问题，如代码清单7-7所示。

代码清单7-7　用特定文件集合构建镜像的Dockerfile

```c
base:
    tar -cvf - file1 file2 Dockerfile | docker build -t corp/base -
```

如果用户目录内包含大量与构建无关的文件，那么这种依赖的显式声明语句将会带来一个显著的速度方面的提升。如果用户想要将所有构建依赖保留在不同的目录里，可以稍微修改一下这个目标，如代码清单7-8所示。

代码清单7-8　用重命名路径下特定文件集合构建镜像的Makefile

```c
base:
    tar --transform 's/^deps\///' -cf - deps/* Dockerfile | \
        docker build -t corp/base -
```

在这里，用户可以将deps目录下的所有内容添加到构建上下文中，然后使用 `--transform` 选项压缩 `tar` 包（Linux上的最新 `tar` 版本支持），这样便可以从文件名中除去任何前导“deps/”。在这个例子里，更好的办法是将deps和Dockerfile放在各自的目录中以允许正常的 `docker build` ，但是了解这种高级用法很有价值，因为它可以在一些最不可能的地方派上用场。在使用这一方案之前往往要考虑清楚，毕竟它会增加构建流程的复杂度。

简单的变量替换是一件相对简单的事情，但是（如之前的 `--transform` ）在使用它之前还是得考虑清楚——Dockerfile之所以故意不支持变量，就是为了保持构建是易于重现的。这里我们将用到传给 `make` 的一些变量，然后使用 `sed` 替换，不过用户也可以按照自己的喜好来传参和替换，如代码清单7-9所示。

代码清单7-9　使用基本Dockerfile变量替换构建镜像的Makefile

```c
VAR1 ?= defaultvalue
base:
    cp Dockerfile.in Dockerfile
    sed -i 's/{VAR1}/$(VAR1)/' Dockerfile
    docker build -t corp/base .
```

Dockerfile将在每次基础目标运行时被重新生成，而且用户可以通过添加更多的 `sed -i` 条目添加更多的变量替换。要覆盖 `VAR1` 的默认值，可以执行 `make VAR1 = newvalue base` 。倘若变量里面包含斜杠，用户可能需要另外指定一个 `sed` 分隔符，如 `sed -i's#VAR1}#$（VAR1）#'Dockerfile` 。

最后，如果用户一直使用Docker作为构建工具，那便需要知道怎样才能从Docker中获取文件。我们将介绍几种不同的可选方案，具体取决于实际用例场景，如代码清单7-10所示。

代码清单7-10　从镜像中复制出文件的Makefile

```c
singlefile: base
    docker run --rm corp/base cat /path/to/myfile > outfile
multifile: base
    docker run --rm -v $(pwd)/outdir:/out corp/base sh \
        -c "cp -r /path/to/dir/* /out/"
```

在这里， `singlefile` 对一个文件执行 `cat` ，然后管道输出到一个新文件。这个方案具有自动设置正确的文件拥有者的优点，但是对于多个文件的处理就会变得很麻烦。推荐的 `multifile` 方案则是在容器里挂载一个卷并将所有文件从一个目录复制到该卷。用户可以使用 `chown` 命令来设置文件的真正拥有者，但是别忘了在调用时可能需要带上 `sudo` 。

Docker项目本身从源代码构建Docker时便是用的挂载卷的方案。

#### 讨论

在这样一本讨论Docker这种较新技术的书中出现像make这样古老的工具似乎是一件比较奇怪的事情。为什么不使用新一点的技术（如Ant、Maven或其他可用的通用构建工具）呢？

答案是，尽管make有一些缺点，但是它有以下优势：

+ 在短期内不会被弃用；
+ 有良好的文档建设；
+ 有很强的灵活性；
+ 使用非常广泛。

我们花费了许多时间在解决较新的构建技术的bug以及一些文档很少（或者压根就没有文档）的功能限制上，尝试安装这些新系统的依赖也很费时。而make的特性拯救了我们很多次。再者，5年以后make很大概率仍然可以继续使用，而其他工具更有可能已经消失，或者它们的负责人不再维护它们了。

