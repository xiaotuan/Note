

Cluster 需要各个节点都进行启动后才可以运行，节点的启动顺序为管理节点Æ数据节点ÆSQL节点。以本章的测试环境为例，启动步骤如下。

（1）在管理节点上，从系统shell发出下述命令以启动管理节点进程：

[zzx2@zzx mysql-cluster]$ ndb_mgmd -f ./config.ini

Cluster configuration warning:

arbitrator with id 1 and db node with id 2 on same host 192.168.7.187

Running arbitrator on the same host as a database node may

cause complete cluster shutdown in case of host failure.

命令行中的 ndb_mgmd是MySQL Cluster的管理服务器，后面的-f表示后面的参数是启动的参数配置文件，也可以用--config-file=name来表示，其他选项可以用 ndb_mgmd --help命令来查看。如果没有任何提示，则集群管理进程成功启动，用ps（进程查看）命令查看，可以看到类似以下进程：

zzx2 7248 1 0 15:41 ? 00:00:00 ndb_mgmd -f ./config.ini

本例中出现了一个 warning，是因为管理节点和数据节点在同一台服务器上，如果主机出现故障，则整个 Cluster会shutdown。在实际生产环境下，最好将管理节点放到单独的服务器上。这里忽略这个warning。

（2）在每台数据节点服务器（本例为192.168.7.55和192.168.7.187）上，运行下述命令启动ndbd进程：

shell> ndbd --initial --ndb-connectstring=192.168.7.187:1186

执行完毕后，查看系统进程，如果可以看到如下进程，则表示数据节点的 ndbd 进程启动成功：

[zzx2@zzx mysql-cluster]$ ps -ef

…（省略其他进程）

zzx2 7862 1 0 18:19? 00:00:00 ndbd --initial --ndb-connectstring=192. 168.7.187:1186

zzx2 7863 7862 2 18:19? 00:00:00 ndbd --initial --ndb-connectstring=192. 168.7.187:1186

…（省略其他进程）

ndbd进程是使用NDB存储引擎处理表中数据的进程。通过该进程，存储节点能够实现分布式事务管理、节点恢复、在线备份等相关的任务。

**注意：**仅应在首次启动ndbd时，或在备份／恢复或配置变化后重启ndbd时使用“--initial”参数，这很重要。原因在于，该参数会使节点删除由早期ndbd实例创建的、用于恢复的任何文件，包括恢复用日志文件。

（3）依次启动SQL节点上的MySQL服务。

对于 node 1（192.168.7.187），启动其上的MySQL服务：

[zzx2@zzx mysql]$ ./bin/mysqld_safe &

[1] 29817

[zzx2@zzx mysql]$ Starting mysqld daemon with databases from /home/zzx2/mysql/ data

对于 node 2（192.168.7.55），启动其上的MySQL服务：

[zzx2@test55 mysql]$ cd /home1/zzx2/mysql

[zzx2@test55 mysql]$ ./bin/mysqld_safe &

[1] 9762

[zzx2@test55 mysql]$ Starting mysqld daemon with databases from /home1/zzx2/ mysql/data

（4）节点全部成功启动后，用ndb_mgm工具的show命令查看集群状态：

[zzx2@zzx data]$ ndb_mgm

-- NDB Cluster -- Management Client --

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

id=4 @192.168.7.187 (Version: 5.1.11)

id=5 @192.168.7.55 (Version: 5.1.11)

id=6 (not connected, accepting connect from any host)

ndb_mgm>

ndb_mgm工具是 ndb_mgmd（MySQL Cluster Server）的客户端管理工具，通过它可以方便地检查Cluster的状态、启动备份、关闭Cluster等功能。更详细的使用方法可以通过ndb_mgm--help命令来进行查看。

从上面显示的状态可以看出以下信息。

（1）集群目前的管理服务器端口是1186。

Connected to Management Server at: localhost:1186

（2）集群的数据节点有3个，详细信息为：

[ndbd(NDB)] 2 node(s)

id=2 @192.168.7.187 (Version: 5.1.11, Nodegroup: 0, Master)

id=3 @192.168.7.55 (Version: 5.1.11, Nodegroup: 0)

（3）管理节点有一个，详细信息为：

[ndb_mgmd(MGM)] 1 node(s)

id=1 @192.168.7.187 (Version: 5.1.11)

（4）SQL节点有3个，目前处于连接状态的有2个，详细信息为：

[mysqld(API)] 3 node(s)

id=4 @192.168.7.187 (Version: 5.1.11)

id=5 @192.168.7.55 (Version: 5.1.11)

id=6 (not connected, accepting connect from any host)



