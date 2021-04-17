

skip-grant-tables这个选项导致服务器根本不使用权限系统，从而给每个人以完全访问所有数据库的权力。通过执行mysqladmin flush-privileges或mysqladmin reload命令，或执行 flush privileges语句，都可以让一个正在运行的服务器再次开始使用授权表。

下面的例子演示了此参数的使用。

使用--skip-grant-tables启动数据库。

[root@localhost bin]# mysqld_safe --skip-grant-tables &

[1] 15298

[root@localhost bin]# Starting mysqld daemon with databases from /var/lib/mysql

此时用root用户可以直接登录，而不需要密码。

[root@localhost bin]# mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 1

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>

此时执行 flush privileges命令，重新使用权限系统。

mysql> flush privileges;

Query OK, 0 rows affected (0.00 sec)

mysql> exit

Bye

退出后再次登录，将无法登录成功。

[root@localhost bin]# mysql -uroot

ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)



