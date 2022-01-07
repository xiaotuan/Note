[toc]

### 1. 获取设备信息

执行下面命令获取设备信息：

```shell
$ lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 011: ID 0e8d:201c MediaTek Inc. 
Bus 001 Device 002: ID 80ee:0021 VirtualBox USB Tablet
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

### 2. 修改或添加 udev 规则文件

执行下面命令打开或创建一个名为 `51-android.rules` 的文件：

```shell
$ sudo vi /etc/udev/rules.d/51-android.rules
```

在文件中添加如下内容：

```shell
SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666"
```

### 3. 修改 udev 规则文件权限

```shell
$ chmod a+rx /etc/udev/rules.d/51-android.rules
```

### 4. 重启 udev 服务

```shell
$ sudo service udev restart
```

### 5. 重启 adb

```shell
$ adb kill-server
$ adb start-server
```

