在 `/etc/passwd` 文件中可以查看用户相关的信息：

```shell
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
xiaotuan:x:1000:1000:Xiaotuan,,,:/home/xiaotuan:/bin/bash
vboxadd:x:999:1::/var/run/vboxadd:/bin/false
mysql:x:121:129:MySQL Server,,,:/nonexistent:/bin/false
test:x:1001:1001:,,,:/home/test:/bin/bash
```

从配置文件 `passwd` 中可以看到，每个用户名后面都有两个数字，比如用户 `xiaotuan` 后面 `1000:1000`，第一个数字是用户的 ID，另一个是用户的 GID，也就是用户组 ID。