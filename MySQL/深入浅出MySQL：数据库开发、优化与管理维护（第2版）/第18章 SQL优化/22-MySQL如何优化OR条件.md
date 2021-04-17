

对于含有OR的查询子句，如果要利用索引，则OR之间的每个条件列都必须用到索引；如果没有索引，则应该考虑增加索引。

例如，首先使用 show index命令查看表 sales2的索引，可知它有 3个索引，在 id和 year两个字段上分别有1个独立的索引，在company_id和year字段上有1个复合索引。

mysql> show index from sales2\G;

********************************* 1. row *********************************

Table: sales2

Non_unique: 1

Key_name: ind_sales2_id

Seq_in_index: 1

Column_name: id

Collation: A

Cardinality: 1000

Sub_part: NULL

Packed: NULL

Null: YES

Index_type: BTREE

Comment:

********************************* 2. row *********************************

Table: sales2

Non_unique: 1

Key_name: ind_sales2_year

Seq_in_index: 1

Column_name: year

Collation: A

Cardinality: 250

Sub_part: NULL

Packed: NULL

Null: YES

Index_type: BTREE

Comment:

********************************* 3. row *********************************

Table: sales2

Non_unique: 1

Key_name: ind_sales2_companyid_moneys

Seq_in_index: 1

Column_name: company_id

Collation: A

Cardinality: 1000

Sub_part: NULL

Packed: NULL

Null: YES

Index_type: BTREE

Comment:

********************************* 4. row *********************************

Table: sales2

Non_unique: 1

Key_name: ind_sales2_companyid_moneys

Seq_in_index: 2

Column_name: year

Collation: A

Cardinality: 1000

Sub_part: NULL

Packed: NULL

Null: YES

Index_type: BTREE

Comment:

4 rows in set (0.00 sec)

然后在两个独立索引上面做OR操作，具体如下：

mysql> explain select * from sales2 where id = 2 or year = 1998\G;

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: sales2

type: index_merge

possible_keys: ind_sales2_id,ind_sales2_year

key: ind_sales2_id,ind_sales2_year

key_len: 5,2

ref: NULL

rows: 2

Extra: Using union(ind_sales2_id,ind_sales2_year); Using where

1 row in set (0.00 sec)

可以发现查询正确地用到了索引，并且从执行计划的描述中，发现MySQL在处理含有OR字句的查询时，实际是对OR的各个字段分别查询后的结果进行了UNION操作。

但是当在建有复合索引的列company_id和moneys上面做OR操作时，却不能用到索引，具体结果如下：

mysql> explain select * from sales2 where company_id = 3 or moneys = 100\G;

********************************* 1. row *********************************

id: 1

select_type: SIMPLE

table: sales2

type: ALL

possible_keys: ind_sales2_companyid_moneys

key: NULL

key_len: NULL

ref: NULL

rows: 1000

Extra: Using where

1 row in set (0.00 sec)

)



