使用 `yum` 安装软件命令如下：

```shell
yum install package_name
```

例如：

```shell
$ su -
password:
# yum install xterm
Loaded plugins: fastestmirror, refresh- packagekit, security
Determining fastest mirrors
  * base: mirrors.bluehost.com
  * extras: mirror.5ninesolutions.com
  * updates: mirror.san.fastserv.com
Setting up Install Process Resolving Dependencies
[...]
```

也可以手动下载 rpm 安装文件并用 `yum` 安装，这叫作**本地安装**。基本的命令是：

```shell
yum localinstall package_name.rpm
```

