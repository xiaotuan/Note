

在MySQL中，SQL Mode常用来解决下面几类问题。

通过设置SQL Mode，可以完成不同严格程度的数据校验，有效地保障数据准确性。

通过设置SQL Mode为ANSI模式，来保证大多数SQL符合标准的SQL语法，这样应用在不同数据库之间进行迁移时，则不需要对业务SQL进行较大的修改。

在不同数据库之间进行数据迁移之前，通过设置SQL Mode可以使MySQL上的数据更方便地迁移到目标数据库中。

下面通过一个简单的实例，让读者了解如何使用SQL Mode实现数据校验。

在 MySQL 5.0 上，查询默认的 SQL Mode（sql_mode 参数）为 REAL_AS_FLOAT、PIPES_AS_CONCAT、ANSI_QUOTES、GNORE_SPACE 和 ANSI。在这种模式下允许插入超过字段长度的值，只是在插入后， MySQL 会返回一个 warning。通过修改 sql_mode 为STRICT_TRANS_TABLES（严格模式）实现了数据的严格校验，使错误数据不能插入表中，从而保证了数据的准确性，具体实现如下。

（1）查看默认SQL Mode的命令如下：

mysql> select @@sql_mode;

+-------------------------------------------------------------+

| @@sql_mode |

+-------------------------------------------------------------+

| REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ANSI |

+-------------------------------------------------------------+

1 row in set (0.00 sec)

（2）查看测试表t的表结构的命令如下：

mysql> desc t;

+-------+-------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| name | varchar(20) | YES | | NULL | |

| email | varchar(40) | YES | | NULL | |

+-------+-------------+------+-----+---------+-------+

2 rows in set (0.00 sec)

（3）在表t中插入一条记录，其中name故意超出了实际的定义值varchar(20)：

mysql> insert into values('12340000000000000000999999','beijing @126.com');

Query OK, 1 row affected, 1 warning (0.00 sec)

（4）可以发现，记录可以插入，但是显示了一个warning，查看warning内容：

mysql> show warnings;

+---------+------+-------------------------------------------+

| Level | Code | Message |

+---------+------+-------------------------------------------+

| Warning | 1265 | Data truncated for column 'name' at row 1 |

+---------+------+-------------------------------------------+

1 row in set (0.00 sec)

（5）warning提示对插入的name值进行了截断，从表t中查看实际插入值：

mysql> select * from t;

+----------------------+-----------------+

| name | email |

+----------------------+-----------------+

| 12340000000000000000 | beijing@126.com |

+----------------------+-----------------+

1 row in set (0.00 sec)

果然，记录虽然插入进去，但是只截取了前20位字符。

（6）接下来设置SQL Mode为STRICT_TRANS_TABLES（严格模式）：

mysql> set session sql_mode='STRICT_TRANS_TABLES';

Query OK, 0 rows affected (0.01 sec)

mysql> select @@sql_mode;

+---------------------+

| @@sql_mode |

+---------------------+

| STRICT_TRANS_TABLES |

+---------------------+

1 row in set (0.01 sec)

（7）再次尝试插入上面的测试记录：

mysql> insert into t values('12340000000000000000999999','beijing@126.com');

ERROR 1406 (22001): Data too long for column 'name' at row 1

结果发现，这次记录没有插入成功，给出了一个ERROR，而不仅仅是warning。

上面的例子中，给出了 sql_mode 的一种修改方法，即 SET [SESSION|GLOBAL] sql_mode='modes'，其中SESSION选项表示只在本次连接中生效；而GLOBAL选项表示在本次连接中并不生效，而对于新的连接则生效，这种方法在MySQL 4.1开始有效。另外，也可以通过使用“--sql-mode="modes"”选项，在MySQL启动时设置sql_mode。



