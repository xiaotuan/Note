

配置MHA的大体步骤如下。

（1）创建MHA工作目录，并且创建相关配置文件：

mkdir -p /etc/masterha/

vi /etc/masterha/app1.cnf

[server default]

manager_log=/masterha/app1/app1.log //设置manager的日志

manager_workdir=/masterha/app1 //设置manager的工作日志

master_binlog_dir=/home/binlog //设置master默认保存binlog的位置，以便MHA可以找到master的日志

master_ip_failover_script=/usr/local/bin/master_ip_failover //设置自动 failover时候的切换脚本。

master_ip_online_change_script=/usr/local/bin/master_ip_online_change //设置手动切换时候的切换脚本。

password=123456//设置mysql中root用户的密码

ping_interval=1 //设置监控主库，发送ping包的时间间隔，默认的是每隔3秒，尝试三次没有回应的时候进行自动failover

remote_workdir=/tmp //设置远端mysql在发生切换时保存binlog的具体位置

repl_password=123456 //设置复制用户的密码

repl_user=repl //设置复制环境中的复制用户名

report_script=/usr/local/bin/send_report //设置发生切换后发送报警的脚本

secondary_check_script=/usr/bin/masterha_secondary_check -s ip83 -s ip81 --user=root--master_host=ip81 --master_ip=192.168.7.81 --master_port=3306 //一旦MHA到ip81的监控之间网络出现问题，MHA Manager将会尝试从ip83登录到ip81

shutdown_script="" // 设置故障发生后关闭故障主机脚本（该脚本主要作用是关闭主机防止发生脑裂）

ssh_user=root //设置ssh的登录用户名

user=root //设置监控用户root

[server1]

hostname=192.168.7.81

port=3307

[server2]

hostname=192.168.7.83

port=3307

candidate_master=1 //设置为候选 master,如果设置该参数后，发生主从切换后将会将此从库提升为主，即使这个库不是集群中最新的slave

check_repl_delay=0 //默认情况下如果一个slave落后master 100M的relay logs的话， MHA 将不会选择该 slave 作为一个新的 master ，因为对于这个 slave 的恢复需要花费很长时间，通过设置check_repl_delay=0 ， MHA 触发切换在选择一个新的 master 的时候将会忽略复制延时，这个参数对于你设置candidate_master=1的主机非常有用，因为它保证了这个候选主在切换过程中一定是新的master

[server3]

hostname=192.168.7.185

port=3307

（2）设置 relay log清除方式（在每个 slave上）：

Mysql>mysql -e "set global relay_log_purge=0; "

MHA在发生切换过程中，从库的恢复过程中依赖于 relay log的相关信息，所以这里我们要将 relay log的自动清除设置为OFF，采用手动清除 relay log的方式。

在默认情况下，从服务器上的中继日志会在SQL线程执行完后被自动删除。但是在MHA环境中，这些中继日志在恢复其他从服务器时可能会被用到，因此需要禁用中继日志的自动清除和定期清除 SQL 线程应用完的中继日志。定期清除中继日志需要考虑到复制延时的问题。在ext3文件系统下，删除大的文件需要一定的时间，会导致严重的复制延时。为了避免复制延时，需要暂时为中继日志创建硬链接，因为在Linux系统中通过硬链接删除大文件速度会很快。

**提示：**在MySQL数据库中删除大表时，通常也采用建立硬链接的方式。

MHA节点中包含了pure_relay_logs命令工具，它可以为中继日志创建硬链接，执行SET GLOBAL relay_log_purge=1，等待几秒钟以便 SQL 线程切换到新的中继日志，再执行 SET GLOBAL relay_log_purge=0。

pure_relay_logs脚本参数如下所示：

--user mysql用户名

--password mysql密码

--host mysql服务器地址

--port 端口号

--workdir指定创建 relay log的硬链接的位置，默认的是/var/tmp,由于系统不通分区创建硬链接文件会失败，故需要执行硬链接具体位置，成功执行脚本后，硬链接的中继日志文件将被删除

--disable_relay_log_purge 默认情况下，如果relay_log_purge=1的情况下，脚本会什么都不处理，自动退出。通过设定这个参数，当relay_log_purge=1的情况下将会将relay_log_purge设置为0.清理relay log,清理之后，最后将参数设置为OFF

（3）设置定期清理relay脚本。

使用如下命令设置 crontab来定期清理Relay Log：

vi /etc/cron.d/purge_relay_logs

0 4 * * * /usr/bin/purge_relay_logs --user=root --password=123456 -disable_relay_log_purge--port=3307 --workdir=/home/mysql_3307/mysqlhome/ -disable_relay_log_purge>>/usr/local/masterha/log/purge_relay_logs.log 2>&1

purge_relay_logs脚本删除中继日志不会阻塞SQL线程。因此在每台从服务器上设置计划任务定期清除中继日志。最好在每台从服务器上不同时间点执行计划任务。

下面列出了脚本清理过程：

[root@ip83 ~]#/usr/bin/purge_relay_logs --user=root -disable_relay_log_purge --port=3307

--workdir=/home/mysql_3307/mysqlhome/

2013-07-23 19:42:42: purge_relay_logs script started.

Found relay_log.info: /home/mysql_3307/mysqlhome/data/relay-log.info

Removing hard linked relay log files ip185-relay-bin* under /home/mysql_3307/mysqlhome.. done.

Current relay log file: /home/mysql_3307/mysqlhome/data/ip185-relay-bin.000005

Archiving unused relay log files (up to

/home/mysql_3307/mysqlhome/data/ip185-relay-bin.000004) ...

Creating hard link for /home/mysql_3307/mysqlhome/data/ip185-relay-bin.000004 under/home/mysql_3307/mysqlhome/ip185-relay-bin.000004 .. ok.

Creating hard links for unused relay log files completed.

Executing SET GLOBAL relay_log_purge=1; FLUSH LOGS; sleeping a few seconds so that SQL thread can delete older relay log files (if it keeps up); SET GLOBAL relay_log_purge=0; .. ok.

Removing hard linked relay log files ip185-relay-bin* under /home/mysql_3307/mysqlhome.. done. 2013-07-23 19:42:45: All relay log purging operations succeeded.

（4）设置 mysqlbinlog（在每个slave上），编辑 ～/.bashr或者/etc/bashrc文件，在文件的末尾处添加以下内容：

PATH="$PATH:/home/mysql/mysqlhome/bin"

export PATH

MHA 在切换过程中会直接调用 mysqlbinlog 命令，故需要在环境变量中指定 mysqlbinlog的具体路径。



