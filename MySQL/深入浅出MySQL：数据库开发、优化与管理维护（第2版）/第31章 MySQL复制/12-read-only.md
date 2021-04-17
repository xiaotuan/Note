

read-only该参数用来设置从库只能接受超级用户的更新操作，从而限制应用程序错误的对从库的更新操作。下面创建了一个普通用户，在默认情况下，该用户是可以更新从数据库中的数据的，但是使用read-only选项启动从数据库以后，该用户对从数据库的更新会提示错误。

（1）在主数据库中创建用户：

mysql> grant ALL PRIVILEGES on test.* to 'lisa'@'%' identified by '1234';

Query OK, 0 rows affected (0.00 sec)

（2）从库使用该用户登录，可以删除表中的记录：

[mysql@master1 log]$ mysql -ulisa -p1234 test

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 12 to server version: 5.1.9-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> select * from repl_test;

+------+---------------------+

| id | createtime|

+------+---------------------+

| 5| 2007-07-24 15:31:37 |

| 5 | 2007-07-24 15:36:47 |

+------+---------------------+

2 rows in set (0.00 sec)

mysql> delete from repl_test;

Query OK, 2 rows affected (0.00 sec)

mysql> select * from repl_test;

Empty set (0.00 sec)

（3）关闭从库，使用read-only选项启动从数据库：

[mysql@master1 log]$ mysqladmin -uroot -p shutdown

Enter password:

STOPPING server from pid file /home/mysql/sysdb/mysqld.pid

070724 17:13:06 mysqld ended

[mysql@master1 mysql_home]$ ./bin/mysqld_safe --read-only&

[1] 9814

[mysql@master1 mysql_home]$ Starting mysqld daemon with databases from /home/mysql/sysdb/data

（4）再使用Lisa用户登录数据库，进行删除操作：

[mysql@master1 data]$ mysql -ulisa -p1234 test

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 4 to server version: 5.1.9-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> select * from repl_test;

Empty set (0.00 sec)

mysql> select * from repl_test;

+------+---------------------+

| id | createtime |

+------+---------------------+

| 5 | 2007-07-24 16:29:49 |

+------+---------------------+

1 row in set (0.00 sec)

mysql> delete from repl_test;

ERROR 1290 (HY000): The MySQL server is running with the --read-only option so it cannot execute this statement

可以看到，使用 read-only 启动的从数据库会拒绝普通用户的更新操作，以确保从数据库的安全性。



