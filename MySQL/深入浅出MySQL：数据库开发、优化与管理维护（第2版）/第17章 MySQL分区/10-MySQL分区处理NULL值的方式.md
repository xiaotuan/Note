

MySQL 不禁止在分区键值上使用 NULL，分区键可能是一个字段或者一个用户定义的表达式。一般情况下，MySQL的分区把NULL当作零值，或者一个最小值进行处理。

**注意：**RANGE分区中，NULL值会被当作最小值来处理；LIST分区中，NULL值必须出现在枚举列表中，否则不被接受；HASH/KEY分区中，NULL值会被当作零值来处理。

例如，创建tb_range表，按照id进行RANGE分区，在RANGE分区中写入NULL值：

mysql>CREATE TABLE tb_range (

-> id INT,

-> name VARCHAR(5)

-> )

-> PARTITION BY RANGE(id) (

-> PARTITION p0 VALUES LESS THAN (-6),

-> PARTITION p1 VALUES LESS THAN (0),

-> PARTITION p2 VALUES LESS THAN (1),

-> PARTITION p3 VALUES LESS THAN MAXVALUE

-> );

Query OK, 0 rows affected (0.06 sec)

mysql>insert into tb_range values (null, 'NULL');

Query OK, 1 row affected (0.00 sec)

查询INFORMATION_SCHEMA.PARTITIONS表确认写入的NULL值被当作最小值处理， NULL值被分配在分区p0内：

mysql>SELECT

->　partition_name part,

->　partition_expression expr,

->　partition_description descr,

->　table_rows

-> FROM

->　INFORMATION_SCHEMA.partitions

-> WHERE

->　TABLE_SCHEMA = schema()

->　AND TABLE_NAME='tb_range';

+------+------+----------+------------+

| part | expr | descr | table_rows |

+------+------+----------+------------+

| p0 | id | -6 | 1 |

| p1 | id | 0 | 0 |

| p2 | id | 1 | 0 |

| p3 | id | MAXVALUE | 0 |

+------+------+----------+------------+

4 rows in set (0.00 sec)

例如，在LIST分区中写入NULL值，分区定义不包含NULL值的时候，会返回一个错误“ERROR 1526 (HY000): Table has no partition for value NULL”。

mysql>CREATE TABLE tb_list (

-> id INT,

-> name VARCHAR(5)

-> )

-> PARTITION BY LIST(id) (

-> PARTITION p1 VALUES IN (0),

-> PARTITION p2 VALUES IN (1)

-> );

Query OK, 0 rows affected (0.01 sec)

mysql>insert into tb_list values (null, 'NULL');

ERROR 1526 (HY000): Table has no partition for value NULL

在LIST分区中增加NULL的定义之后，就能够成功写入NULL值：

mysql>CREATE TABLE tb_list (

-> id INT,

-> name VARCHAR(5)

-> )

-> PARTITION BY LIST(id) (

-> PARTITION p1 VALUES IN (0, NULL),

-> PARTITION p2 VALUES IN (1)

-> );

Query OK, 0 rows affected (0.01 sec)

root@localhost:test 16:43>insert into tb_list values (NULL, 'NULL');

Query OK, 1 row affected (0.00 sec)

root@localhost:test 16:43>SELECT

->　partition_name part,

->　partition_expression expr,

->　partition_description descr,

->　table_rows

-> FROM

->　INFORMATION_SCHEMA.partitions

-> WHERE

->　TABLE_SCHEMA = schema()

->　AND TABLE_NAME='tb_list';

+------+------+--------+------------+

| part | expr | descr | table_rows |

+------+------+--------+------------+

| p1 | id | NULL,0 |1|

| p2 | id | 1|0|

+------+------+--------+------------+

2 rows in set (0.00 sec)

例如，创建tb_hash表，按照id列HASH分区，在HASH分区中写入NULL值：

mysql>CREATE TABLE tb_hash (

->　id INT,

->　name VARCHAR(5)

-> )

-> PARTITION BY HASH(id)

-> PARTITIONS 2;

Query OK, 0 rows affected (0.04 sec)

mysql>insert into tb_hash values (null, 'NULL');

Query OK, 1 row affected (0.00 sec)

mysql>SELECT

->　partition_name part,

->　partition_expression expr,

->　partition_description descr,

->　table_rows

-> FROM

->　INFORMATION_SCHEMA.partitions

-> WHERE

->　TABLE_SCHEMA = schema()

->　AND TABLE_NAME='tb_hash';

+------+------+-------+------------+

| part | expr | descr | table_rows |

+------+------+-------+------------+

| p0 | id | NULL | 1 |

| p1 | id | NULL |0|

+------+------+-------+------------+

2 rows in set (0.00 sec)

由于针对不同的分区类型，NULL值时而被当作零值处理，时而被当作最小值处理，为了避免在处理 NULL 值时出现误判，更推荐通过设置字段非空和默认值来绕开 MySQL 默认对NULL值的处理。



