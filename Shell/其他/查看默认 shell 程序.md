系统启动什么样的 shell 程序取决于你个人的用户 ID 配置。在 `/etc/passwd` 文件中，在用户 ID记录的第 7 个字段中列出了默认的 shell 程序。

```shell
qintuanye@WB-SVR-27:~/AndroidProjectConfig$ cat /etc/passwd
qintuanye:x:1001:1001:,,,:/home/qintuanye:/bin/bash
```

默认的交互 shell 会在用户登录某个虚拟控制台终端或在 GUI 中运行终端仿真器时启动。不过还有另外一个默认 shell 是 `/bin/sh`，它作为默认的系统 shell，用于那些需要在启动时使用的系统脚本。