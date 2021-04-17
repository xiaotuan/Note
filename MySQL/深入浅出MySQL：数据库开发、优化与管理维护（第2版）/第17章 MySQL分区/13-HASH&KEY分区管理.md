

在改变分区设置方面，HASH分区和KEY分区的表非常类似，所以这两种分区的管理合并在一起讨论。

不能以RANGE或者LIST分区表中删除分区的相同方式，来从HASH或者KEY分区的表中删除分区，而可以通过ALTER TABLE COALESCE PARTITION语句来合并HASH分区或者KEY分区。例如，emp表按照store_id分成了4个分区：

mysql> CREATE TABLE emp (

->　　id INT NOT NULL,

->　　ename VARCHAR(30),

->　　hired DATE NOT NULL DEFAULT '1970-01-01',

->　　separated DATE NOT NULL DEFAULT '9999-12-31',

->　　job VARCHAR(30) NOT NULL,

->　　store_id INT NOT NULL

-> )

-> PARTITION BY HASH (store_id) PARTITIONS 4;

Query OK, 0 rows affected (0.05 sec)

要减少HASH分区的数量，从 4个分区变为 2个分区，可以执行下面的ALTER TABLE命令：

mysql>alter table emp coalesce partition 2;

Query OK, 0 rows affected (0.03 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql>show create table emp\G

*************************** 1. row ***************************

Table: emp

Create Table: CREATE TABLE `emp` (

`id` int(11) NOT NULL,

`ename` varchar(30) DEFAULT NULL,

`hired` date NOT NULL DEFAULT '1970-01-01',

`separated` date NOT NULL DEFAULT '9999-12-31',

`job` varchar(30) NOT NULL,

`store_id` int(11) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY HASH (store_id)

PARTITIONS 2 */

1 row in set (0.00 sec)

COALESCE不能用来增加分区的数量，否则会出现以下错误：

mysql>alter table emp coalesce partition 8;

ERROR 1508 (HY000): Cannot remove all partitions, use DROP TABLE instead

要增加分区，可以通过ALTER TABLE ADD PARTITION语句来实现，例如，当前 emp表有2个HASH分区，现在增加8个分区，最终emp表一共有10个HASH分区：

mysql>alter table emp add partition partitions 8;

Query OK, 0 rows affected (0.05 sec)

Records: 0 Duplicates: 0 Warnings: 0

root@localhost:test 22:34>show create table emp\G

*************************** 1. row ***************************

Table: emp

Create Table: CREATE TABLE `emp` (

`id` int(11) NOT NULL,

`ename` varchar(30) DEFAULT NULL,

`hired` date NOT NULL DEFAULT '1970-01-01',

`separated` date NOT NULL DEFAULT '9999-12-31',

`job` varchar(30) NOT NULL,

`store_id` int(11) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1

/*!50100 PARTITION BY HASH (store_id)

PARTITIONS 10 */

1 row in set (0.01 sec)

**注意：**通过ALTER TABLE ADD PARTITION PARTITIONS n语句新增HASH分区或者KEY分区时，其实是对原表新增n个分区，而不是增加到n个分区。



