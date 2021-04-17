

通常情况自动切换后，原 master 可能已经废弃掉，待原 master 主机修复后，如果数据完整的情况下，可能想把原 master 重新作为新主库的 slave，这时我们就需要借助当时自动切换时刻的MHA日志来完成对原master的修复。下面是提取相关日志的命令：

grep -i "All other slaves should start replication from" /masterha/app1/app1.log

Mon Jul 22 14:08:42 2013 - [info] All other slaves should start replication from here. Statement should be: CHANGE MASTER TO MASTER_HOST='192.168.7.83', MASTER_PORT=3307, MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=407, MASTER_USER='repl', MASTER_PASSWORD='xxx';

获取上述信息后，就可以直接在修复后的master上执行 change master to操作了。



