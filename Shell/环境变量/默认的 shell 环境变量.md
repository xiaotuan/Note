[toc]

### 1. bash shell 支持的 Bourne 变量

| 变量     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| CDPATH   | 冒号分隔的目录列表，作为 cd 命令的搜索路径                   |
| HOME     | 当前用户的主目录                                             |
| IFS      | shell 用来将文本字符串分割成字段的一系列字符                 |
| MAIL     | 当前用户收件箱的文件名（bash shell 会检查这个文件，看看有没有新邮件） |
| MAILPATH | 冒号分隔的当前用户收件箱的文件名列表（bash shell 会检查列表中每个文件，看看有没有新邮件） |
| OPTARG   | getopts 命令处理的最后一个选项参数值                         |
| OPTIND   | getopts 命令处理的最后一个选项参数的索引号                   |
| PATH     | shell 查找命令的目录列表，由冒号分隔                         |
| PS1      | shell 命令行界面的主提示符                                   |
| PS2      | shell 命令行界面的次提示符                                   |

### 2. bash shell 环境变量

| 变量                  | 描述                                                         |
| --------------------- | ------------------------------------------------------------ |
| BASH                  | 当前 shell 实例的全路径名                                    |
| BASH_ALIASES          | 含有当前已设置别名的关联数据                                 |
| BASH_ARGC             | 含有传入子函数或 shell 脚本的参数总数的数组变量              |
| BASH_ARCV             | 含有传入子函数或 shell 脚本的参数的数组变量                  |
| BASH_CMDS             | 关联数组，包含 shell 执行过的命令的所在位置                  |
| BASH_COMMAND          | shell 正在执行的命令或马上就执行的命令                       |
| BASH_ENV              | 设置了的话，每个 bash 脚本会在运行前先尝试运行该变量定义的启动文件 |
| BASH_EXECUTION_STRING | 使用 bash -c 选项传递过来的命令                              |
| BASH_LINENO           | 含有当前执行的 shell 函数的源代码行号的数组变量              |
| BASH_REMATCH          | 进行肯定匹配时，包含了匹配到的模式和子模式                   |
| BASH_SOURCE           | 含有当前正在执行的 shell 函数所在源文件名的数组变量          |
| BASH_SUBSHELL         | 当前子 shell 环境的嵌套级别（初始值是 0）                    |
| BASH_VERSINFO         | 含有当前运行的 bash shell 的主版本号和次版本号的数组变量     |
| BASH_VERSION          | 当前运行的 bash shell 的版本号                               |
| BASH_XTRACEFD         | 若设置成了有效的文件描述符（0、1、2），则 `set -x` 调试选项生成的跟踪输出可被重定向。通常用来将跟踪输出到一个文件中。 |
| BASHOPTS              | 当前启用的 bash shell 选项的列表                             |
| BASHPID               | 当前 bash  进程的 PID                                        |
| COLUMNS               | 当前 bash shell 示例所用终端的宽度                           |
| COMP_CWORD            | COMP_CWORD 变量的索引值，后者含有当前光标的位置              |
| COMP_LINE             | 当前命令行                                                   |
| COMP_POINT            | 当前光标位置相对于当前命令起始的索引                         |
| COMP_KEY              | 用来调用 shell 函数补全功能的最后一个键                      |
| COMP_TYPE             | 一个整数值，表示所尝试的补全类型，用以完成 shell 函数补全    |
| COMP_WORDBREAKS       | Readline 库中用于单词补全的词分隔字符                        |
| COMP_WORDS            | 含有当前命令行所有单词的数组变量                             |
| COMPREPLY             | 含有由 shell 函数生成的可能填充代码的数组变量                |
| COPROC                | 占用未命名的协进程的 I\O 文件描述符的数组变量                |
| DIRSTACK              | 含有目录栈当前内容的数组变量                                 |
| EMACS                 | 设置为 't' 时，表明 emacs shell 缓冲区正在工作，而行编辑功能被禁止 |
| ENV                   | 如果设置了该环境变量，在 bash shell 脚本运行之前会先执行已定义的启动文件（仅用于当 bash shell 以 POSIX 模式被调用时) |
| EUID                  | 当前用户的有效用户 ID（数字形式）                            |
| FCEDIT                | 供 fc 命令使用的默认编辑器                                   |
| FIGNORE               | 在进行文件名补全时可以忽略后缀名列表，由冒号分隔             |
| FUNCNAME              | 当前执行的 shell 函数的名称                                  |
| FUNCNEST              | 当设置成非零值时，表示所允许的最大函数嵌套级数（一旦超出，当前命令即被终止） |
| GLOBIGNORE            | 冒号分隔的模式列表，定义了在进行文件名扩展时可以忽略的一组文件名 |
| GROUPS                | 含有当前用户属组列表的数组变量                               |
| histchars             | 控制历史记录扩展，最多可有 3 个字符                          |
| HISTCMD               | 当前命令在历史记录中的编号                                   |
| HISTCONTROL           | 控制哪些命令留在历史记录列表中                               |
| HISTFILE              | 保存 shell 历史记录列表的文件名（默认是 `.bash_history`）    |
| HISTFILESIZE          | 最多在历史文件中存多少行                                     |
| HISTTIMEFORMAT        | 如果设置了且非空，就用作格式化字符串，以显示 bash 历史中每条命令的时间戳 |
| HISTIGNORE            | 由冒号分隔的模式列表，用来决定历史文件中哪些命令会被忽略     |
| HISTSIZE              | 最多在历史文件中存多少条命令                                 |
| HOSTFILE              | shell 在补全主机名时读取的文件名称                           |
| HOSTNAME              | 当前主机名称                                                 |
| HOSTTYPE              | 当前运行 bash shell 的机器                                   |
| IGNOREEOF             | shell 在退出前必须收到连续的 EOF 字符的数量（如果这个值不存在，默认是 1） |
| INPUTRC               | Readline 初始化文件名（默认是 `.inputrc`）                   |
| LANG                  | shell 的语言环境类别                                         |
| LC_ALL                | 定义了一个语言环境类别，能够覆盖 LANG 变量                   |
| LC_COLLATE            | 设置对字符串排序时用的排序规则                               |
| LC_CTYPE              | 决定如何解释出现在文件名扩展和模式匹配中的字符               |
| LC_MESSAGES           | 在解释前面带有 $ 的双引号字符串时，该环境变量决定了所采用的语言环境设置 |
| LC_NUMERIC            | 决定着格式化数字时采用的语言环境设置                         |
| LINENO                | 当前执行的脚本的行号                                         |
| LINES                 | 定义了终端上可见的行数                                       |
| MACHTYPE              | 用 "CPU-公司-系统" （CPU-company-system） 格式定义的系统类型 |
| MAPFILE               | 一个数组变量，当 mapfile 命令未指定数组变量作为参数时，它存储了 mapfile 所读入的文本 |
| MALLCHECK             | shell 查看新邮件的频率（以秒为单位，默认是 60 秒）           |
| OLDPWD                | shell 之前的工作目录                                         |
| PWD                   | 当前工作目录                                                 |
| RANDOM                | 返回一个 0 ~ 32767 的随机数（对其的赋值可作为随机数生成器的种子） |
| READLINE_LINE         | 当使用 `bind -x` 命令时，存储 Readline 缓存区的内容          |
| READLINE_POINT        | 当使用 `bind -x` 命令时，表示 Readline 缓存区内容插入点的当前位置 |
| REPLY                 | read 命令的默认变量                                          |
| SECONDS               | 自从 shell 启动到现在的秒数（对其赋值将会重置计数器          |
| SHELL                 | bash shell 的全路径名                                        |
| SHELLOPTS             | 已启用 bash shell 选项列表，列表项之间以冒号分隔             |
| SHLVL                 | shell 的层级；每次启动一个新 bash shell，该值增加 1          |
| TIMEFORMAT            | 指定了 shell 的时间显示格式                                  |
| TMOUT                 | select 和 read 命令在没输入的情况下等待多久（以秒为单位）。默认值为 0，表示无限长 |
| TMPDIR                | 目录名，保存 bash shell 创建的临时文件                       |
| UID                   | 当前用户的真实用户 ID（数字形式）                            |

