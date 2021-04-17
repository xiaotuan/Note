

本节将模拟网络中断情况下，MHA Manager无法连接到主库，候选主也无法连接到主库，此时MHA的切换情况。

在ip81上设置防火墙，drop掉来自ip186和ip183的包，以模拟网络问题。

[root@ip81 ~]# iptables -A INPUT -s 192.168.7.186 -j DROP;iptables -A INPUT -s 192.168.7.83-j DROP

在ip186上：

[root@ip186 ~]#tail -f /masterha/app1/app1.log

Mon Jul 22 12:45:14 2013 - [info] Ping(SELECT) succeeded, waiting until MySQL doesn't respond..

Mon Jul 22 13:37:54 2013 - [warning] Got error on MySQL select ping: 2013 (Lost connection toMySQL server during query)

Mon Jul 22 13:37:54 2013 - [warning] Got timeout on MySQL Ping child process and killed it! at /usr/lib/perl5/site_perl/5.8.8/MHA/HealthCheck.pm line 381.

Mon Jul 22 13:37:54 2013 - [info] Executing seconary network check script:/usr/bin/masterha_secondary_check -s ip83 -s ip81 --user=root --master_host=ip81--master_ip=192.168.7.81 --master_port=3307 --user=root --master_host=192.168.7.81--master_ip=192.168.7.81 --master_port=3307

Mon Jul 22 13:37:54 2013 - [info] Executing SSH check script: save_binary_logs --command=test--start_pos=4 --binlog_dir=/home/binlog_3307 --output_file=/tmp/save_binary_logs_test--manager_version=0.53 --binlog_prefix=mysql-bin

Mon Jul 22 13:37:55 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (110))

Mon Jul 22 13:37:55 2013 - [warning] Connection failed 1 time(s)..

Mon Jul 22 13:37:56 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (110))

Mon Jul 22 13:37:56 2013 - [warning] Connection failed 2 time(s)..

Mon Jul 22 13:37:57 2013 - [warning] HealthCheck: Got timeout on checking SSH connection to 192.168.7.81! at /usr/lib/perl5/site_perl/5.8.8/MHA/HealthCheck.pm line 298.

Mon Jul 22 13:37:57 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (110))

Mon Jul 22 13:37:57 2013 - [warning] Connection failed 3 time(s)..

Monitoring server ip83 is reachable, Master is not reachable from ip83. OK.

ssh: connect to host ip81 port 22: Connection timed out

Monitoring server ip81 is NOT reachable!

Mon Jul 22 13:38:03 2013 - [warning] At least one of monitoring servers is not reachable from this script. This is likely network problem. Failover should not happen.

Mon Jul 22 13:38:03 2013 - [warning] Secondary network check script returned errors. Failover should not start so checking server status again. Check network settings for details.

Mon Jul 22 13:38:04 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (110))

0))

Mon Jul 22 13:38:04 2013 - [warning] Connection failed 1 time(s)..

Mon Jul 22 13:38:04 2013 - [info] Executing seconary network check script:/usr/bin/masterha_secondary_check -s ip83 -s ip81 --user=root --master_host=ip81--master_ip=192.168.7.81 --master_port=3307 --user=root --master_host=192.168.7.81--master_ip=192.168.7.81 --master_port=3307

Mon Jul 22 13:38:04 2013 - [info] Executing SSH check script: save_binary_logs --command=test--start_pos=4 --binlog_dir=/home/binlog_3307 --output_file=/tmp/save_binary_logs_test--manager_version=0.53 --binlog_prefix=mysql-bin

Mon Jul 22 13:38:05 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (110))

Mon Jul 22 13:38:05 2013 - [warning] Connection failed 2 time(s)..

Mon Jul 22 13:38:06 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (110))

Mon Jul 22 13:38:06 2013 - [warning] Connection failed 3 time(s)..

Mon Jul 22 13:38:07 2013 - [warning] HealthCheck

从上述日志输出可以看到，即便是主库ip81禁止所有来自ip186和ip83的包，切换也不会发生，只是反复地进行重试，提示监控机到ip83可以连接，ip83到ip81不可达，并且提示让你检查网络。因此在网络有问题的情况下，MHA并不会进行误切换。

查看monitor 状态：

[root@ip186 home]# masterha_check_status --conf=/etc/masterha/app1.cnf

App1 master maybe down(20:PING_FAILING). master:192.168.7.81

可以看到，这个时候monitor的状况是master maybe down(20:PING_FAILING)状态，但是MHA没有进行故障切换操作，需要DBA介入，检查是否是网络问题造成，如果是，则可以忽略；如果不是，则可以手动进行数据库切换操作。因此说，日常工作中很有必要通过 shell 脚本检测monitor状态。



