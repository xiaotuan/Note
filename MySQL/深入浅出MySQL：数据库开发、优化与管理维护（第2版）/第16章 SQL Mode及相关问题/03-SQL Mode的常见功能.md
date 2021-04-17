

下面介绍一下SQL Mode的常见功能。

（1）效验日期数据合法性，这是SQL Mode的一项常见功能。

在下面的例子中，观察一下非法日期“2007-04-31”（因为4月份没有31日）在不同SQL Mode下能否正确插入。

mysql> set session sql_mode='ANSI';

Query OK, 0 rows affected (0.00 sec)

mysql> create table t (d datetime);

Query OK, 0 rows affected (0.03 sec)

mysql> insert into t values('2007-04-31');

Query OK, 1 row affected, 1 warning (0.00 sec)

mysql> select * from t;

+---------------------+

| d|

+---------------------+

| 0000-00-00 00:00:00 |

+---------------------+

1 row in set (0.00 sec)

mysql> set session sql_mode='TRADITIONAL';

Query OK, 0 rows affected (0.00 sec)

mysql> insert into t values('2007-04-31');

ERROR 1292 (22007): Incorrect datetime value: '2007-04-31' for column 'd' at row 1

很显然，在ANSI模式下，非法日期可以插入，但是插入值却变为“0000-00-00 00:00:00”，并且系统给出了warning；而在TRADITIONAL模式下，会直接提示日期非法，拒绝插入。

（2）在 INSERT或UPDATE过程中，如果SQL Mode处于TRADITIONAL模式，那么运行 MOD(X，0)就会产生错误，这是因为 TRADITIONAL 也属于严格模式，在非严格模式下MOD(X，0)返回的结果是NULL，所以在含有MOD的运算中要根据实际情况设定好sql_mode。

下面的实例展示了不同sql_mode下，MOD(X，0)返回的结果。

mysql> set sql_mode='ANSI' ;

Query OK, 0 rows affected (0.00 sec)

mysql> create table t (i int);

Query OK, 0 rows affected (0.02 sec)

mysql> insert into t values(9%0);

Query OK, 1 row affected (0.00 sec)

mysql> select * from t;

+------+

| i |

+------+

| NULL |

+------+

1 row in set (0.00 sec)

mysql> set session sql_mode='TRADITIONAL';

Query OK, 0 rows affected (0.00 sec)

mysql> insert into t values(9%0);

ERROR 1365 (22012): Division by 0

（3）启用NO_BACKSLASH_ESCAPES模式，使反斜线成为普通字符。在导入数据时，如果数据中含有反斜线字符，那么启用NO_BACKSLASH_ESCAPES模式保证数据的正确性，是个不错的选择。

以下实例说明了启用NO_BACKSLASH_ESCAPES模式前后对反斜线“\”插入的变化。

mysql> set sql_mode='ansi';

Query OK, 0 rows affected (0.00 sec)

mysql> select @@sql_mode;

+-------------------------------------------------------------+

| @@sql_mode |

+-------------------------------------------------------------+

| REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ANSI |

+-------------------------------------------------------------+

1 row in set (0.00 sec)

mysql> create table t (context varchar(20));

Query OK, 0 rows affected (0.04 sec)

mysql> insert into t values('\beijing');

Query OK, 1 row affected (0.00 sec)

mysql> select * from t;

+---------+

| context |

+---------+

|eijing |

+---------+

1 row in set (0.00 sec)

mysql> insert into t values('\\beijing');

Query OK, 1 row affected (0.00 sec)

mysql> select * from t;

+----------+

| context |

+----------+

|eijing |

| \beijing |

+----------+

2 rows in set (0.00 sec)

mysql>set

sql_mode='REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ANSI,NO_BACKSLASH_ESCAPES';

Query OK, 0 rows affected (0.00 sec)

mysql> select @@sql_mode;

+-----------------------------------------------------------------------+

| @@sql_mode |

+-----------------------------------------------------------------------+

| REAL_AS_FLOAT,PIPES_AS_CONCAT, ANSI_QUOTES,IGNORE_SPACE,ANSI,NO_ BACKSLASH_ ESCAPES |

+-----------------------------------------------------------------------+

1 row in set (0.00 sec)

mysql> insert into t values('\\beijing');

Query OK, 1 row affected (0.00 sec)

mysql> select * from t;

+-----------+

| context |

+-----------+

|eijing|

| \beijing |

| \\beijing |

+-----------+

3 rows in set (0.00 sec)

通过上面的实例可以看到，当在ANSI模式中增加了NO_BACKSLASH_ESCAPES模式后，反斜线变为了普通字符。如果导入的数据存在反斜线，可以设置此模式，保证导入数据的正确性。

（4）启用PIPES_AS_CONCAT模式。将“|”视为字符串连接操作符，在Oracle等数据库中，“|”被视为字符串的连接操作符，所以，在其他数据库中含有“|”操作符的SQL在MySQL中将无法执行，为了解决这个问题，MySQL提供了PIPES_AS_CONCAT模式。

下面通过实例介绍一下PIPES_AS_CONCAT模式的作用。

mysql> set sql_mode='ansi';

Query OK, 0 rows affected (0.00 sec)

mysql> select @@sql_mode;

+-------------------------------------------------------------+

| @@sql_mode |

+-------------------------------------------------------------+

| REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ANSI |

+-------------------------------------------------------------+

1 row in set (0.00 sec)

mysql> select 'beijing'||'2008' ;

+-------------------+

| 'beijing'||'2008' |

+-------------------+

| beijing2008|

+-------------------+

1 row in set (0.01 sec)

通过上面的实例可以看到，ANSI模式中包含了PIPES_AS_CONCAT模式，所以默认情况下MySQL新版本支持将“|”视为字符串连接操作符。



