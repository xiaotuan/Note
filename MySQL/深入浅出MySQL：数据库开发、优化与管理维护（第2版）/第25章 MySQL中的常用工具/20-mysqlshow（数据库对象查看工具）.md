

mysqlshow客户端对象查找工具，用来很快地查找存在哪些数据库、数据库中的表、表中的列或索引。和mysql客户端工具很类似，不过有些特性是mysql客户端工具所不具备的。

mysqlshow的使用方法如下：

shell> mysqlshow[option] [db_name [tbl_name [col_name]]]

如果不加任何选项，默认情况下会显示所有数据库。下例中显示了当前MySQL中的所有数据库：

[zzx@localhost～]$ mysqlshow -uroot

+--------------------+

|Databases|

+--------------------+

| information_schema |

| backup |

| data |

| index |

| mysql |

| test |

| test1 |

+--------------------+

下面是mysqlshow的一些常用选项。

（1）--count（显示数据库和表的统计信息）。

如果不指定数据库，则显示每个数据库的名称、表数量、记录数量；如果指定数据库，则显示指定数据库的每个表名、字段数量，记录数量；如果指定具体数据库中的具体表，则显示表的字段信息，如下例所示。

不指定数据库：

[zzx@localhost mysql]$ mysqlshow -uroot --count

+--------------------+--------+--------------+

| Databases | Tables | Total Rows |

+--------------------+--------+--------------+

| information_schema | 17 | 887 |

| bak | 0 | 0 |

| mysql | 18 | 1685 |

| test | 6 | 522 |

| test1 | 3 | 4 |

+--------------------+--------+--------------+

5 rows in set.

指定数据库：

[zzx@localhost mysql]$ mysqlshow -uroot test --count

Database: test

+--------+----------+------------+

| Tables | Columns | Total Rows |

+--------+----------+------------+

| books2 | 3 | 1 |

| dept | 2 | 512 |

| emp | 3 | 5 |

| emp1 | 3 | 3 |

| t2 | 1 | 1 |

| users2 | 2 | 0 |

+--------+----------+------------+

6 rows in set.

指定数据库和表：

[zzx@localhost mysql]$ mysqlshow -uroot test emp --count

Database: test Table: emp Rows: 5

+-------+-------+-----------+-----+-----+--------+------+----------+---------+

| Field | Type | Collation | Null| Key | Default| Extra|Privileges| Comment |

+-------+-------+-----------+-----+-----+--------+------+---------------------------------+-------+

| id |int(11)| | NO | PRI | 0 | | select, nsert, pdate,references | |

| name | varchar(200)| latin1_swedish_ci | YES | | | |select,insert,update,references | |

| content | text | latin1_swedish_ci | YES | | | |select,insert,update,references | |

+--------+-------------+------------+-------+------+------+-------+------+--------------------------------+--------+

（2）-k 或者--keys（显示指定表中的所有索引）。

此选项显示了两部分内容，一部分是指定表的表结构，另外一部分是指定表的当前索引信息。下例中显示了test库中表emp的表结构和当前索引信息：

[zzx@localhost mysql]$ mysqlshow -uroot test emp -k

Database: test Table: emp

+-------+---------+-----------+-----+----+-------+------+---------------+---------+

| Field | Type | Collation | Null| Key|Default|Extra |Privileges | Comment |

+-------+---------+----------------+---+---+-+-+-------------------------------+---+

| id | int(11) | |NO|PRI|0| |select,insert,update,references| |

| name |varchar(200)|latin1_swedish_ci|YES| | | |select,insert,update,references| |

|content| text |latin1_swedish_ci|YES| | | |select,insert,update,references| |

+-------+---------+----------------+---+---+-+-+-------------------------------+---+

+-------+---------+-----------+--------------+-------------+-----------+-------------+--------+--------+------+------------+---------+

| Table |Non_unique| Key_name | Seq_in_index | Column_name | Collation | Cardinality |

Sub_part| Packed | Null | Index_type | Comment |

+-------+---------+-----------+-----+----+-------+---------+-----------+-------------+

| emp | 0 | PRIMARY | 1 | id | A | 5| | BTREE|

+-------+---------+-----------+-----+----+-------+---------+-----------+-------------+

细心的读者可能会发现，显示的内容实际上和在mysql客户端执行“show full columns from emp”和“show index from emp”的结果完全一致。

[zzx@localhost～]$ mysql -uroot test -e 'show full columns from emp;show index from emp'

（3）-i 或者--status（显示表的一些状态信息）。

下例中显示了test数据库中emp表的一些状态信息：

[zzx@localhost mysql]$ mysqlshow -uroot test emp -i

Database: test Wildcard: emp

+------+------+--------+----------+----+---------------+------------+---------------+--------------+-----------+----------------+-------------------+------------+-----------+---------------+---------+---------------+----------+

| Name |Engine| Version | Row_format | Rows | Avg_row_length | Data_length | Max_data_length| Index_length | Data_free | Auto_increment | Create_time | Update_time | Check_time |Collation | Checksum| Create_options | Comment |

+------+-------+--------+------------+-----+--------------+------------+-+---------+-----------+--------------+---------------------+---------------++-------------------+---------+-------------+-----------------------+

| emp | InnoDB| 10 | Compact | 5 | 3276| 16384|0|0|

0 | | 2007-08-30 06:47:22 | || latin1_swedish_ci |

| | InnoDB free: 97280 kB |

+------+-------+--------+------------+-----+--------------+------------+-+---------+-----------+--------------+---------------------+---------------++-------------------+---------+-------------+-----------------------+

此命令和mysql客户端执行“show table status from test like 'emp'”的结果完全一致。



