…



Zabbix Server安装配置和启动大概需要以下几个步骤。

（1）创建Zabbix数据库和MySQL用户：

mysql> create schema zabbix character set utf8;

Query OK, 1 row affected (0.05 sec)

mysql> create user 'zabbix'@'%' identified by '123456';

Query OK, 0 rows affected (0.16 sec)

mysql> grant all on zabbix.* to 'zabbix'@'%';

Query OK, 0 rows affected (0.03 sec)

mysql> flush privileges;

Query OK, 0 rows affected (0.04 sec)

（2）导入Zabbix数据库初始数据：

[root@ip81 ~]#cd database/mysql/

[root@ip81 ~]#mysql -S /tmp/mysql.sock zabbix <schema.sql

[root@ip81 ~]#mysql -S /tmp/mysql.sock zabbix <schema.sql

[root@ip81 ~]#mysql -S /tmp/mysql.sock zabbix < images.sql;

[root@ip81 ~]#mysql -S /tmp/mysql.sock zabbix < data.sql;

（3）配置Zabbix配置文件。

编辑Zabbix Server的配置文件/usr/local/zabbix/etc/zabbix_server.conf，修改以下参数：

ListenPort=10051

LogFile= /usr/local/zabbix/logs/zabbix_server.log

PidFile= /usr/local/zabbix/logs/zabbix_server.pid

DBHost=192.168.7.81

DBName=zabbix

DBUser=zabbix

DBPassword=123456

DBPort=3306

DBSocket=/tmp/mysql.sock

FpingLocation=/usr/local/sbin/fping

（4）配置Zabbix服务。

从安装目录复制zabbix_server脚本并编辑：

[root@ip81 ~]#cd zabbix-2.0.6

[root@ip81 ~]#cp misc/init.d/fedora/core5/zabbix_server /etc/init.d/

[root@ip81 ~]#mkdir -p /usr/local/zabbix/logs

[root@ip81 ~]#chown -R zabbix:zabbix /usr/local/zabbix

[root@ip81 ~]#vi /etc/init.d/zabbix_server

[root@ip81 ~]#cat /etc/init.d/zabbix_server

…

ZABBIX_BIN="/usr/local/zabbix/sbin/zabbix_server"

CONF_FILE="/usr/local/zabbix/etc/zabbix_server.conf"

…

start() {

…

daemon $ZABBIX_BIN -c $CONF_FILE

}

（5）开启Zabbix安全限制。

调整防火墙规则（开放端口10051）：

[root@ip81 ~]#iptables -A INPUT -p tcp -m tcp --dport 10051 -j ACCEPT

[root@ip81 ~]#service iptables save

Saving firewall rules to /etc/sysconfig/iptables: [ OK ]

（6）启动Zabbix Server：

[root@ip81 ~]#service zabbix_server start

Starting Zabbix Server: [ OK ]

（7）停止Zabbix Server：

[root@ip81 ~]#service zabbix_server stop

Stopping Zabbix Server: [ OK ]

（8）配置Zabbix Server开机自动启动：

[root@ip81 ~]#chkconfig --add zabbix_server

[root@ip81 ~]#chkconfig --level 35 zabbix_server on



