在 CLI 提示符后输入 `/bin/bash` 命令或其他等效的 bash 命令时，会创建一个新的 shell 程序。这个 shell 程序被称为**子 shell**（child shell）。子 shell  也拥有 CLI 提示符，同样会等待命令输入。

可以利用 `exit` 命令有条不紊地退出子 shell。

```shell
$ ps --forest
  PID TTY          TIME CMD
50882 pts/11   00:00:00 bash
 6498 pts/11   00:00:00  \_ bash
 9925 pts/11   00:00:00      \_ ps
$ exit
exit
$ ps --forest
  PID TTY          TIME CMD
50882 pts/11   00:00:00 bash
14230 pts/11   00:00:00  \_ ps
```

`exit` 命令不仅能退出子 shell，还能用来登出当前的虚拟控制台终端或终端仿真器软件。只需要在父 shell 中输入 exit，就能够从容退出 CLI 了。