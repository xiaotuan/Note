

[root@ip186 home]# nohup masterha_manager --conf=/etc/masterha/app1.cnf --remove_dead_master_conf --ignore_last_failover< /dev/null >/masterha/app1/manager.log 2>&1 &

对启动中的参数说明如下。

--remove_dead_master_conf：该参数代表当发生主从切换后，老的主库的IP将会从配置文件中移除。

--ignore_last_failover：在缺省情况下，如果MHA检测到连续发生宕机，且两次宕机时间间隔不足8小时的话，则不会进行Failover，之所以这样限制是为了避免ping-pong效应。该参数代表忽略上次 MHA 触发切换产生的文件，默认情况下， MHA 发生切换后将会在/masterha/app1下产生app1.failover.complete文件，下次再次切换的时候如果发现目录下存在该文件将不允许触发切换，除非在第一次切换后手动 rm -f /masterha/app1/app1.failover.complete，出于方便考虑，我们每次在启动MHA时会添加--ignore_last_failover参数。

查看MHA Manager监控是否正常：

[root@ip186 home]# masterha_check_status --conf=/etc/masterha/app1.cnf

app1 (pid:2960) is running(0:PING_OK), master:192.168.7.81

在默认情况下，10秒内状态会为10:INITIALIZING_MONITOR，当状态转变为0:PING_OK后表明已经开启了到master端的监控，master主机为192.168.7.81。



