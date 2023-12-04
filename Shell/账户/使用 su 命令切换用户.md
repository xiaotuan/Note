`su` 命令可以直接将当前用户切换到指定的用户，其命令格式如下：

```shell
su [选项] [用户名]
```

常用选项参数如下：

+ `-c`、`--command`：执行指定的命令，执行完毕以后恢复原用户身份。
+ `-login`：改变用户身份，同时改变工作目录和 `PATH` 环境变量。
+ `-m`：改变用户身份的时候不改变环境变量
+ `-h`：显示帮助信息

```shell
xiaotuan@xiaotuan:~$ sudo su
[sudo] xiaotuan 的密码： 
root@xiaotuan:/home/xiaotuan# 
root@xiaotuan:/home/xiaotuan# sudo su xiaotuan
xiaotuan@xiaotuan:~$ 
```

> 提示：`su` 命令不写明用户名的话默认切换到 `root` 用户。