[toc]

Debian Linux 发行版创建了自己的 ash shell 版本（称作 Debian ash，或 dash）以供自用。dash 赋值了 ash shell 的 NetBSD 版本的大多数功能，提供了一些高级命令行编辑能力。

但令人不解的是，实际上 dash shell 在许多基于 Debian 的 Linux 发行版中并不是默认的 shell 。由于 bash shell 在 Linux 中的流行，大多数基于 Debian 的 Linux 发行版将 bash shell 用作普通登录 shell，而只将 dash shell 作为安装脚本的快速启动 shell，用于安装发行版文件。

### 1. dash 命令行参数

| 参数 | 描述                                                      |
| ---- | --------------------------------------------------------- |
| -a   | 导出分配给 shell 的所有变量                               |
| -c   | 从特定命令字符串中读取命令                                |
| -e   | 如果是非交互式 shell 的话，在有未测试的命令失败时立即退出 |
| -f   | 显示路径名通配符                                          |
| -n   | 如果是非交互式 shell 的话，读取命令但不执行它们           |
| -u   | 在尝试展开一个未设置的变量时，将错误消息写出到 STDERR     |
| -v   | 在读取输入时将输入写出到 STDERR                           |
| -x   | 在执行命令时将每个命令写出到 STDERR                       |
| `-I` | 在交互式模式下，忽略输入中的 EOF 字符                     |
| -i   | 强制 shell 运行在交互式模式下                             |
| -m   | 启用作业控制（在交互式模式下默认开启）                    |
| -s   | 从 STDIN 读取命令（在没有指定文件参数时的默认行为）       |
| -E   | 启用 emacs 命令行编辑器                                   |
| -V   | 启用 vi 命令行编辑器                                      |

### 2. 环境变量

#### 2.1 默认环境变量

由于 dash 的目标是简洁，因此它的环境变量比 bash shell 少多了。在 dash shell 环境中编写脚本是要记住这点。

dash shell 用 `set` 命令来显示环境变量。

```shell
$ set
CLASSPATH='/home/xiatuan/ProgramFiles/jdk8u345-b01/jre/lib'
CLUTTER_IM_MODULE='xim'
DBUS_SESSION_BUS_ADDRESS='unix:abstract=/tmp/dbus-o6T4nHpRo3'
DEFAULTS_PATH='/usr/share/gconf/gnome-flashback-metacity.default.path'
DESKTOP_SESSION='gnome-flashback-metacity'
DISPLAY=':0'
GDMSESSION='gnome-flashback-metacity'
GDM_LANG='zh_CN'
GNOME_DESKTOP_SESSION_ID='this-is-deprecated'
GNOME_KEYRING_CONTROL=''
GNOME_KEYRING_PID=''
```

#### 2.2 位置参数

除了默认环境变量，dash shell 还给命令行上定义的参数分配了特殊变量。下面是 dash shell 中用到的位置参数变量。

+ `$0`：shell 的名称。
+ `$n`：第 n 个位置参数。
+ `$*`：含有所有参数内容的单个值，由 IFS 环境变量中的第一个字符分隔；没有定义 IFS 的话，由空格分隔。
+ `$@`：将所有的命令行参数展开为多个参数。
+ `$#`：位置参数的总数。
+ `$?`：最近一个命令的退出状态码。
+ `$-`：当前选项标记。
+ `$$`：当前 shell 的进程 ID（PID）。
+ `$!`：最近一个后台命令的 PID。

#### 2.3 用户自定义的环境变量

与 bash 一样，你可以在命令行上用赋值语句来定义新的环境变量。

```shell
$ testing=10; export testing
p$ echo $testing
10
```

如果不用 `export` 命令，用户自定义的环境变量就只在当前 shell 或进程中可见。

> 警告：dash 变量和 bash 变量之间有一个巨大的差异。dash shell 不支持数组。

### 3. dash 内建命令

