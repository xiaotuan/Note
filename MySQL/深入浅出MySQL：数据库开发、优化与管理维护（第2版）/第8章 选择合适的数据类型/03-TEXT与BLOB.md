

一般在保存少量字符串的时候，我们会选择CHAR或者VARCHAR；而在保存较大文本时，通常会选择使用TEXT或者BLOB。二者之间的主要差别是BLOB能用来保存二进制数据，比如照片；而TEXT只能保存字符数据，比如一篇文章或者日记。TEXT和BLOB中又分别包括TEXT、MEDIUMTEXT、LONGTEXT和BLOB、MEDIUMBLOB、LONGBLOB三种不同的类型，它们之间的主要区别是存储文本长度不同和存储字节不同，用户应该根据实际情况选择能够满足需求的最小存储类型。本节主要对BLOB和TEXT存在的一些常见问题进行介绍。

（1）BLOB和TEXT值会引起一些性能问题，特别是在执行了大量的删除操作时。

删除操作会在数据表中留下很大的“空洞”，以后填入这些“空洞”的记录在插入的性能上会有影响。为了提高性能，建议定期使用OPTIMIZE TABLE功能对这类表进行碎片整理，避免因为“空洞”导致性能问题。

下面的例子描述了OPTIMIZE TABLE的碎片整理功能。首先创建测试表 t，字段 id和context的类型分别为varchar(100)和text：

mysql> create table t (id varchar(100),context text);

Query OK, 0 rows affected (0.01 sec)

然后往t中插入大量记录，这里使用repeat函数插入大量字符串：

mysql> insert into t values(1,repeat('haha',100));

Query OK, 1 row affected (0.00 sec)

mysql> insert into t values(2,repeat('haha',100));

Query OK, 1 row affected (0.00 sec)

mysql> insert into t values(3,repeat('haha',100));

Query OK, 1 row affected (0.00 sec)

mysql> insert into t select * from t;

…

mysql> insert into t select * from t;

Query OK, 196608 rows affected (4.86 sec)

Records: 196608 Duplicates: 0 Warnings: 0

mysql> exit

Bye

退出到操作系统下，查看表t的物理文件大小：

[bjguan@zzx test]$ du -sh t.*

16K t.frm

155Mt.MYD

8.0Kt.MYI

这里数据文件显示为155MB。从表t中删除id为“1”的数据，这些数据占总数据量的1/3：

[bjguan@localhost test]$ mysql -u root -p1234

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 24 to server version: 5.0.45-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> use test

Database changed

mysql> delete from t where id=1;

Query OK, 131072 rows affected (4.33 sec)

mysql> exit

Bye

再次退出到操作系统下，查看表t的物理文件大小：

[bjguan@zzx test]$ du -sh t.*

16K t.frm

155M t.MYD

8.0K t.MYI

可以发现，表t的数据文件仍然为155MB，并没有因为数据删除而减少。接下来对表进行OPTIMIZE（优化）操作：

[bjguan@localhost test]$ mysql -u root -p1234

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 24 to server version: 5.0.45-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> use test;

Database changed

mysql> OPTIMIZE TABLE t;

+--------+----------+----------+----------+

| Table | Op | Msg_type | Msg_text |

+--------+----------+----------+----------+

| test.t | optimize | status | OK |

+--------+----------+----------+----------+

1 row in set (2.88 sec)

mysql> exit

Bye

再次查看表t的物理文件大小：

[bjguan@localhost test]$ du -sh t.*

16K　t.frm

104M　t.MYD

8.0K　t.MYI

可以发现，表的数据文件大大缩小，“空洞”空间已经被回收。

（2）可以使用合成的（Synthetic）索引来提高大文本字段（BLOB或TEXT）的查询性能。

简单来说，合成索引就是根据大文本字段的内容建立一个散列值，并把这个值存储在单独的数据列中，接下来就可以通过检索散列值找到数据行了。但是，要注意这种技术只能用于精确匹配的查询（散列值对于类似“<”或“>=”等范围搜索操作符是没有用处的）。可以使用MD5()函数生成散列值，也可以使用SHA1()或CRC32()，或者使用自己的应用程序逻辑来计算散列值。请记住数值型散列值可以很高效率地存储。同样，如果散列算法生成的字符串带有尾部空格，就不要把它们存储在CHAR或VARCHAR列中，它们会受到尾部空格去除的影响。合成的散列索引对于那些BLOB或TEXT数据列特别有用。用散列标识符值查找的速度比搜索BLOB列本身的速度快很多。

下面通过实例介绍一下合成索引的使用方法。首先创建测试表t，字段id、context、hash_value字段类型分别为varchar(100)、blob、varchar(40)：

mysql> create table t (id varchar(100),context blob,hash_value varchar(40));

Query OK, 0 rows affected (0.03 sec)

然后往t中插入测试数据，其中hash_value用来存放context列的MD5散列值：

mysql> insert into t values(1,repeat('beijing',2),md5(context));

Query OK, 1 row affected (0.00 sec)

mysql> insert into t values(2,repeat('beijing',2),md5(context));

Query OK, 1 row affected (0.00 sec)

mysql> insert into t values(3,repeat('beijing 2008',2),md5(context));

Query OK, 1 row affected (0.00 sec)

mysql> select * from t;

+------+--------------------------+----------------------------------+

| id | context | hash_value |

+------+--------------------------+----------------------------------+

| 1 | beijingbeijing | 09746eef633dbbccb7997dfd795cff17 |

| 2 | beijingbeijing | 09746eef633dbbccb7997dfd795cff17 |

| 3 | beijing 2008beijing 2008 | 1c0ddb82cca9ed63e1cacbddd3f74082 |

+------+--------------------------+----------------------------------+

3 rows in set (0.00 sec)

如果要查询 context值为“beijing 2008beijing 2008”的记录，则可以通过相应的散列值来查询：

mysql> select * from t where hash_value=md5(repeat('beijing 2008',2));

+------+--------------------------+----------------------------------+

| id | context | hash_value |

+------+--------------------------+----------------------------------+

| 3 | beijing 2008beijing 2008 | 1c0ddb82cca9ed63e1cacbddd3f74082 |

+------+--------------------------+----------------------------------+

1 row in set (0.00 sec)

上面的例子展示了合成索引的用法，由于这种技术只能用于精确匹配，在一定程度上减少了I/O，从而提高了查询效率。如果需要对BLOB或者CLOB字段进行模糊查询，MySQL提供了前缀索引，也就是只为字段的前n列创建索引，举例如下：

mysql> create index idx_blob on t(context(100));

Query OK, 3 rows affected (0.04 sec)

Records: 3 Duplicates: 0 Warnings: 0

mysql> desc select * from t where context like 'beijing%' \G;

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: t

type: range

possible_keys: idx_blob

key: idx_blob

key_len: 103

ref: NULL

rows: 2

Extra: Using where

1 row in set (0.00 sec)

可以发现，对context前100个字符进行模糊查询，就可以用到前缀索引。注意，这里的查询条件中，“%”不能放在最前面，否则索引将不会被使用。

（3）在不必要的时候避免检索大型的BLOB或TEXT值。

例如，SELECT *查询就不是很好的想法，除非能够确定作为约束条件的WHERE子句只会找到所需要的数据行。否则，很可能毫无目的地在网络上传输大量的值。这也是 BLOB 或TEXT标识符信息存储在合成的索引列中对用户有所帮助的例子。用户可以搜索索引列，决定需要的哪些数据行，然后从符合条件的数据行中检索BLOB或TEXT值。

（4）把BLOB或TEXT列分离到单独的表中。

在某些环境中，如果把这些数据列移动到第二张数据表中，可以把原数据表中的数据列转换为固定长度的数据行格式，那么它就是有意义的。这会减少主表中的碎片，可以得到固定长度数据行的性能优势。它还可以使主数据表在运行 SELECT *查询的时候不会通过网络传输大量的BLOB或TEXT值。



