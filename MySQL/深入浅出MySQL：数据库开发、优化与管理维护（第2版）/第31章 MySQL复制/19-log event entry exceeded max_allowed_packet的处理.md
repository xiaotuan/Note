

如果应用中使用大的BLOG列或者长字符串，那么在从库上恢复时，可能会出现“log event entry exceeded max_allowed_packet”错误，这是因为含有大文本的记录无法通过网络进行传输导致。解决的办法就是在主从库上增加max_allowed_packet参数的大小，这个参数的默认值为1MB，可以按照实际需要进行修改，比如下例中将其增大为16MB：

mysql> show variables like 'max_allowed_packet';

+--------------------+---------+

| Variable_name| Value |

+--------------------+---------+

| max_allowed_packet | 1047552 |

+--------------------+---------+

1 row in set (0.00 sec)

mysql> SET @@global.max_allowed_packet=16777216;

Query OK, 0 rows affected (0.01 sec)

同时在my.cnf中，设置 max_allowed_packet = 16MB，保证下次数据库重新启动后参数继续有效。



