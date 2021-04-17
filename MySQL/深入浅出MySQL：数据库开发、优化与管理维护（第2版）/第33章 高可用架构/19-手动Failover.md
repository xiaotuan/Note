

手动failover，这种场景意味着在业务上没有启用MHA自动切换功能，当主服务器故障时，人工调用MHA来进行故障切换操作，具体命令如下：

masterha_master_switch --master_state=dead --conf=/etc/masterha/app1.cnf

--dead_master_host=192.168.7.81 --dead_master_port=3307 --new_master_host=192.168.7.83

--new_master_port=3307 --ignore_last_failover

切换过程中的部分输出信息如下：

Tue Jul 23 18:36:57 2013 - [info] Dead Servers:

Tue Jul 23 18:36:57 2013 - [info] 192.168.7.81(192.168.7.81:3307)

Tue Jul 23 18:36:57 2013 - [info] Checking master reachability via mysql(double check)..

Tue Jul 23 18:36:57 2013 - [info] ok.

Tue Jul 23 18:36:57 2013 - [info] Alive Servers:

Tue Jul 23 18:36:57 2013 - [info] 192.168.7.83(192.168.7.83:3307)

Tue Jul 23 18:36:57 2013 - [info] 192.168.7.185(192.168.7.185:3307)

Tue Jul 23 18:36:57 2013 - [info] Replicating from 192.168.7.81(192.168.7.81:3307)

Master 192.168.7.81 is dead. Proceed? (yes/NO): yes

From:

192.168.7.81 (current master)

+--192.168.7.83

+--192.168.7.185

To:

192.168.7.83 (new master)

+--192.168.7.185

Starting master switch from 192.168.7.81(192.168.7.81:3307) to 192.168.7.83(192.168.7.83:3307)? (yes/NO): yes

…

上述模拟了ip81宕机的情况下手动把ip83提升为主库的操作。



