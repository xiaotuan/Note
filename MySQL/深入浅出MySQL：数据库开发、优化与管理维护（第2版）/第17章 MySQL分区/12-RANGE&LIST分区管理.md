

在添加、删除、重新定义分区的处理上，RANGE分区和LIST分区非常相似，所以合并一起来说。

从一个 RANGE或者 LIST分区的表中删除一个分区，可以使用 ALTER TABLE DROP PARTITION语句来实现，以之前创建的按照表达式 YEAR(seperated) 的值进行RANGE分区的 emp_date表为例，执行如下语句创建 emp_date表：

mysql> CREATE TABLE emp_date (

->　id INT NOT NULL,

->　ename VARCHAR(30),

->　hired DATE NOT NULL DEFAULT '1970-01-01',

->　separated DATE NOT NULL DEFAULT '9999-12-31',

->　job VARCHAR(30) NOT NULL,

->　store_id INT NOT NULL

-> )

-> PARTITION BY RANGE (YEAR(separated)) (

->　PARTITION p0 VALUES LESS THAN (1995),

->　PARTITION p1 VALUES LESS THAN (2000),

->　PARTITION p2 VALUES LESS THAN (2005),

->　PARTITION p3 VALUES LESS THAN (2015)

-> );

Query OK, 0 rows affected (0.08 sec)

写入测试数据：

mysql>insert into emp_date(id, ename, hired, separated, job, store_id) values -> (7499, 'ALLEN', '1981-02-20', '2003-08-03', 'SALESMAN', 30 ),

-> (7521, 'WARD', '1981-02-22', '1993-09-01', 'SALESMAN', 30),

-> (7566, 'JONES', '1981-04-02', '2000-08-01', 'MANAGER', 20),

-> (7654, 'MARTIN','1981-09-28', '2012-12-31', 'SALESMAN', 30),

-> (7698, 'BLAKE', '1981-05-01', '1998-09-08', 'MANAGER', 30),

-> (7782, 'CLARK', '1981-06-09', '2007-08-01', 'MANAGER', 10),

-> (7788, 'SCOTT', '1987-04-19', '2012-05-01', 'ANALYST', 20),

-> (7839, 'KING', '1981-11-17', '2011-03-09', 'PRESIDENT', 10),

-> (7844, 'TURNER','1981-09-08', '2010-12-31', 'SALESMAN', 30),

-> (7876, 'ADAMS', '1987-05-23', '2000-01-01', 'CLERK', 20),

-> (7900, 'JAMES', '1981-12-03', '2004-09-02', 'CLERK', 30),

-> (7902, 'FORD', '1981-12-03', '2010-12-31', 'ANALYST', 20),

-> (7934, 'MILLER','1982-01-23', '2011-12-31', 'CLERK', 10);

Query OK, 13 rows affected (0.01 sec)

Records: 13 Duplicates: 0 Warnings: 0

通过下面的查询语句查看哪些记录在分区 p2中（LESS THAN 2005）：

mysql>select * from emp_date where separated between '2000-01-01' and '2004-12-31';

+------+-------+------------+------------+----------+----------+

| id | ename | hired | separated | job | store_id |

+------+-------+------------+------------+----------+----------+

| 7499 | ALLEN | 1981-02-20 | 2003-08-03 | SALESMAN | 30 |

| 7566 | JONES | 1981-04-02 | 2000-08-01 | MANAGER | 20 |

| 7876 | ADAMS | 1987-05-23 | 2000-01-01 | CLERK | 20 |

| 7900 | JAMES | 1981-12-03 | 2004-09-02 | CLERK | 30 |

+------+-------+------------+------------+----------+----------+

4 rows in set (0.00 sec)

执行下面的语句删除p2分区：

mysql>alter table emp_date drop partition p2;

Query OK, 0 rows affected (0.01 sec)

Records: 0 Duplicates: 0 Warnings: 0

**注意：**删除分区的命令执行之后，并不显示实际从表中删除的行数，并不是真的没有记录被删除。

从表结构定义上，可以观察到p2分区确实被删除了：

mysql>show create table emp_date\G

*************************** 1. row ***************************

Table: emp_date

Create Table: CREATE TABLE `emp_date` (

`id` int(11) NOT NULL,

`ename` varchar(30) DEFAULT NULL,

`hired` date NOT NULL DEFAULT '1970-01-01',

`separated` date NOT NULL DEFAULT '9999-12-31',

`job` varchar(30) NOT NULL,

`store_id` int(11) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY RANGE (YEAR(separated))

(PARTITION p0 VALUES LESS THAN (1995) ENGINE = InnoDB,

PARTITION p1 VALUES LESS THAN (2000) ENGINE = InnoDB,

PARTITION p3 VALUES LESS THAN (2015) ENGINE = InnoDB) */

1 row in set (0.00 sec)

删除了p2分区，那么也同时删除了该分区中所有数据，重新执行前面的查询来确认下：

mysql>select * from emp_date where separated between '2000-01-01' and '2004-12-31';

Empty set (0.00 sec)

同时检查emp_date表的记录数，确认受影响的仅是原来在p2分区中的记录：

mysql>select count(1) from emp_date;

+-----------+

| count(11) |

+-----------+

| 9 |

+-----------+

1 row in set (0.00 sec)

再次写入 separated日期在 '2000-01-01'和'2004-12-31'之间的新记录到 emp_date表时，这些行会被保存在 p3 分区中，确认一下，首先检查 emp_date 表的记录分布，p3 分区中仅有 7条记录：

mysql>SELECT

->　partition_name part,

->　partition_expression expr,

->　partition_description descr,

->　table_rows

-> FROM

->　INFORMATION_SCHEMA.partitions

-> WHERE

->　TABLE_SCHEMA = schema()

->　AND TABLE_NAME='emp_date';

+------+-----------------+----------+------------+

| part | expr | descr | table_rows |

+------+-----------------+----------+------------+

| p0 | YEAR(separated) | 1995 | 0 |

| p1 | YEAR(separated) | 2000 | 0 |

| p3 | YEAR(separated) | 2015 | 7 |

+------+-----------------+----------+------------+

3 rows in set (0.00 sec)

在emp_date表中写入一条separated日期在'2000-01-01'和'2004-12-31'之间的新记录：

mysql>insert into emp_date(id, ename, hired, separated, job, store_id) values

-> (7566, 'JONES', '1981-04-02', '2000-08-01', 'MANAGER', 20);

Query OK, 1 row affected (0.00 sec)

再次检查emp_date表的记录分布，发现p3分区的记录数增加为8条，确认新写入的记录写入p3分区：

mysql>SELECT

->　partition_name part,

->　partition_expression expr,

->　partition_description descr,

->　table_rows

-> FROM

->　INFORMATION_SCHEMA.partitions

-> WHERE

->　TABLE_SCHEMA = schema()

->　AND TABLE_NAME='emp_date';

+------+-----------------+----------+------------+

| part | expr | descr | table_rows |

+------+-----------------+----------+------------+

| p0 | YEAR(separated) | 1995 | 0 |

| p1 | YEAR(separated) | 2000 | 0 |

| p3 | YEAR(separated) | 2015 | 8 |

+------+-----------------+----------+------------+

3 rows in set (0.00 sec)

删除LIST分区和删除RANGE分区使用的语句完全相同，只不过删除LIST分区之后，由于在 LIST 分区的定义中不再包含已经被删除了的分区的值列表，所以后续无法写入包含有已经删除了的分区的值列表的数据。

为一个 RANGE 或者 LIST 分区的表增加一个分区，可以使用 ALTER TABLE ADD PARTITION语句来实现。对于RANGE分区来说，只能通过ADD PARTITION方式添加新的分区到分区列表的最大一端，例如，给 emp_date 表增加 p4 分区，存放 separated 日期在'2015-01-01'和'2029-12-31'之间的记录：

mysql>alter table emp_date add partition (partition p4 values less than (2030));

Query OK, 0 rows affected (0.01 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql>show create table emp_date\G

*************************** 1. row ***************************

Table: emp_date

Create Table: CREATE TABLE `emp_date` (

`id` int(11) NOT NULL,

`ename` varchar(30) DEFAULT NULL,

`hired` date NOT NULL DEFAULT '1970-01-01',

`separated` date NOT NULL DEFAULT '9999-12-31',

`job` varchar(30) NOT NULL,

`store_id` int(11) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY RANGE (YEAR(separated))

(PARTITION p0 VALUES LESS THAN (1995) ENGINE = InnoDB,

PARTITION p1 VALUES LESS THAN (2000) ENGINE = InnoDB,

PARTITION p3 VALUES LESS THAN (2015) ENGINE = InnoDB,

PARTITION p4 VALUES LESS THAN (2030) ENGINE = InnoDB) */

1 row in set (0.01 sec)

只能从RANGE分区列表最大端增加分区的话，否则会出现如下错误：

mysql>alter table emp_date add partition (partition p5 values less than (2025));

ERROR 1493 (HY000): VALUES LESS THAN value must be strictly increasing for each partition

给LIST分区增加新分区的方式也类似，以之前创建的expenses表为例，当前的expenses表结构如下：

mysql>CREATE TABLE expenses (

->　　expense_date DATE NOT NULL,

->　　category INT,

->　　amount DECIMAL (10,3)

->　)PARTITION BY LIST(category) (

->　　PARTITION p0 VALUES IN (3, 5),

->　　PARTITION p1 VALUES IN (1, 10),

->　　PARTITION p2 VALUES IN (4, 9),

->　　PARTITION p3 VALUES IN (2),

->　　PARTITION p4 VALUES IN (6)

-> );

Query OK, 0 rows affected (0.04 sec)

为expenses表新增p5分区存储category分类为7和8的记录：

mysql>alter table expenses add partition (partition p5 values in (7,8));

Query OK, 0 rows affected (0.01 sec)

Records: 0 Duplicates: 0 Warnings: 0

增加 LIST 分区时，不能添加一个包含现有分区值列表中的任意值的分区，也就是说对一个固定的分区键值，必须指定并且只能指定一个唯一的分区，否则会出现错误：

mysql>alter table expenses add partition (partition p6 values in (6,11));

ERROR 1495 (HY000): Multiple definition of same constant in list partitioning

MySQL 也提供了在不丢失数据的情况下，通过重新定义分区的语句 ALTER TABLE REORGANIZE PARTITION INTO重定义分区。仍以RANGE分区的 emp_date表为例，当前emp_date的表结构如下：

mysql>show create table emp_date\G

*************************** 1. row ***************************

Table: emp_date

Create Table: CREATE TABLE `emp_date` (

`id` int(11) NOT NULL,

`ename` varchar(30) DEFAULT NULL,

`hired` date NOT NULL DEFAULT '1970-01-01',

`separated` date NOT NULL DEFAULT '9999-12-31',

`job` varchar(30) NOT NULL,

`store_id` int(11) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY RANGE (YEAR(separated))

(PARTITION p0 VALUES LESS THAN (1995) ENGINE = InnoDB,

PARTITION p1 VALUES LESS THAN (2000) ENGINE = InnoDB,

PARTITION p3 VALUES LESS THAN (2015) ENGINE = InnoDB,

PARTITION p4 VALUES LESS THAN (2030) ENGINE = InnoDB) */

1 row in set (0.00 sec)

计划拆分p3分区（2000～2015）为两个分区p2（2000～2005）和p3（2005～2015）：

mysql>alter table emp_date reorganize partition p3 into (

->　partition p2 values less than (2005),

->　partition p3 values less than (2015)

-> );

Query OK, 8 rows affected (0.03 sec)

Records: 8 Duplicates: 0 Warnings: 0

确认拆分之后emp_date表的表结构：

mysql>show create table emp_date\G

*************************** 1. row ***************************

Table: emp_date

Create Table: CREATE TABLE `emp_date` (

`id` int(11) NOT NULL,

`ename` varchar(30) DEFAULT NULL,

`hired` date NOT NULL DEFAULT '1970-01-01',

`separated` date NOT NULL DEFAULT '9999-12-31',

`job` varchar(30) NOT NULL,

`store_id` int(11) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY RANGE (YEAR(separated))

(PARTITION p0 VALUES LESS THAN (1995) ENGINE = InnoDB,

PARTITION p1 VALUES LESS THAN (2000) ENGINE = InnoDB,

PARTITION p2 VALUES LESS THAN (2005) ENGINE = InnoDB,

PARTITION p3 VALUES LESS THAN (2015) ENGINE = InnoDB,

PARTITION p4 VALUES LESS THAN (2030) ENGINE = InnoDB) */

1 row in set (0.00 sec)

重新定义分区可以用来拆分一个RANGE分区为多个RANGE分区，也可以用来合并多个相邻RANGE分区为一个RANGE分区或者多个RANGE分区：

mysql>alter table emp_date reorganize partition p1,p2,p3 into (

->　partition p1 values less than (2015)

-> );

Query OK, 9 rows affected (0.05 sec)

Records: 9 Duplicates: 0 Warnings: 0

mysql>show create table emp_date\G

*************************** 1. row ***************************

Table: emp_date

Create Table: CREATE TABLE `emp_date` (

`id` int(11) NOT NULL,

`ename` varchar(30) DEFAULT NULL,

`hired` date NOT NULL DEFAULT '1970-01-01',

`separated` date NOT NULL DEFAULT '9999-12-31',

`job` varchar(30) NOT NULL,

`store_id` int(11) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY RANGE (YEAR(separated))

(PARTITION p0 VALUES LESS THAN (1995) ENGINE = InnoDB,

PARTITION p1 VALUES LESS THAN (2015) ENGINE = InnoDB,

PARTITION p4 VALUES LESS THAN (2030) ENGINE = InnoDB) */

1 row in set (0.00 sec)

**注意：**重新定义RANGE分区时，只能够重新定义相邻的分区，不能跳过某个RANGE分区进行重新定义，同时重新定义的分区区间必须和原分区区间覆盖相同的区间；也不能使用重新定义分区来改变表分区的类型，例如，不能把RANGE分区变为HASH分区，也不能把HASH分区变成RANGE分区。

同样的，对LIST分区，也可以使用ALTER TABLE REORGANIZE PARTITION INTO语句重定义分区，例如，当前expenses表的分区如下：

mysql>show create table expenses\G

*************************** 1. row ***************************

Table: expenses

Create Table: CREATE TABLE `expenses` (

`expense_date` date NOT NULL,

`category` int(11) DEFAULT NULL,

`amount` decimal(10,3) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY LIST (category)

(PARTITION p0 VALUES IN (3,5) ENGINE = InnoDB,

PARTITION p1 VALUES IN (1,10) ENGINE = InnoDB,

PARTITION p2 VALUES IN (4,9) ENGINE = InnoDB,

PARTITION p3 VALUES IN (2) ENGINE = InnoDB,

PARTITION p4 VALUES IN (6) ENGINE = InnoDB,

PARTITION p5 VALUES IN (7,8) ENGINE = InnoDB) */

1 row in set (0.00 sec)

现在需要调整 p4 分区，使得 p4 分区包含值为 6 和 11 的记录，即 p4 分区的定义为PARTITION p4 VALUES IN (6,11)，之前我们单纯通过ADD PARTITION的方式是不可以的：

mysql>alter table expenses add partition (partition p6 values in (6,11));

ERROR 1495 (HY000): Multiple definition of same constant in list partitioning

可以变通地通过增加分区和重定义分区来实现，首先现增加不重复值列表的 p6 分区，包含值11：

mysql>alter table expenses add partition (partition p6 values in (11));

Query OK, 0 rows affected (0.02 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql>show create table expenses\G;

*************************** 1. row ***************************

Table: expenses

Create Table: CREATE TABLE `expenses` (

`expense_date` date NOT NULL,

`category` int(11) DEFAULT NULL,

`amount` decimal(10,3) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY LIST (category)

(PARTITION p0 VALUES IN (3,5) ENGINE = InnoDB,

PARTITION p1 VALUES IN (1,10) ENGINE = InnoDB,

PARTITION p2 VALUES IN (4,9) ENGINE = InnoDB,

PARTITION p3 VALUES IN (2) ENGINE = InnoDB,

PARTITION p4 VALUES IN (6) ENGINE = InnoDB,

PARTITION p5 VALUES IN (7,8) ENGINE = InnoDB,

PARTITION p6 VALUES IN (11) ENGINE = InnoDB) */

1 row in set (0.00 sec)

之后通过 REORGANIZE PARTITION方式，重定义 p4、p5、p6这 3个分区，合并 p4和p6两个分区为新的p4分区，包含值6和11：

myql>alter table expenses reorganize partition p4,p5,p6 into (

->　partition p4 values in (6,11),

->　partition p5 values in (7,8)

-> );

Query OK, 0 rows affected (0.05 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql>show create table expenses\G

*************************** 1. row ***************************

Table: expenses

Create Table: CREATE TABLE `expenses` (

`expense_date` date NOT NULL,

`category` int(11) DEFAULT NULL,

`amount` decimal(10,3) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY LIST (category)

(PARTITION p0 VALUES IN (3,5) ENGINE = InnoDB,

PARTITION p1 VALUES IN (1,10) ENGINE = InnoDB,

PARTITION p2 VALUES IN (4,9) ENGINE = InnoDB,

PARTITION p3 VALUES IN (2) ENGINE = InnoDB,

PARTITION p4 VALUES IN (6,11) ENGINE = InnoDB,

PARTITION p5 VALUES IN (7,8) ENGINE = InnoDB) */

1 row in set (0.00 sec)

通过重定义分区之后，p4分区的值包含了6和11。类似的重定义RANGE分区，重新定义LIST分区时，只能够重新定义相邻的分区，不能跳过LIST分区进行重新定义，否则提示以下信息：

mysql>alter table expenses reorganize partition p4,p6 into (partition p4 values in (6,11));

ERROR 1519 (HY000): When reorganizing a set of partitions they must be in consecutive order

**注意：**类似重新定义RANGE分区，重新定义LIST分区时，只能够重新定义相邻的分区，不能跳过LIST分区进行重新定义，同时重新定义的分区区间必须和原分区区间覆盖相同的区间；也不能使用重新定义分区来改变表分区的类型，例如，不能把LIST分区变为RANGE分区，也不能把RANGE分区变成LIST分区。



