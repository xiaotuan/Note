

在MySQL服务器本机上连接数据库时，经常会出现mysql.sock不存在，导致无法连接的问题。这是因为如果指定localhost作为一个主机名，则mysqladmin默认使用UNIX套接字文件连接，而不是TCP/IP。而这个套接字文件（一般命名为mysql.sock）经常会因为各种原因而被删除。从MySQL 4.1开始，通过--protocol= TCP | SOCKET | PIPE | MEMORY}选项，用户可以显式地指定连接协议，下面演示了使用UNIX套接字失败后使用TCP协议连接成功的例子。

（1）UNIX 套接字连接：

[zzx@zzx mysql]$ mysql -uroot

ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/home/zzx/mysql/mysql.sock' (2)

（2）TCP连接：

[zzx@zzx mysql]$ mysql --protocol=TCP -uroot -p -P3307 -hlocalhost

Enter password:

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 73 to server version: 5.0.15-standard

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>



