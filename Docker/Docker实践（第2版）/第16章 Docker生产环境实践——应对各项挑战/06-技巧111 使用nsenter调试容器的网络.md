### 技巧111　使用nsenter调试容器的网络

在理想世界中，用户可以使用socat（见技巧4）在 **大使容器** （ambassador container）中诊断与容器通信的问题。用户可以启动一个额外的容器，并确保连接转到这个作为代理的新容器。该代理允许诊断和监控连接，然后它将其转发到正确的地方。但是，现实世界里，往往不那么方便（或可能）设置这样一个只用于调试的容器。



**提示**

见技巧74对大使模式的描述。



读者已经在技巧15和技巧19中了解了 `docker exec` 命令。本技巧讨论nsenter，这个工具和 `docker exec` 命令看起来很相似，但允许在容器中使用自己机器上的工具，而不是局限于容器已经安装的东西。

#### 问题

想要调试容器中的网络问题，但使用的工具却不在容器中。

#### 解决方案

使用nsenter来跳到容器的网络，但是工具仍然在宿主机上。

如果Docker宿主机上还未安装nsenter，可以通过以下命令来安装：

```c
$ docker run -v /usr/local/bin:/target jpetazzo/nsenter
```

这将在/usr/local/bin中安装nsenter，然后便即刻可以使用。nsenter也可能包含在所使用的系统发行版中（在util-linux包）。

读者可能已经注意到，一般可用的BusyBox镜像默认不附带bash。作为nsenter的演示，我们将展示如何使用宿主机的bash程序进入BusyBox容器：

```c
$ docker run -ti busybox /bin/bash
FATA[0000] Error response from daemon: Cannot start container >
a81e7e6b2c030c29565ef7adb94de20ad516a6697deeeb617604e652e979fda6: >
exec: "/bin/bash": stat /bin/bash: no such file or directory
$ CID=$(docker run -d busybox sleep 9999) 　　⇽---　启动BusyBox容器并保存容器ID（CID）
$ PID=$(docker inspect --format {{.State.Pid}} $CID) 　　⇽---　检查容器，提取进程ID（PID）（见技巧30）
$ sudo nsenter --target $PID \　　⇽---　运行nsenter，指定--target标志来进入容器可能无须带上sudo
--uts --ipc --net /bin/bash　　⇽---　通过余下的标志指定进入容器时的命名空间
root@781c1fed2b18:~#
```

更多关于命名空间的细节参见技巧109。命名空间的关键点是不使用 `--mount` 标志，因为它会使用容器的文件系统，因为该文件系统没有安装 bash。指定/bin/bash 作为可执行命令来启动容器。

需要指出的是虽然不能直接访问容器的文件系统，但是用户可以使用宿主机拥有的所有工具。

我们之前的某个需求是想有一种办法找出宿主机上哪个veth接口设备对应于哪个容器。例如，有时候我们需要快速将容器从网络上卸载。但是，一个没有特权的容器无法禁用网络接口，所以我们需要找出 veth 接口的名称然后在宿主机上完成这项任务。

```c
$ docker run -d --name offlinetest ubuntu:14.04.2 sleep infinity
fad037a77a2fc337b7b12bc484babb2145774fde7718d1b5b53fb7e9dc0ad7b3
$ docker exec offlinetest ping -q -c1 8.8.8.8　　⇽---　尝试从新容器内部执行ping命令验证连接成功与否
 PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 2.966/2.966/2.966/0.000 ms
$ docker exec offlinetest ifconfig eth0 down　　⇽---　我们不能关闭容器中的接口。注意，用户的接口可能不是eth0, 所以如果该命令不生效，那么不妨试试通过ifconfig找出主接口的名称
 SIOCSIFFLAGS: Operation not permitted
$ PID=$(docker inspect --format {{.State.Pid}} offlinetest)
$ nsenter --target $PID --net ethtool -S eth0　　⇽---　进入该容器的网络空间，使用ethtool命令从宿主机查找对等接口的索引，即虚拟接口的另一端
 NIC statistics:
     peer_ifindex: 53
$ ip addr | grep '^53'　　⇽---　查找宿主机上的接口列表，从而找出容器的对应veth接口
 53: veth2e7d114: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue >
master docker0 state UP
$ sudo ifconfig veth2e7d114 down　　⇽---　关闭虚拟接口
$ docker exec offlinetest ping -q -c1 8.8.8.8　　⇽---　从容器内部使用ping命令验证连接是失败的
 PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
--- 8.8.8.8 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms
```

作为最后一个例子，读者可能想要在容器里使用的程序应该是tcpdump，这是一种在网络接口上记录所有TCP分组的工具。要使用它，需要使用 `--net` 命令运行 `nsenter` ，这样可以在宿主机上“查看”容器的网络，这样一来便可以使用tcpdump监控分组。

例如，下面代码中的 `tcpdump` 命令会将所有分组记录到/tmp/google.tcpdump文件中（我们假设用户仍然在前面启动的nsenter会话中）。然后，我们可以通过访问网页触发一些网络流量：

```c
root@781c1fed2b18:/# tcpdump -XXs 0 -w /tmp/google.tcpdump &
root@781c1fed2b18:/# wget ××××.com
--2015-08-07 15:12:04--  http:// ××××.com/
Resolving ××××.com (××××.com)... 216.58.208.46, 2a00:1450:4009:80d::200e
Connecting to ××××.com (××××.com)|216.58.208.46|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: http://www.××××.co.uk/?gfe_rd=cr&ei=tLzEVcCXN7Lj8wepgarQAQ >
[following]
--2015-08-07 15:12:04-- >
http://www.××××.co.uk/?gfe_rd=cr&ei=tLzEVcCXN7Lj8wepgarQAQ
Resolving www.××××.co.uk (www.××××.co.uk)... 216.58.208.67, >
2a00:1450:4009:80a::2003
Connecting to www.××××.co.uk (www.××××.co.uk)|216.58.208.67|:80... >
connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: 'index.html'
index.html             [ <=>             ]  18.28K  --.-KB/s   in 0.008s
2015-08-07 15:12:05 (2.18 MB/s) – 'index.html' saved [18720]
root@781c1fed2b18:# 15:12:04.839152 IP 172.17.0.26.52092 > >
google-public-dns-a.××××.com.domain: 7950+ A? ××××.com. (28)
15:12:04.844754 IP 172.17.0.26.52092 > >
google-public-dns-a.××××.com.domain: 18121+ AAAA? ××××.com. (28)
15:12:04.860430 IP google-public-dns-a.××××.com.domain > >
172.17.0.26.52092: 7950 1/0/0 A 216.58.208.46 (44)
15:12:04.869571 IP google-public-dns-a.××××.com.domain > >
172.17.0.26.52092: 18121 1/0/0 AAAA 2a00:1450:4009:80d::200e (56)
15:12:04.870246 IP 172.17.0.26.47834 > lhr08s07-in-f14.1e100.net.http: >
Flags [S], seq 2242275586, win 29200, options [mss 1460,sackOK,TS val >
49337583 ecr 0,nop,wscale 7], length 0
```



**提示**

这取决于读者的网络配置，读者可能需要临时修改resolv.conf文件，使DNS查找可以正常工作。如果收到“Temporary failure in name resolution”（域名解析暂时失败）错误，请尝试将 `nameserver 8.8.8.8`  这行添加到/etc/resolv.conf文件的顶部。别忘了在完成实验后还原它。



#### 讨论

本技巧给了用户一种迅速调整网络行为的方式，而且无须通过第10章（技巧78和技巧79）中的方法设置任何工具来模拟网络损坏。

我们还看到了Docker另外一个备受瞩目的使用场景——在Docker提供的隔离网络环境中调试网络问题会比在不受管控的环境中更加容易。试着记住tcpdump的一些正确的参数，从而妥善地过滤掉一些不相关的分组，这在半夜里维护系统时会是一个容易出错的环节。使用nsenter，大可忘掉这一点，使用tcpdump捕获容器内的所有内容，而无须在镜像里安装（或不必安装）它。

