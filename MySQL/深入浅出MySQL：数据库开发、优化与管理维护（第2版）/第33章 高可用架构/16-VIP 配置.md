

VIP配置可以采用两种方式，一种为通过keepalived的方式管理虚拟IP的浮动，另一种为通过脚本方式手动摘除的方式。

**1．keepalived方式管理虚拟IP**

keepalived配置步骤如下。

（1）下载集群心跳软件keepalived，并进行安装：

wget http://www.keepalived.org/software/keepalived-1.2.1.tar.gz

tar zxvf keepalived-1.2.1.tar.gz

cd keepalived-1.2.1

./configure --prefix=/usr/local/keepalived

--with-kernel-dir=/usr/src/kernels/2.6.18-164.el5-i686/

make && make install

cp /usr/local/keepalived/etc/rc.d/init.d/keepalived /etc/rc.d/init.d/

cp /usr/local/keepalived/etc/sysconfig/keepalived /etc/sysconfig/

mkdir /etc/keepalived

cp /usr/local/keepalived/etc/keepalived/keepalived.conf /etc/keepalived/

cp /usr/local/keepalived/sbin/keepalived /usr/sbin/

（2）配置keepalived的配置文件。

在ip81上设置：

[root@ip81 tools]# cat /etc/keepalived/keepalived.conf

! Configuration File for keepalived

global_defs {

notification_email {

wanghq@corp.netease.com

}

notification_email_from dba@corp.netease.com

smtp_server 127.0.0.1

smtp_connect_timeout 30

router_id MySQL-ha

}

vrrp_instance VI_1 {

state BACKUP

interface eth0

virtual_router_id 51

priority 150

advert_int 1

nopreempt

authentication {

auth_type PASS

auth_pass 1111

}

virtual_ipaddress {

192.168.7.201/23

}}

注意黑体部分的代码，其中 router_id MySQL-ha 表示设定 keepalived 组的名称，将192.168.7.201/23这个 IP绑定到 ip81主机 interface eth0上，并且设置了状态为backup模式，将 keepalived的模式设置为非抢占模式（nopreempt），priority 150优先级别设置为 150。

在候选主ip83上设置：

[root@ip83 ~]# cat /etc/keepalived/keepalived.conf

onfiguration File for keepalived

global_defs {

notification_email {

wanghq@corp.netease.com

}

notification_email_from dba@corp.netease.com

smtp_server 127.0.0.1

smtp_connect_timeout 30

router_id MySQL-ha

}

vrrp_instance VI_1 {

state BACKUP

interface eth0

virtual_router_id 51

priority 120

advert_int 1

nopreempt

authentication {

auth_type PASS

auth_pass 1111

}

virtual_ipaddress {

192.168.7.201/23

}

}

注意黑体部分的代码，其中 router_id MySQL-ha表示设定 keepalived组的名称，并且设置了状态为backup模式，将 keepalived的模式设置为非抢占模式（nopreempt），priority 120优先级别设置为120。

（3）启动keepalived服务。

在ip81上启动keepalived服务：

[root@ip81 tools]# service keepalived start

[root@ip81 tools]# tail -f /var/log/messages

Jul 19 18:10:13 ip81 Keepalived_vrrp: Registering Kernel netlink reflector

Jul 19 18:10:13 ip81 Keepalived_vrrp: Registering Kernel netlink command channel

Jul 19 18:10:13 ip81 Keepalived: Starting VRRP child process, pid=18426

Jul 19 18:10:13 ip81 Keepalived_healthcheckers:Using LinkWatch kernel netlink reflector...

Jul 19 18:10:13 ip81 Keepalived_vrrp: Registering gratutious ARP shared channel

Jul 19 18:10:13 ip81 Keepalived_vrrp: Opening file '/etc/keepalived/keepalived.conf'.

Jul 19 18:10:13 ip81 Keepalived_vrrp: Configuration is using : 35902 Bytes

Jul 19 18:10:13 ip81 Keepalived_vrrp: Using LinkWatch kernel netlink reflector...

Jul 19 18:10:13 ip81 Keepalived_vrrp: VRRP_Instance(VI_1) Entering BACKUP STATE

Jul 19 18:10:13 ip81 Keepalived_vrrp: VRRP sockpool:[ifindex(2), proto(112), fd(10,11)]

Jul 19 18:10:16 ip81 Keepalived_vrrp: VRRP_Instance(VI_1) Transition to MASTER STATE

Jul 19 18:10:17 ip81 Keepalived_vrrp: VRRP_Instance(VI_1) Entering MASTER STATE

Jul 19 18:10:17 ip81 Keepalived_vrrp: VRRP_Instance(VI_1) setting protocol VIPs.

Jul 19 18:10:17 ip81 Keepalived_healthcheckers: Netlink reflector reports IP 192.168. 7.188 added

Jul 19 18:10:17 ip81 Keepalived_vrrp: VRRP_Instance(VI_1) Sending gratuitous ARPs on eth0 for 192.168.7.188

Jul 19 18:10:17 ip81 Keepalived_vrrp: Netlink reflector reports IP 192.168.7.201 added

Jul 19 18:10:17 ip81 avahi-daemon[2799]: Registering new address record for 192.168.7.201 on eth0.

Jul 19 18:10:22 ip81 Keepalived_vrrp: VRRP_Instance(VI_1) Sending gratuitous ARPs on eth0 for 192.168.7.201

通过输出可以看到虚拟IP（192.168.7.201）已经绑定到ip81的eth0网卡上了。

（4）查看绑定情况。

在ip81上查看IP地址绑定情况：

[root@ip81 mysqlhome]# ip addr

2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000

link/ether 00:11:43:de:78:78 brd ff:ff:ff:ff:ff:ff

inet 192.168.7.81/23 brd 192.168.7.255 scope global eth0

inet 192.168.7.201/23 scope global secondary eth0

inet6 fe80::211:43ff:fede:7878/64 scope link

valid_lft forever preferred_lft forever

从keepalived 的输出信息和系统的网卡信息可以看到，虚拟IP（192.168.7.201）已经添加成功。在ip83上：

[root@ip83 ~]# service keepalived start

[root@ip83 ~]# tail -f /var/log/messages

Jul 19 18:15:36 ip83 Keepalived_vrrp: Registering Kernel netlink reflector

Jul 19 18:15:36 ip83 Keepalived_vrrp: Registering Kernel netlink command channel

Jul 19 18:15:36 ip83 Keepalived_vrrp: Registering gratutious ARP shared channel

Jul 19 18:15:36 ip83 Keepalived_vrrp: Opening file '/etc/keepalived/keepalived.conf'.

Jul 19 18:15:36 ip83 Keepalived_healthcheckers: Using LinkWatch kernel netlink reflector...

Jul 19 18:15:36 ip83 Keepalived_vrrp: Configuration is using : 35910 Bytes

Jul 19 18:15:36 ip83 Keepalived: Starting VRRP child process, pid=9505

Jul 19 18:15:36 ip83 Keepalived_vrrp: Using LinkWatch kernel netlink reflector...

Jul 19 18:15:36 ip83 Keepalived_vrrp: VRRP_Instance(VI_1) Entering BACKUP STATE

Jul 19 18:15:36 ip83 Keepalived_vrrp: VRRP sockpool: [ifindex(2), proto(112), fd(10,11)]

从上面的输出可以看到keepalived已经配置成功。

**注意：**这里ip81和ip83都要设置为BACKUP模式。在keepalived中有2种模式，分别是master-->backup模式和backup-->backup模式，这两种模式分别有什么区别呢？

在 master-->backup 模式下，一旦主库宕掉，虚拟 IP 会自动漂移到从库，当主库修复后， keepalived 启动后，还会把虚拟 IP 抢过来，即使你设置 nopreempt（不抢占）的方式抢占 IP的动作也会发生。在backup-->backup模式下，当主库宕掉后虚拟IP会自动漂移到从库上，当原主恢复之后重启keepalived服务，并不会抢占新主的虚拟IP，即使是优先级高于从库的优先级别，也不会抢占IP。为了减少IP的漂移次数，生产中我们通常是把修复好的主库当作新主库的备库。

keepalived还存在一种脑裂状况，当主从间网络出现问题，这时主库会持有虚拟IP不变，从库失去和主库的联系后，从库也会抢夺IP（即便你采用backup-->backup非抢占模式），这样造成的后果是主从数据库都持有虚拟IP。于是造成IP冲突，业务也会受到影响，因此在网络不是很好的状况下，强烈不建议采用keepavlived服务。

（5）MHA引入keepalived。

那么如何才能把keepalived服务引入MHA呢？很简单，只需修改切换时触发的脚本文件master_ip_failover即可，在该脚本中添加在master发生宕机时对keepalived的处理。

使用vi编辑MHA切换时调用的配置文件master_ip_failover：

vi /usr/local/bin/master_ip_failover

#!/usr/bin/env perl

# Copyright (C) 2011 DeNA Co.,Ltd.

#

# This program is free software; you can redistribute it and/or modify

# it under the terms of the GNU General Public License as published by

# the Free Software Foundation; either version 2 of the License, or

# (at your option) any later version.

#

# This program is distributed in the hope that it will be useful,

# but WITHOUT ANY WARRANTY; without even the implied warranty of

# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

# GNU General Public License for more details.

#

# You should have received a copy of the GNU General Public License

# along with this program; if not, write to the Free Software

# Foundation, Inc.,

# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

## Note: This is a sample script and is not complete. Modify the script based on your environment.

use strict;

use warnings FATAL => 'all';

use Getopt::Long;

use MHA::DBHelper;

my (

$command, $ssh_user, $orig_master_host, $orig_master_ip,

$orig_master_port, $new_master_host, $new_master_ip, $new_master_port,

$user, $password

);

GetOptions(

'command=s' => \$command,

'ssh_user=s' => \$ssh_user,

'orig_master_host=s' => \$orig_master_host,

'orig_master_ip=s' => \$orig_master_ip,

'orig_master_port=i' => \$orig_master_port,

'new_master_host=s' => \$new_master_host,

'new_master_ip=s' => \$new_master_ip,

'new_master_port=i' => \$new_master_port,

'user=s' => \$user,

'password=s' => \$password,

);

exit &main();

sub main {

if ( $command eq "stop" || $command eq "stopssh" ) {

# $orig_master_host, $orig_master_ip, $orig_master_port are passed.

# If you manage master ip address at global catalog database,

# invalidate orig_master_ip here.

my $exit_code = 1;

eval {

# updating global catalog, etc

$exit_code = 0;

};

if ($@) {

warn "Got Error: $@\n";

exit $exit_code;

}

exit $exit_code;

}

elsif ( $command eq "start" ) {

# all arguments are passed.

# If you manage master ip address at global catalog database,

# activate new_master_ip here.

# You can also grant write access (create user, set read_only=0, etc) here.

my $exit_code = 10;

eval {

my $new_master_handler = new MHA::DBHelper();

# args: hostname, port, user, password, raise_error_or_not

$new_master_handler->connect( $new_master_ip, $new_master_port, $user,

$password, 1 );

## Set read_only=0 on the new master

#$new_master_handler->disable_log_bin_local();

print "Set read_only=0 on the new master.\n";

$new_master_handler->disable_read_only();

## Creating an app user on the new master

#print "Creating app user on the new master..\n";

#FIXME_xxx_create_user( $new_master_handler->{dbh} );

#$new_master_handler->enable_log_bin_local();

$new_master_handler->disconnect();

## Update master ip on the catalog database, etc

#FIXME_xxx;

$cmd = 'ssh '.$ssh_user.'@'.$orig_master_ip.' \'./lvs-admin stop\'';

system($cmd);

$exit_code = 0;

};

if ($@) {

warn $@;

# If you want to continue failover, exit 10.

exit $exit_code;

}

exit $exit_code;

}

elsif ( $command eq "status" ) {

# do nothing

exit 0;

}

else {

&usage();

exit 1;

}

}

sub usage {

print

"Usage: master_ip_failover --command=start|stop|stopssh|status --ssh_user=s--orig_master_host=host --orig_master_ip=ip --orig_master_port=port --new_master_host=host--new_master_ip=ip --new_master_port=port --user=user --password=password\n";

}

上述黑体加粗部分即为添加的代码。在主库ip81上的根目录下编辑lvs-admin脚本：

case "$1" in

"stop")

echo;

echo "stop keepalived.....";

service keepalived stop

;;

"start")

echo

echo "start keepalive....."

service keepalived start

;;

*)

echo "please input you select!"

;;

esac

/usr/local/bin/master_ip_failover 添加内容的大体意思是，当主库数据库发生故障时刻，会触发MHA切换，MHA Manager会执行停掉主库上 keepalived服务，触发虚拟 IP漂移到备选从库，从而完成切换。

**2．通过脚本的方式管理VIP**

（1）修改触发故障切换脚本/usr/local/bin/master_ip_failover，修改内容如下：

#!/usr/bin/env perl

use strict;

use warnings FATAL => 'all';

use Getopt::Long;

my (

$command, $ssh_user, $orig_master_host, $orig_master_ip,

$orig_master_port, $new_master_host, $new_master_ip, $new_master_port

);

my $vip = '192.168.7.201/23'; # Virtual IP

my $key = "2";

my $ssh_start_vip = "/sbin/ifconfig eth0:$key $vip";

my $ssh_stop_vip = "/sbin/ifconfig eth0:$key down";

GetOptions(

'command=s' => \$command,

'ssh_user=s' => \$ssh_user,

'orig_master_host=s' => \$orig_master_host,

'orig_master_ip=s' => \$orig_master_ip,

'orig_master_port=i' => \$orig_master_port,

'new_master_host=s' => \$new_master_host,

'new_master_ip=s' => \$new_master_ip,

'new_master_port=i' => \$new_master_port,

);

exit &main();

sub main {

if ( $command eq "stop" || $command eq "stopssh" ) {

# $orig_master_host, $orig_master_ip, $orig_master_port are passed.

# If you manage master ip address at global catalog database,

# invalidate orig_master_ip here.

my $exit_code = 1;

eval {

print "Disabling the VIP on old master: $orig_master_host \n";

&stop_vip();

$exit_code = 0;

};

if ($@) {

warn "Got Error: $@\n";

exit $exit_code;

}

exit $exit_code;

}

elsif ( $command eq "start" ) {

# all arguments are passed.

# If you manage master ip address at global catalog database,

# activate new_master_ip here.

# You can also grant write access (create user, set read_only=0, etc) here.

my $exit_code = 10;

eval {

print "Enabling the VIP - $vip on the new master - $new_master_host \n";

&start_vip();

$exit_code = 0;

};

if ($@) {

warn $@;

exit $exit_code;

}

exit $exit_code;

}

elsif ( $command eq "status" ) {

print "Checking the Status of the script.. OK \n";

# do nothing

exit 0;

}

else {

&usage();

exit 1;

}

}

# A simple system call that enable the VIP on the new master

sub start_vip() {

`ssh $ssh_user\@$new_master_host \" $ssh_start_vip \"`;

}

# A simple system call that disable the VIP on the old_master

sub stop_vip() {

`ssh $ssh_user\@$orig_master_host \" $ssh_stop_vip \"`;

}

sub usage {

print

"Usage: master_ip_failover --command=start|stop|stopssh|status --orig_master_ host=host --orig_master_ip=ip --orig_master_port=port --new_master_host=host --new_master_ip=ip--new_master_port=port\n";

}

为了防止脑裂情况的发生，这里将采用通过脚本的方式来管理虚拟IP，到此为止，基本上MHA 集群环境已经配置完毕，接下来我们将通过生产中的一些案例来看一下 MHA 到底是如何进行工作的。下面将从 MHA 自动 failover、手动 failover、在线切换三种方式来介绍 MHA的工作情况。



