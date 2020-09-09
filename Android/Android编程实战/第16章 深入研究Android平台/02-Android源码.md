`Android` 开源项目（AOSP）是针对 `Android` 平台的公开可用的源代码，网址为：<http://source.android.com/>。

**设置构建环境**

开发者可在 <http://source.android.com/source/initializing.html> 找到设置 AOSP 构建环境的最新指南。

由于 OS X 默认的分区是不区分大小写的，所以对于 Mac OS X，开发者需要创建一个新的区分大小写的磁盘映象。

**Nexus 二进制文件**

`Galaxy Nexus` 手机的图形驱动程序是 `Imagination Technologies` 公司的专用库，它的源代码并没有被公开。因此，在构建自定义固件前还需要下载所有必要的二进制驱动程序。<https://developers.google.com/android/nexus/drivers> 上有可用的驱动程序列表。

接下来下载所有设备可用的二进制驱动程序，并把它放在刚才下载的 `Android` 平台项目的根目录中。运行下面的命令提取归档文件，这时会提示许可协议：

```shell
$ tar xzvf imgtec-maguro-jdq39-bb3c4e4e.tgz
x extract-imgtec-maguro.sh
$ sh ./extract-imgtec-maguro.sh

The license for this software will now be displayed. 

You must agree to this license before using this software.

-n Press Enter to view the license
```

**构建并刷新固件**

在这之前请确保安装并配置好了 ccache (见 <http://source.android.com/source/initializing.html#setting-up-ccache>)，因为它可以加速后续的构建过程。

首先，开发者需要把构建环境加载到当前的 shell 中，并告诉构建系统需要构建的设备和配置。

```shell
$ source build/envsetup.sh
$ lunch full_maguro-userdebug
```

为了加快速度，给 make 命令提供 `-jN` 参数可以指示构建系统使用额外的线程，其中 N 是电脑支持的硬件线程数的 2 倍。一般情况下，每个 CPU 核心（使用超线程）可以支持两个硬件线程，因此一个四核 CPU 电脑可以支持 8 个线程。

```shell
$ make -j8
```

构建成功后可以重启到快速启动模式，然后给设备刷新固件。

```shell
$ adb reboot-bootloader
$ fastboot flashall -w
```

这个过程完成后设备会使用新的固件启动。在终端运行下面的命令来确认获取了 root 权限：

```shell
$ adb root
restarting adbd as root
$ adb remount
remount successed
$ adb shell
root@android:/ #
```

