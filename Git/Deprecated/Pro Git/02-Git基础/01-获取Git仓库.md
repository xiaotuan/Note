**在已存在目录中初始化仓库**

首先需要进入该项目目录中。

在 Linux 上：

```shell
$ cd /home/user/my_project
```

在 macOS 上：

```shell
$ cd /Users/user/my_project
```

在 Windows 上：

```shell
$ cd /c/user/my_project
```

之后执行：

```shell
$ git init
```

可以通过 git add 命令来指定所需的文件来进行追踪，然后执行 git commit：

```shell
$ git add *.c
$ git add LICENSE
$ git commit -m 'initial project version'
```

**克隆现有的仓库**

克隆仓库的命令是 git clone \<url\>。比如，要克隆 Git  的链接库 libgit2，可以用下面的命令：

```shell
$ git clone https://github.com/libgit2/libgit2
```

如果你想在克隆远程仓库的时候，自定义本地仓库的名字，你可以通过额外的参数指定新的目录名：

```shell
$ git clone https://github.com/libgit2/libgit2 mylibgit
```

