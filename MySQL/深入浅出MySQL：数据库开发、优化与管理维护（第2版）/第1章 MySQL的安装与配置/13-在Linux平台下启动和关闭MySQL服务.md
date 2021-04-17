

在Linux平台下，可以采用如下命令查看MySQL服务的状态：

[root@localhost bin]# netstat -nlp

Active Internet connections (only servers)

Proto Recv-Q Send-Q Local Address　Foreign Address　State　PID/Program name

tcp　0　0　0.0.0.0:3306　0.0.0.0:*　LISTEN　3168/mysqld

tcp　0　0:::9922　:::*　LISTEN　1864/sshd

Active UNIX domain sockets (only servers)

Proto RefCnt Flags　Type　State　I-Node　PID/Program name Path

unix 2　[ ACC ] STREAM LISTENING 16537243 3168/mysqld　/var/lib/mysql/ mysql.sock

unix 2　[ ACC ] STREAM LISTENING 4875　1915/xfs　/tmp/.font-unix/fs7100

其中3306端口是MySQL服务器监听端口。

与在Windows平台上类似，在Linux平台上启动和关闭MySQL也有两种方法，一种是通过命令行方式启动和关闭，另一种是通过服务的方式启动和关闭（适用于RPM包安装方式）。下面将分别对这两种方法进行介绍。

**1．命令行方式**

在命令行方式下，启动和关闭MySQL服务命令如下所示。

（1）启动服务：

[root@localhost bin]# cd /usr/bin

[root@localhost bin]# ./mysqld_safe &

[1] 23013

[root@localhost bin]# Starting mysqld daemon with databases from /var/lib/mysql

（2）关闭服务：

[root@localhost bin]# mysqladmin -uroot shutdown

STOPPING server from pid file /var/lib/mysql/localhost.localdomain.pid

070820 04:36:30 mysqld ended

[1]+ Done　./mysqld_safe

**2．服务的方式**

如果MySQL是用RPM包安装的，则启动和关闭MySQL服务过程如下所示。

（1）启动服务：

[root@localhost zzx]# service mysql start

Starting MySQL[ OK ]

如果在启动状态，需要重启服务，可以用以下命令直接重启，而不需要先关闭再启动：

[root@localhost mysql]# service mysql restart

Shutting down MySQL..[ OK ]

Starting MySQL[ O K ]

（2）关闭服务：

[root@localhost bin]# service mysql stop

Shutting down MySQL.STOPPING server from pid file /var/lib/mysql/localhost. localdomain.pid

070727 06:30:31 mysqld ended

[ OK ]

[1]+ Done　mysqld_safe

**注意：**在命令行启动MySQL时，如果不加“--console”，启动关闭信息将不会在界面中显示，而是记录在安装目录下的 data 目录里面，文件名字一般是 hostname.err，可以通过此文件查看MySQL的控制台信息。



