

MEMORY存储引擎的表可以选择使用BTREE索引或者HASH索引，两种不同类型的索引各有其不同的适用范围。HASH索引有一些重要的特征需要在使用的时候特别注意，如下所示。

只用于使用=或<=>操作符的等式比较。

优化器不能使用HASH索引来加速ORDER BY操作。

MySQL 不能确定在两个值之间大约有多少行。如果将一个 MyISAM 表改为 HASH索引的MEMORY表，会影响一些查询的执行效率。

只能使用整个关键字来搜索一行。

而对于BTREE索引，当使用>、<、>=、<=、BETWEEN、!=或者<>，或者LIKE 'pattern' （其中'pattern'不以通配符开始）操作符时，都可以使用相关列上的索引。

下列范围查询适用于BTREE索引和HASH索引：

SELECT * FROM t1 WHERE key_col = 1 OR key_col IN (15,18,20);

下列范围查询只适用于BTREE索引：

SELECT * FROM t1 WHERE key_col > 1 AND key_col < 10;

SELECT * FROM t1 WHERE key_col LIKE 'ab%' OR key_col BETWEEN 'lisa' AND 'simon';

例如，创建一个和city表完全相同的MEMORY存储引擎的表city_memory：

mysql> CREATE TABLE city_memory (

-> city_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,

-> city VARCHAR(50) NOT NULL,

-> country_id SMALLINT UNSIGNED NOT NULL,

-> last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_ TIMESTAMP,

-> PRIMARY KEY (city_id),

-> KEY idx_fk_country_id (country_id)

-> )ENGINE=Memory DEFAULT CHARSET=utf8;

Query OK, 0 rows affected (0.03 sec)

mysql> insert into city_memory select * from city;

Query OK, 600 rows affected (0.00 sec)

Records: 600 Duplicates: 0 Warnings: 0

当对索引字段进行范围查询的时候，只有BTREE索引可以通过索引访问：

mysql> explain SELECT * FROM city WHERE country_id > 1 and country_id < 10 \G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: city

type: range

possible_keys: idx_fk_country_id

key: idx_fk_country_id

key_len: 2

ref: NULL

rows: 24

Extra: Using where

1 row in set (0.00 sec)

而HASH索引实际上是全表扫描的：

mysql> explain SELECT * FROM city_memory WHERE country_id > 1 and country_id < 10 \G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: city_memory

type: ALL

possible_keys: idx_fk_country_id

key: NULL

key_len: NULL

ref: NULL

rows: 600

Extra: Using where

1 row in set (0.00 sec)

了解了 BTREE 索引和 HASH 索引不同后，当使用 MEMORY 表时，如果是默认创建的HASH 索引，就要注意 SQL 语句的编写，确保可以使用上索引，如果一定要使用范围查询，那么在创建索引时，就应该选择创建成BTREE索引。



