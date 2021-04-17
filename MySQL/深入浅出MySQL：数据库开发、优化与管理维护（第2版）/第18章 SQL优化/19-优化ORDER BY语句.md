id: 1



优化ORDER BY语句之前，首先来了解一下MySQL中的排序方式。先看 customer表上的索引情况：

mysql> show index from customer\G

*************************** 1. row ***************************

Table: customer

Non_unique: 0

Key_name: PRIMARY

Seq_in_index: 1

Column_name: customer_id

Collation: A

Cardinality: 541

Sub_part: NULL

Packed: NULL

Null:

Index_type: BTREE

Comment:

*************************** 2. row ***************************

Table: customer

Non_unique: 1

Key_name: idx_fk_store_id

Seq_in_index: 1

Column_name: store_id

Collation: A

Cardinality: 3

Sub_part: NULL

Packed: NULL

Null:

Index_type: BTREE

Comment:

*************************** 3. row ***************************

Table: customer

Non_unique: 1

Key_name: idx_fk_address_id

Seq_in_index: 1

Column_name: address_id

Collation: A

Cardinality: 541

Sub_part: NULL

Packed: NULL

Null:

Index_type: BTREE

Comment:

*************************** 4. row ***************************

Table: customer

Non_unique: 1

Key_name: idx_last_name

Seq_in_index: 1

Column_name: last_name

Collation: A

Cardinality: 541

Sub_part: NULL

Packed: NULL

Null:

Index_type: BTREE

Comment:

4 rows in set (1.05 sec)

**1．MySQL中有两种排序方式**

第一种通过有序索引顺序扫描直接返回有序数据，这种方式在使用 explain 分析查询的时候显示为Using Index，不需要额外的排序，操作效率较高，例如：

mysql> explain select customer_id from customer order by store_id\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: customer

type: index

possible_keys: NULL

key: idx_fk_store_id

key_len: 1

ref: NULL

rows: 541

Extra: Using index

1 row in set (0.41 sec)

第二种是通过对返回数据进行排序，也就是通常说的 Filesort 排序，所有不是通过索引直接返回排序结果的排序都叫Filesort排序。Filesort并不代表通过磁盘文件进行排序，而只是说明进行了一个排序操作，至于排序操作是否使用了磁盘文件或临时表等，则取决于MySQL服务器对排序参数的设置和需要排序数据的大小。例如，按照商店store_id排序返回所有客户记录时，出现了对全表扫描的结果的排序：

mysql> explain select * from customer order by store_id\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: customer

type: ALL

possible_keys: NULL

key: NULL

key_len: NULL

ref: NULL

rows: 541

Extra: Using filesort

1 row in set (0.68 sec)

又如，只需要获取商店store_id和顾客email信息时，对表customer的扫描就被对覆盖索引 idx_storeid_email 扫描替代，此时虽然只访问了索引就足够，但是在索引 idx_storeid_email上发生了一次排序操作，所以执行计划中仍然有Using Filesort。

mysql> alter table customer add index idx_storeid_email (store_id, email);

Query OK, 599 rows affected (1.17 sec)

Records: 599 Duplicates: 0 Warnings: 0

mysql> explain select store_id, email, customer_id from customer order by email\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: customer

type: index

possible_keys: NULL

key: idx_storeid_email

key_len: 154

ref: NULL

rows: 590

Extra: Using index; Using filesort

1 row in set (0.10 sec)

Filesort是通过相应的排序算法，将取得的数据在sort_buffer_size系统变量设置的内存排序区中进行排序，如果内存装载不下，它就会将磁盘上的数据进行分块，再对各个数据块进行排序，然后将各个块合并成有序的结果集。sort_buffer_size 设置的排序区是每个线程独占的，所以同一个时刻，MySQL中存在多个 sort buffer排序区。

了解了MySQL排序的方式，优化目标就清晰了：**尽量减少额外的排序，通过索引直接返回有序数据。**WHERE条件和ORDER BY使用相同的索引，并且ORDER BY的顺序和索引顺序相同，并且ORDER BY的字段都是升序或者都是降序。否则肯定需要额外的排序操作，这样就会出现Filesort。

例如，查询商店编号store_id为1，按照email逆序排序的记录主键customer_id时，优化器使用扫描索引idx_storeid_email直接返回排序完毕的记录：

mysql> explain select store_id, email, customer_id from customer where store_id = 1 order by email desc \G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: customer

type: ref

possible_keys: idx_fk_store_id,idx_storeid_email

key: idx_storeid_email

key_len: 1

ref: const

rows: 295

Extra: Using where; Using index

1 row in set (1.93 sec)

而查询商店编号store_id大于等于1小于等于3，按照email排序的记录主键customer_id的时候，由于优化器评估使用索引idx_storeid_email进行范围扫描代价cost最低，所以最终是对索引扫描的结果，进行了额外的按照ename逆序排序操作：

mysql> explain select store_id, email, customer_id from customer where store_id >= 1 and store_id <= 3 order by email desc \G

*************************** 1. row ***************************

select_type: SIMPLE

table: customer

type: range

possible_keys: idx_fk_store_id,idx_storeid_email

key: idx_storeid_email

key_len: 1

ref: NULL

rows: 295

Extra: Using where; Using index; Using filesort

1 row in set (1.53 sec)

总结，下列SQL可以使用索引：

SELECT * FROM tabname ORDER BY key_part1,key_part2,... ;

SELECT * FROM tabname WHERE key_part1=1 ORDER BY key_part1 DESC, key_part2 DESC;

SELECT * FROM tabname ORDER BY key_part1 DESC, key_part2 DESC;

但是在以下几种情况下则不使用索引：

SELECT * FROM tabname ORDER BY key_part1 DESC, key_part2 ASC；

--order by的字段混合ASC和DESC

SELECT * FROM tabname WHERE key2=constant ORDER BY key1；

--用于查询行的关键字与ORDER BY中所使用的不相同

SELECT * FROM tabname ORDER BY key1, key2；

--对不同的关键字使用ORDER BY：

**2．Filesort的优化**

通过创建合适的索引能够减少Filesort出现，但是在某些情况下，条件限制不能让Filesort消失，那就需要想办法加快Filesort的操作。对于Filesort，MySQL有两种排序算法。

**两次扫描算法**（Two Passes）：首先根据条件取出排序字段和行指针信息，之后在排序区 sort buffer中排序。如果排序区 sort buffer不够，则在临时表Temporary Table中存储排序结果。完成排序后根据行指针回表读取记录。该算法是MySQL 4.1之前采用的算法，需要两次访问数据，第一次获取排序字段和行指针信息，第二次根据行指针获取记录，尤其是第二次读取操作可能导致大量随机I/O操作；优点是排序的时候内存开销较少。

**一次扫描算法**（Single Pass）：一次性取出满足条件的行的所有字段，然后在排序区sort buffer中排序后直接输出结果集。排序的时候内存开销比较大，但是排序效率比两次扫描算法要高。

MySQL通过比较系统变量max_length_for_sort_data的大小和Query语句取出的字段总大小来判断使用哪种排序算法。如果max_length_for_sort_data更大，那么使用第二种优化之后的算法；否则使用第一种算法。

适当加大系统变量 max_length_for_sort_data 的值，能够让 MySQL 选择更优化的 Filesort排序算法。当然，假如max_length_for_sort_data设置过大，会造成CPU利用率过低和磁盘I/O过高，CPU和I/O利用平衡就足够了。

适当加大sort_buffer_size排序区，尽量让排序在内存中完成，而不是通过创建临时表放在文件中进行；当然也不能无限制加大sort_buffer_size排序区，因为sort_buffer_size参数是每个线程独占的，设置过大，会导致服务器SWAP严重，要考虑数据库活动连接数和服务器内存的大小来适当设置排序区。

尽量只使用必要的字段，SELECT具体的字段名称，而不是SELECT *选择所有字段，这样可以减少排序区的使用，提高SQL性能。



