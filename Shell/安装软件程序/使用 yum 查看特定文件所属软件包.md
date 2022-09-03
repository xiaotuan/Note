可以使用如下命令查看特定文件属于那个软件包：

```shell
yum provides file_name
```

例如：

```shell
# yum provides /etc/yum.conf
Loaded plugins: fastestmirror, refresh-packagekit, security
Determining fastest mirrors 
  * base: mirror. web-ster.com
  * extras: centos.chi.host-engine.com 
  * updates: mirror.umd.edu
yum-3.2.29-40.el6.centos.noarch : RPM package installer/updater/manager
Repo : base
Matched from:
Filename : /etc/yum.conf

yum-3.2.29-43.el6.centos.noarch : RPM package installer/updater/manager
Repo : updates
Matched from:
Filename : /etc/yum.conf

yum-3.2.29-40.el6.centos.noarch : RPM package installer/updater/manager 
Repo : installed
Matched from:
Other : Provides- match: /etc/yum.conf
```

