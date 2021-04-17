…



安装Zabbix Agent大概需要以下几个步骤。

（1）下载安装Zabbix Agent软件：

[root@ip83~]#wget -c http://downloads.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/2.0.6/zabbix-2.0.6.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fzabbix%2F%3 Fsource%3Ddlp&ts=1367916060&use_mirror=ncu

[root@ip83~]#tar zxvf zabbix-2.0.6.tar.gz

[root@ip83~]#cd zabbix-2.0.6

[root@ip83~]#./configure --prefix=/usr/local/zabbix --enable-agent

[root@ip83~]#make && make install

[root@ip83~]#cp misc/init.d/fedora/core5/zabbix_agentd /etc/init.d/

（2）配置zabbix_agentd：

[root@ip83~]#groupadd zabbix

[root@ip83~]#useradd -g zabbix zabbix

[root@ip83~]#mkdir -p /usr/local/zabbix/logs

[root@ip83~]#chown zabbix:zabbix -R /usr/local/zabbix/

[root@ip83~]#vi /usr/local/zabbix/etc/zabbix_agentd.conf

[root@ip83~]#cat /usr/local/zabbix/etc/zabbix_agentd.conf

…

PidFile=/usr/local/zabbix/logs/zabbix_agentd.pid

LogFile=/usr/local/zabbix/logs/zabbix_agentd.log

Server=192.168.7.81

ListenPort=10050

ServerActive=192.168.7.81

Hostname=zabbix_agent83

Timeout=15

Include=/usr/local/zabbix/etc/zabbix_agentd.conf.d/

…

（3）配置Zabbix Agent系统服务启动脚本：

cat /etc/init.d/zabbix_agentd

prog="Zabbix Agent"

ZABBIX_BIN="/usr/local/zabbix/sbin/zabbix_agentd"

CONF_FILE="/usr/local/zabbix/etc/zabbix_agentd.conf"

…

start() {

…

daemon $ZABBIX_BIN -c $CONF_FILE

…

}

…

（4）防火墙设置。开启防火墙端口10050：

[root@ip83~]iptables -A INPUT -p tcp -m tcp --dport 10050 -j ACCEPT

[root@ip83~]service iptables save

（5）启动zabbix_agentd：

[root@ip83~]#/etc/init.d/zabbix_agentd start

Starting Zabbix Agent: [ OK ]

（6）配置开机自动启动：

[root@ip83~]#chkconfig --add zabbix_agentd

[root@ip83~]#chkconfig --level 35 zabbix_agentd on

（7）测试Zabbix Agent。测试Zabbix Agent是否正常工作：

[root@ip83~]#/usr/local/zabbix/sbin/zabbix_agentd -c /usr/local/zabbix/etc/zabbix_agentd.conf -t system.uptime

system.uptime [u|1725087]



