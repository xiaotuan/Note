

在Linux平台下安装和在Windows平台下安装有所不同，不能用图形化的方式来安装，并且在Linux下支持RPM包、二进制包、源码包3种安装方式。下面以RPM包为例来介绍如何在Linux平台下进行MySQL的安装，其他安装方式还会在本书的第24章中详细介绍。

RPM是Redhat Package Manage的缩写。透过RPM的管理，使用者可以把Source Code包装成一种Source和Binary的档案形式，更加便于安装。MySQL的RPM包包括很多套件，一般只安装Server和Client就可以了。其中Server包是MySQL服务端套件，为用户提供核心的MySQL服务；Client包是连接MySQL服务的客户端工具，方便管理员和开发人员在服务器上进行各种管理工作。

安装RPM包的具体操作步骤如下。

（1）切换到root下（只有root才可以执行RPM包）：

[zzx@bj52 zzx]$ su

Password:

[root@bj52 zzx]#

（2）安装MySQL Server包：

[root@localhost zzx]# rpm -ivh MySQL-server-community-5.0.45-0.rhel3.i386. rpm

warning: MySQL-server-community-5.0.45-0.rhel3.i386.rpm: V3 DSA signature: NOKEY, key ID 5072e1f5

Preparing... ########################################### [100%]

1:MySQL-server-community######################################### [100%]

PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !

To do so, start the server, then issue the following commands:

/usr/bin/mysqladmin -u root password 'new-password'

/usr/bin/mysqladmin -u root -h localhost.localdomain password 'new-password'

See the manual for more instructions.

Please report any problems with the /usr/bin/mysqlbug script!

The latest information about MySQL is available on the web at

http://www.mysql.com

Support MySQL by buying support/licenses at http://shop.mysql.com

Starting MySQL[ OK ]

（3）安装MySQL Client包：

[root@localhost zzx]# rpm -ivh MySQL-client-community-5.0.45-0.rhel3.i386. rpm

warning: MySQL-client-community-5.0.45-0.rhel3.i386.rpm: V3 DSA signature: NOKEY, key ID 5072e1f5

Preparing... ######################################### [100%]

1:MySQL-client-community ######################################## [100%]

（4）最后运行MySQL：

[root@localhost zzx]# mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 2

Server version: 5.0.45-community MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>

至此，MySQL安装完毕。

**注意：**在Server安装过程中，有时候会提示缺少perl-DBI-1.40-8.i386.rpm，这时就需要先下载一个安装包，下载地址为ftp://ftp.chg.ru/pub/Linux/scientific/43/i386/SL/RPMS/perl-DBI-1.40-8.i386.rpm。



