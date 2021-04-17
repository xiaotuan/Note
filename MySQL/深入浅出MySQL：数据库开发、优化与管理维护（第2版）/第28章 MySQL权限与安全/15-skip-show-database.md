

使用 skip-show-database选项，只允许有 show databases权限的用户执行 show databases语句，该语句显示所有数据库名。不使用该选项，允许所有用户执行 show databases，但只显示用户有 show databases 权限或部分数据库权限的数据库名。下面的例子显示了启用此选项后show databases的执行结果：

[root@localhost bin]# mysqld_safe --skip-show-database &

[1] 15027

[root@localhost bin]# Starting mysqld daemon with databases from /var/lib/mysql

[root@localhost bin]# mysql -uz2

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 4

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> show databases;

ERROR 1227 (42000): Access denied; you need the SHOW DATABASES privilege for this operation



