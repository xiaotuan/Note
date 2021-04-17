

DCL语句主要是DBA用来管理系统中的对象权限时使用，一般的开发人员很少使用。下面通过一个例子简单说明一下。

创建一个数据库用户z1，具有对sakila数据库中所有表的SELECT/INSERT权限：

mysql> grant select,insert on sakila.* to 'z1'@'localhost' identified by '123';

Query OK, 0 rows affected (0.00 sec)

mysql> exit

Bye

[mysql@db3～]$ mysql -uz1 -p123

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 21671 to server version: 5.1.9-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> use sakila

Database changed

mysql> insert into emp values('bzshen','2005-04-01',3000,'3');

Query OK, 1 row affected (0.04 sec)

由于权限变更，需要将z1的权限变更，收回INSERT，只能对数据进行SELECT操作：

[mysql@db3～]$ mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 21757 to server version: 5.1.9-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> revoke insert on sakila.* from 'z1'@'localhost';

Query OK, 0 rows affected (0.00 sec)

mysql> exit

Bye

用户z1重新登录后执行前面语句：

[mysql@db3～]$ mysql -uz1 -p123

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 21763 to server version: 5.1.9-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> insert into emp values('bzshen','2005-04-01',3000,'3');

ERROR 1046 (3D000): No database selected

mysql> use sakila

Database changed

mysql> insert into emp values('bzshen','2005-04-01',3000,'3');

ERROR 1142 (42000): INSERT command denied to user 'z1'@'localhost' for table 'emp'

以上例子中的grant和revoke分别授出和收回了用户z1的部分权限，达到了我们的目的。关于权限的更多内容，将会在本书的第28章中详细介绍。



