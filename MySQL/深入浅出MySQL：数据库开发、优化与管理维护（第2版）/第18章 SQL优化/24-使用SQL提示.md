

SQL提示（SQL HINT）是优化数据库的一个重要手段，简单来说就是在SQL语句中加入一些人为的提示来达到优化操作的目的。下面是一个使用SQL提示的例子：

SELECT SQL_BUFFER_RESULTS * FROM...

这个语句将强制MySQL生成一个临时结果集。只要临时结果集生成后，所有表上的锁定均被释放。这能在遇到表锁定问题时或要花很长时间将结果传给客户端时有所帮助，因为可以尽快释放锁资源。

下面是一些在MySQL中常用的SQL提示。

**1．USE INDEX**

在查询语句中表名的后面，添加USE INDEX来提供希望MySQL去参考的索引列表，就可以让MySQL不再考虑其他可用的索引。

mysql> explain select count(*) from rental use index (idx_rental_date)\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: rental

type: index

possible_keys: NULL

key: idx_rental_date

key_len: 13

ref: NULL

rows: 16291

Extra: Using index

1 row in set (0.00 sec)

**2．IGNORE INDEX**

如果用户只是单纯地想让MySQL忽略一个或者多个索引，则可以使用 IGNORE INDEX作为HINT。同样是上面的例子，这次来看一下查询过程忽略索引ind_sales2_id的情况：

mysql> explain select count(*) from rental ignore index (idx_rental_date)\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: rental

type: index

possible_keys: NULL

key: idx_fk_staff_id

key_len: 1

ref: NULL

rows: 16291

Extra: Using index

1 row in set (0.00 sec)

从执行计划可以看出，系统忽略了指定的索引，使用索引idx_fk_staff_id。

**3．FORCE INDEX**

为强制MySQL使用一个特定的索引，可在查询中使用FORCE INDEX作为HINT。例如，当不强制使用索引的时候，因为大部分库存inventory_id的值都是大于1的，因此MySQL会默认进行全表扫描，而不使用索引，如下所示：

mysql> explain select * from rental where inventory_id > 1\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: rental

type: ALL

possible_keys: idx_fk_inventory_id

key: NULL

key_len: NULL

ref: NULL

rows: 16291

Extra: Using where

1 row in set (0.00 sec)

尝试使用 use index的 hint看看：

mysql> explain select * from rental use index (idx_fk_inventory_id) where inventory_id >1\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: rental

type: ALL

possible_keys: idx_fk_inventory_id

key: NULL

key_len: NULL

ref: NULL

rows: 16291

Extra: Using where

1 row in set (0.00 sec)

发现仍然不行，MySQL还是选择走全表扫描。但是，当使用FORCE INDEX进行提示时，即便使用索引的效率不是最高，MySQL还是选择使用了索引，这是MySQL留给用户的一个自行选择执行计划的权力。加入FORCE INDEX提示后再次执行上面的SQL：

mysql> explain select * from rental force index (idx_fk_inventory_id) where inventory_id > 1\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: rental

type: range

possible_keys: idx_fk_inventory_id

key: idx_fk_inventory_id

key_len: 3

ref: NULL

rows: 8145

Extra: Using where

1 row in set (0.01 sec)

果然，执行计划中使用了FORCE INDEX后的索引。



