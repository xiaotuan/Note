

当一个日志文件写满后，InnoDB 会自动切换到另一个日志文件，但切换时会触发数据库检查点（Checkpoint），这将导致InnoDB缓存脏页的小批量刷新，会明显降低InnoDB的性能。

那是不是将innodb_log_file_size设得越大越好呢？理论上是，但如果日志文件设置得太大，恢复时将需要更长时间，同时也不便于管理。一般来说，平均每半小时写满1个日志文件比较合适。我们可以通过下面的方法来计算 InnoDB 每小时产生的日志量并估算合适的innodb_log_file_size值。

首先，计算InnoDB每分钟产生的日志量：

mysql> pager grep -i "Log sequence number"

PAGER set to 'grep -i "Log sequence number"'

6mysql> SHOW ENGINE INNODB STATUS\G SELECT SLEEP(60); SHOW ENGINE INNODB STATUS\G

Log sequence number 90176272406

1 row in set (0.00 sec)

1 row in set (59.99 sec)

Log sequence number 90196407469

1 row in set (0.00 sec)

mysql> nopager

PAGER set to stdout

mysql> select ROUND((90196407469 - 90176272406)/ 1024 / 1024) as MB;

+------+

| MB |

+------+

| 19 |

+------+

1 row in set (0.00 sec)

这一步也可以通过查询INFORMATION_SCHEMA.GLOBAL_STATUS表来计算：

SELECT @a1 := variable_value AS a1

FROM information_schema.global_status

WHERE variable_name = 'innodb_os_log_written'

UNION ALL

SELECT Sleep(60)

UNION ALL

SELECT @a2 := variable_value AS a2

FROM information_schema.global_status

WHERE variable_name = 'innodb_os_log_written';

+--------------+

| a1|

+--------------+

| 90176272406 |

| 0 |

| 90196407469 |

+--------------+

1 row in set (0.01 sec)

SELECT ROUND((@a2-@a1) / 1024 / 1024 / @@innodb_log_files_in_group) as MB;

+------+

| MB |

+------+

| 19 |

+------+

1 row in set (0.01 sec)

通过上述操作得到InnoDB每分钟产生的日志量是19MB。然后，计算每半小时的日志量：



![0-2.jpg](../images/0-2.jpg)
这样，就可以得出innodb_log_file_size的大小至少应该是512MB。



