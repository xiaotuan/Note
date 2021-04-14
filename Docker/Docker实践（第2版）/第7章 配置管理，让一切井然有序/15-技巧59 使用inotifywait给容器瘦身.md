### 技巧59　使用inotifywait给容器瘦身

现在我们将使用一个小巧的工具来进一步给容器瘦身，它会告诉我们当运行一个容器时有哪些文件会被引用。

这可以称作是一项“核武器”，因为在生产中实施可能是相当危险的。但是，它算是一个有助于了解系统的指导手段，即使不遵循下面的介绍去实际使用它也没关系——要知道配置管理的一个关键部分便是理解应用正常运转所需的条件。

#### 问题

想要将容器里的文件集和权限集尽可能缩减到最小。

#### 解决方案

使用inotify来确定程序需要哪些文件，然后删除所有其他文件。

从整体上来说，用户需要知道当其在一个容器里执行一条命令时会访问哪些文件。如果用户将容器文件系统上所有其他文件都删除，理论上来说依旧可以拥有一切运行时所需的东西。

在这次演示中，将会用到技巧 56 里介绍过的log-cleaner-purged镜像。用户需要安装好inotify-tools，然后执行 `inotifywait` 得到一个访问了哪些文件的报告。随后运行模拟该镜像的入口点的程序（log_clean脚本）。紧接着，用户可以依据生成的文件报告，删除任何没有访问到的文件，如代码清单7-27所示。

代码清单7-27　执行手动安装步骤的同时使用inotifywait监控

```c
[host]$ docker run -ti --entrypoint /bin/bash \　　⇽---　覆盖此镜像默认的入口点
 --name reduce dockerinpractice/log-cleaner-purged　　⇽---　给容器起一个名字，后面可以用它来引用该容器
 $ apt-get update && apt-get install -y inotify-tools　　⇽---　安装inotify-tools包
 $ inotifywait -r -d -o /tmp/inotifywaitout.txt \　　⇽---　以递归（-r）和守护进程（-d）模式执行inotifywait，获取一个已访问文件的清单并写到outfile（以-o标志指定的）里
  /bin /etc /lib /sbin /var　　⇽---　指定感兴趣的需要关注的文件夹。注意不要监听/tmp，因为/tmp/inotifywaitout. txt文件如果自己监听自己可能会造成一个死循环
inotifywait[115]: Setting up watches. Beware: since -r was given, this >
may take a while!
inotifywait[115]: Watches established.
$ inotifywait -r -d -o /tmp/inotifywaitout.txt /usr/bin /usr/games \　　⇽---　对/usr文件夹上的子文件夹再次调用inotifywait。由于/usr文件夹里有太多文件需要inotifywait来处理，因此用户需要单独一个个地去指定
 /usr/include /usr/lib /usr/local /usr/sbin /usr/share /usr/src
inotifywait[118]: Setting up watches. Beware: since -r was given, this >
may take a while!
inotifywait[118]: Watches established.
$ sleep 5　　⇽---　 sleep会给予inotifywait一个合理的等待启动的时间
$ cp /usr/bin/clean_log /tmp/clean_log　　⇽---　
$ rm /tmp/clean_log　　⇽---　记得访问一个要用到的脚本文件。还有，要确保有执行rm命令的权限
$ bash　　⇽---　
$ echo "Cleaning logs over 0 days old"
$ find /log_dir -ctime "0" -name '*log' -exec rm {} \;　　⇽---　像脚本里做的那样，启动一个bash shell，然后运行脚本里本来要执行的一些命令。注意这个操作会失败，因为我们没有从宿主机上挂载任何实际的日志目录
$ awk '{print $1$3}' /tmp/inotifywaitout.txt | sort -u > \
/tmp/inotify.txt　　⇽---　利用awk工具从inotifywait的日志输出里生成一个文件名清单，然后将它去重并排序
$ comm -2 -3 \　　⇽---　使用comm工具输出一个文件系统上未访问的文件清单
 <(find /bin /etc /lib /sbin /var /usr -type f | sort) \
 <(cat /tmp/inotify.txt) > /tmp/candidates.txt
$ cat /tmp/candidates.txt | xargs rm　　⇽---　删除所有未访问的文件
$ exit　　⇽---　
$ exit　　⇽---　退出之前打开的bash shell，随后再退出容器本身
```

现在已经完成：

+ 给一些文件设置监听以查看哪些文件是被访问的；
+ 执行所有的命令来模拟脚本的运行；
+ 执行一些命令以确保用户有权限访问后面肯定要用到的脚本和rm实用工具；
+ 获取一个运行期间未被访问的所有文件的清单；
+ 删除所有未被访问的文件。

现在，可以将此容器扁平化（见技巧52），创建一个新镜像，然后测试它是否仍然能够正常工作，如代码清单7-28所示。

代码清单7-28　扁平化镜像并运行它

```c
$ ID=$(docker export reduce | docker import -)　　⇽---　将镜像扁平化然后把镜像ID放到环境变量ID里
$ docker tag $ID smaller　　⇽---　给新的扁平镜像打上smaller的标签
$ docker images | grep smaller
smaller latest 2af3bde3836a 18 minutes ago 6.378 MB　　⇽---　现在该镜像甚至比之前大小的10%还小
$ mkdir -p /tmp/tmp　　⇽---　
$ touch /tmp/tmp/a.log　　⇽---　为了测试创建一个新的文件夹和文件，模拟一个日志目录
$ docker run -v /tmp/tmp:/log_dir smaller \
 /usr/bin/clean_log 0
Cleaning logs over 0 days old
$ ls /tmp/tmp/a.log　　⇽---　在测试目录上运行新创建的镜像，并检查创建的文件是否已经被删除
 ls: cannot access /tmp/tmp/a.log: No such file or directory
```

我们将此镜像的大小从96 MB缩减到了大约6.5 MB，而它似乎仍然可以正常工作。相当节俭！



**警告**

本技巧就像CPU超频一样，并不是一个无关紧要的优化。这个特定案例之所以能够很正常地运转，是因为它是一个运行范围相当有限的应用程序，但是用户的一些核心关键业务应用程序可能是更复杂的，而且在如何访问文件方面可能是更加动态的。用户可以轻易删除一个在运行时未访问的文件，但是该文件可能会在某些其他场景下需要用到。



如果有点儿担心删掉的这些文件后面可能会用到而导致镜像损坏，可以用/tmp/candidates.txt文件收录未触及的最大文件的清单，如下所示：

```c
cat /tmp/candidates.txt | xargs wc -c | sort -n | tail
```

然后可以删掉那些确定应用程序将来不会用到的大一点儿的文件。这也是一场大的胜利！

#### 讨论

尽管本技巧是作为一种Docker技巧呈现的，但是在一些其他场景里，它也可以被归类为通用的技巧。当用户在调试不是很熟悉的进程时，或者想知道哪些文件被进程引用时，这个技巧格外有用。strace是实现这一目的的另一个工具，但是inotifywait在某些情况下更简单一些。

在技巧97中，这个通用方法也作为抵抗攻击的一种手段，用于减少容器的攻击面。

