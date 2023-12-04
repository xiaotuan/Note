`ifconfig` 是一个跟网络属性配置和现实密切相关的命令，通过次命令我们可以查看当前网络属性，也可以通过此命令配置网络属性，比如设置网络 IP 地址等等，此命令格式如下：

```shell
ifconfig interface options|address
```

主要参数如下：

+ `interface`：网络接口名称，比如 eth0 等。
+ `up`：开启网络设备。
+ `down`：关闭网络设备。
+ `add`：IP 地址，设置网络 IP 地址。
+ `netmask add`：子网掩码。

例如：

```shell
xiaotuan@xiaotuan:~$ ifconfig
enp0s3    Link encap:以太网  硬件地址 08:00:27:d1:1a:16  
          inet 地址:10.0.2.15  广播:10.0.2.255  掩码:255.255.255.0
          inet6 地址: fe80::76b3:c89a:9138:f11b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:2142679 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:554711 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:3214854252 (3.2 GB)  发送字节:35109359 (35.1 MB)

lo        Link encap:本地环回  
          inet 地址:127.0.0.1  掩码:255.0.0.0
          inet6 地址: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  跃点数:1
          接收数据包:2396 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:2396 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:274962 (274.9 KB)  发送字节:274962 (274.9 KB)

xiaotuan@xiaotuan:~$ ifconfig enp0s3
enp0s3    Link encap:以太网  硬件地址 08:00:27:d1:1a:16  
          inet 地址:10.0.2.15  广播:10.0.2.255  掩码:255.255.255.0
          inet6 地址: fe80::76b3:c89a:9138:f11b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:2142679 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:554711 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:3214854252 (3.2 GB)  发送字节:35109359 (35.1 MB)

xiaotuan@xiaotuan:~$ sudo ifconfig enp0s3 10.0.2.20
[sudo] xiaotuan 的密码： 
xiaotuan@xiaotuan:~$ ifconfig enp0s3
enp0s3    Link encap:以太网  硬件地址 08:00:27:d1:1a:16  
          inet 地址:10.0.2.20  广播:10.255.255.255  掩码:255.0.0.0
          inet6 地址: fe80::76b3:c89a:9138:f11b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:2142679 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:554727 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:3214854252 (3.2 GB)  发送字节:35111592 (35.1 MB)
```

