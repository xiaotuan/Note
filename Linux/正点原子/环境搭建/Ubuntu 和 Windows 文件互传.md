[toc]

### 1. 开启 Ubuntu 下的 FTP 服务

打开 `Ubuntu` 的终端窗口，然后执行如下命令来安装 `FTP` 服务：

```shell
$ sudo apt-get install vsftpd
```

等待软件自动安装，安装完成以后使用 `vi` 命令打开 `/etc/vsftpd.conf`，命令如下：

```shell
$ sudo vi /etc/vsftpd.conf
```

打开 `vsftpd.conf` 文件以后找到如下两行：

```properties
local_enable=YES
write_enable=YES
```

确保上面两行前面没有 `#`，有的话就取消，完成以后如下所示：

```
# Uncomment this to allow local users to log in.
local_enable=YES
#
# Uncomment this to enable any form of FTP write command.
write_enable=YES
#
```

修改完 `vsftpd.conf` 以后保存退出，使用如下命令重启 `FTP` 服务：

```shell
$ sudo /etc/init.d/vsftpd restart
```

### 2. Windows 下 FTP 客户端安装

`Windows` 下 `FTP` 客户端我们使用 `FileZilla`，可以在 `FileZilla` 官网下载，下载地址如下：<https://www.filezilla.cn/download>。

