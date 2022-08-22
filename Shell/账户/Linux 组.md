组权限允许多个用户对系统中的对象（比如文件、目录或设备等）共享一组共用的权限。

`/etc/group` 文件包含系统上用到的每个组的信息：

```shell
$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,xiaotuan
tty:x:5:syslog
```

系统账户用的组通常会分配低于 500 的 GID 值，而用户组的 GID 则会从 500 开始分配。`/etc/group` 文件有 4 个字段：

+ 组名
+ 组密码
+ GID
+ 属于该组的用户列表

组密码允许非组内成员通过它临时成为该组成员。
