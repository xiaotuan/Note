

CHAR和VARCHAR很类似，都用来保存MySQL中较短的字符串。二者的主要区别在于存储方式的不同：CHAR列的长度固定为创建表时声明的长度，长度可以为从0～255的任何值；而VARCHAR列中的值为可变长字符串，长度可以指定为0～255（MySQL 5.0.3版本以前）或者 65535（MySQL 5.0.3版本以后）之间的值。在检索的时候，CHAR列删除了尾部的空格，而VARCHAR则保留这些空格。下面的例子中通过给表vc中的VARCHAR(4)和char(4)字段插入相同的字符串来描述这个区别。

（1）创建测试表 vc，并定义两个字段“v VARCHAR(4)”和“c CHAR(4)”：

mysql> CREATE TABLE vc (v VARCHAR(4), c CHAR(4));

Query OK, 0 rows affected (0.16 sec)

（2）v和c列中同时插入字符串“ab ”：

mysql> INSERT INTO vc VALUES ('ab ', 'ab ');

Query OK, 1 row affected (0.05 sec)

（3）显示查询结果：

mysql> select length(v),length(c) from vc;

+-----------+-----------+

| length(v) | length(c) |

+-----------+-----------+

| 4 | 2 |

+-----------+-----------+

1 row in set (0.01 sec)

可以发现，c字段的length只有2。给两个字段分别追加一个“+”字符看得更清楚：

mysql> SELECT CONCAT(v, '+'), CONCAT(c, '+') FROM vc;

+----------------+----------------+

| CONCAT(v, '+') | CONCAT(c, '+') |

+----------------+----------------+

| ab + | ab+ |

+----------------+----------------+

1 row in set (0.00 sec)

显然，CHAR列最后的空格在做操作时都已经被删除，而VARCHAR依然保留空格。



