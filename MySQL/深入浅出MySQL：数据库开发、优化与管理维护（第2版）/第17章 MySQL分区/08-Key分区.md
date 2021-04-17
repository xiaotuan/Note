

按照Key进行分区非常类似于按照HASH进行分区，只不过HASH分区允许使用用户自定义的表达式，而Key分区不允许使用用户自定义的表达式，需要使用MySQL服务器提供的HASH函数；同时HASH分区只支持整数分区，而Key分区支持使用除BLOB or Text类型外其他类型的列作为分区键。

我们同样可以用PARTITION BY KEY(expr)子句来创建一个Key分区表，expr是零个或者多个字段名名的列表。下面语句创建了一个基于job字段进行Key分区的表，表被分成了4个分区：

mysql> CREATE TABLE emp (

->　　id INT NOT NULL,

->　　ename VARCHAR(30),

->　　hired DATE NOT NULL DEFAULT '1970-01-01',

->　　separated DATE NOT NULL DEFAULT '9999-12-31',

->　　job VARCHAR(30) NOT NULL,

->　　store_id INT NOT NULL

->　)

->　PARTITION BY KEY (job) PARTITIONS 4;

Query OK, 0 rows affected (0.04 sec)

与 HASH 分区不同，创建 Key 分区表的时候，可以不指定分区键，默认会首先选择使用主键作为分区键，例如：

mysql> CREATE TABLE emp (

->　　id INT NOT NULL,

->　　ename VARCHAR(30),

->　　hired DATE NOT NULL DEFAULT '1970-01-01',

->　　separated DATE NOT NULL DEFAULT '9999-12-31',

->　　job VARCHAR(30) NOT NULL,

->　　store_id INT NOT NULL,

->　　PRIMARY KEY (id)

->　)

->　PARTITION BY KEY ( ) PARTITIONS 4;

Query OK, 0 rows affected (0.02 sec)

在没有主键的情况，会选择非空唯一键作为分区键：

mysql> drop table emp;

Query OK, 0 rows affected (0.02 sec)

mysql> CREATE TABLE emp (

->　　id INT NOT NULL,

->　　ename VARCHAR(30),

->　　hired DATE NOT NULL DEFAULT '1970-01-01',

->　　separated DATE NOT NULL DEFAULT '9999-12-31',

->　　job VARCHAR(30) NOT NULL,

->　　store_id INT NOT NULL,

->　　UNIQUE KEY (id)

->　)

->　PARTITION BY KEY ( ) PARTITIONS 4;

Query OK, 0 rows affected (0.01 sec)

**注意：**作为分区键的唯一键必须是非空的，如果不是非空的，依然会报错。

mysql> CREATE TABLE emp (

->　　id INT,

->　　ename VARCHAR(30),

->　　hired DATE NOT NULL DEFAULT '1970-01-01',

->　　separated DATE NOT NULL DEFAULT '9999-12-31',

->　　job VARCHAR(30) NOT NULL,

->　　store_id INT NOT NULL,

->　　UNIQUE KEY (id,ename)

->　)

->　PARTITION BY KEY ( ) PARTITIONS 4;

ERROR 1488 (HY000): Field in list of fields for partition function not found in table

在没有主键、也没有唯一键的情况下，就不能不指定分区键了：

mysql> drop table emp;

Query OK, 0 rows affected (0.01 sec)

mysql> CREATE TABLE emp (

->　　id INT NOT NULL,

->　　ename VARCHAR(30),

->　　hired DATE NOT NULL DEFAULT '1970-01-01',

->　　separated DATE NOT NULL DEFAULT '9999-12-31',

->　　job VARCHAR(30) NOT NULL,

->　　store_id INT NOT NULL

->　)

->　PARTITION BY KEY ( ) PARTITIONS 4;

ERROR 1488 (HY000): Field in list of fields for partition function not found in table

**注意：**在按照Key分区的分区表上，不能够执行“ALTER TABLE DROP PRIMARY KEY;”语句来删除主键，MySQL会返回错误“Field in list of fields for partition function not found in table”。

和HASH分区类似，在KEY分区中使用关键字LINEAR具有同样的作用，也就是LINEAR KEY分区时，分区的编号是通过2的幂算法得到的，而不是通过取模得到的。

KEY分区和HASH分区类似，在处理大量数据记录时，能够有效地分散热点。



