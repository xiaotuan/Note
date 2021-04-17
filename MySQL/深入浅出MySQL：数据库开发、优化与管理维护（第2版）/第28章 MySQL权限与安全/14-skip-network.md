

在网络上不允许TCP/IP连接，所有到数据库的连接必须经由命名管道（Named Pipes）、共享内存（Shared Memory）或UNIX套接字（SOCKET）文件进行。这个选项适合应用和数据库共用一台服务器的情况，其他客户端将无法通过网络远程访问数据库，大大增强了数据库的安全性，但同时也带来了管理维护上的不方便，来看下面的例子。

服务器上打开此选项（默认关闭）并重启MySQL服务。

[mysqld]

skip-networking

port = 3311

…

远程客户端进行连接。

C:\mysql\bin>mysql -h192.168.7.55 -P3311 -uz2 -p

Enter password: ***

ERROR 2003 (HY000): Can't connect to MySQL server on '192.168.7.55' (10061)

关闭此选项后重启服务器。

[mysqld]

#skip-networking

port = 3311

…

远程客户端进行连接。

C:\mysql\bin>mysql -h192.168.7.55 -P3311 -uz2 -p

Enter password: ***

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 3 to server version: 5.1.11-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.



