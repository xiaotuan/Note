要用软件仓库中的新版本妥善地更新系统上所有的软件包，可用 `safe-upgrade` 选项：

```shell
aptitude safe-upgrade
```

> 注意：这个命令不需要使用软件包名称作为参数。因为 `safe-upgrade` 选项会将所有已安装的包更新到软件仓库中的最新版本，更有利于系统稳定。

例如：

```shell
$ sudo aptitude safe-upgrade
[sudo] xiatuan 的密码： 
依赖关系分析中...                
下列“新”软件包将被安装。
  distro-info{a} libzstd1{a} python3-distro-info{a} python3-yaml{a} 
下列软件包将被升级：
  apt apt-transport-https apt-utils base-files dpkg dpkg-dev grub-common 
  grub-pc grub-pc-bin grub2-common initramfs-tools initramfs-tools-bin 
  initramfs-tools-core libapt-inst2.0 libapt-pkg5.0 libdpkg-perl 
  libgnutls-openssl27 libgnutls30 libpam-modules libpam-modules-bin 
  libpam-runtime libpam-systemd libpam0g libseccomp2 libsystemd0 libudev1 
  python-apt-common python3-apt python3-distupgrade systemd systemd-sysv 
  ubuntu-advantage-tools ubuntu-desktop ubuntu-minimal 
  ubuntu-release-upgrader-core ubuntu-release-upgrader-gtk ubuntu-standard 
  udev unattended-upgrades update-notifier update-notifier-common 
下列软件包被“推荐”安装但是将“不会”被安装：
  update-motd 
41 个软件包被升级，新安装 4 个， 0 个将被删除， 同时 0 个将不升级。
需要获取 15.9 MB 的存档。 解包后将要使用 3,676 kB。
您要继续吗？[Y/n/?] 
```

还有一些不那么保守的软件升级选项：

+ `aptitude full-upgrade`
+ `aptitude dist-upgrade`

这些选项执行相同的任务，将所有软件包升级到最新版本。它们同 `safe-upgrade` 的区别在于，它们不会检查包与包之间的依赖关系。整个包依赖关系问题非常麻烦。如果不是很确定各种包的依赖关系，那么还是坚持用 `safe-upgrade` 选项吧。