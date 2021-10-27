我们可以使用 `<` 和 `>` 对输入输出进行重定向，使用|在同时执行的程序之间实现数据的管道传递，使用 `$(...)` 获取子进程的输出。

你可以使用如下命令来查看bash的版本号：

```shell
$ /bin/bash --version
GNU bash，版本 4.3.48(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2013 Free Software Foundation, Inc.
许可证 GPLv3+: GNU GPL 许可证第三版或者更新版本 <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

> 了。如果你使用的是 UNIX 系统并且 bash 没有被安装，你可以从 GNUWeb 网站 <www.gnu.org> 上免费下载它。
>

| shell名称 | 相关历史 |
| :----- | :----- |
| sh（Bourne） | 源于 UNIX 早期版本的最初的 shell |
| csh、tcsh、zsh | C shell 及其变体，最初是由 BillJoy 在 Berkeley UNIX 上创建的。它可能是继 bash 和 Korn shell 之后第三个最流行的 shell |
| ksh、pdksh | korn shell 和它的公共域兄弟 pdksh（public domain korn shell）由 David Korn编写，它是许多商业版本 UNIX 的默认 shell |
| bash | 来自 GNU 项目的 bash 或 Bourne Again Shell 是 Linux 的主要 shell。它的优点是可以免费获取其源代码，即使你的 UNIX 系统目前没有运行它，它也很可能已经被移植到该系统中。bash 与 Korn shell 有许多相似之处 |

