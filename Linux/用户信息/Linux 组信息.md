出于管理目的，尤其是为了控制对文件和其他资源的访问，将多个用户分组是非常实用的做法。每个用户组都对应着系统组文件 `/etc/group` 中的一行记录，该记录包含如下信息：

+ 组名：（唯一的）组名称。
+ 组 ID（ GID ）：与组相关的整数型 ID。
+ 用户列表：隶属于该组的用户登录名列表（通过密码文件记录的 `group ID` 字段未能标识出的该组其他成员，也在此列），以逗号分隔。

例如：

```shell
$ cat /etc/group
root:x:0:
daemon:x:1:
adm:x:4:syslog,anserver
bin:x:2:
wunanshi:x:1002:
qintuanye:x:1003:
wanchuanming:x:1004:
lixiang:x:1005:
fanyanmin:x:1006:
......
```

