

mysqlhotcopy是一个Perl脚本，它使用 lock tables、flush tables、cp或 scp来快速备份数据库。它是备份数据库或单个表的最快途径，其缺点是mysqlhotcopy只用于备份MyISAM，而且它需要运行在Linux/UNIX环境中。

需要注意的是，mysqlhotcopy是Perl脚本，因此需要安装Perl的MySQL数据库接口包，我们可以从Linux的官方FTP（ftp.redhat.com）上下载它，以笔者的测试环境（Linux AS4，INTEL 32 位处理器）为例，从目录/pub/redhat/linux/enterprise/4/en/os/i386/SRPMS 中下载包perl-DBD-MySQL-2.9004-3.1.src.rpm。而此包的安装又依赖于 MySQL 的开发包，因此还需要下载 MySQL 相应版本的开发包，笔者测试环境中下载的包名为 MySQL-devel- community-5.0.41-0.rhel4.i386.rpm。后者的安装过程和普通 RPM 一样，这里不再赘述，而前者从 FTP 站点下载的是源码包，需要重新编译后才可以安装。编译的过程简单描述如下。

（1）在操作系统上su到root用户。

（2）执行如下命令，生成.spec文件。

[root@localhost～]# rpm -i perl-DBD-MySQL-2.9004-3.1.src.rpm

warning: perl-DBD-MySQL-2.9004-3.1.src.rpm: V3 DSA signature: NOKEY, key ID db42a60e

（3）此时进入 cd /usr/src/redhat/SPECS，可以看到 perl-DBD-MySQL.spec。

[root@localhost～]# cd /usr/src/redhat/SPECS

[root@localhost SPECS]# ls -l

total 32

-rw-rw-r-- 1 root root 3703 Nov 27 2004 perl-DBD-MySQL.spec

-rw-rw-r-- 1 root root 4369 Jun 15 2004 perl-DBI.spec

-rw-rw-r-- 1 root root 7683 May 28 2003 telnet.spec

（4）执行如下命令，将.spec文件编译为RPM安装文件。

[root@localhost SPECS]# rpmbuild -bb perl-DBD-MySQL.spec

Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.905

…（省略中间日志）

+ cd /usr/src/redhat/BUILD

+ cd DBD-mysql-2.9004

+ rm -rf /var/tmp/perl-DBD-MySQL-2.9004-root

+ exit 0

（5）进入RPM最后的放置目录，一般为/usr/src/redhat/RPMS/i386。

[root@localhost SPECS]# cd /usr/src/redhat/RPMS/i386

[root@localhost i386]# ls -ltr

total 2068

-rw-r--r-- 1 root root 29385 Mar 17 2006 telnet-server-0.17-26.i386.rpm

-rw-r--r-- 1 root root 171509 Mar 17 2006 telnet-debuginfo-0.17-26.i386.rpm-rw-r--r-- 1 root root 46858 Mar 17 2006 telnet-0.17-26.i386.rpm

-rw-r--r-- 1 root root 974749 Dec 29 15:42 perl-DBD-MySQL-2.9004- 3.1.i386. rpm

-rw-r--r-- 1 root root 855503 Dec 29 15:42 perl-DBD-MySQL-debuginfo- 2.9004- 3.1.i386.rpm

（6）安装生成的.rpm包。

rpm ivh perl-DBD-MySQL-2.9004-3.1.i386.rpm

至此，源码包安装完毕。

mysqlhotcopy的用法如下：

shell> mysqlhotcopy db_name [/path/to/new_directory]

shell> mysqlhotcopy db_name_1 . . db_name_n

/path/to/new_directory

以下例子将mysql数据库备份到当前目录下的backup中：

[root@localhost mysql]# mysqlhotcopy -u root mysql ./backup/

Existing hotcopy directory renamed to './backup//mysql_old'

Locked 18 tables in 0 seconds.

Flushed tables ('mysql'.'columns_priv', 'mysql'.'db', 'mysql'.'func', 'mysql'. 'help_category', 'mysql'.'help_keyword', 'mysql'.'help_relation', 'mysql'.'help_ topic', 'mysql'.'host', 'mysql'.'proc', 'mysql'.'procs_priv', 'mysql'.'t1', 'mysql'.'tables_priv','mysql'.'time_zone', 'mysql'.'time_zone_leap_second', 'mysql'.'time_zone_name', 'mysql'. 'time_zone_transition', 'mysql'.'time_ zone_ transition_type', 'mysql'.'user') in 0 seconds.

Copying 54 files...

Copying indices for 0 files...

Unlocked tables.

mysqlhotcopy copied 18 tables (54 files) in 0 seconds (0 seconds overall).

mysqlhotcopy的常用选项如下。

--allowold：如果备份路径下含有同名备份，则将旧的备份目录 rename 为“目录名_old”。

--addtodest：如果备份路径下存在同名目录，则仅仅将新的文件加入目录。

--noindices：不备份所有的索引文件。

--flushlog：表被锁定后刷新日志。

这些选项的含义都很简单，读者可以自行测试，这里就不再举例。更多的选项，可以使用mysqlhotcopy –help命令或者 perldoc /usr/bin/mysqlhotcopy命令进行查询。



