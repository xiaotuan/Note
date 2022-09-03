在 Ubuntu 16.04 中安装搜狗输入法报如下错误：

```shell
$ sudo dpkg -i sogoupinyin_2.4.0.3469_amd64.deb
正在选中未选择的软件包 sogoupinyin。
dpkg: 处理归档 sogoupinyin_2.4.0.3469_amd64.deb (--install)时出错：
 安装 sogoupinyin 将破坏 fcitx-ui-qimpanel，并且
不允许反配置(--auto-deconfigure 也许会有帮助)
在处理时有错误发生：
 sogoupinyin_2.4.0.3469_amd64.deb
```

可以通过卸载 fcitx-ui-qimpanel 软件包来解决该问题：

```shell
$ sudo apt-get remove fcitx-ui-qimpanel
正在读取软件包列表... 完成
正在分析软件包的依赖关系树       
正在读取状态信息... 完成       
下列软件包将被【卸载】：
  fcitx-ui-qimpanel
升级了 0 个软件包，新安装了 0 个软件包，要卸载 1 个软件包，有 39 个软件包未被升级。
解压缩后将会空出 770 kB 的空间。
您希望继续执行吗？ [Y/n] y
(正在读取数据库 ... 系统当前共安装有 215489 个文件和目录。)
正在卸载 fcitx-ui-qimpanel (2.1.2-1) ...
正在处理用于 gnome-menus (3.13.3-6ubuntu3.1) 的触发器 ...
正在处理用于 desktop-file-utils (0.22-1ubuntu5.2) 的触发器 ...
正在处理用于 bamfdaemon (0.5.3~bzr0+16.04.20180209-0ubuntu1) 的触发器 ...
Rebuilding /usr/share/applications/bamf-2.index...
正在处理用于 mime-support (3.59ubuntu1) 的触发器 ...
```

卸载完后再重新安装搜狗输入即可：

```shell
$ sudo dpkg -i sogoupinyin_2.4.0.3469_amd64.deb
(正在读取数据库 ... 系统当前共安装有 215459 个文件和目录。)
正准备解包 sogoupinyin_2.4.0.3469_amd64.deb  ...
正在解包 sogoupinyin (2.4.0.3469) ...
正在设置 sogoupinyin (2.4.0.3469) ...
正在处理用于 gnome-menus (3.13.3-6ubuntu3.1) 的触发器 ...
正在处理用于 desktop-file-utils (0.22-1ubuntu5.2) 的触发器 ...
正在处理用于 bamfdaemon (0.5.3~bzr0+16.04.20180209-0ubuntu1) 的触发器 ...
Rebuilding /usr/share/applications/bamf-2.index...
正在处理用于 mime-support (3.59ubuntu1) 的触发器 ...
正在处理用于 hicolor-icon-theme (0.15-0ubuntu1.1) 的触发器 ...
```

> 注意：安装完成后需要注销系统或者重启系统才能生效。