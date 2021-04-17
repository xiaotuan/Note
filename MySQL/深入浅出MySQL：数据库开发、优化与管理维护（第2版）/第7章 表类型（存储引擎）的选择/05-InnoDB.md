

InnoDB存储引擎提供了具有提交、回滚和崩溃恢复能力的事务安全。但是对比MyISAM的存储引擎，InnoDB写的处理效率差一些，并且会占用更多的磁盘空间以保留数据和索引。

下面将重点介绍存储引擎为InnoDB的表在使用过程中不同于使用其他存储引擎的表的特点。

**1．自动增长列**

InnoDB 表的自动增长列可以手工插入，但是插入的值如果是空或者 0，则实际插入的将是自动增长后的值。下面定义新表autoincre_demo，其中列i使用自动增长列，对该表插入记录，然后查看自动增长列的处理情况，可以发现插入0或者空时，实际插入的都将是自动增长后的值：

mysql> create table autoincre_demo

-> (i smallint not null auto_increment,

-> name varchar(10),primary key(i)

-> )engine=innodb;

Query OK, 0 rows affected (0.13 sec)

mysql> insert into autoincre_demo values(1,'1'),(0,'2'),(null,'3');

Query OK, 3 rows affected (0.04 sec)

Records: 3 Duplicates: 0 Warnings: 0

mysql> select * from autoincre_demo;

+---+------+

| i | name |

+---+------+

| 1 | 1 |

| 2 | 2 |

| 3 | 3 |

+---+------+

3 rows in set (0.00 sec)

可以通过“ALTER TABLE *** AUTO_INCREMENT = n;”语句强制设置自动增长列的初始值，默认从1开始，但是该强制的默认值是保留在内存中的，如果该值在使用之前数据库重新启动，那么这个强制的默认值就会丢失，就需要在数据库启动以后重新设置。

可以使用LAST_INSERT_ID()查询当前线程最后插入记录使用的值。如果一次插入了多条记录，那么返回的是第一条记录使用的自动增长值。下面的例子演示了使用LAST_ INSERT_ID()的情况：

mysql> insert into autoincre_demo values(4,'4');

Query OK, 1 row affected (0.04 sec)

mysql> select LAST_INSERT_ID();

+------------------+

| LAST_INSERT_ID() |

+------------------+

| 2 |

+------------------+

1 row in set (0.00 sec)

mysql> insert into autoincre_demo(name) values('5'),('6'),('7');

Query OK, 3 rows affected (0.05 sec)

Records: 3 Duplicates: 0 Warnings: 0

mysql> select LAST_INSERT_ID();

+------------------+

| LAST_INSERT_ID() |

+------------------+

| 5|

+------------------+

1 row in set (0.00 sec)

对于InnoDB表，自动增长列必须是索引。如果是组合索引，也必须是组合索引的第一列，但是对于 MyISAM 表，自动增长列可以是组合索引的其他列，这样插入记录后，自动增长列是按照组合索引的前面几列进行排序后递增的。例如，创建一个新的 MyISAM 类型的表autoincre_demo，自动增长列d1作为组合索引的第二列，对该表插入一些记录后，可以发现自动增长列是按照组合索引的第一列d2进行排序后递增的：

mysql> create table autoincre_demo

-> (d1 smallint not null auto_increment,

-> d2 smallint not null,

-> name varchar(10),

-> index(d2,d1)

-> )engine=myisam;

Query OK, 0 rows affected (0.03 sec)

mysql> insert into autoincre_demo(d2,name) values(2,'2'),(3,'3'),(4, '4'), (2,'2'), (3,'3'), (4,'4');

Query OK, 6 rows affected (0.00 sec)

Records: 6 Duplicates: 0 Warnings: 0

mysql> select * from autoincre_demo;

+----+----+------+

| d1 | d2 | name |

+----+----+------+

| 1 | 2 | 2|

| 1 | 3 | 3|

| 1 | 4 | 4|

| 2 | 2 | 2|

| 2 | 3 | 3|

| 2 | 4 | 4|

+----+----+------+

6 rows in set (0.00 sec)

**2．外键约束**

MySQL支持外键的存储引擎只有InnoDB，在创建外键的时候，要求父表必须有对应的索引，子表在创建外键的时候也会自动创建对应的索引。

下面是样例数据库中的两个表，country表是父表，country_id为主键索引，city表是子表， country_id字段为外键，对应于country表的主键country_id。

CREATE TABLE country (

country_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,

country VARCHAR(50) NOT NULL,

last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_ TIMESTAMP,

PRIMARY KEY (country_id)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE city (

city_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,

city VARCHAR(50) NOT NULL,

country_id SMALLINT UNSIGNED NOT NULL,

last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

PRIMARY KEY (city_id),

KEY idx_fk_country_id (country_id),

CONSTRAINT 'fk_city_country' FOREIGN KEY (country_id) REFERENCES country (country_id)ON DELETE RESTRICT ON UPDATE CASCADE

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

在创建索引时，可以指定在删除、更新父表时，对子表进行的相应操作，包括RESTRICT、CASCADE、SET NULL和NO ACTION。其中RESTRICT和NO ACTION相同，是指限制在子表有关联记录的情况下父表不能更新；CASCADE表示父表在更新或者删除时，更新或者删除子表对应记录；SET NULL 则表示父表在更新或者删除的时候，子表的对应字段被 SET NULL。选择后两种方式的时候要谨慎，可能会因为错误的操作导致数据的丢失。

例如，对上面创建的两个表，子表的外键指定是 ON DELETE RESTRICT ON UPDATE CASCADE方式的，那么在主表删除记录的时候，如果子表有对应记录，则不允许删除，主表在更新记录的时候，如果子表有对应记录，则子表对应更新：

mysql> select * from country where country_id = 1;

+------------+-------------+---------------------+

| country_id | country | last_update |

+------------+-------------+---------------------+

| 1 | Afghanistan | 2006-02-15 04:44:00 |

+------------+-------------+---------------------+

1 row in set (0.00 sec)

mysql> select * from city where country_id = 1;

+---------+-------+------------+---------------------+

| city_id | city | country_id | last_update |

+---------+-------+------------+---------------------+

| 251 | Kabul | 1 | 2006-02-15 04:45:25 |

+---------+-------+------------+---------------------+

1 row in set (0.00 sec)

mysql> delete from country where country_id=1;

ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails ('sakila/city', CONSTRAINT 'fk_city_country' FOREIGN KEY ('country_id') REFERENCES 'country' ('country_id') ON UPDATE CASCADE)

mysql> update country set country_id = 10000 where country_id = 1;

Query OK, 1 row affected (0.04 sec)

Rows matched: 1 Changed: 1 Warnings: 0

mysql> select * from country where country = 'Afghanistan';

+------------+-------------+---------------------+

| country_id | country | last_update |

+------------+-------------+---------------------+

| 10000 | Afghanistan | 2007-07-17 09:45:23 |

+------------+-------------+---------------------+

1 row in set (0.00 sec)

mysql> select * from city where city_id = 251;

+---------+-------+------------+---------------------+

| city_id | city | country_id | last_update |

+---------+-------+------------+---------------------+

| 251 | Kabul | 10000 | 2006-02-15 04:45:25 |

+---------+-------+------------+---------------------+

1 row in set (0.00 sec)

当某个表被其他表创建了外键参照，那么该表的对应索引或者主键禁止被删除。

在导入多个表的数据时，如果需要忽略表之前的导入顺序，可以暂时关闭外键的检查；同样，在执行LOAD DATA和ALTER TABLE操作的时候，可以通过暂时关闭外键约束来加快处理的速度，关闭的命令是“SET FOREIGN_KEY_CHECKS = 0;”，执行完成之后，通过执行“SET FOREIGN_KEY_CHECKS = 1;”语句改回原状态。

对于 InnoDB类型的表，外键的信息通过使用 show create table或者 show table status命令都可以显示。

mysql> show table status like 'city' \G

*************************** 1. row ***************************

Name: city

Engine: InnoDB

Version: 10

Row_format: Compact

Rows: 427

Avg_row_length: 115

Data_length: 49152

Max_data_length: 0

Index_length: 16384

Data_free: 0

Auto_increment: 601

Create_time: 2007-07-17 09:45:33

Update_time: NULL

Check_time: NULL

Collation: utf8_general_ci

Checksum: NULL

Create_options:

Comment: InnoDB free: 0 kB; ('country_id') REFER 'sakila/country'' ('country_id')ON UPDATE

1 row in set (0.00 sec)

**3．存储方式**

InnoDB存储表和索引有以下两种方式。

使用共享表空间存储，这种方式创建的表的表结构保存在.frm文件中，数据和索引保存在innodb_data_home_dir 和innodb_data_file_path定义的表空间中，可以是多个文件。

使用多表空间存储，这种方式创建的表的表结构仍然保存在.frm文件中，但是每个表的数据和索引单独保存在.ibd 中。如果是个分区表，则每个分区对应单独的.ibd 文件，文件名是“表名+分区名”，可以在创建分区的时候指定每个分区的数据文件的位置，以此来将表的IO均匀分布在多个磁盘上。

要使用多表空间的存储方式，需要设置参数innodb_file_per_table，并且重新启动服务后才可以生效，对于新建的表按照多表空间的方式创建，已有的表仍然使用共享表空间存储。如果将已有的多表空间方式修改回共享表空间的方式，则新建表会在共享表空间中创建，但已有的多表空间的表仍然保存原来的访问方式。所以多表空间的参数生效后，只对新建的表生效。

多表空间的数据文件没有大小限制，不需要设置初始大小，也不需要设置文件的最大限制、扩展大小等参数。

对于使用多表空间特性的表，可以比较方便地进行单表备份和恢复操作，但是直接复制.ibd文件是不行的，因为没有共享表空间的数据字典信息，直接复制的.ibd文件和.frm文件恢复时是不能被正确识别的，但可以通过以下命令：

ALTER TABLE tbl_name DISCARD TABLESPACE;

ALTER TABLE tbl_name IMPORT TABLESPACE;

将备份恢复到数据库中，但是这样的单表备份，只能恢复到表原来所在的数据库中，而不能恢复到其他的数据库中。如果要将单表恢复到目标数据库，则需要通过mysqldump和mysqlimport来实现。

**注意：**即便在多表空间的存储方式下，共享表空间仍然是必须的，InnoDB把内部数据词典和在线重做日志放在这个文件中。



