系统密码文件 `/etc/passwd` 为每个用户都定义有一行记录，除了上述两项信息外，该记录还包含如下信息：

+ 组 ID：用户所属第一个组的整数型组 ID。
+ 主目录：用户登录后所居于的初始目录。
+ 登录 shell：执行以解释用户命令的程序名称。

例如：

```shell
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
qintuanye:x:1003:1003:,,,:/home/qintuanye:/bin/bash
wanchuanming:x:1004:1004:,,,:/home/wanchuanming:/bin/bash
lixiang:x:1005:1005:,,,:/home/lixiang:/bin/bash
fanyanmin:x:1006:1006:,,,:/home/fanyanmin:/bin/bash
......
```

该记录还能以加密形式保存用户密码。然而，出于安全考虑，用户密码往往存储于单独的 `shadow` 密码文件中，仅供特权用户阅读。

