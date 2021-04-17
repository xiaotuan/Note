

MySQL客户端连接成功后，通过 show [session|global]status命令可以提供服务器状态信息，也可以在操作系统上使用mysqladmin extended-status命令获得这些消息。show [session|global] status可以根据需要加上参数“session”或者“global”来显示session级（当前连接）的统计结果和global级（自数据库上次启动至今）的统计结果。如果不写，默认使用的参数是“session”。

下面的命令显示了当前session中所有统计参数的值：

mysql> show status like 'Com_%';

+--------------------------+-------+

| Variable_name | Value |

+--------------------------+-------+

| Com_admin_commands| 0|

| Com_alter_db| 0|

| Com_alter_event| 0|

| Com_alter_table| 0|

| Com_analyze| 0|

| Com_backup_table | 0 |

| Com_begin | 0 |

| Com_change_db | 1|

| Com_change_master | 0 |

| Com_check | 0 |

| Com_checksum | 0 |

| Com_commit| 0|

…

Com_xxx表示每个xxx语句执行的次数，我们通常比较关心的是以下几个统计参数。

Com_select：执行SELECT操作的次数，一次查询只累加1。

Com_insert：执行INSERT操作的次数，对于批量插入的INSERT操作，只累加一次。

Com_update：执行UPDATE操作的次数。

Com_delete：执行DELETE操作的次数。

上面这些参数对于所有存储引擎的表操作都会进行累计。下面这几个参数只是针对InnoDB存储引擎的，累加的算法也略有不同。

Innodb_rows_read：SELECT查询返回的行数。

Innodb_rows_inserted：执行INSERT操作插入的行数。

Innodb_rows_updated：执行UPDATE操作更新的行数。

Innodb_rows_deleted：执行DELETE操作删除的行数。

通过以上几个参数，可以很容易地了解当前数据库的应用是以插入更新为主还是以查询操作为主，以及各种类型的 SQL 大致的执行比例是多少。对于更新操作的计数，是对执行次数的计数，不论提交还是回滚都会进行累加。

对于事务型的应用，通过Com_commit和Com_rollback可以了解事务提交和回滚的情况，对于回滚操作非常频繁的数据库，可能意味着应用编写存在问题。

此外，以下几个参数便于用户了解数据库的基本情况。

Connections：试图连接MySQL服务器的次数。

Uptime：服务器工作时间。

Slow_queries：慢查询的次数。



