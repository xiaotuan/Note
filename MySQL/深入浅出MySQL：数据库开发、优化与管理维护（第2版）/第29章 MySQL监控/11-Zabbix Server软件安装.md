

Zabbix Server软件安装大概需要以下几个步骤。

（1）安装LAMP环境：

[root@ip81 ~]#yum install mysql-server httpd php

（2）安装Zabbix Web所需的依赖包：

[root@ip81 ~]#yum install mysql-dev gcc net-snmp-devel curl-devel perl-DBI php-gd php-mysql php-bcmath php-mbstring php-xml

安装Fping：

[root@ip81 ~]#wget -c http://fping.org/dist/fping-3.4.tar.gz

[root@ip81 ~]#tar zxvf fping-3.4.tar.gz

[root@ip81 ~]#cd fping-3.4

[root@ip81 ~]#./configure

[root@ip81 ~]#make && make install

[root@ip81 ~]#chown root:zabbix /usr/local/sbin/fping

[root@ip81 ~]#chmod 4710 /usr/local/sbin/fping

（3）创建Zabbix运行的用户：

[root@ip81 ~]#groupadd zabbix

[root@ip81 ~]#useradd -g zabbix zabbix

（4）安装Zabbix Server：

[root@ip81~]#wget -c http://downloads.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/2.0.6/zabbix-2.0.6.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fzabbix%2F%3 Fsource%3Ddlp&ts=1367916060&use_mirror=ncu

[root@ip81 ~]#tar zxvf zabbix-2.0.6.tar.gz

[root@ip81 ~]#cd zabbix-2.0.6

[root@ip81 ~]#export MYSQL_HOME=/home/mysql/mysqlhome

[root@ip81 ~]#export C_INCLUDE_PATH=$MYSQL_HOME/include

[root@ip81 ~]#export LD_LIBRARY_PATH=$MYSQL_HOME/lib

[root@ip81~ ]#./configure --prefix=/usr/local/zabbix --enable-server --enable-agent--enable-proxy --with-mysql=/usr/bin/mysql_config --with-net-snmp --with-libcurl

[root@ip81 ~]#make && make install



