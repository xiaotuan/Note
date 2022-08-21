安装命令：

```shell
$ sudo apt-get update
$ sudo apt-get install mysql-server
```

启动和关闭`mysql` 服务器：

```shell
$ service mysql start
$ service mysql stop
```

检查 `mysql` 服务器是否启动成功：

```shell
$ sudo netstat -tap | grep mysql
tcp        0      0 localhost:mysql         *:*                     LISTEN      8039/mysqld 
```

