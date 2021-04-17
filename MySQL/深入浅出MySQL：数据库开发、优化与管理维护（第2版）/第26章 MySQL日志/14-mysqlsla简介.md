

在很多情况下，都需要对MySQL日志进行各种分析，来了解系统运行的方方面面。比如我们可能需要对查询日志进行分析，看一下哪些语句执行最频繁，从而了解客户最关心的功能，哪些重要的功能为什么点击率低，需要我们进一步来完善；再比如 DBA 很关心性能问题，需要从慢查询日志中进行分析，找到最消耗时间的SQL进行优化，等等。

如前所述，MySQL自带了一些工具可以对日志进行分析，比如mysqlbinlog可以用来分析二进制日志，mysqlslow可以用来分析慢查询日志，但这些工具相对功能较单一，而且对查询日志没有提供分析工具。因此，很多第三方工具应用而生，而mysqlsla是其中使用较广泛的一个。

mysqlsla是MySQL Statement Log Analyzer的缩写，可以从 http://hackmysql.com/mysqlsla进行下载，它可以分析查询日志、慢查询日志（包括微秒日志）、二进制日志和具有固定格式的自定义日志。mysqlsla的基本用法很简单，但参数众多，我们这里只简单地介绍一些常用参数，更详细的用法可以通过man mysqlsla命令来查看。

mysqlsla最基本的用法如下。

解析查询日志和慢查询日志：

mysqlsla --log-type slow LOG

mysqlsla --log-type general LOG

解析二进制日志，需要先通过mysqlbinlog进行转换：

mysqlbinlog LOG│ mysqlsla --log-type binary –

解析微秒日志：

mysqlsla --log-type msl LOG

解析用户自定义日志：

mysqlsla --log-type udl --udl-format FILE

需要注意的是，除二进制日志外，其他类型日志的--log-type 参数在正常情况下可以省略， mysqlsla会自动分析日志类型进行解析；而mysqlsla是无法判断经过标准输出后的日志类型，因此二进制日志通过mysqlbinlog LOG解析后mysqlsla无法判断日志类型，必须加上--log-type参数。

下面以查询日志为例来详细了解一下mysqlsla的输出报表：

[mysql55@bj55 data]$ mysqlsla bj55.log

Auto-detected logs as general logs

Report for general logs: bj55.log

109 queries total, 36 unique

Sorted by 'c_sum'

______________________________________________________________________ 001 ___

Count : 18 (16.51%)

Connection ID : 1

Database : test

Users :

root@localhost : 100.00% (18) of query, 100.00% (109) of all users

Query abstract:

SELECT @@version_comment LIMIT N

Query sample:

select @@version_comment limit 1

______________________________________________________________________ 002 ___

Count : 16 (14.68%)

Connection ID : 2

Database : test

Users :

root@localhost : 100.00% (16) of query, 100.00% (109) of all users

Query abstract:

SHOW variables LIKE 'S'

Query sample:

show variables like 'long%'

…（此处省略003~009）

______________________________________________________________________ 010 ___

Count : 3 (2.56%)

Connection ID : 5

Database : test

Users :

root@localhost : 100.00% (3) of query, 100.00% (117) of all users

Query abstract:

SELECT COUNT(N) FROM t1 a,t1 b WHERE a.id=b.id

Query sample:

select count(1) from t1 a,t1 b where a.id=b.id

日志的第一部分是对分析结果的一个总体介绍，显示了自动探测到的日志类型、总的查询次数、唯一的查询次数以及结果的排序方式：

109 queries total, 36 unique

Sorted by 'c_sum'

其中，总的查询次数和唯一查询次数的区别在于唯一查询次数是 SQL 语句将实际条件值抽象为固定字符，并且过滤空格后进行 distinct 后的结果，这样我们可以很方便地知道数据库中SQL的大致数量和执行频率。

日志的第二部分是报告的主题，按照执行次数从大到小进行排序的 SQL 统计，默认显示前十条SQL，每个SQL包含的统计内容如下：

Count : 16 (14.68%) --此类SQL一共执行的次数

Connection ID : 2

Database : test --执行操作的数据库

Users : --执行操作的用户名，如果有多个用户执行过，会按照用户的执行比例显示

root@localhost : 100.00% (16) of query, 100.00% (109) of all users

Query abstract: --SQL语句抽象后的结果

SHOW variables LIKE 'S'

Query sample: --SQL带入实际值的样例

show variables like 'long%'

mysqlsla提供了很多可选参数，下面列出了一些常用的参数。

--statement-filter (-sf) CONDTIONS用来过滤语句类型，CONDTIONS前面可以加“+”或者“-”，表示报表中“仅显示”或者“仅去掉”后面的语句类型，比如statement-filter=+UPDATE,INSERT，表示结果中只显示update和insert语句，statement-filter=-UPDATE,INSERT表示结果中显示除了update和insert的其他SQL语句。

--explain (-ex)用来在报表中显示执行计划。

--sort是排序方式，慢查询日志和微秒日志默认是按照总执行时间t_sum来排序，其他日志都按照执行次数c_sum来排序。

--grep PATTERN用来匹配SQL语句中的特定字符串，比如--grep 'COUNT'，则结果只显示SQL语句中包含 'COUNT'的语句相关内容。

为了方便使用，可以将mysqlsla的常用配置选项写入~/.mysqlsla，这个文件是mysqlsla的配置文件，mysqlsla 使用时会读取里面的配置。对于更多的参数用法，读者可以参考 mysqlsla的帮助日志。

除了mysqlsla，还有一些常用日志分析工具，比如myprofi、mysql-explain-slow-log、mysqllogfilter等，这些工具在日志分析方面各有特色，尤其是myprofi（***http://myprofi.sourceforge.net/***），在样式输出方面更加简洁方便，读者如果有兴趣可以进一步了解。



