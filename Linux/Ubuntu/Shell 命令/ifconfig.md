`ifconfig` 命令用于显示网络配置信息：

```shell
xiaotuan@xiaotuan:~$ ifconfig
enp0s3    Link encap:以太网  硬件地址 08:00:27:d1:1a:16  
          inet 地址:10.0.2.15  广播:10.0.2.255  掩码:255.255.255.0
          inet6 地址: fe80::76b3:c89a:9138:f11b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:254426 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:133058 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:292161906 (292.1 MB)  发送字节:12422996 (12.4 MB)

lo        Link encap:本地环回  
          inet 地址:127.0.0.1  掩码:255.0.0.0
          inet6 地址: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  跃点数:1
          接收数据包:20762 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:20762 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:6884062 (6.8 MB)  发送字节:6884062 (6.8 MB)

```

显示当前设备上所有的网卡信息：

```shell
xiaotuan@xiaotuan:~$ ifconfig -a
enp0s3    Link encap:以太网  硬件地址 08:00:27:d1:1a:16  
          inet 地址:10.0.2.15  广播:10.0.2.255  掩码:255.255.255.0
          inet6 地址: fe80::76b3:c89a:9138:f11b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:254445 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:133077 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:292167094 (292.1 MB)  发送字节:12425857 (12.4 MB)

lo        Link encap:本地环回  
          inet 地址:127.0.0.1  掩码:255.0.0.0
          inet6 地址: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  跃点数:1
          接收数据包:20768 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:20768 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:6884589 (6.8 MB)  发送字节:6884589 (6.8 MB)
```

打开或关闭网卡：

```shell
关闭网卡
xiaotuan@xiaotuan:~$ sudo ifconfig enp0s3 down
打开网卡 
xiaotuan@xiaotuan:~$ sudo ifconfig enp0s3 up
```

修改 IP 地址：

```shell
xiaotuan@xiaotuan:~$ sudo ifconfig enp0s3 10.0.2.100
```

