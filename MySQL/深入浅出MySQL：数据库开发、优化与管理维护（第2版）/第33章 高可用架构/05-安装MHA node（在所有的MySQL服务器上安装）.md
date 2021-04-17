

（1）在MySQL服务器上安装MHA node所需的 perl模块（DBD::mysql）。

本环境为CentOS部署MHA，需要在所有MHA node上安装Perl模块（DBD::mysql）。安装脚本（install.sh）如下：

install.sh

#!/bin/bash

wget http://xrl.us/cpanm --no-check-certificate

mv cpanm /usr/bin/

chmod 755 /usr/bin/cpanm

cat >/root/list<<EOF

install DBD::mysql

EOF

for package in `cat /root/list`

do

cpanm $package

done

（2）在所有的节点上安装mha node：

wget http://mysql-master-ha.googlecode.com/files/mha4mysql-node-0.53.tar.gz

tar xvzf mha4mysql-node-0.53.tar.gz

cd mha4mysql-node-0.53

perl Makefile.PL

make

make install

安装后会在/usr/bin/下生成以下脚本文件：

/usr/bin/save_binary_logs

/usr/bin/apply_diff_relay_logs

/usr/bin/filter_mysqlbinlog

/usr/bin/purge_relay_logs

关于上述脚本的功能MHA介绍，上文已经介绍，这里不再赘述。



