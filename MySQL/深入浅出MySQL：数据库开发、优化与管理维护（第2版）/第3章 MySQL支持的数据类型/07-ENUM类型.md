

ENUM中文名称叫枚举类型，它的值范围需要在创建表时通过枚举方式显式指定，对1～255个成员的枚举需要1个字节存储；对于255～65535个成员，需要2个字节存储。最多允许有65535个成员。下面往测试表t中插入几条记录来看看ENUM的使用方法。

（1）创建测试表t，定义gender字段为枚举类型，成员为“M”和“F”：

mysql> create table t (gender enum('M','F'));

Query OK, 0 rows affected (0.14 sec)

（2）插入4条不同的记录：

mysql> INSERT INTO t VALUES('M'),('1'),('f'),(NULL);

Query OK, 4 rows affected (0.00 sec)

Records: 4 Duplicates: 0 Warnings: 0

mysql> select * from t;

+--------+

| gender |

+--------+

| M|

| M |

| F|

| NULL |

+--------+

4 rows in set (0.01 sec)

从上面的例子中，可以看出ENUM类型是忽略大小写的，在存储“M”、“f”时将它们都转成了大写，还可以看出对于插入不在 ENUM 指定范围内的值时，并没有返回警告，而是插入了enum('M','F')的第一个值“M”，这点用户在使用时要特别注意。

另外，ENUM类型只允许从值集合中选取单个值，而不能一次取多个值。



