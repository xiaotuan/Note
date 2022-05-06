[toc]

### 1. Unix 风格的字段意思

```shell
$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root       87093       1  0 09:03 ?        00:00:00 /usr/bin/python3 /usr/bin/ne
syslog     89635       1  0 09:04 ?        00:00:00 /usr/sbin/rsyslogd -n -iNONE
xiaotuan   92664    1382  0 15:03 ?        00:00:05 /usr/bin/gedit --gapplicatio
root       95796       2  0 15:58 ?        00:00:02 [kworker/2:2-mm_percpu_wq]
xiaotuan   97709   39281  0 19:38 pts/0    00:00:00 ps -ef
$
```

+ **UID**：启动这些进程的用户。
+ **PID**：进程的进程 ID。
+ **PPID**：父进程的进程号（如果该进程是由另一个进程启动的）。
+ **C**：进程生命周期中的 CPU 利用率。
+ **STIME**：进程启动时的系统时间。
+ **TTY**：进程启动时的终端设备。
+ **TIME**：运行进程需要的累计 CPU 时间。
+ **CMD**：启动的程序名称。

```shell
$ ps -l
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000   39281   39270  0  80   0 -  3563 do_wai pts/0    00:00:00 bash
4 R  1000   97720   39281  0  80   0 -  3627 -      pts/0    00:00:00 ps
$
```

+ **F**：内核分配给进程的系统标记。
+ **S**：进程的状态（O 代表正在运行；S 代表在休眠；R 代表可运行，正等待运行；Z 代表僵化，进程已结束但父进程已不存在；T 代表停止）。
+ **PRI**：进程的优先级（越大的数字代表越低的优先级）。
+ **NI**：谦让度值用来参与决定优先级。
+ **ADDR**：进程的内存地址。
+ **SZ**：假如进程被换出，所需交换空间的大致大小。
+ **WCHAN**：进程休眠的内核函数的地址。