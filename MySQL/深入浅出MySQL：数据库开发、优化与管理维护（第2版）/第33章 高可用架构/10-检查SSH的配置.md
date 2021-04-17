

检查MHA Manager到所有MHA Node的SSH连接状态：

[root@ip186 home]# masterha_check_ssh --conf=/etc/masterha/app1.cnf

Fri Jul 19 18:21:09 2013 - [warning] Global configuration file /etc/masterha_default.cnf not found. Skipping.

Fri Jul 19 18:21:09 2013 - [info] Reading application default configurations from/etc/masterha/app1.cnf..

Fri Jul 19 18:21:09 2013 - [info] Reading server configurations from/etc/masterha/app1.cnf..

Fri Jul 19 18:21:09 2013 - [info] Starting SSH connection tests..

Fri Jul 19 18:21:12 2013 - [debug]

Fri Jul 19 18:21:09 2013 - [debug] Connecting via SSH from root@192.168.7.83(192.168.7.83:22) to root@192.168.7.81(192.168.7.81:22)..

Fri Jul 19 18:21:12 2013 - [debug] ok.

Fri Jul 19 18:21:12 2013 - [debug] Connecting via SSH from root@192.168.7.83(192.168.7.83:22) to root@192.168.7.185(192.168.7.185:22)..

Fri Jul 19 18:21:12 2013 - [debug] ok.

Fri Jul 19 18:21:12 2013 - [debug]

Fri Jul 19 18:21:10 2013 - [debug] Connecting via SSH from root@192.168.7.185(192.168.7. 185:22) to root@192.168.7.81(192.168.7.81:22)..

Fri Jul 19 18:21:12 2013 - [debug] ok.

Fri Jul 19 18:21:12 2013 - [debug] Connecting via SSH from root@192.168.7.185(192.168.7. 185:22) to root@192.168.7.83(192.168.7.83:22)..

Fri Jul 19 18:21:12 2013 - [debug] ok.

Fri Jul 19 18:21:13 2013 - [debug]

Fri Jul 19 18:21:09 2013 - [debug] Connecting via SSH from root@192.168.7.81(192.168.7. 81:22) to root@192.168.7.83(192.168.7.83:22)..

Fri Jul 19 18:21:11 2013 - [debug] ok.

Fri Jul 19 18:21:11 2013 - [debug] Connecting via SSH from root@192.168.7.81(192.168.7. 81:22) to root@192.168.7.185(192.168.7.185:22)..

Fri Jul 19 18:21:13 2013 - [debug] ok.

Fri Jul 19 18:21:13 2013 - [info] All SSH connection tests passed successfully.

从输出可以看出 ip83到 ip81和 ip85 ssh ok，ip85到 ip81和 ip83 ssh ok，ip81到 ip83和 ip185 ssh ok。



