Welcome to the MySQL monitor. Commands end with ; or \g.



此参数如果启用，用户将不能用GRANT语句创建新用户，除非用户有mysql数据库中user表的INSERT权限。如果想让用户具有授权权限来创建新用户，应给用户授予下面的权限：

mysql > GRANT INSERT(user) ON mysql.user TO 'user_name'@'host_name';

这样确保用户不能直接更改权限列，必须使用GRANT语句给其他用户授予该权限。以下例子描述了这个过程。

（1）用root创建用户z1，z1可以将权限授予其他用户：

[zzx@localhost～]$ mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 57

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> grant select,insert on test1.* to z1@localhost with grant option;

Query OK, 0 rows affected (0.00 sec)

mysql> exit

Bye

（2）使用z1创建新用户成功：

[zzx@localhost～]$ mysql -uz1

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 58

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> grant select on test1.* to z3@localhost;

Query OK, 0 rows affected (0.00 sec)

mysql> exit

（3）用safe-user-create选项重启数据库：

[root@localhost bin]# ./mysqld_safe --safe-user-create &

[1] 32422

[root@localhost bin]# Starting mysqld daemon with databases from /var/lib/mysql

（4）重新用z1创建用户失败：

[root@localhost bin]# mysql -uz1

Your MySQL connection id is 2

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> grant select on test1.* to 'z4'@'192.168';

ERROR 1410 (42000): You are not allowed to create a user with GRANT

mysql> exit

（5）用root登录，给z1赋予mysql数据库中user表的insert权限：

[root@localhost bin]# mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 5

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> grant insert on mysql.user to z1@localhost;

Query OK, 0 rows affected (0.00 sec)

mysql> exit

Bye

（6）用z1重新登录，授权用户成功：

[root@localhost bin]# mysql -uz1

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 7

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> grant select on test1.* to 'z4'@localhost;

Query OK, 0 rows affected (0.00 sec)



