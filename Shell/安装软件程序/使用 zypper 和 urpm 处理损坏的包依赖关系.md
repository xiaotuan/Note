用 `zypper` 时，只有一个命令能够用来验证和修复损坏的依赖关系。用 `urpm` 时，如果 `clean` 选项不工作，你可以跳过更新那些有问题的包。要这么做的话，就必须将有问题包的名字添加到文件 `/etc/urpmi/skip.list`。

<center><b>用 zypper 和 urpm 修复损坏的依赖关系</b></center>

| 前端工具 | 命令          |
| -------- | ------------- |
| urpm     | urpmi -clean  |
| zyppyer  | zypper verify |

