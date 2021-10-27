[toc]

### 1. 简单使用

`ps` 是收集进程信息的重要工具。例如：

```shell
$ ps
  PID TTY          TIME CMD
 3933 pts/3    00:00:00 bash
 3943 pts/3    00:00:00 ps
```

`ps` 命令通常结合一系列参数使用。如果不使用任何参数，`ps` 将显示运行在当前终端中的进程。第一列显示进程 ID（PID），第二列是 TTY （终端），第三列是进程启动后过去的时间，最后一列是 CMD （进程所对应的命令）。

### 2. 使用 -f 参数来显示多列

可以使用 `-f` （表示 full）来显示多列：

```shell
$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
xiaotuan  3933  3928  0 14:42 pts/3    00:00:00 bash
xiaotuan  4439  3933  0 14:47 pts/3    00:00:00 ps -f
```

### 3. 使用 -e 参数显示所有进程信息

要获取运行在系统中的每个进程的信息，使用选项 `-e`（every）。选项 `-ax`（all）也可以生成同样的输出。运行如下命令之一：`ps -e`，`ps -ef`，`ps -ax` 或 `ps -axf`。

```shell
$ ps -e | head
  PID TTY          TIME CMD
    1 ?        00:00:03 systemd
    2 ?        00:00:00 kthreadd
    4 ?        00:00:00 kworker/0:0H
    6 ?        00:00:00 mm_percpu_wq
    7 ?        00:00:00 ksoftirqd/0
    8 ?        00:00:00 rcu_sched
    9 ?        00:00:00 rcu_bh
   10 ?        00:00:00 migration/0
   11 ?        00:00:00 watchdog/0
```

> 提示： 我们使用 `head` 进行了过滤，所以只列出了前 11 项。

### 4. 使用 -o 参数显示指定列

可以使用 `-o` 来指定想要显示的列。用法如下：

```shell
$ ps [OTHER OPTIONS] -o parameter1,parameter2,parameter3 ...
```

> 注意：`-o` 的参数以逗号操作符（,）作为定界符。值得注意的是，逗号操作符与它分隔的参数之间是没有空格的。在大多数情况下，选项 `-o` 都是和选项 `-e` 结合使用的 （`-oe`），因为它需要列出运行在系统中的每一个进程。但是如果 `-o` 需要使用某些过滤器，例如列出特定用户拥有的进程，那么就不再使用 `-e` 。`-e` 和过滤器结合使用没有任何实际效果，依旧会显示所有的进程。

```shell
$ ps -eo comm,pcpu | head
COMMAND         %CPU
systemd          0.0
kthreadd         0.0
kworker/0:0H     0.0
mm_percpu_wq     0.0
ksoftirqd/0      0.0
rcu_sched        0.0
rcu_bh           0.0
migration/0      0.0
watchdog/0       0.0
```

选项 `-o` 可以使用不同的参数，如下表所示：

| 参数  | 描述                 |
| ----- | -------------------- |
| pcpu  | CPU 占用率           |
| pid   | 进程 ID              |
| ppid  | 父进程 ID            |
| pmem  | 内存使用率           |
| comm  | 可执行文件名         |
| cmd   | 简单命令             |
| user  | 启动进程的用户       |
| nice  | 优先级               |
| time  | 累计的 CPU 时间      |
| etime | 进程启动后流逝的时间 |
| tty   | 所关联的 TTY 设备    |
| euid  | 有效用户 ID          |
| stat  | 进程状态             |

### 5. 根据参数对 ps 输出进行排序

可以用 `--sort` 将 `ps`命令的输出根据特定的列进行排序。在参数前加上 `+`（升序）或 `-` （降序）来指定排序方式：

```shell
$ ps [OPTIONS] --sort -paramter1,+parameter2,parameter3 ...
```

例如：

```shell
$ ps -eo comm,pcpu --sort -pcpu | head
COMMAND         %CPU
update-manager   0.3
VBoxClient       0.1
gnome-software   0.1
systemd          0.0
kthreadd         0.0
kworker/0:0H     0.0
mm_percpu_wq     0.0
ksoftirqd/0      0.0
rcu_sched        0.0
```

可以使用 `grep` 从 `ps` 的输出中提取与给定进程名或其他参数相关的条目。例如：

```shell
$ ps -eo comm,pid,pcpu,pmem | grep bash
bash             3933  0.0  0.2
```

### 6. 找出给定命令名所对应的进程 ID

可以通过下面命令获取给定命令名所对应的进程 ID：

```shell
$ ps -C COMMAND_NAME
```

或者

```shell
$ ps -C COMMAND_NAME -o pid=
```

在参数后加上 = 就可以移除列名：

```shell
$ ps -C bash -o pid=
 3933
```

也可以使用 `pgrep` 工具获取特定命令的进程 ID 列表：

```shell
$ pgrep COMMAND
```

例如：

```shell
$ pgrep bash
3933
```

> 提示：`pgrep` 只需要命令名的一部分作为输入参数来提取 `Bash` 命令，诸如 `pgrep ash` 或者 `pgrep bas` 都能奏效。

### 7. 根据真实用户名或 ID 以及有效用户名或 ID 过滤 ps 输出

实现方法如下：

+ 用 `-u EUSER1,EUSER2...`，指定有效用户列表；
+ 用 `-U RUSER1, RUSER2...`，指定真实用户列表。

例如：

```shell
$ ps -u root -U root -o user,p
```

### 8. 用 TTY 过滤 ps 输出

用选项 `-t` 指定 TTY 列表：

```shell
$ ps -t TTY1, TTY2 ...
```

例如：

```shell
$ ps -t pts/1,pts/14
  PID TTY          TIME CMD
 2474 pts/1    00:00:00 bash
 2484 pts/14   00:00:00 bash
 2608 pts/14   00:00:00 ps
```

### 9. 进程线程的相关信息

可以使用选项 `-L` 在 `ps` 输出中显示线程的相关信息。这会显示出两列：NLWP 和 NLP。NLWP 是进程的线程数量，NLP 是 ps 输出中每个条目的线程 ID。例如：

```shell
$ ps -eLf
```

或者：

```shell
$ ps -eLf --sort -nlwp | head
UID        PID  PPID   LWP  C NLWP STIME TTY          TIME CMD
root      1176     1  1176  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1178  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1179  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1180  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1181  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1182  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1183  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1184  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1176     1  1185  0    9 10:17 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
```

### 10. 指定输出宽度以及所要显示的列

尝试以下选项：

+ -f ps -ef
+ u ps -e u
+ ps ps -e w（w 表示宽松输出）

例如：

```shell
$ ps -ef | head
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 10:17 ?        00:00:03 /sbin/init splash
root         2     0  0 10:17 ?        00:00:00 [kthreadd]
root         4     2  0 10:17 ?        00:00:00 [kworker/0:0H]
root         5     2  0 10:17 ?        00:00:00 [kworker/u4:0]
root         6     2  0 10:17 ?        00:00:00 [mm_percpu_wq]
root         7     2  0 10:17 ?        00:00:00 [ksoftirqd/0]
root         8     2  0 10:17 ?        00:00:00 [rcu_sched]
root         9     2  0 10:17 ?        00:00:00 [rcu_bh]
root        10     2  0 10:17 ?        00:00:00 [migration/0]
$ ps -e u | head
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.5  0.2 119860  5928 ?        Ss   10:17   0:03 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S    10:17   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   10:17   0:00 [kworker/0:0H]
root         5  0.0  0.0      0     0 ?        I    10:17   0:00 [kworker/u4:0]
root         6  0.0  0.0      0     0 ?        I<   10:17   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    10:17   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    10:17   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    10:17   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    10:17   0:00 [migration/0]
$ ps -e w | head
  PID TTY      STAT   TIME COMMAND
    1 ?        Ss     0:03 /sbin/init splash
    2 ?        S      0:00 [kthreadd]
    4 ?        I<     0:00 [kworker/0:0H]
    5 ?        I      0:00 [kworker/u4:0]
    6 ?        I<     0:00 [mm_percpu_wq]
    7 ?        S      0:00 [ksoftirqd/0]
    8 ?        I      0:00 [rcu_sched]
    9 ?        I      0:00 [rcu_bh]
   10 ?        S      0:00 [migration/0]
```

### 11. 显示进程的环境变量

要在 `ps` 的输出条目中同时列出环境变量，可以使用：

```shell
$ ps -eo cmd e
```

例如：

```shell
$ ps -eo pid,cmd e | tail -n 3
 5638 [kworker/u4:2]
 5642 ps -eo pid,cmd e XDG_VTNR=7 LC_PAPER=zh_CN.UTF-8 LC_ADDRESS=zh_CN.UTF-8 XDG_SESSION_ID=c2 XDG_GREETER_DATA_DIR=/var/lib/lightdm-data/xiaotuan LC_MONETARY=zh_CN.UTF-8 CLUTTER_IM_MODULE=xim SESSION=gnome-flashback-metacity GPG_AGENT_INFO=/home/xiaotuan/.gnupg/S.gpg-agent:0:1 TERM=xterm-256color VTE_VERSION=4205 XDG_MENU_PREFIX=gnome-flashback- SHELL=/bin/bash QT_LINUX_ACCESSIBILITY_ALWAYS_ON=1 WINDOWID=56623166 LC_NUMERIC=zh_CN.UTF-8 UPSTART_SESSION=unix:abstract=/com/ubuntu/upstart-session/1000/1714 GNOME_KEYRING_CONTROL= GTK_MODULES=gail:atk-bridge:unity-gtk-module
......
```



