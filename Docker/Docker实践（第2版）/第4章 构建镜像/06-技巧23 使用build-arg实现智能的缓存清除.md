### 技巧23　使用build-arg实现智能的缓存清除

在技巧22里，用户已经看到了如何通过修改相关的内容来清理构建中间环节里的缓存。在本技巧里，我们将进一步来看看怎么通过构建命令来控制是否清除缓存。

#### 问题

想要在不改动Dockerfile的情况下，执行构建时按需清除缓存。

#### 解决方案

在Dockerfile里使用 `ARG` 指令，从外部清除缓存。要证明这一点，用户需要再次用到 https://github.com/docker-in-practice/todo提供的Dockerfile，但是可以做一些小改动。用户想要实现的便是清除在执行 `npminstall` 之前的缓存。为什么想做这个呢？如你所知，默认情况下Docker只会在Dockerfile里的命令变更后中断缓存。但是我们不妨假设现在有更新的 `npm` 包，并且用户想要确保可以更新到这个版本。一种办法是手动改动那行代码（正如技巧22所看到的那样），但是另外一个能够实现同样效果并且更优雅的方式就涉及使用Docker的 `ARG` 指令以及一项bash技巧。

如代码清单4-7所示，在Dockerfile里增加一行 `ARG` 的定义。

代码清单4-7　支持可清除的缓存的简单Dockerfile

```c
WORKDIR todo
ARG CACHEBUST=no　　⇽---　 ARG指令在构建时会设置一个环境变量
RUN npm install
```

在上述例子里，用户可以使用 `ARG` 指令设置 `CACHEBUST` 环境变量，然后如果在执行 `dockerbuild` 命令时没有设置，会默认将它设置为 `no` 。

现在“正常地”使用Dockerfile做构建：

```c
$ docker build .
Sending build context to Docker daemon   2.56kB
Step 1/7 : FROM node
latest: Pulling from library/node
aa18ad1a0d33: Pull complete
15a33158a136: Pull complete
f67323742a64: Pull complete
c4b45e832c38: Pull complete
f83e14495c19: Pull complete
41fea39113bf: Pull complete
f617216d7379: Pull complete
cbb91377826f: Pull complete
Digest: sha256:
➥ a8918e06476bef51ab83991aea7c199bb50bfb131668c9739e6aa7984da1c1f6
Status: Downloaded newer image for node:latest
 ---> 9ea1c3e33a0b
Step 2/7 : MAINTAINER ian.miell@gmail.com
 ---> Running in 03dba6770157
 ---> a5b55873d2d8
Removing intermediate container 03dba6770157
Step 3/7 : RUN git clone https://github.com/docker-in-practice/todo.git
 ---> Running in 23336fd5991f
Cloning into 'todo'...
 ---> 8ba06824d184
Removing intermediate container 23336fd5991f
Step 4/7 : WORKDIR todo
 ---> f322e2dbeb85
Removing intermediate container 2aa5ae19fa63
Step 5/7 : ARG CACHEBUST=no
 ---> Running in 9b4917f2e38b
 ---> f7e86497dd72
Removing intermediate container 9b4917f2e38b
Step 6/7 : RUN npm install
 ---> Running in a48e38987b04
npm info it worked if it ends with ok
[...]
added 249 packages in 49.418s
npm info ok
 ---> 324ba92563fd
Removing intermediate container a48e38987b04
Step 7/7 : CMD npm start
 ---> Running in ae76fa693697
 ---> b84dbc4bf5f1
Removing intermediate container ae76fa693697
Successfully built b84dbc4bf5f1
```

如果使用相同的 `docker build` 命令再次构建，用户会发现Docker在这次构建时会使用之前的缓存，最终产出的镜像没有任何变化。

```c
$ docker build .
Sending build context to Docker daemon   2.56kB
Step 1/7 : FROM node
 ---> 9ea1c3e33a0b
Step 2/7 : MAINTAINER ian.miell@gmail.com
 ---> Using cache
 ---> a5b55873d2d8
Step 3/7 : RUN git clone https://github.com/docker-in-practice/todo.git
 ---> Using cache
 ---> 8ba06824d184
Step 4/7 : WORKDIR todo
 ---> Using cache
 ---> f322e2dbeb85
Step 5/7 : ARG CACHEBUST=no
 ---> Using cache
 ---> f7e86497dd72
Step 6/7 : RUN npm install
 ---> Using cache
 ---> 324ba92563fd
Step 7/7 : CMD npm start
 ---> Using cache
 ---> b84dbc4bf5f1
Successfully built b84dbc4bf5f1
```

这时候用户决定要强制重新构建npm包。也许是修复了一个bug，或者想要确保npm包是最新的版本。这也正是之前在代码清单4-7添加到Dockerfile里 `ARG` 变量的位置。如果这个 `ARG` 变量被设置成在宿主机上从未使用过的值，那么这里的缓存就会被清除。

这是使用 `build-arg` 标志进行 `dockerbuild` 的地方，在这里也用到了一个bash技巧强制获取最新值：

```c
$ docker build --build-arg CACHEBUST=${RANDOM} . 　　⇽---　带上build-arg标志执行docker build，将CACHEBUST参数设置为一个由bash生成的伪随机数
Sending build context to Docker daemon 4.096 kB
Step 1/9 : FROM node
 ---> 53d4d5f3b46e
Step 2/9 : MAINTAINER ian.miell@gmail.com
 ---> Using cache
 ---> 3a252318543d
Step 3/9 : RUN git clone https://github.com/docker-in-practice/todo.git
 ---> Using cache
 ---> c0f682653a4a
Step 4/9 : WORKDIR todo
 ---> Using cache
 ---> bd54f5d70700
Step 5/9 : ARG CACHEBUST=no　　⇽---　由于ARG CACHEBUST=no这一行本身没有变动，所以仍然使用了缓存
 ---> Using cache
 ---> 3229d52b7c33
Step 6/9 : RUN npm install　　⇽---　由于CAHCEBUST参数被设置为之前未设定过的值，缓存被清除了，并且触发了再次执行npm install命令
 ---> Running in 42f9b1f37a50
npm info it worked if it ends with ok
npm info using npm@4.1.2
npm info using node@v7.7.2
npm info attempt registry request try #1 at 11:25:55 AM
npm http request GET https://registry.npmjs.org/compression
npm info attempt registry request try #1 at 11:25:55 AM
[...]
Step 9/9 : CMD npm start
 ---> Running in 19219fe5307b
 ---> 129bab5e908a
Removing intermediate container 19219fe5307b
Successfully built 129bab5e908a
```

注意，缓存是在 `ARG` 一行之后的部分被清除了，而不是 `ARG` 这一行。这可能会有点让人困惑。需要注意的是“Running in”一词，这意味着Docker已经创建了一个新的容器来运行构建这一行。

值得一提的还有这里用到的 `${RANDOM}` 参数。bash为用户提供了这个保留变量名称，用户可以轻松地获取一个一到五位数的值：

```c
$ echo ${RANDOM}
19856
$ echo ${RANDOM}
26429
$ echo ${RANDOM}
2856
```

这个技巧挺好用的，比如当用户想要一个可能唯一的值创建文件来运行特定的脚本。如果用户担心冲突，甚至可以生成更长的随机数：

```c
$ echo ${RANDOM}${RANDOM}
434320509
$ echo ${RANDOM}${RANDOM}
1327340
```

注意，如果不使用bash（或是带有 `RANDOM` 变量的shell），那么这个技巧将会不起作用。在这种情况下，用户可以使用 `date` 命令来生成新的值：

```c
$ docker build --build-arg CACHEBUST=$(date +%s) .
```

#### 讨论

这项技巧已经演示了一些可以在使用Docker时派上用场的东西。用户已经了解了该如何使用 `--build-arg` 标志将值传递给Dockerfile并根据需要清除缓存，从而在不更改Dockerfile的情况下创建一个全新的构建。

如果用户使用bash，那么现在你也了解了 `RANDOM` 变量，以及它在其他上下文里的用途，而不只是Docker构建。

