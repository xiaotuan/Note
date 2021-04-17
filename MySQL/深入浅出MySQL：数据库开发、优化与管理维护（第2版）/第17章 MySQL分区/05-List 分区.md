

LIST分区是建立离散的值列表告诉数据库特定的值属于哪个分区，LIST分区在很多方面类似于RANGE分区，区别在LIST分区是从属于一个枚举列表的值的集合，RANGE分区是从属于一个连续区间值的集合。

LIST分区通过使用PARTITION BY LIST(expr)子句来实现，expr是某列值或一个基于某列值返回一个整数值的表达式，然后通过VALUES IN(value_list)的方式来定义分区，其中value_list是一个逗号分隔的整数列表。与RANGE分区不同，LIST分区不必声明任何特定的顺序，例如：

mysql> CREATE TABLE expenses (

->　expense_date DATE NOT NULL,

->　category INT,

->　amount DECIMAL (10,3)

-> )PARTITION BY LIST(category) (

->　PARTITION p0 VALUES IN (3, 5),

->　PARTITION p1 VALUES IN (1, 10),

->　PARTITION p2 VALUES IN (4, 9),

->　PARTITION p3 VALUES IN (2),

->　PARTITION p4 VALUES IN (6)

-> );

Query OK, 0 rows affected (0.09 sec)

**注意：**在MySQL 5.1中，LIST分区只能匹配整数列表。category只能是 INT类型，所以需要额外的转换表来记录类别编号和类别的名称。

如果试图插入的列值（或者分区表达式的返回值）不包含分区值列表中时，那么 INSERT操作会失败并报错。要重点注意的是，LIST分区不存在类似VALUES LESS THAN MAXVALUE这样包含其他值在内的定义方式。将要匹配的任何值都必须在值列表中找得到。

由于MySQL 5.5中支持非整数分区，所以创建LIST分区就不需要额外的转换表：

mysql> CREATE TABLE expenses (

->　expense_date DATE NOT NULL,

->　category VARCHAR(30),

->　amount DECIMAL (10,3)

-> )PARTITION BY LIST COLUMNS (category) (

->　PARTITION p0 VALUES IN ( 'lodging', 'food'),

->　PARTITION p1 VALUES IN ( 'flights', 'ground transportation'),

->　PARTITION p2 VALUES IN ( 'leisure', 'customer entertainment'),

->　PARTITION p3 VALUES IN ( 'communications'),

->　PARTITION p4 VALUES IN ( 'fees')

-> );

Query OK, 0 rows affected (0.07 sec)



