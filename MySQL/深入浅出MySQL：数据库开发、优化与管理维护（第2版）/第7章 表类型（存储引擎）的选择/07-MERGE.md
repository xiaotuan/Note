

MERGE存储引擎是一组MyISAM表的组合，这些MyISAM表必须结构完全相同，MERGE表本身并没有数据，对MERGE类型的表可以进行查询、更新、删除操作，这些操作实际上是对内部的MyISAM表进行的。对于MERGE类型表的插入操作，是通过INSERT_METHOD子句定义插入的表，可以有3个不同的值，使用FIRST或LAST值使得插入操作被相应地作用在第一或最后一个表上，不定义这个子句或者定义为NO，表示不能对这个MERGE表执行插入操作。

可以对MERGE表进行DROP操作，这个操作只是删除MERGE的定义，对内部的表没有任何的影响。

MERGE表在磁盘上保留两个文件，文件名以表的名字开始，一个.frm文件存储表定义，另一个.MRG文件包含组合表的信息，包括MERGE表由哪些表组成、插入新的数据时的依据。可以通过修改.MRG文件来修改MERGE表，但是修改后要通过FLUSH TABLES刷新。

下面是一个创建和使用MERGE表的示例。

（1）创建3个测试表payment_2006、payment_2007和payment_all，其中payment_all是前两个表的MERGE表：

mysql> create table payment_2006(

-> country_id smallint,

-> payment_date datetime,

-> amount DECIMAL(15,2),

-> KEY idx_fk_country_id (country_id)

-> )engine=myisam;

Query OK, 0 rows affected (0.03 sec)

mysql> create table payment_2007(

-> country_id smallint,

-> payment_date datetime,

-> amount DECIMAL(15,2),

-> KEY idx_fk_country_id (country_id)

-> )engine=myisam;

Query OK, 0 rows affected (0.02 sec)

mysql> CREATE TABLE payment_all(

-> country_id smallint,

-> payment_date datetime,

-> amount DECIMAL(15,2),

-> INDEX(country_id)

-> )engine=merge union=(payment_2006,payment_2007) INSERT_METHOD=LAST;

Query OK, 0 rows affected (0.04 sec)

（2）分别向payment_2006和payment_2007表中插入测试数据：

mysql> insert into payment_2006 values(1,'2006-05-01',100000),(2, '2006-08-15',150000);

Query OK, 2 rows affected (0.00 sec)

Records: 2 Duplicates: 0 Warnings: 0

mysql> insert into payment_2007 values(1, '2007-02-20',35000),(2, '2007-07-15', 220000);

Query OK, 2 rows affected (0.00 sec)

Records: 2 Duplicates: 0 Warnings: 0

（3）分别查看这3个表中的记录：

mysql> select * from payment_2006;

+------------+---------------------+-----------+

| country_id | payment_date | amount |

+------------+---------------------+-----------+

| 1 | 2006-05-01 00:00:00 | 100000.00 |

| 2 | 2006-08-15 00:00:00 | 150000.00 |

+------------+---------------------+-----------+

2 rows in set (0.00 sec)

mysql> select * from payment_2007;

+------------+---------------------+-----------+

| country_id | payment_date | amount |

+------------+---------------------+-----------+

| 1 | 2007-02-20 00:00:00 | 35000.00 |

| 2 | 2007-07-15 00:00:00 | 220000.00 |

+------------+---------------------+-----------+

2 rows in set (0.00 sec)

mysql> select * from payment_all;

+------------+---------------------+-----------+

| country_id | payment_date | amount |

+------------+---------------------+-----------+

| 1 | 2006-05-01 00:00:00 | 100000.00 |

| 2 | 2006-08-15 00:00:00 | 150000.00 |

| 1 | 2007-02-20 00:00:00 | 35000.00 |

| 2 | 2007-07-15 00:00:00 | 220000.00 |

+------------+---------------------+-----------+

4 rows in set (0.00 sec)

可以发现，payment_all表中的数据是payment_2006和payment_2007表的记录合并后的结果集。

下面向MERGE表中插入一条记录，由于MERGE表的定义是INSERT_METHOD=LAST，就会向最后一个表中插入记录，所以虽然这里插入的记录是 2006 年的，但仍然会写到payment_2007表中。

mysql> insert into payment_all values(3, '2006-03-31',112200);

Query OK, 1 row affected (0.00 sec)

mysql> select * from payment_all;

+------------+---------------------+-----------+

| country_id | payment_date | amount |

+------------+---------------------+-----------+

| 1 | 2006-05-01 00:00:00 | 100000.00 |

| 2 | 2006-08-15 00:00:00 | 150000.00 |

| 1 | 2007-02-20 00:00:00 | 35000.00 |

| 2 | 2007-07-15 00:00:00 | 220000.00 |

| 3 | 2006-03-31 00:00:00 | 112200.00 |

+------------+---------------------+-----------+

5 rows in set (0.00 sec)

mysql> select * from payment_2007;

+------------+---------------------+-----------+

| country_id | payment_date | amount |

+------------+---------------------+-----------+

| 1 | 2007-02-20 00:00:00 | 35000.00 |

| 2 | 2007-07-15 00:00:00 | 220000.00 |

| 3 | 2006-03-31 00:00:00 | 112200.00 |

+------------+---------------------+-----------+

3 rows in set (0.00 sec)

这也是MERGE表和分区表的区别，MERGE表并不能智能地将记录写到对应的表中，而分区表是可以的（分区功能在5.1版中正式推出）。通常我们使用MERGE表来透明地对多个表进行查询和更新操作，而对这种按照时间记录的操作日志表则可以透明地进行插入操作。



