[toc]

### 1. 安装 ssh 服务端

```shell
sudo apt-get install openssh-server
```

### 2. 修改 ssh 配置文件

打开 `/etc/ssh/sshd_config` 文件，在 `#PermitRootLogin prohibit-password` 下添加 `PermitRootLogin yes` 代码：

```
# Logging
#SyslogFacility AUTH
#LogLevel INFO

# Authentication:

#LoginGraceTime 2m
#PermitRootLogin prohibit-password
PermitRootLogin yes
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10

#PubkeyAuthentication yes

# Expect .ssh/authorized_keys2 to be disregarded by default in future.
#AuthorizedKeysFile     .ssh/authorized_keys .ssh/authorized_keys2

#AuthorizedPrincipalsFile none
```

### 3. 重启 ssh 服务

```shell
sudo service ssh restart
```

### 4. 查看本机 IP 地址

```shell
$ ifconfig
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.19.7.119  netmask 255.255.255.0  broadcast 172.19.7.255
        inet6 fe80::814e:317b:90ff:2725  prefixlen 64  scopeid 0x20<link>
        ether a8:a1:59:8c:0d:db  txqueuelen 1000  (Ethernet)
        RX packets 93888843  bytes 97100340913 (97.1 GB)
        RX errors 0  dropped 18844  overruns 0  frame 0
        TX packets 185670719  bytes 238871691631 (238.8 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 16  memory 0xb1000000-b1020000  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 4031  bytes 442098 (442.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4031  bytes 442098 (442.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### 5. 远程 ssh 连接本机

```shell
ssh 你的用户名@你的IP地址 -p 端口号
```

例如：

```shell
$ ssh qty@172.19.7.119 -p 22
```

> 注意：
>
> 如果没有传递端口号，则默认是 22。