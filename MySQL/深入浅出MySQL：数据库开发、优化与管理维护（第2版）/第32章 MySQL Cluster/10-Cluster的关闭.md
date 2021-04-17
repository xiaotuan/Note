

Cluster的关闭命令很简单，只需要在shell下执行如下命令即可：

[zzx2@zzx mysql-cluster]$ ndb_mgm -e shutdown

Connected to Management Server at: localhost:1186

Node 2: Cluster shutdown initiated

Node 3: Cluster shutdown initiated

Node 3: Node shutdown completed.

Node 2: Node shutdown completed.

2 NDB Cluster node(s) have shutdown.

Shutdown of NDB Cluster management server failed.

* 0: No error

* Executing: ndb_mgm_stop2

也可以用ndb_mgm工具进入管理界面后，使用shutdown命令关闭：

ndb_mgm> shutdown

Node 2: Cluster shutdown initiated

Node 3: Cluster shutdown initiated

Node 2: Node shutdown completed.

Node 3: Node shutdown completed.

2 NDB Cluster node(s) have shutdown.

Shutdown of NDB Cluster management server failed.

* 0: No error

* Executing: ndb_mgm_stop2

需要注意的是，集群关闭后，SQL节点的MySQL服务并不会停止。



