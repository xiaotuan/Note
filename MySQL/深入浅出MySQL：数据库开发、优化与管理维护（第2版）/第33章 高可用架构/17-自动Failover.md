

先来看一下自动failover，本节测试环境如表33-6所示。

表33-6 测试环境信息



![figure_0643_0251.jpg](../images/figure_0643_0251.jpg)
自动failover模拟测试的操作步骤如下。

（1）sysbench生成测试数据。

在ip81上进行sysbench数据生成，在sbtest库下生成sbtest表，共100万数据。

[root@ip81 tools]# sysbench --test=oltp --oltp-table-size=1000000 --oltp-read-only=off--init-rng=on --num-threads=16 --max-requests=0 --oltp-dist-type=uniform --max-time=1800--mysql-user=root --db-driver=mysql --mysql-table-engine=innodb --oltp-test-mode=complex prepare

（2）停掉 slave sql线程，模拟主从延时。

在ip83上停掉slave的io线程，以模拟日志不一致。

mysql> stop slave io_thread;

Query OK, 0 rows affected (0.00 sec)

ip185继续传输日志。

（3）模拟sysbench压力测试。

在ip81上进行sysbench测试，运行3分钟，产生大量的binlog。

[root@ip81 tools]# sysbench --test=oltp --oltp-table-size=1000000 --oltp-read-only=off--init-rng=on --num-threads=16 --max-requests=0 --oltp-dist-type=uniform --max-time=180 --mysql-user=root --db-driver=mysql --mysql-table-engine=innodb --oltp-test-mode=complex run

sysbench 0.4.10: multi-threaded system evaluation benchmark

WARNING: Preparing of "BEGIN" is unsupported, using emulation

(last message repeated 15 times)

Running the test with following options:

Number of threads: 16

Initializing random number generator from timer.

Doing OLTP test.

Running mixed OLTP test

Using Uniform distribution

Using "BEGIN" for starting transactions

Using auto_inc on the id column

Threads started!

Time limit exceeded, exiting...

(last message repeated 15 times)

Done.

OLTP test statistics:

queries performed:

read: 788284

write:281530

other:112612

total:1182426

transactions: 56306 (312.71 per sec.)

deadlocks:0 (0.00 per sec.)

read/write requests: 1069814 (5941.48 per sec.)

other operations: 112612 (625.42 per sec.)

Test execution summary:

total time: 180.0584s

total number of events: 56306

total time taken by event execution: 2879.1054

per-request statistics:

min:5.63ms

avg:51.13ms

max:317.74ms

approx. 95 percentile:76.16ms

Threads fairness:

events (avg/stddev):3519.1250/17.86

execution time (avg/stddev): 179.9441/0.02

（4）开启 slave的 io线程，追赶落后于master的 binlog。在 ip83上开启 slave io线程：

mysql> start slave io_thread;

Query OK, 0 rows affected (0.00 sec)

（5）杀掉主库mysql进程，模拟主库发生故障，进行自动failover操作，在ip81数据库上：

[root@ip81 ~]# ps axu|grep mysql_3307|awk‘{print $2}’|xargs kill -9

（6）查看MHA切换日志，了解整个切换过程。在ip186上查看MHA切换日志：

Mon Jul 22 14:08:27 2013 - [warning] Connection failed 1 time(s)..

Mon Jul 22 14:08:28 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (111))

Mon Jul 22 14:08:28 2013 - [warning] Connection failed 2 time(s)..

Mon Jul 22 14:08:28 2013 - [info] HealthCheck: SSH to 192.168.7.81 is reachable.

Monitoring server ip81 is reachable, Master is not reachable from ip81. OK.

Mon Jul 22 14:08:28 2013 - [info] Master is not reachable from all other monitoring servers. Failover should start.

Mon Jul 22 14:08:29 2013 - [warning] Got error on MySQL connect: 2003 (Can't connect to MySQL server on '192.168.7.81' (111))

Mon Jul 22 14:08:29 2013 - [warning] Connection failed 3 time(s)..

Mon Jul 22 14:08:29 2013 - [warning] Master is not reachable from health checker!

Mon Jul 22 14:08:29 2013 - [warning] Master 192.168.7.81(192.168.7.81:3307) is not reachable!

Mon Jul 22 14:08:29 2013 - [warning] SSH is reachable.

Mon Jul 22 14:08:29 2013 - [info] Connecting to a master server failed. Reading configuration file /etc/masterha_default.cnf and /etc/masterha/app1.cnf again, and trying to connect to all servers to check server status..

Mon Jul 22 14:08:29 2013 - [warning] Global configuration file /etc/masterha_default.cnf not found. Skipping.

Mon Jul 22 14:08:29 2013 - [info] Reading application default configurations from/etc/masterha/app1.cnf..

Mon Jul 22 14:08:29 2013 - [info] Reading server configurations from/etc/masterha/app1.cnf..

Mon Jul 22 14:08:29 2013 - [info] Dead Servers:

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:29 2013 - [info] Alive Servers:

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.83(192.168.7.83:3307)

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.185(192.168.7.185:3307)

Mon Jul 22 14:08:29 2013 - [info] Alive Slaves:

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.83(192.168.7.83:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:29 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:29 2013 - [info] Primary candidate for the new Master (candidate_master is set)

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.185(192.168.7.185:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:29 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:29 2013 - [info] Checking slave configurations..

Mon Jul 22 14:08:29 2013 - [info] Checking replication filtering settings..

Mon Jul 22 14:08:29 2013 - [info] Replication filtering check ok.

Mon Jul 22 14:08:29 2013 - [info] Master is down!

Mon Jul 22 14:08:29 2013 - [info] Terminating monitoring script.

Mon Jul 22 14:08:29 2013 - [info] Got exit code 20 (Master dead).

Mon Jul 22 14:08:29 2013 - [info] MHA::MasterFailover version 0.53.

Mon Jul 22 14:08:29 2013 - [info] Starting master failover.

Mon Jul 22 14:08:29 2013 - [info]

Mon Jul 22 14:08:29 2013 - [info] * Phase 1: Configuration Check Phase..

Mon Jul 22 14:08:29 2013 - [info]

Mon Jul 22 14:08:29 2013 - [info] Dead Servers:

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:29 2013 - [info] Checking master reachability via mysql(double check)..

Mon Jul 22 14:08:29 2013 - [info] ok.

Mon Jul 22 14:08:29 2013 - [info] Alive Servers:

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.83(192.168.7.83:3307)

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.185(192.168.7.185:3307)

Mon Jul 22 14:08:29 2013 - [info] Alive Slaves:

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.83(192.168.7.83:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:29 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:29 2013 - [info] Primary candidate for the new Master (candidate_master is set)

Mon Jul 22 14:08:29 2013 - [info] 192.168.7.185(192.168.7.185:3307)Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:29 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:29 2013 - [info] ** Phase 1: Configuration Check Phase completed.

Mon Jul 22 14:08:29 2013 - [info]

Mon Jul 22 14:08:29 2013 - [info] * Phase 2: Dead Master Shutdown Phase..

Mon Jul 22 14:08:29 2013 - [info]

Mon Jul 22 14:08:29 2013 - [info] Forcing shutdown so that applications never connect to the current master..

Mon Jul 22 14:08:29 2013 - [info] Executing master IP deactivatation script:

Mon Jul 22 14:08:29 2013 - [info] /usr/local/bin/master_ip_failover_3307--orig_master_host=192.168.7.81 --orig_master_ip=192.168.7.81 --orig_master_port=3307--command=stopssh --ssh_user=root

Disabling the VIP on old master: 192.168.7.81

Mon Jul 22 14:08:32 2013 - [info] done.

Mon Jul 22 14:08:32 2013 - [warning] shutdown_script is not set. Skipping explicit shutting down of the dead master.

Mon Jul 22 14:08:32 2013 - [info] * Phase 2: Dead Master Shutdown Phase completed.

Mon Jul 22 14:08:32 2013 - [info]

Mon Jul 22 14:08:32 2013 - [info] * Phase 3: Master Recovery Phase..

Mon Jul 22 14:08:32 2013 - [info]

Mon Jul 22 14:08:32 2013 - [info] * Phase 3.1: Getting Latest Slaves Phase..

Mon Jul 22 14:08:32 2013 - [info]

Mon Jul 22 14:08:32 2013 - [info] The latest binary log file/position on all slaves is mysql-bin.000037:107

Mon Jul 22 14:08:32 2013 - [info] Latest slaves (Slaves that received relay log files to the latest):

Mon Jul 22 14:08:32 2013 - [info] 192.168.7.83(192.168.7.83:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:32 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:32 2013 - [info] Primary candidate for the new Master (candidate_master is set)

Mon Jul 22 14:08:32 2013 - [info] 192.168.7.185(192.168.7.185:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:32 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:32 2013 - [info] The oldest binary log file/position on all slaves ismysql-bin.000037:107

Mon Jul 22 14:08:32 2013 - [info] Oldest slaves:

Mon Jul 22 14:08:32 2013 - [info] 192.168.7.83(192.168.7.83:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:32 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:32 2013 - [info] Primary candidate for the new Master (candidate_masteris set)

Mon Jul 22 14:08:32 2013 - [info] 192.168.7.185(192.168.7.185:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:32 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:32 2013 - [info]

Mon Jul 22 14:08:32 2013 - [info] * Phase 3.2: Saving Dead Master's Binlog Phase..

Mon Jul 22 14:08:32 2013 - [info]

Mon Jul 22 14:08:34 2013 - [info] Fetching dead master's binary logs..

Mon Jul 22 14:08:34 2013 - [info] Executing command on the dead master

192.168.7.81(192.168.7.81:3307): save_binary_logs --command=save

--start_file=mysql-bin.000037 --start_pos=107 --binlog_dir=/home/binlog_3307

--output_file=/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog

--handle_raw_binlog=1 --disable_log_bin=0 --manager_version=0.53

Creating /tmp if not exists.. ok.

Concat binary/relay logs from mysql-bin.000037 pos 107 to mysql-bin.000037 EOF into/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog ..

Dumping binlog format description event, from position 0 to 107.. ok.

Dumping effective binlog data from /home/binlog_3307/mysql-bin.000037 position 107 to tail(126).. ok.

Concat succeeded.

Mon Jul 22 14:08:40 2013 - [info] scp from root@192.168.7.81:/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog to local:/masterha/app1/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog

succeeded.

Mon Jul 22 14:08:40 2013 - [info] HealthCheck: SSH to 192.168.7.83 is reachable.

Mon Jul 22 14:08:41 2013 - [info] HealthCheck: SSH to 192.168.7.185 is reachable.

Mon Jul 22 14:08:41 2013 - [info]

Mon Jul 22 14:08:41 2013 - [info] * Phase 3.3: Determining New Master Phase..

Mon Jul 22 14:08:41 2013 - [info]

Mon Jul 22 14:08:41 2013 - [info] Finding the latest slave that has all relay logs for recovering other slaves..

Mon Jul 22 14:08:41 2013 - [info] All slaves received relay logs to the same position. No need to resync each other.

Mon Jul 22 14:08:41 2013 - [info] Searching new master from slaves..

Mon Jul 22 14:08:41 2013 - [info] Candidate masters from the configuration file:

Mon Jul 22 14:08:41 2013 - [info] 192.168.7.83(192.168.7.83:3307) Version=5.5.28-rel29.1-log (oldest major version between slaves) log-bin:enabled

Mon Jul 22 14:08:41 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Mon Jul 22 14:08:41 2013 - [info] Primary candidate for the new Master (candidate_master is set)

Mon Jul 22 14:08:41 2013 - [info] Non-candidate masters:

Mon Jul 22 14:08:41 2013 - [info] Searching from candidate_master slaves which have received the latest relay log events..

Mon Jul 22 14:08:41 2013 - [info] New master is 192.168.7.83(192.168.7.83:3307)

Mon Jul 22 14:08:41 2013 - [info] Starting master failover..

Mon Jul 22 14:08:41 2013 - [info]

From:

192.168.7.81 (current master)

+--192.168.7.83

+--192.168.7.185

To:

192.168.7.83 (new master)

+--192.168.7.185

Mon Jul 22 14:08:41 2013 - [info]

Mon Jul 22 14:08:41 2013 - [info] * Phase 3.3: New Master Diff Log Generation Phase..

Mon Jul 22 14:08:41 2013 - [info]

Mon Jul 22 14:08:41 2013 - [info] This server has all relay logs. No need to generate diff files from the latest slave.

Mon Jul 22 14:08:41 2013 - [info] Sending binlog..

Mon Jul 22 14:08:41 2013 - [info] scp from local:/masterha/app1/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog to root@192.168.7.83:/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlogsucceeded.

Mon Jul 22 14:08:41 2013 - [info]

Mon Jul 22 14:08:41 2013 - [info] * Phase 3.4: Master Log Apply Phase..

Mon Jul 22 14:08:41 2013 - [info]

Mon Jul 22 14:08:41 2013 - [info] *NOTICE: If any error happens from this phase, manual recovery is needed.

Mon Jul 22 14:08:41 2013 - [info] Starting recovery on 192.168.7.83(192.168.7.83:3307)..

Mon Jul 22 14:08:41 2013 - [info] Generating diffs succeeded.

Mon Jul 22 14:08:41 2013 - [info] Waiting until all relay logs are applied.

Mon Jul 22 14:08:41 2013 - [info] done.

Mon Jul 22 14:08:41 2013 - [info] Getting slave status..

Mon Jul 22 14:08:41 2013 - [info] This slave(192.168.7.83)'s Exec_Master_Log_Pos equals to Read_Master_Log_Pos(mysql-bin.000037:107). No need to recover from Exec_Master_Log_Pos.

Mon Jul 22 14:08:41 2013 - [info] Connecting to the target slave host 192.168.7.83, running recover script..

Mon Jul 22 14:08:41 2013 - [info] Executing command: apply_diff_relay_logs --command=apply--slave_user=root --slave_host=192.168.7.83 --slave_ip=192.168.7.83 --slave_port=3307--apply_files=/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog

--workdir=/tmp --target_version=5.5.28-rel29.1-log --timestamp=20130722140829--handle_raw_binlog=1 --disable_log_bin=0 --manager_version=0.53 --slave_pass=xxx

Mon Jul 22 14:08:42 2013 - [info]

Applyingdifferential binary/relay log files

/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog on 192.168.7.83:3307.

This may take long time...

Applying log files succeeded.

Mon Jul 22 14:08:42 2013 - [info] All relay logs were successfully applied.

Mon Jul 22 14:08:42 2013 - [info] Getting new master's binlog name and position..

Mon Jul 22 14:08:42 2013 - [info] mysql-bin.000001:407

Mon Jul 22 14:08:42 2013 - [info] All other slaves should start replication from here. Statement should be: CHANGE MASTER TO MASTER_HOST='192.168.7.83', MASTER_PORT=3307, MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=407, MASTER_USER='repl', MASTER_PASSWORD='xxx';

Mon Jul 22 14:08:42 2013 - [info] Executing master IP activate script:

Mon Jul 22 14:08:42 2013 - [info] /usr/local/bin/master_ip_failover_3307 --command=start--ssh_user=root --orig_master_host=192.168.7.81 --orig_master_ip=192.168.7.81--orig_master_port=3307 --new_master_host=192.168.7.83 --new_master_ip=192.168.7.83--new_master_port=3307

IN SCRIPT TEST====/sbin/ifconfig eth0:2 down==/sbin/ifconfig eth0:2 192.168.7.201/23===

Enabling the VIP - 192.168.7.201/23 on the new master - 192.168.7.83

Mon Jul 22 14:08:42 2013 - [info] OK.

Mon Jul 22 14:08:42 2013 - [info] Setting read_only=0 on 192.168.7.83(192.168.7.83:3307)..

Mon Jul 22 14:08:42 2013 - [info] ok.

Mon Jul 22 14:08:42 2013 - [info] ** Finished master recovery successfully.

Mon Jul 22 14:08:42 2013 - [info] * Phase 3: Master Recovery Phase completed.

Mon Jul 22 14:08:42 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] * Phase 4: Slaves Recovery Phase..

Mon Jul 22 14:08:42 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] * Phase 4.1: Starting Parallel Slave Diff Log Generation Phase..

Mon Jul 22 14:08:42 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] -- Slave diff file generation on host 192.168.7.185(192.168.7.185:3307) started, pid: 27521. Check tmp log/masterha/app1/192.168.7.185_3307_20130722140829.log if it takes time..

Mon Jul 22 14:08:42 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] Log messages from 192.168.7.185 ...

Mon Jul 22 14:08:42 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] This server has all relay logs. No need to generate diff files from the latest slave.

Mon Jul 22 14:08:42 2013 - [info] End of log messages from 192.168.7.185.

Mon Jul 22 14:08:42 2013 - [info] -- 192.168.7.185(192.168.7.185:3307) has the latest relay log events.

Mon Jul 22 14:08:42 2013 - [info] Generating relay diff files from the latest slave succeeded.

Mon Jul 22 14:08:42 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] * Phase 4.2: Starting Parallel Slave Log Apply Phase..

Mon Jul 22 14:08:42 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] -- Slave recovery on host 192.168.7.185(192.168.7.185:3307) started, pid: 27523. Check tmp log /masterha/app1/192.168.7.185_3307_20130722140829.log if it takes time..

Mon Jul 22 14:08:43 2013 - [info]

Mon Jul 22 14:08:43 2013 - [info] Log messages from 192.168.7.185 ...

Mon Jul 22 14:08:43 2013 - [info]

Mon Jul 22 14:08:42 2013 - [info] Sending binlog..

Mon Jul 22 14:08:42 2013 - [info] scp from local:/masterha/app1/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog to root@192.168.7.185:/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog succeeded.

Mon Jul 22 14:08:42 2013 - [info] Starting recovery on 192.168.7.185(192.168.7.185:3307)..

Mon Jul 22 14:08:42 2013 - [info] Generating diffs succeeded.

Mon Jul 22 14:08:42 2013 - [info] Waiting until all relay logs are applied.

Mon Jul 22 14:08:42 2013 - [info] done.

Mon Jul 22 14:08:42 2013 - [info] Getting slave status..

Mon Jul 22 14:08:42 2013 - [info] This slave(192.168.7.185)'s Exec_Master_Log_Pos equals to Read_Master_Log_Pos(mysql-bin.000037:107). No need to recover from Exec_Master_Log_Pos.

Mon Jul 22 14:08:42 2013 - [info] Connecting to the target slave host 192.168.7.185, running recover script..

Mon Jul 22 14:08:42 2013 - [info] Executing command: apply_diff_relay_logs --command=apply--slave_user=root --slave_host=192.168.7.185 --slave_ip=192.168.7.185 --slave_port=3307--apply_files=/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog

--workdir=/tmp --target_version=5.5.28-rel29.1-log --timestamp=20130722140829--handle_raw_binlog=1 --disable_log_bin=0 --manager_version=0.53 --slave_pass=xxx

Mon Jul 22 14:08:43 2013 - [info]

Applying differential binary/relay log files/tmp/saved_master_binlog_from_192.168.7.81_3307_20130722140829.binlog on 192.168.7.185:3307. This may take long time...

Applying log files succeeded.

Mon Jul 22 14:08:43 2013 - [info] All relay logs were successfully applied.

Mon Jul 22 14:08:43 2013 - [info] Resetting slave 192.168.7.185(192.168.7.185:3307) and starting replication from the new master 192.168.7.83(192.168.7.83:3307)..

Mon Jul 22 14:08:43 2013 - [info] Executed CHANGE MASTER.

Mon Jul 22 14:08:43 2013 - [info] Slave started.

Mon Jul 22 14:08:43 2013 - [info] End of log messages from 192.168.7.185.

Mon Jul 22 14:08:43 2013 - [info] -- Slave recovery on host 192.168.7.185(192.168.7.185:3307) succeeded.

Mon Jul 22 14:08:43 2013 - [info] All new slave servers recovered successfully.

Mon Jul 22 14:08:43 2013 - [info]

Mon Jul 22 14:08:43 2013 - [info] * Phase 5: New master cleanup phease..

Mon Jul 22 14:08:43 2013 - [info]

Mon Jul 22 14:08:43 2013 - [info] Resetting slave info on the new master..

Mon Jul 22 14:08:43 2013 - [info] 192.168.7.83: Resetting slave info succeeded.

Mon Jul 22 14:08:43 2013 - [info] Master failover to 192.168.7.83(192.168.7.83:3307) completed successfully.

Mon Jul 22 14:08:43 2013 - [info] Deleted server1 entry from /etc/masterha/app1.cnf .

Mon Jul 22 14:08:43 2013 - [info]

----- Failover Report -----

app2: MySQL Master failover 192.168.7.81 to 192.168.7.83 succeeded

Master 192.168.7.81 is down!

Check MHA Manager logs at ip186:/masterha/app1/app1.log for details.

Started automated(non-interactive) failover.

Invalidated master IP address on 192.168.7.81.

The latest slave 192.168.7.83(192.168.7.83:3307) has all relay logs for recovery.

Selected 192.168.7.83 as a new master.

192.168.7.83: OK: Applying all logs succeeded.

192.168.7.83: OK: Activated master IP address.

192.168.7.185: This host has the latest relay log events.

Generating relay diff files from the latest slave succeeded.

192.168.7.185: OK: Applying all logs succeeded. Slave started, replicating from 192.168.7.83.

192.168.7.83: Resetting slave info succeeded.

Master failover to 192.168.7.83(192.168.7.83:3307) completed successfully.

Mon Jul 22 14:08:43 2013 - [info] Sending mail..

从上面的输出可以看出整个MHA的切换过程，共包括以下几个步骤：

配置文件检查阶段，这个阶段将会检查整个集群配置文件设置；

宕机的master 处理，这个阶段包括虚拟IP摘除操作，主机关机等操作；

复制 dead master和最新 slave相差的 relay log，并保存到MHA Manager具体目录下；

识别含有最新更新的slave；

应用差异的中继日志（relay log）到其他 slave；

应用从master保存的二进制日志事件（binlog events）；

提升一个slave为新master；

使其他的slave连接新的master进行复制。

（7）切换过程中，查看monitor状况。

masterha_check_status --conf=/etc/masterha/app1.cnf

app1 master is down and failover is running(50:FAILOVER_RUNNING). master:192.168.7.81

可以看出这个时候monitor中已经FAILOVER_RUNNING，说明主库数据库已经宕掉。



