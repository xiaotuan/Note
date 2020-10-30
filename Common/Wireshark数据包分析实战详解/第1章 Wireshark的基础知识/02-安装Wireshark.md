[toc]



### 1. Windows 下安装 Wireshark

下载地址：<http://www.wireshark.org>

> 如果要使用 Wireshark 捕获数据，必须要安装 WinPcap。

### 2. 在 Linux 系统中安装 Wireshark

下面演示在 Red Hat Linux 系统中安装 Wireshark。具体操作步骤如下所示：

（1）从 Wireshark 官网下载 Wireshark 的源码包，其软件名为 wireshark-1.10.7.tar.bz2。

（2）解压 Wireshark 软件包。执行命令如下：

```shell
[root@localhost ~]# tar jxvf wireshark-1.10.7.tar.bz2 -C /usr/
```

执行以上命令后，Wireashark 将被解压到 /usr/ 目录下。

（3）配置 Wireshark 软件包，执行命令如下：

```shell
[root@localhost ~]# cd /usr/wireshark-1.10.7/
[root@localhost wireshark-1.10.7]# ./configure
```

（4）编译 Wireshark 软件包。执行命令如下：

```shell
[root@localhost wireshark-1.10.7]# make
```

（5）安装 Wireshark 软件包。执行命令如下：

```shell
[root@localhost wireshark-1.10.7]# make install
```

以上过程成功执行完后，表示 Wireshark 软件已经成功安装。

接下来就可以使用 Wireshark 工具了。在终端输入命令 wireshark，启动该工具。如下：

```shell
[root@localhost ~]# wireshark
```



