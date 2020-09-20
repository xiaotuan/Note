如果不想每次都输入完整的 Git 命令，可以通过 git config 命令来轻松地为每一个命令设置一个别名。这里有一些例子可以试试：

```shell
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```

这意味着，当要输入 git commit 时，只需要输入 git ci。

例如，为了解决取消暂存文件的易用性问题，可以向 Git 中添加你自己的取消暂存别名：

```shell
$ git config --global alias.unstage 'reset HEAD --'
```

然而，你可能想要执行外部命令，而不是一个 Git 子命令。如果是那样的话，可以在命令前面加入 \!  符号。如果你自己要些一些与 Git 仓库协作的工具的话，那会很有用。我们现在演示将 git visual 定义为 gitk 的别名：

```shell 
$ git config --global alias.visual '!gitk'
```

