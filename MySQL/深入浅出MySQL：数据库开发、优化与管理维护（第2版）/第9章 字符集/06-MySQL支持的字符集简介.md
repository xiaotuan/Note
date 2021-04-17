+-----------------------------------------------------------------------+



MySQL 服务器可以支持多种字符集，在同一台服务器、同一个数据库甚至同一个表的不同字段都可以指定使用不同的字符集，相比Oracle等其他数据库管理系统，在同一个数据库只能使用相同的字符集，MySQL明显存在更大的灵活性。

查看所有可用的字符集的命令是 show character set：

mysql> show character set;

+----------+-----------------------------+---------------------+--------+

| Charset | Description | Default collation | Maxlen |

+----------+-----------------------------+---------------------+--------+

| dec8 | DEC West European | dec8_swedish_ci | 1 |

| cp850 | DOS West European | cp850_general_ci | 1 |

| hp8 | HP West European | hp8_english_ci | 1 |

| koi8r | KOI8-R Relcom Russian | koi8r_general_ci | 1 |

……

或者查看information_schema.character_set，可以显示所有的字符集和该字符集默认的校对规则。

mysql> desc information_schema.character_sets;

+----------------------+-------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+----------------------+-------------+------+-----+---------+-------+

| CHARACTER_SET_NAME | varchar(64) | NO | | | |

| DEFAULT_COLLATE_NAME | varchar(64) | NO | | | |

| DESCRIPTION | varchar(60) | NO | | | |

| MAXLEN | bigint(3) | NO | | 0 | |

+----------------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)

MySQL的字符集包括**字符集**（CHARACTER）和**校对规则**（COLLATION）两个概念。其中字符集用来定义MySQL存储字符串的方式，校对规则用来定义比较字符串的方式。字符集和校对规则是一对多的关系，MySQL支持30多种字符集的70多种校对规则。

每个字符集至少对应一个校对规则。可以用“SHOW COLLATION LIKE '***';”命令或者通过系统表information_schema.COLLATIONS来查看相关字符集的校对规则。

mysql> SHOW COLLATION LIKE 'gbk%';

+----------------+---------+----+---------+----------+---------+

| Collation | Charset | Id | Default | Compiled | Sortlen |

+----------------+---------+----+---------+----------+---------+

| gbk_chinese_ci | gbk | 28 | Yes | Yes | 1 |

| gbk_bin | gbk | 87 | | Yes | 1 |

+----------------+---------+----+---------+----------+---------+

2 rows in set (0.00 sec)

校对规则命名约定：它们以其相关的字符集名开始，通常包括一个语言名，并且以_ci（大小写不敏感）、_cs（大小写敏感）或_bin（二元，即比较是基于字符编码的值而与language无关）结束。

例如，上面例子中 GBK 的校对规则，其中 gbk_chinese_ci 是默认的校对规则，对大小写不敏感；而gbk_bin按照编码的值进行比较，对大小写敏感。

下面的这个例子中，如果指定“A”和“a”按照gbk_chinese_ci校对规则进行比较，则认为两个字符是相同的，如果按照gbk_bin校对规则进行比较，则认为两个字符是不同的。我们事先需要确认应用的需求，是需要按照什么样的排序方式，是否需要区分大小写，以确定校对规则的选择。

mysql> select case when 'A' COLLATE gbk_chinese_ci = 'a' collate gbk_chinese_ci then 1 else 0 end;

+-----------------------------------------------------------------------+

| case when 'A' COLLATE gbk_chinese_ci = 'a' collate gbk_chinese_ci then 1 else 0 end |

+-----------------------------------------------------------------------+

| 1 |

+-----------------------------------------------------------------------+

1 row in set (0.00 sec)

mysql> select case when 'A' COLLATE gbk_bin = 'a' collate gbk_bin then 1 else 0 end;

| case when 'A' COLLATE gbk_bin = 'a' collate gbk_bin then 1 else 0 end|

+-----------------------------------------------------------------------+

| 0 |

+-----------------------------------------------------------------------+

1 row in set (0.00 sec)



