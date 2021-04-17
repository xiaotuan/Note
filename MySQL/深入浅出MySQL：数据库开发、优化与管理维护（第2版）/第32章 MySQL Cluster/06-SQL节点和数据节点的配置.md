

SQL节点和数据节点的配置非常简单，只需要在对MySQL的配置文件（my.cnf）中增加如下内容即可（参数含义见后面的注释）：

# Options for mysqld process:

[MYSQLD]

ndbcluster #运行NDB存储引擎

ndb-connectstring=192.168.7.187 #定位管理节点

# Options for ndbd process:

[MYSQL_CLUSTER]

ndb-connectstring=192.168.7.187 #定位管理节点

SQL节点和数据节点的不同之处在于数据节点只需要配置上述选项即可，SQL节点还需要配置MySQL服务器的其他选项。



