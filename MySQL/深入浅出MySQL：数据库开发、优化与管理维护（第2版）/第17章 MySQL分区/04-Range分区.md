

按照RANGE分区的表是利用取值范围将数据分成分区，区间要连续并且不能互相重叠，使用VALUES LESS THAN操作符进行分区定义。

例如，雇员表 emp中按商店 ID store_id进行RANGE分区：

mysql> CREATE TABLE emp (

->　id INT NOT NULL,

->　ename VARCHAR(30),

->　hired DATE NOT NULL DEFAULT '1970-01-01',

->　separated DATE NOT NULL DEFAULT '9999-12-31',

->　job VARCHAR(30) NOT NULL,

->　store_id INT NOT NULL

-> )

-> PARTITION BY RANGE (store_id) (

->　PARTITION p0 VALUES LESS THAN (10),

->　PARTITION p1 VALUES LESS THAN (20),

->　PARTITION p2 VALUES LESS THAN (30)

-> );

Query OK, 0 rows affected (0.05 sec)

按照这种分区方案，在商店1～9工作的雇员相对应的所有行被保存在分区P0中，商店10～19的雇员保存在P1中，依次类推。注意，每个分区都是按顺序进行定义的，从最低到最高。这是PARTITION BY RANGE语法的要求；类似 JAVA或者C中的“switch case”语句。

这个时候，如果增加了商店ID大于等于30的行，会出现错误，因为没有规则包含了商店ID大于等于30的行，服务器不知道应该把记录保存在哪里。

mysql> insert into emp(id, ename, hired, job, store_id) values ('7934', 'MILLER', '1982-01-23', 'CLERK', 50);

ERROR 1526 (HY000): Table has no partition for value 50

可以在设置分区的时候使用VALUES LESS THAN MAXVALUE子句，该子句提供给所有大于明确指定的最高值的值，MAXVALUE 表示最大的可能的整数值。例如，增加 p3 分区存储所有商店ID大于等于30的行之后再执行插入语句就没有问题了：

mysql> alter table emp add partition (partition p3 VALUES LESS THAN MAXVALUE);

Query OK, 0 rows affected (0.21 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> insert into emp(id, ename, hired, job, store_id) values ('7934', 'MILLER', '1982-01-23', 'CLERK', 50);

Query OK, 1 row affected (0.04 sec)

MySQL支持在VALUES LESS THAN子句中使用表达式，比如，以日期作为RANGE分区的分区列：

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

->　PARTITION p2 VALUES LESS THAN (2005)

-> );

Query OK, 0 rows affected (0.08 sec)

**注意：**在 RANGE 分区中，分区键如果是 NULL 值会被当作一个最小值来处理，在后续的“17.2.7 MySQL分区处理NULL值的方式”小节中有详细的说明。

MySQL 5.1支持整数列分区，要想在日期或者字符串列上进行分区，就得使用函数进行转换。但要是查询如果不用函数转换，那么就无法利用RANGE分区特性来提高查询性能。

MySQL 5.5改进了RANGE分区功能，提供了RANGE COLUMNS分区支持非整数分区，这样创建日期分区就不需要通过函数进行转换了，例如：

mysql> CREATE TABLE emp_date(

->　id INT NOT NULL,

->　ename VARCHAR(30),

->　hired DATE NOT NULL DEFAULT '1970-01-01',

->　separated DATE NOT NULL DEFAULT '9999-12-31',

->　job VARCHAR(30) NOT NULL,

->　store_id INT NOT NULL

-> )

-> PARTITION BY RANGE COLUMNS (separated) (

->　PARTITION p0 VALUES LESS THAN ('1996-01-01'),

->　PARTITION p1 VALUES LESS THAN ('2001-01-01'),

->　PARTITION p2 VALUES LESS THAN ('2006-01-01')

-> );

Query OK, 0 rows affected (0.07 sec)

**注意：**MySQL 5.1分区日期处理上支持的函数只有两个YEAR()和TO_DAYS()。MySQL 5.5分区日期处理上增加了支持函数TO_SECONDS()，把日期转换成秒，从而能够实现比按天分区更细化的分区。

RANGE分区功能特别适用于以下两种情况。

当需要删除过期的数据时，只需要简单的ALTER TABLE emp DROP PARTITION p0来删除p0分区中的数据。对于具有上百万条记录的表来说，删除分区要比运行一个DELETE语句有效得多。

经常运行包含分区键的查询，MySQL可以很快地确定只有某一个或者某些分区需要扫描，因为其他分区不可能包含有符合该WHERE子句的任何记录。例如，检索商店ID大于等于25的记录数，MySQL只需要扫描p2分区即可。

mysql> explain partitions select count(1) from emp where store_id >= 25\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: emp

partitions: p2

type: ALL

possible_keys: NULL

key: NULL

key_len: NULL

ref: NULL

rows: 5

Extra: Using where

1 row in set (0.00 sec)



