① 首先我们开启 CentOS 7 系统并确保系统可以连接外网，本篇中采用 `ping www.baidu` 进行测试，具体展示如下图所示。

```shell
$ ping www.baidu.com
PING www.a.shifen.com (220.181.38.150) 56(84) bytes of data.
64 bytes from 220.181.38.150 (220.181.38.150): icmp_seq=1 ttl=53 time=4.42 ms
64 bytes from 220.181.38.150 (220.181.38.150): icmp_seq=2 ttl=53 time=4.41 ms
64 bytes from 220.181.38.150 (220.181.38.150): icmp_seq=3 ttl=53 time=4.37 ms
64 bytes from 220.181.38.150 (220.181.38.150): icmp_seq=4 ttl=53 time=4.42 ms
^C
--- www.a.shifen.com ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9012ms
rtt min/avg/max/mdev = 4.378/4.413/4.429/0.080 ms
```

② 然后执行命令 `yum update -y` 进行手动更新系统，具体展示如下图所示。

③ 在系统执行更新完毕后，然后我们执行命令 `yum install yum-cron -y`，进行安装软件。

④ 然后我们使用 vi 打开 /etc/yum/yum-cron.conf。修改以下内容为下面的值：

```consolse
update_cmd = security
update_message = yes
download_updates = yes
apply_updates = yes
```

具体内容如下所示：

```txt
[commands]
#  What kind of update to use:
# default                            = yum upgrade
# security                           = yum --security upgrade
# security-severity:Critical         = yum --sec-severity=Critical upgrade
# minimal                            = yum --bugfix update-minimal
# minimal-security                   = yum --security update-minimal
# minimal-security-severity:Critical =  --sec-severity=Critical update-minimal
#update_cmd = default
update_cmd = security

# Whether a message should be emitted when updates are available,
# were downloaded, or applied.
#update_messages = yes
update_messages = yes

# Whether updates should be downloaded when they are available.
#download_updates = yes
download_updates = yes

# Whether updates should be applied when they are available.  Note
# that download_updates must also be yes for the update to be applied.
#apply_updates = no
apply_updates = yes

# Maximum amout of time to randomly sleep, in minutes.  The program
# will sleep for a random amount of time between 0 and random_sleep
# minutes before running.  This is useful for e.g. staggering the
# times that multiple systems will access update servers.  If
# random_sleep is 0 or negative, the program will run immediately.
# 6*60 = 360
random_sleep = 360

.......
```

⑤ 然后我们执行命令 `systemctl start yum-cron`，启动 yum-cron 即可。

⑥ 最后我们将 yum-cron 加入开机自动启动。执行命令 `systemctl enable yum-cron`。

⑦ 可以执行下面命令直接进行更新：

```shell
[commands]
#  What kind of update to use:
# default                            = yum upgrade
# security                           = yum --security upgrade
# security-severity:Critical         = yum --sec-severity=Critical upgrade
# minimal                            = yum --bugfix update-minimal
# minimal-security                   = yum --security update-minimal
# minimal-security-severity:Critical =  --sec-severity=Critical update-minimal
```

