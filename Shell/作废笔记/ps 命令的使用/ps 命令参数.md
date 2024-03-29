[toc]

### 1. Unix 风格的 ps 命令参数

| 参数        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| -A          | 显示所有进程                                                 |
| -N          | 显示与指定参数不符的所有进程                                 |
| -a          | 显示除控制进程（session leader[^1]）和无终端进程外的所有进程 |
| -d          | 显示除控制进程外的所有进程                                   |
| -e          | 显示所有进程                                                 |
| -C cmdList  | 显示包含在 cmdList 列表中的进程                              |
| -G grpList  | 显示组 ID 在 grpList 列表中的进程                            |
| -U userList | 显示属主的用户 ID 在 userList 列表中的进程                   |
| -g grpList  | 显示会话或组 ID 在 grpList 列表中的进程[^2]                  |
| -p pidList  | 显示 PID 在 pidList 列表中的进程                             |
| -s sessList | 显示会话 ID 在 sessList 列表中的进程                         |
| -t ttyList  | 显示终端 ID 在 ttyList 列表中的进程                          |
| -u userList | 显示有效用户 ID 在 userList 列表中的进程                     |
| -F          | 显示更多额外输出（相对 -f 参数而言）                         |
| -O format   | 显示默认的输出列以及 format 列表指定的特定列                 |
| -M          | 显示进程的安全信息                                           |
| -c          | 显示进程的额外调度器信息                                     |
| -f          | 显示完整格式的输出                                           |
| -j          | 显示任务信息                                                 |
| -l          | 显示长列表                                                   |
| -o format   | 仅显示由 format 指定的列                                     |
| -y          | 不要显示进程标记（process flag，表明进程状态的标记）         |
| -Z          | 显示安全标签（security context）[^3]信息                     |
| -H          | 用层级格式来显示进程（树状，用来显示父进程）                 |
| -n nameList | 定义了 WCHAN 列显示的值                                      |
| -w          | 采用宽输出模式，不限宽度显示                                 |
| -L          | 显示进程中的线程                                             |
| -V          | 显示 ps 命令的版本号                                         |

[^1]: 关于 session leader 的概念，可参考《Unix 环境高级编程（第 3 版）》 第 9 章的内容。
[^2]: 这个在不同的 Linux 发行版中可能不尽相同，有的发行版中 grplist 代表会话 ID，有的发行版中 grpList 代表有效组 ID。
[^3]: security context 也叫 security label，是 SELinux 采用声明资源的一种机制。

### 2. BSD 风格的 ps 命令参数

| 参数       | 描述                                                      |
| ---------- | --------------------------------------------------------- |
| T          | 显示跟当前终端关联的所有进程                              |
| a          | 显示跟任意终端关联的所有进程                              |
| g          | 显示所有的进程，包括控制进程                              |
| r          | 仅显示运行中的进程                                        |
| x          | 显示所有的进程，甚至包括未分配任何终端的进程              |
| u userList | 显示归 userList 列表中某用户 ID 所有的进程                |
| p pidList  | 显示 PID 在 pidList 列表中的进程                          |
| t ttyList  | 显示所关联的终端在 ttyList 列表中的进程                   |
| O format   | 除了默认输出的列之外，还输出由 format 指定的列            |
| X          | 按过去的 Linux i386 寄存器格式显示                        |
| Z          | 将安全信息添加到输出中                                    |
| j          | 显示任务信息                                              |
| l          | 采用长模式                                                |
| o format   | 仅显示由 format 指定的列                                  |
| s          | 采用信号格式显示                                          |
| u          | 采用基于用户的格式显示                                    |
| v          | 采用虚拟内存格式显示                                      |
| N nameList | 定义在 WCHAN 列中使用的值                                 |
| O order    | 定义显示信息列的顺序                                      |
| S          | 将数值信息从子进程加到父进程上，比如 CPU 和内存的使用情况 |
| c          | 显示真实的命令名称（用以启动进程的程序名称）              |
| e          | 显示命令使用的环境变量                                    |
| f          | 用分层格式来显示进程，表明哪些进程启动了哪些进程          |
| h          | 不显示头信息                                              |
| k sort     | 指定用以将输出排序的列                                    |
| n          | 和 WCHAN 信息一起显示出来，用数值来表示用户 ID 和组 ID    |
| w          | 为较宽屏幕显示输出                                        |
| H          | 将线程按进程来显示                                        |
| m          | 在进程后显示线程                                          |
| L          | 列出所有格式指定符                                        |
| V          | 显示 ps 命令的版本号                                      |

### 3. GNU 风格的 ps 命令参数

| 参数            | 描述                                     |
| --------------- | ---------------------------------------- |
| --deselect      | 显示所有进程，命令行中列出的进程         |
| --Group grpList | 显示组 ID 在 grpList 列表中的进程        |
| --User userList | 显示用户 ID 在 userList 列表中的进程     |
| --group grpList | 显示有效组 ID 在 grpList 列表中的进程    |
| --pid pidList   | 显示 PID 在 pidList 列表中的进程         |
| --ppid pidList  | 显示父 PID 在 pidList 列表中的进程       |
| --sid sidList   | 显示会话 ID 在 sidList 列表中的进程      |
| --tty ttyList   | 显示终端设备号在 ttyList 列表中的进程    |
| --user userList | 显示有效用户 ID 在 userList 列表中的进程 |
| --format format | 仅显示由 format 指定的列                 |
| --context       | 显示额外的安全信息                       |
| --cols n        | 将屏幕宽度设置为 n 列                    |
| --columns n     | 将屏幕宽度设置为 n 列                    |
| --cumulative    | 包含已停止的子进程的信息                 |
| --forest        | 用层级结构显示出进程和父进程之间的关系   |
| --headers       | 在每页输出中都显示列的头                 |
| --no-headers    | 不显示列的头                             |
| --lines n       | 将屏幕高度设为 n 行                      |
| --rows n        | 将屏幕高度设为 n 排                      |
| --sort order    | 指定将输出按哪列排序                     |
| --width n       | 将屏幕宽度设为 n 列                      |
| --help          | 显示帮助信息                             |
| --info          | 显示调试信息                             |
| --version       | 显示 ps 命令的版本号                     |



