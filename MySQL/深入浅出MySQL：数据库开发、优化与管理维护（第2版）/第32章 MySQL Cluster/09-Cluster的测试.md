

成功启动后，下面来测试一下 Cluster的功能。上文提到过，如果要使用 Cluster，则表的存储引擎必须为NDB，其他类型存储引擎的数据将不会保存到数据节点中。对于Cluster的一个重要功能就是防止单点故障，本节将对这些问题分别进行测试。

**1．NDB存储引擎测试**

（1）在任意一个SQL节点（这里用192.168.7.187）的test库中创建测试表t1，设置存储引擎为NDB，并插入两条测试数据：

mysql> create table t1(id int) engine=ndb;

Query OK, 0 rows affected (0.92 sec)

mysql> insert into t1 values(1);

Query OK, 1 row affected (0.04 sec)

mysql> insert into t1 values(2);

Query OK, 1 row affected (0.01 sec)

（2）在另外一个SQL节点（192.168.7.55），查询test库中的t1表，结果如下：

mysql> select * from t1;

+------+

| id |

+------+

| 1 |

| 2 |

+------+

2 rows in set (0.06 sec)

显然，两个SQL节点查询到的数据是一致的。

（3）在SQL节点192.168.7.187上将测试表t1的存储引擎改为MyISAM，再次插入测试记录：

mysql> alter table t1 engine=myisam;

Query OK, 2 rows affected (0.89 sec)

Records: 2 Duplicates: 0 Warnings: 0

mysql> insert into t1 values(3);

Query OK, 1 row affected (0.00 sec)

（4）在SQL节点192.168.7.55上再次查询表t1，结果如下：

mysql> select * from t1;

ERROR 1412 (HY000): Table definition has changed, please retry transaction

可以发现，表t1已经无法查询。

（5）在SQL节点192.168.7.187上再次将t1的存储引擎改为NDB：

mysql> alter table t1 engine=ndb;

Query OK, 3 rows affected (0.99 sec)

Records: 3 Duplicates: 0 Warnings: 0

（6）在SQL节点192.168.7.55上再次查询，结果如下：

mysql> select * from t1;

+------+

| id |

+------+

| 2 |

| 3 |

| 1 |

+------+

3 rows in set (0.00 sec)

显然，表t1的数据被再次同步到了数据节点。所有SQL节点又都可以正常查询数据。

**2．单点故障测试**

对于任意一种节点，都存在单点故障的可能性。在 Cluster 的设置过程中，应该尽量对每一类节点设置冗余，以防止单点故障发生时造成的应用中断。对于管理节点，一般不需要特殊的配置，只需要将管理工具和配置文件放在多台主机上即可。下面将测试一下 SQL 节点和数据节点的单点故障。

SQL节点发生单点故障。

对于上面的测试环境，我们设置了两个 SQL 节点，应用从两个节点对数据访问都可以得到一致的结果。如果有一个节点故障，系统还会正常运行吗？具体的测试过程如下。

（1）将SQL节点192.168.7.187上的MySQL服务停止：

[zzx2@zzx ndb_2_fs]$ mysqladmin -uroot shutdown

STOPPING server from pid file /home/zzx2/mysql/data/zzx.pid

071211 11:50:31 mysqld ended

[1]+ Done ./bin/mysqld_safe (wd:～/mysql)

(wd now:～/mysql/data/ndb_2_fs)

（2）查看一下Cluster的状态：

[zzx2@zzx ndb_2_fs]$ ndb_mgm-- NDB Cluster -- Management Client --

ndb_mgm> show

Connected to Management Server at: localhost:1186

Cluster Configuration

---------------------

[ndbd(NDB)] 2 node(s)

id=2 @192.168.7.187 (Version: 5.1.11, Nodegroup: 0, Master)

id=3 @192.168.7.55 (Version: 5.1.11, Nodegroup: 0)

[ndb_mgmd(MGM)] 1 node(s)

id=1 @192.168.7.187 (Version: 5.1.11)

[mysqld(API)] 3 node(s)

id=4 (not connected, accepting connect from 192.168.7.187)

id=5 @192.168.7.55 (Version: 5.1.11)

id=6 (not connected, accepting connect from any host)

从粗体代码部分中可以看出，SQL节点192.168.7.187已经断开，但是另外一个SQL节点192.168.7.55仍然处于正常连接中。

（3）从节点192.168.7.55上查看表t1，结果如下。

mysql> select * from t1;

+------+

| id |

+------+

| 2 |

| 4 |

| 3 |

| 1 |

+------+

4 rows in set (0.04 sec)

显然，SQL节点的单点故障并没有引起数据的查询故障。对于应用说，需要改变的就是将以前对故障节点的访问改为对非故障节点的访问。

数据节点的单点故障。

在这个测试环境中，数据节点也是有两个，那么它们对数据的存储是互相镜像还是一份数据分成几块存储呢（就像是磁盘阵列的 RAID1 还是 RAID0）？这个答案关键在于配置文件中[NDBD DEFAULT]组中的NoOfReplicas参数，如果这个参数等于 1，表示只有一份数据，但是分成n块分别存储在n个数据节点上；如果等于2，则表示数据被分成n/2块，每块数据都有两个备份，这样即使有任意一个节点发生故障，只要它的备份节点正常，系统就可以正常运行。

在下面的例子中，先将两个数据节点之一停掉，观察一下表 t1 能否正常访问；然后将NoOfReplicas配置改为2，这时，数据节点实际上已经互为镜像，保存了两份。这时再停掉任意一个数据节点，观察表t1还能否正常访问。

（1）将数据节点192.168.7.187上的NDB进程停止：

[zzx2@zzx～]$ ps -ef|grep 'ndbd'

zzx2 31271 1 0 10:50 ? 00:00:00 ndbd --initial --ndb-connectstring= 192.168. 7.187:1186

zzx2 31272 31271 0 10:50 ? 00:00:06 ndbd --initial --ndb-connectstring= 192.168. 7.187:1186

zzx2 8536 8508 0 17:54 pts/1 00:00:00 grep ndbd

[zzx2@zzx～]$ kill 31271 31272

（2）在任意一个SQL节点（这里用192.168.7.55）查看表t1数据，结果如下：

mysql> select * from t1;

ERROR 1296 (HY000): Got error 4009 'Cluster Failure' from NDBCLUSTER

显然，这里的Cluster出现了故障，无法访问。

（3）将配置文件中的NoOfReplicas改为2，按照前面所述步骤重新启动集群：

[zzx2@zzx mysql-cluster]$ more config.ini

[NDBD DEFAULT]

NoOfReplicas=2

DataMemory=500M

IndexMemory=300M

[TCP DEFAULT]

portnumber=2202

……省略其他参数

（4）此时，停掉任何一个数据节点的数据（这里选192.168.7.187）：

[zzx2@zzx mysql]$ ps -ef|grep ndbd

zzx2 5668 1 0 14:39 ? 00:00:00 ndbd --initial --ndb-connectstring=192.168.7.187:1186

zzx2 5669 5668 0 14:39 ? 00:00:00 ndbd --initial --ndb-connectstring=192.168.7.187:1186

zzx2 5875 5384 0 14:42 pts/2 00:00:00 grep ndbd

[zzx2@zzx mysql]$ kill 5668 5669

（5）再次从任意一个SQL节点查询表t1：

mysql> select * from t1;

+------+

| id |

+------+

| 3 |

| 2 |

| 1 |

| 4 |

+------+

4 rows in set (0.04 sec)

显然，结果依然正确。数据节点的冗余同样防止了单点故障的发生。



