下面是 Linux 系统上典型的 /etc/passwd 文件内容：

```shell
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
```

`/etc/passwd` 文件的字段包含了如下信息：

+ 登录用户
+ 用户密码
+ 用户账户的 UID（数字形式）
+ 用户账户的组 ID（GID）（数字形式）
+ 用户账户的文本描述（称为备注字段）
+ 用户 HOME 目录的位置
+ 用户的默认 shell

现在，绝大多数 Linux 系统都将用户密码报错在另一个单独的文件中（叫作 shadow 文件，位置在 `/etc/shadow`）。只有特定的程序（比如登录程序）才能访问这个文件。