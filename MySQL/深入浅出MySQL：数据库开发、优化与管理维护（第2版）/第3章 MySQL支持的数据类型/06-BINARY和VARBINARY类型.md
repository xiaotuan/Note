

BINARY和VARBINARY类似于CHAR和VARCHAR，不同的是它们包含二进制字符串而不包含非二进制字符串。在下面的例子中，对表t中的binary字段c插入一个字符，研究一下这个字符到底是怎么样存储的。

（1）创建测试表 t，字段为 c BINARY(3)：

mysql> CREATE TABLE t (c BINARY(3));

Query OK, 0 rows affected (0.14 sec)

（2）往c字段中插入字符“a”：

mysql> INSERT INTO t SET c='a';

Query OK, 1 row affected (0.06 sec)

（3）分别用以下几种模式来查看c列的内容：

mysql> select *,hex(c),c='a',c='a\0',c='a\0\0' from t;

+------+--------+-------+---------+-----------+

| c | hex(c) | c='a' | c='a\0' | c='a\0\0' |

+------+--------+-------+---------+-----------+

| a| 610000 |0|0|1|

+------+--------+-------+---------+-----------+

1 row in set (0.00 sec)

可以发现，当保存BINARY值时，在值的最后通过填充“0x00”（零字节）以达到指定的字段定义长度。从上例中看出，对于一个BINARY(3)列，当插入时“a”变为“a\0\0”。



