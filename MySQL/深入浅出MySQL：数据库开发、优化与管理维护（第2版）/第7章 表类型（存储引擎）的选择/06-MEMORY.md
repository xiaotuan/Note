

MEMORY存储引擎使用存在于内存中的内容来创建表。每个MEMORY表只实际对应一个磁盘文件，格式是.frm。MEMORY类型的表访问非常地快，因为它的数据是放在内存中的，并且默认使用HASH索引，但是一旦服务关闭，表中的数据就会丢失掉。

下面的例子创建了一个MEMORY的表，并从city表获得记录：

mysql> CREATE TABLE tab_memory ENGINE=MEMORY

-> SELECT city_id,city,country_id

-> FROM city GROUP BY city_id;

Query OK, 600 rows affected (0.06 sec)

Records: 600 Duplicates: 0 Warnings: 0

mysql> select count(*) from tab_memory;

+----------+

| count(*) |

+----------+

| 600 |

+----------+

1 row in set (0.00 sec)

mysql> show table status like 'tab_memory' \G

*************************** 1. row ***************************

Name: tab_memory

Engine: MEMORY

Version: 10

Row_format: Fixed

Rows: 600

Avg_row_length: 155

Data_length: 127040

Max_data_length: 16252835

Index_length: 0

Data_free: 0

Auto_increment: NULL

Create_time: NULL

Update_time: NULL

Check_time: NULL

Collation: gbk_chinese_ci

Checksum: NULL

Create_options:

Comment:

1 row in set (0.00 sec)

给MEMORY表创建索引的时候，可以指定使用HASH索引还是BTREE索引：

mysql> create index mem_hash USING HASH on tab_memory (city_id) ;

Query OK, 600 rows affected (0.04 sec)

Records: 600 Duplicates: 0 Warnings: 0

mysql> SHOW INDEX FROM tab_memory \G

*************************** 1. row ***************************

Table: tab_memory

Non_unique: 1

Key_name: mem_hash

Seq_in_index: 1

Column_name: city_id

Collation: NULL

Cardinality: 300

Sub_part: NULL

Packed: NULL

Null:

Index_type: HASH

Comment:

1 row in set (0.01 sec)

mysql> drop index mem_hash on tab_memory;

Query OK, 600 rows affected (0.04 sec)

Records: 600 Duplicates: 0 Warnings: 0

mysql> create index mem_hash USING BTREE on tab_memory (city_id) ;

Query OK, 600 rows affected (0.03 sec)

Records: 600 Duplicates: 0 Warnings: 0

mysql> SHOW INDEX FROM tab_memory \G

*************************** 1. row ***************************

Table: tab_memory

Non_unique: 1

Key_name: mem_hash

Seq_in_index: 1

Column_name: city_id

Collation: A

Cardinality: NULL

Sub_part: NULL

Packed: NULL

Null:

Index_type: BTREE

Comment:

1 row in set (0.00 sec)

在启动MySQL服务的时候使用--init-file选项，把 INSERT INTO ... SELECT或LOAD DATA INFILE这样的语句放入这个文件中，就可以在服务启动时从持久稳固的数据源装载表。

服务器需要足够内存来维持所有在同一时间使用的MEMORY表，当不再需要MEMORY表的内容之时，要释放被MEMORY表使用的内存，应该执行DELETE FROM或TRUNCATE TABLE，或者整个地删除表（使用DROP TABLE操作）。

每个MEMORY表中可以放置的数据量的大小，受到max_heap_table_size系统变量的约束，这个系统变量的初始值是16MB，可以根据需要加大。此外，在定义MEMORY表的时候，可以通过MAX_ROWS子句指定表的最大行数。

MEMORY 类型的存储引擎主要用于那些内容变化不频繁的代码表，或者作为统计操作的中间结果表，便于高效地对中间结果进行分析并得到最终的统计结果。对存储引擎为MEMORY的表进行更新操作要谨慎，因为数据并没有实际写入到磁盘中，所以一定要对下次重新启动服务后如何获得这些修改后的数据有所考虑。



