`Git` 简单易用。只要输入 `git`，`Git` 就会不带任何参数地列出它的选项和最常用的子命令。

```shell
$ git
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

这些是各种场合常见的 Git 命令：

开始一个工作区（参见：git help tutorial）
   clone      克隆一个仓库到一个新目录
   init       创建一个空的 Git 仓库或重新初始化一个已存在的仓库

在当前变更上工作（参见：git help everyday）
   add        添加文件内容至索引
   mv         移动或重命名一个文件、目录或符号链接
   reset      重置当前 HEAD 到指定状态
   rm         从工作区和索引中删除文件

检查历史和状态（参见：git help revisions）
   bisect     通过二分查找定位引入 bug 的提交
   grep       输出和模式匹配的行
   log        显示提交日志
   show       显示各种类型的对象
   status     显示工作区状态

扩展、标记和调校您的历史记录
   branch     列出、创建或删除分支
   checkout   切换分支或恢复工作区文件
   commit     记录变更到仓库
   diff       显示提交之间、提交和工作区之间等的差异
   merge      合并两个或更多开发历史
   rebase     本地提交转移至更新后的上游分支中
   tag        创建、列出、删除或校验一个 GPG 签名的标签对象

协同（参见：git help workflows）
   fetch      从另外一个仓库下载对象和引用
   pull       获取并整合另外的仓库或一个本地分支
   push       更新远程引用和相关的对象

命令 'git help -a' 和 'git help -g' 显示可用的子命令和一些概念帮助。
查看 'git help <命令>' 或 'git help <概念>' 以获取给定子命令或概念的
帮助。
```

> 要得到一个完整的 `git` 子命令列表，可以输入 `git help --all`。

每个 git 子命令的文档都可以通过使用 `git help subcommand`、`git --help subcommand` 或者 `git subcommand --help` 来查看。

`Git` 的命令能够理解 ”短“和“长”的选项。例如， `git commit` 命令将下面两条命令视为等价的。

```shell
$ git commit -m "Fixed a typo."
$ git commit --message="Fixed a typo."
```

缩写形式 `-m` 使用了一个连字符，而长形式 `--message` 使用了两个连字符，有些选项只存在一种形式。

最后，可以通过”裸双破折号“的约定来分离一系列参数。例如，使用双破折号来分离命令行的控制部分与操作数部分，如文件名。

```shell
$ git diff -w master origin -- tools/Makefile
```

你可能需要使用双破折号分离并显式标识文件名，否则可能会误认为他们是命令的另一部分。例如，如果你碰巧有一个文件和一个标签都叫 main.c ，然后你会看到不同的行为。

```shell
# Checkout the tag named "main.c"
$ git checkout main.c

# Checkout the file name "main.c"
$ git checkout -- main.c
```
