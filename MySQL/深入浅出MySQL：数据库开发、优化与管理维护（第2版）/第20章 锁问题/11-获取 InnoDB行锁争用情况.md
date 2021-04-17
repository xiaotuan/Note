

可以通过检查InnoDB_row_lock状态变量来分析系统上的行锁的争夺情况：

mysql> show status like 'innodb_row_lock%';

+-------------------------------+-------+

| Variable_name | Value |

+-------------------------------+-------+

| InnoDB_row_lock_current_waits | 0 |

| InnoDB_row_lock_time | 0 |

| InnoDB_row_lock_time_avg | 0 |

| InnoDB_row_lock_time_max | 0 |

| InnoDB_row_lock_waits | 0 |

+-------------------------------+-------+

5 rows in set (0.01 sec)

如果发现锁争用比较严重，如InnoDB_row_lock_waits和InnoDB_row_lock_time_avg的值比较高，可以通过查询 information_schema 数据库中相关的表来查看锁情况，或者通过设置InnoDB Monitors来进一步观察发生锁冲突的表、数据行等，并分析锁争用的原因。

（1）通过查询information_schema数据库中的表了解锁等待情况：

mysql> select * from innodb_locks \G;

*************************** 1. row ***************************

lock_id: 403D:0:427:2

lock_trx_id: 403D

lock_mode: X

lock_type: RECORD

lock_table: `test`.`tab_no_index`

lock_index: `GEN_CLUST_INDEX`

lock_space: 0

lock_page: 427

lock_rec: 2

lock_data: 0x000000007A01

*************************** 2. row ***************************

lock_id: 403C:0:427:2

lock_trx_id: 403C

lock_mode: X

lock_type: RECORD

lock_table: `test`.`tab_no_index`

lock_index: `GEN_CLUST_INDEX`

lock_space: 0

lock_page: 427

lock_rec: 2

lock_data: 0x000000007A01

2 rows in set (0.01 sec)

mysql> select * from innodb_lock_waits \G;

*************************** 1. row ***************************

requesting_trx_id: 403D

requested_lock_id: 403D:0:427:2

blocking_trx_id: 403C

blocking_lock_id: 403C:0:427:2

1 row in set (0.00 sec)

（2）通过设置 InnoDB Monitors观察锁冲突情况：

mysql> CREATE TABLE innodb_monitor(a INT) ENGINE=INNODB;

Query OK, 0 rows affected (0.14 sec)

然后就可以用下面的语句来进行查看：

mysql> Show engine innodb status\G;

*************************** 1. row ***************************

Type: InnoDB

Name:

Status:

…

------------

TRANSACTIONS

------------

Trx id counter 0 117472192

Purge done for trx's n:o < 0 117472190 undo n:o < 0 0

History list length 17

Total number of lock structs in row lock hash table 0

LIST OF TRANSACTIONS FOR EACH SESSION:

---TRANSACTION 0 117472185, not started, process no 11052, OS thread id 1158191456

MySQL thread id 200610, query id 291197 localhost root

---TRANSACTION 0 117472183, not started, process no 11052, OS thread id 1158723936

MySQL thread id 199285, query id 291199 localhost root

Show innodb status

…

监视器可以通过发出下列语句来停止：

mysql> DROP TABLE innodb_monitor;

Query OK, 0 rows affected (0.05 sec)

设置监视器后，在SHOW INNODB STATUS的显示内容中，会有详细的当前锁等待的信息，包括表名、锁类型、锁定记录的情况等，便于进行进一步的分析和问题的确定。打开监视器以后，默认情况下每15秒会向日志中记录监控的内容，如果长时间打开会导致.err文件变得非常的巨大，所以用户在确认问题原因之后，要记得删除监控表以关闭监视器，或者通过使用“--console”选项来启动服务器以关闭写日志文件。



