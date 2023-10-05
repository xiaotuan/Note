[toc]

#### 1. 查看网络配置命令

可以通过 `ifconfig` 命令查看设备的网络配置：

```shell
root@ATK-IMX6U:~# ifconfig          
eth0      Link encap:Ethernet  HWaddr 88:ca:7b:db:f4:44  
          inet addr:192.168.137.57  Bcast:192.168.137.255  Mask:255.255.255.0
          inet6 addr: fe80::8aca:7bff:fedb:f444/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:382 errors:0 dropped:0 overruns:0 frame:0
          TX packets:104 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:37049 (36.1 KiB)  TX bytes:39792 (38.8 KiB)

eth1      Link encap:Ethernet  HWaddr 88:c9:08:e4:6c:0a  
          UP BROADCAST MULTICAST DYNAMIC  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:174 errors:0 dropped:0 overruns:0 frame:0
          TX packets:174 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:11756 (11.4 KiB)  TX bytes:11756 (11.4 KiB)

root@ATK-IMX6U:~# 
```

#### 2. 关闭 connmand 网络连接守护进程

<font color="red">注意：若文件系统 `/etc/init.d/` 目录下有 `connman` 文件，执行以下指令将 `connman` 命名为 `connman2`。</font>

这样做的目的是让系统找不到 `connman` 文件，关闭了 `connmand` 网络连接守护进程，如果不关闭，那么在后面的设置完成后会有两个 `IP` 地址。如果系统下没有这个文件，这步不必操作。

```shell
mv /etc/init.d/connman /etc/init.d/connman2
```

#### 3. 设置永久静态 IP 地址（自启动执行命令）(无效)

在开发板文件系统中执行以下指令，执行完重启开发板：

```shell
root@ATK-IMX6U:/# echo "ifconfig eth0 192.168.137.110 netmask 255.255.255.0" | tee -a /etc/init.d/rcS
ifconfig eth0 192.168.137.110 netmask 255.255.255.0
root@ATK-IMX6U:/# echo "route add default gw 192.168.137.1" | tee -a /etc/init.d/rcS
route add default gw 192.168.137.1
```

也可以执行下面的命令：

```shell
root@ATK-IMX6U:/# echo "ifconfig eth0 192.168.137.110 netmask 255.255.255.0" | tee >> /etc/init.d/rcS
ifconfig eth0 192.168.137.110 netmask 255.255.255.0
root@ATK-IMX6U:/# echo "route add default gw 192.168.137.1" | tee >> /etc/init.d/rcS
route add default gw 192.168.137.1
```

执行完以上指令后，执行 `cat -n /etc/init.d/rcS` 命令可以发现 `/etc/init.d/rcS` 文件最后两行添加了以上两条指令：

```shell
root@ATK-IMX6U:/# cat -n /etc/init.d/rcS
     1  #!/bin/sh
     2  #
     3  # rcS           Call all S??* scripts in /etc/rcS.d in
     4  #               numerical/alphabetical order.
     5  #
     6  # Version:      @(#)/etc/init.d/rcS  2.76  19-Apr-1999  miquels@cistron.nl
     7  #
     8
     9  PATH=/sbin:/bin:/usr/sbin:/usr/bin
    10  runlevel=S
    11  prevlevel=N
    12  umask 022
    13  export PATH runlevel prevlevel
    14
    15  #       Make sure proc is mounted
    16  #
    17  [ -d "/proc/1" ] || mount /proc
    18
    19  #
    20  #       Source defaults.
    21  #
    22  . /etc/default/rcS
    23
    24  #
    25  #       Trap CTRL-C &c only in this shell so we can interrupt subprocesses.
    26  #
    27  trap ":" INT QUIT TSTP
    28
    29  #
    30  #       Call all parts in order.
    31  #
    32  exec /etc/init.d/rc S
    33
    34
    35  ifconfig eth0 192.168.137.110 netmask 255.255.255.0
    36  route add default gw 192.168.137.1
```

重启开发板，执行 `ifconfig` 指令或者 `ip -a` 查看 `IP` 地址修改成功。这种设置的好处在于操作简单，一次修改成功，下次再重启开发板 `IP` 地址不会变换，即永久生效。

> 提示：`/etc/init.d/rcS` 文件的原始内容如下：
>
> ```shell
> #!/bin/sh
> #
> # rcS           Call all S??* scripts in /etc/rcS.d in
> #               numerical/alphabetical order.
> #
> # Version:      @(#)/etc/init.d/rcS  2.76  19-Apr-1999  miquels@cistron.nl
> #
> 
> PATH=/sbin:/bin:/usr/sbin:/usr/bin
> runlevel=S
> prevlevel=N
> umask 022
> export PATH runlevel prevlevel
> 
> #       Make sure proc is mounted
> #
> [ -d "/proc/1" ] || mount /proc
> 
> #
> #       Source defaults.
> #
> . /etc/default/rcS
> 
> #
> #       Trap CTRL-C &c only in this shell so we can interrupt subprocesses.
> #
> trap ":" INT QUIT TSTP
> 
> #
> #       Call all parts in order.
> #
> exec /etc/init.d/rc S
> 
> ```

#### 3. 设置永久静态 IP 地址（修改配置文件）

修改配置文件 `/etc/network/interfaces` （这个配置文件在有的文件系统中有，有的文件系统下没有，没有的话，这种方法就不合适了）

`/etc/network/interfaces` 原始内容如下：

```
root@ATK-IMX6U:~# cat /etc/network/interfaces
# /etc/network/interfaces -- configuration file for ifup(8), ifdown(8)
 
# The loopback interface
auto lo
iface lo inet loopback

# Wireless interfaces
iface wlan0 inet dhcp
        wireless_mode managed
        wireless_essid any
        wpa-driver wext
        wpa-conf /etc/wpa_supplicant.conf

iface atml0 inet dhcp

# Wired or wireless interfaces
auto eth0
iface eth0 inet dhcp
iface eth1 inet dhcp

# Ethernet/RNDIS gadget (g_ether)
# ... or on host side, usbnet and random hwaddr
iface usb0 inet static
        address 192.168.7.2
        netmask 255.255.255.0
        network 192.168.7.0
        gateway 192.168.7.1

# Bluetooth networking
iface bnep0 inet dhcp

```

修改后的内容如下：

```
root@ATK-IMX6U:~# cat /etc/network/interfaces
# /etc/network/interfaces -- configuration file for ifup(8), ifdown(8)
 
# The loopback interface
auto lo
iface lo inet loopback

# Wireless interfaces
iface wlan0 inet dhcp
        wireless_mode managed
        wireless_essid any
        wpa-driver wext
        wpa-conf /etc/wpa_supplicant.conf

iface atml0 inet dhcp

# Wired or wireless interfaces
auto eth0
#iface eth0 inet dhcp
#iface eth1 inet dhcp
iface eth0 inet static
address 192.168.137.110
gateway 192.168.137.1
netmask 255.255.255.0

# Ethernet/RNDIS gadget (g_ether)
# ... or on host side, usbnet and random hwaddr
iface usb0 inet static
        address 192.168.7.2
        netmask 255.255.255.0
        network 192.168.7.0
        gateway 192.168.7.1

# Bluetooth networking
iface bnep0 inet dhcp

```

修改完成后执行 `/etc/init.d/networking restart` 命令重启网络配置即可，这种修改方法是改完后执行 `/etc/init.d/networking restart` 就永久生效了。

#### 4. 设置临时静态 IP 地址

在开发板文件系统中执行下面指令：

```shell
root@ATK-IMX6U:~# ifconfig eth0 192.168.137.10 netmask 255.255.255.0
root@ATK-IMX6U:~# route add default gw 192.168.137.1
```

