

通过masterha_check_status脚本查看Manager的状态：

[root@ip186 home]# masterha_check_status --conf=/etc/masterha/app1.cnf

app1 is stopped(2:NOT_RUNNING).

注意：如果正常，会显示“PING_OK”，否则会显示“NOT_RUNNING”，这代表MHA监控没有开启。



