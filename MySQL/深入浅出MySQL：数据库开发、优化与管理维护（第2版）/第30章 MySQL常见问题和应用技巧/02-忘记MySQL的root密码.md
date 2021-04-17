

经常会有朋友或者同事问起，MySQL的root密码忘了，不知道改怎么办。其实解决方法很简单，这在前面的章节中也曾提及，下面是详细的操作步骤。

（1）登录到数据库所在的服务器，手工kill掉MySQL进程：

kill' cat /mysql-data-directory/hostname.pid'

其中，/mysql-data-directory/hostname.pid指的是MySQL数据目录下的.pid文件，它记录了MySQL服务的进程号。

（2）使用--skip-grant-tables选项重启MySQL服务：

[root@localhost mysql]# ./bin/mysqld_safe --skip-grant-tables --user=zzx &

[1] 20881

[root@localhost mysql]# Starting mysqld daemon with databases from /home/zzx/ mysql/data

其中--skip-grant-tables选项前面曾经介绍过，意思是启动MySQL服务时跳过权限表认证。启动后，连接到MySQL的root将不需要口令。

（3）用空密码的root用户连接到MySQL，并且更改root口令：

[root@localhost mysql]# mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 53

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>

mysql> set password = password('123');

ERROR 1290 (HY000): The MySQL server is running with the --skip-grant-tables option so it cannot execute this statement

mysql> update user set password=password('123') where user='root' and host='localhost';

Query OK, 1 row affected (0.00 sec)

Rows matched: 1 Changed: 1 Warnings: 0

此时，由于使用了--skip-grant-tables选项启动，使用“set password”命令更改密码失败，直接更新user表的password字段后更改密码成功。

（4）刷新权限表，使得权限认证重新生效：

mysql> flush privileges;

Query OK, 0 rows affected (0.00 sec)

（5）重新用root登录时，必须输入新口令：

[root@localhost mysql]# mysql -uroot

ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

[root@localhost mysql]# mysql -uroot -p123

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 6 to server version: 5.1.11-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>

**注意：**在MySQL中，密码丢失后无法找回，只能通过上述方式修改密码。



