

MPM（Performance Monitor for MySQL）是一套比较完整的监控MySQL数据库的Zabbix插件，该插件中包括丰富的监控项和触发器规则，通过和 Zabbix 客户端整合，可以完美地实现对MySQL数据库的监控。

Zabbix使用MPM插件后的监控结构，如图29-8所示。



![figure_0532_0209.jpg](../images/figure_0532_0209.jpg)
图29-8 Zabbix和MPM实现对MySQL监控

图 29-8 显示了 MPM 作为 Zabbix 插件监控 MySQL 的整体架构，首先 Zabbix 客户端zabbix_agentd 会读取配置文件 zabbix_agentd.conf ， zabbix_agentd.conf 则会根据设置载入FromDual_MySQL_monitoring.conf文件，将Zabbix客户端和MPM插件实现挂接。MPM的主要功能是完成对数据库的相关信息收集和上传操作。对数据库信息的收集操作，主要通过自身配置的FromDualMySQLagent.conf文件来读取相关配置信息，在收集过程中会调用插件自身的FromDualMySQL*.pm 模块，通过 FromDualMySQLagent.pl 实现解析，最终通过调用zabbix_sender实现上传。

部署MPM插件大概需要以下几个步骤。

（1）安装和部署Zabbix Server软件、Zabbix Web。

（2）下载安装MPM软件包及其依赖的Perl模块。

（3）通过Zabbix Web导入MPM中所需要的模板文件。

（4）在Zabbix Web端创建Host Group（主机组）。

（5）在Zabbix Web端创建Host（即MPM Agent配置中的数据库，注意在Web端配置的Hostname必须与MPM Agent配置中所使用的一致）。

（6）将模板关联到所创建的Host。

（7）安装和配置MPM Agent，将MPM整合到Zabbix中。

（8）重启Zabbix客户端服务。

本章的开头部分已经介绍了Zabbix Server和客户端的部署，后面关于这两部分的内容将略过。

**1．MPM下载及其依赖安装**

安装MPM依赖的相关Perl模块：

[root@ip83~]#perl -MCPAN -e shell

cpan> install File::Which

cpan> install Bundle::LWP

cpan> install Digest::SHA1

cpan> install DBD::mysql

cpan> install Time::HiRes

cpan> install Crypt::SSLeay

下载MPM并解压：

[root@ip83~]#wget -c http://www.shinguz.ch/download/mysql_performance_monitor-latest. tar.gz

[root@ip83~]#tar zxvf mysql_performance_monitor-latest.tar.gz

[root@ip83~]#ls -lrt

-rw-rw-r-- 1 1000 1000 40991 04-10 02:42 mysql_performance_monitor_templates-0.9.1.tar.gz

-rw-r--r-- 1 root root 76498 04-10 02:44 mysql_performance_monitor_agent-0.9.1.tar.gz

解压后会有两个文件，其中mysql_performance_monitor_templates-0.9.1.tar.gz主要是Zabbix Server Web端导入的模板文件，mysql_performance_monitor_agent-0.9.1.tar.gz文件为Zabbix客户端需要部署的MPM客户端文件。

**2．Zabbix Web端导入MPM模板**

什么是 MPM 模板？将 mysql_performance_monitor_templates-0.9.1.tar.gz 文件上传到Windows，解压该文件，进入xml目录下，就会发现存在大量XML类型的文件，这些文件即为需要导入到Zabbix Server Web端的模板文件。

mysql_performance_monitor_templates-0.9.1\xml下的XML文件如图29-9所示。



![figure_0534_0210.jpg](../images/figure_0534_0210.jpg)
图29-9 Zabbix Fromdual模板列表

这些模板的具体功能如下：

Template_FromDual.MySQL.mpm.xml (监控MPM Agent本身,这个必须导入，因为它会触发发送进程)

Template_FromDual.MySQL.server.xml (监控Linux系统和附加的数据库的信息)

Template_FromDual.MySQL.process.xml (监控各种Linux进程,比如:mysqld信息)

Template_FromDual.MySQL.mysql.xml (监控MySQL常用状态变量信息)

Template_FromDual.MySQL.innodb.xml (监控InnoDB存储引擎状态变量信息)

Template_FromDual.MySQL.myisam.xml (监控MyISAM存储引擎状态变量信息)

Template_FromDual.MySQL.master.xml (监控MySQL主从复制的Master状态信息)

Template_FromDual.MySQL.slave.xml (监控MySQL主从复制的Slave状态信息)

MPM可选的模板如下：

Template_FromDual.MySQL.ndb.xml (监控MySQL NDB Cluster的状态变量)

Template_FromDual.MySQL.galera.xml (监控MySQL Galera Cluster的状态变量)

Template_FromDual.MySQL.pbxt.xml (监控PBXT存储引擎状态变量)

Template_FromDual.MySQL.aria.xml (监控Aria存储引擎的状态变量)

Template_FromDual.MySQL.drbd.xml (监控DRBD设备状态信息)

上述模板可以根据自己业务的需要导入到Zabbix Server Web端。

要导入MPM模板，可以在Zabbix Web中选择ConfigurationÆTemplates，然后在“Import”栏下单击“浏览”按钮，选中所需要的 XML 文件，单击“Import”按钮即可导入相应的监控模板，如图29-10所示。

在Zabbix Web中，选择ConfigurationÆTemplates，可以查看刚才导入的模板，如图 29-11所示。

MPM中的模板带有丰富的Item项和Trigger项，基本上能覆盖MySQL日常运维中的所有监控项。



![figure_0535_0211.jpg](../images/figure_0535_0211.jpg)
图29-10 Fromdual模板导入



![figure_0535_0212.jpg](../images/figure_0535_0212.jpg)
图29-11 Fromdual模板查看

**3．安装MPM并且配置MPM Agent的Zabbix Keys，以实现Zabbix挂接MPM**

安装MPM Agent：

[root@ip83~]#tar zxvf mysql_performance_monitor_agent-0.9.1.tar.gz

[root@ip83~]#mv mysql_performance_monitor_agent-0.9.1 /usr/local/mysql_performance_monitor-agent

在FromDualMySQLagent.pl脚本中修改相应的zabbix_sender的路径：

[root@ip83~]#cd /usr/local/mysql_performance_monitor-agent/

[root@ip83~]#sed -i "s|/usr/local/bin|/usr/local/zabbix/bin/|g" FromDualMySQLagent.pl

将MPM Agent的Keys信息加入到 zabbix_agentd的配置目录中：

[root@ip83~]#cd /usr/local/zabbix/etc/zabbix_agentd.conf.d

[root@ip83~]#vi FromDual_MySQL_monitoring.conf

[root@ip83~]#cat FromDual_MySQL_monitoring.conf

UserParameter=FromDual.MySQL.check,/usr/local/mysql_performance_monitor-agent/FromDua lMySQLagent.pl /usr/local/mysql_performance_monitor-agent/etc/FromDualMySQLagent.conf

**4．MPM Agent配置**

创建MPM的MySQL监控用户：

mysql> create user 'mpm'@'127.0.0.1' identified by '123456';

mysql> grant process, replication client on *.* to 'mpm'@'127.0.0.1';

mysql> flush privileges;

配置MPM Agent：

[root@ip83~]#cd /usr/local/mysql_performance_monitor-agent/etc

[root@ip83~]#cp FromDualMySQLagent.conf.template FromDualMySQLagent.conf

[root@ip83~]#mkdir -p /var/log/zabbix

[root@ip83~]#mkdir -p /var/log/zabbix/cache

[root@ip83~]#touch /var/log/zabbix/FromDualMySQLagent.log

[root@ip83~]#chown -R zabbix:zabbix /var/log/zabbix

[root@ip83~]#chmod o+r /home/mysql/mysqlhome/data/ip83.pid

[root@ip83~]#vi FromDualMySQLagent.conf

[root@ip83~]#cat FromDualMySQLagent.conf

[default]

# Type of section:

# mysqld for a normal MySQL database

# ndbd for a MySQL cluster

Type = mysqld

# Debug levels are:

# 1 is logging only errors

# 2 is logging errors and warnings (this is the default)

# 3 logs some informations messages as well

# 4 logs everything (for debugging purposes only)

Debug = 2

LogFile = /var/log/zabbix/FromDualMySQLagent.log

# Directory where the Cache files should be written to:

CacheFileBase = /var/log/zabbix/cache/FromDualAgentCache

# If you agent is not located in the same time zone as your server

# TimeShift = +0.0

# Information for MySQL connections:

Username = mpm

Password = 123456

MysqlHost = 127.0.0.1

MysqlPort = 3306

# Zabbix Server IP address

ZabbixServer = 192.168.7.81

# If section is disabled

Disabled = false

# Possible modules for databases are:

# process mysql myisam aria innodb pbxt ndb master slave drbd galera memcache

# Possible modules for servers are:

# mpm server

# Usual modules are

Modules = process mysql myisam innodb

# Special parameter which is used for module ndb and process

#ClusterLog = /var/lib/mysql-cluster/ndb_1_cluster.log

# MySQL Pid file, need read permission for zabbix user

#PidFile = /home/mysql/mysqlhome/data/ip83.pid

[db_server]

Type = mysqld

Modules = mpm server

# All MySQL databases here

# Try to avoid section names with spaces!

[192.168.7.83_MySQL_5.5.28_3306_PerconaServer] # This MUST match Hostname in Zabbix!

Type = mysqld

MysqlPort = 3306

Modules = process mysql myisam innodb slave

PidFile = /home/mysql/mysqlhome/data/ip83.pid

Debug = 1

**说明：**这里监控的MySQL Server使用了process、mysql、myisam、innodb、slave这5个模块。

检查MPM插件工作状况：

[root@ip83~]#/usr/local/mysql_performance_monitor-agent/FromDualMySQLagent.pl/usr/local/mysql_performance_monitor-agent/etc/FromDualMySQLagent.conf

1

输出“1”，代表插件工作正常，重启Zabbix Agentd：

# /etc/init.d/zabbix_agentd restart

重启Zabbix Agent，载入MPM模块。



