

MHA Manager 中主要包括了几个管理员的命令行工具，例如 masterha_manager、masterha_master_switch等。MHA Manager也是依赖于一些Perl模块的，具体如下。

（1）安装MHA Node软件包。注意，在MHA Manager的主机上也要安装MHA Node。

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

安装MHA Node软件包：

wget http://mysql-master-ha.googlecode.com/files/mha4mysql-node-0.53.tar.gz

tar xvzf mha4mysql-node-0.53.tar.gz

cd mha4mysql-node-0.53

perl Makefile.PL

make

make install

（2）安装MHA Manager软件。

安装MHA Manager所需要的Perl模块：

#!/bin/bash

wget http://xrl.us/cpanm --no-check-certificate

mv cpanm /usr/bin/

chmod 755 /usr/bin/cpanm

cat >/root/list<<EOF

install DBD::mysql

install Config::Tiny

install Log::Dispatch

install Parallel::ForkManager

install Time::HiRes

EOF

for package in `cat /root/list`

do

cpanm $package

done

安装MHA Manager软件包：

wget http://mysql-master-ha.googlecode.com/files/mha4mysql-manager-0.53.tar.gz

tar -zxf mha4mysql-manager-0.53.tar.gz

mha4mysql-manager-0.53.

perl Makefile.PL

make

make install

安装后会在/usr/bin/下生成以下脚本文件：

/usr/bin/masterha_check_repl

/usr/bin/masterha_check_ssh

/usr/bin/masterha_check_status

/usr/bin/masterha_conf_host

/usr/bin/masterha_manager

/usr/bin/masterha_master_monitor

/usr/bin/masterha_master_switch

/usr/bin/masterha_secondary_check

/usr/bin/masterha_stop



