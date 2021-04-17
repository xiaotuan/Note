

myisampack是一个表压缩工具，可以使用很高的压缩率来对MyISAM存储引擎的表进行压缩，使得压缩后的表占用比压缩前小得多的磁盘空间。但是压缩后的表也将成为一个只读表，不能进行DML操作。

此工具的用法如下：

shell> myisampack [options] filename

下面是一个使用myisampack工具前后的对比示例。

（1）压缩前，粗体显示表t2的数据文件大小为1146894字节。

[root@localhost test]# ls -ltr

total 440

-rw-rw---- 1 mysql mysql　59 Aug 11 06:38 db.opt

-rw-rw---- 1 mysql mysql　1024 Aug 11 06:38 dept.MYI

-rw-rw---- 1 mysql mysql　10240 Aug 11 06:38 dept.MYD

-rw-rw---- 1 mysql mysql　8586 Aug 11 06:38 dept.frm

-rw-rw---- 1 mysql mysql　8556 Aug 17 04:21 t2.frm

-rw-rw---- 1 mysql mysql　8622 Aug 27 06:53 emp.frm

-rw-rw---- 1 mysql mysql　8622 Aug 27 07:13 emp1.frm

-rw-rw---- 1 mysql mysql　1024 Aug 30 03:11 t2.MYI

-rw-rw---- 1 mysql mysql　1146894 Aug 30 03:11 t2.MYD

（2）对表t2进行压缩。

[root@localhost test]# myisampack t2

Compressing t2.MYD: (163842 records)

- Calculating statistics

- Compressing file

93.46%

（3）压缩后t2的数据文件大小变为75016字节（粗体显示），压缩后的文件仅占原文件的6.54%（1-93.46%）。

[root@localhost test]# ls -ltr

total 188

-rw-rw---- 1 mysql mysql 59 Aug 11 06:38 db.opt

-rw-rw---- 1 mysql mysql 1024 Aug 11 06:38 dept.MYI

-rw-rw---- 1 mysql mysql 10240 Aug 11 06:38 dept.MYD

-rw-rw---- 1 mysql mysql 8586 Aug 11 06:38 dept.frm

-rw-rw---- 1 mysql mysql 8556 Aug 17 04:21 t2.frm

-rw-rw---- 1 mysql mysql 8622 Aug 27 06:53 emp.frm

-rw-rw---- 1 mysql mysql 8622 Aug 27 07:13 emp1.frm

-rw-rw---- 1 mysql mysql 75016 Aug 30 03:11 t2.MYD

-rw-rw---- 1 mysql mysql 1024 Aug 30 03:11 t2.MYI

（4）测试压缩后的表功能：往表t2中做插入和查询操作。

[root@localhost test]# mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 47

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> use test

Reading table information for completion of table and column names

You can turn off this feature to get a quicker startup with -A

Database changed

mysql> flush tables;

Query OK, 0 rows affected (0.00 sec)

mysql> insert into t2 values(1);

ERROR 1036 (HY000): Table 't2' is read only

mysql> select count(1) from t2;

+----------+

| count(1) |

+----------+

| 163842 |

+----------+

1 row in set (0.00 sec)

显然，查询正常，却无法进行更新操作。



