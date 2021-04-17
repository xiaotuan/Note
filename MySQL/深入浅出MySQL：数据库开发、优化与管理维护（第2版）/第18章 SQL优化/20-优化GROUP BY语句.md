

默认情况下，MySQL对所有GROUP BY col1,col2,…的字段进行排序。这与在查询中指定ORDER BY col1,col2,…类似。因此，如果显式包括一个包含相同列的ORDER BY子句，则对MySQL的实际执行性能没有什么影响。

如果查询包括GROUP BY但用户想要避免排序结果的消耗，则可以指定ORDER BY NULL禁止排序，如下面的例子：

mysql> explain select payment_date, sum(amount) from payment group by payment_date\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: payment

type: ALL

possible_keys: NULL

key: NULL

key_len: NULL

ref: NULL

rows: 16310

Extra: Using temporary; Using filesort

1 row in set (0.01 sec)

mysql> explain select payment_date, sum(amount) from payment group by payment_date order by null\G

*************************** 1. row ***************************

id: 1

select_type: SIMPLE

table: payment

type: ALL

possible_keys: NULL

key: NULL

key_len: NULL

ref: NULL

rows: 16310

Extra: Using temporary

1 row in set (0.06 sec)

从上面的例子可以看出，第一个SQL语句需要进行“Filesort”，而第二个SQL由于ORDER BY NULL不需要进行“Filesort”，而上文提过Filesort往往非常耗费时间。



