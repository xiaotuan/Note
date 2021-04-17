

对于 MyISAM 存储引擎的表，在建表时可以用如下选项分别指定数据目录和索引目录存储到不同的磁盘空间，而默认会同时放在数据目录下：

DATA DIRECTORY = 'absolute path to directory'

INDEX DIRECTORY = 'absolute path to directory'

下例中创建了表t1，并使得数据目录和索引目录不同：

mysql> create table t1 (id int,name varchar(10))

-> data directory='/var/lib/mysql/data'

-> index directory='/var/lib/mysql/index';

Query OK, 0 rows affected (0.07 sec)

从操作系统上看表t1的物理文件如下：

lrwxrwxrwx 1 mysql mysql 27 Dec 4 14:29 t1.MYI -> /var/lib/mysql/index/t1.MYI

lrwxrwxrwx 1 mysql mysql 26 Dec 4 14:29 t1.MYD -> /var/lib/mysql/data/t1.MYD

-rw-rw---- 1 mysql mysql 8586 Dec 4 14:29 t1.frm

很显然，对数据文件和索引文件指定了两个不同的存放目录，实际上是在操作系统上创建了两个符号链接，指向了不同的目录。读者可能会想到，既然创建的时候可以指定数据索引分离，那么在使用过程中是不是也可以随时对这些路径进行再次变更呢？答案是否定的。在下例中，将尝试把t1的数据和索引目录放在一起：

mysql> alter table t1 index directory='/var/lib/mysql/data';

Query OK, 0 rows affected, 1 warning (0.03 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> show warnings;

+---------+------+--------------------------------+

| Level | Code | Message |

+---------+------+--------------------------------+

| Warning | 0 | INDEX DIRECTORY option ignored |

+---------+------+--------------------------------+

1 row in set (0.00 sec)

从warning中的提示可以看出，修改索引路径并没有成功。

对于上面这种情况，如果表已经创建，还可以将表的数据文件和索引文件mv到磁盘充足的分区上，然后在原文件处创建符号链接即可。当然，mv前必须要停机或者将表锁定，以防止表的更改。



