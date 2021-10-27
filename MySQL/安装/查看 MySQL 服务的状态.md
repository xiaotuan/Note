[toc]

### 1. Linux

可以使用 `netstat -nlp` 命令查看 MySQL 服务的状态：

```shell
$ netstat -nlp
（并非所有进程都能被检测到，所有非本用户的进程信息将不会显示，如果想看到所有信息，则必须切换到 root 用户）
...           
unix  2      [ ACC ]     流        LISTENING     18612    -                   /var/run/NetworkManager/private-dhcp
unix  2      [ ACC ]     流        LISTENING     56304    -                   /var/run/mysqld/mysqld.sock
```

