**系统版本：**Android 11.0    

**平         台：**RK3568

在 Android 系统的开发及适配过程中，我们常常需要对 SELinux avc  权限进行修改，以下是我对 SELinux avc  权限修改总结的方法。

### 一、验证功能是否存在 selinux 权限问题
**获取root权限**

```shell
adb root
```

**进入Android终端**

```shell
adb shell
```

**查看系统当前 selinux 的工作模式**

```shell
getenforce
```

**将 selinux 切换为 Enforcing 强制模式**

```shell
setentforce 1
```

**验证功能并打印log**

例如，让 app 通过接口对节点进行读写操作，发现 log 报以下 selinux avc 权限错误：

```
type=1400 audit(0.0:875): avc: denied { read } for name="value" dev="sysfs" ino=29545 scontext=u:r:system_server:s0 tcontext=u:object_r:sysfs:s0 tclass=file permissive=0

type=1400 audit(0.0:876): avc: denied { write } for name="value" dev="sysfs" ino=29545 scontext=u:r:system_server:s0 tcontext=u:object_r:sysfs:s0 tclass=file permissive=0
```

### 二、SELinux avc权限规则快速生成配置

(1) 收集相关 selinux avc 权限的 log，并存放在一个文件中，如：log；

(2) 平台代码根目录下打开终端，执行以下命令 ：

**初始化参数设置**

```shell
source build/envsetup.sh
```

**选择lunch并读取目标配置和平台信息**

```shell
lunch
```

(3) 生成的 selinux avc 权限配置信息

**将 log 文件拷贝并切换终端到以下路径中：**

```shell
external/selinux/prebuilts/bin
```

**输出selinux avc权限配置信息**

```shell
./audit2allow -i log > audio.txt
```

执行以上命令可将生成的 avc 权限配置信息输出到 audio.txt 文件。例如，输出信息如下：

```
#============= system_server ==============
allow system_server sysfs:file { read write };
```

>  注意：如果生成的信息为空的话，多放几条log即可

(4) 加上 open 和 getattr 权限

> 注意，读写等 avc 权限的配置，往往还需要 open 和 getattr 权限，应当手动加上，例如:
>
> ```
> allow system_server sysfs:file { write read open getattr};
> ```

如果不加就可能报以下错误：

```
type=1400 audit(0.0:604): avc: denied { getattr } for path="/sys/devices/platform/fdd60000.gpio/gpiochip0/gpio/gpio27/value" dev="sysfs" ino=29545 scontext=u:r:system_server:s0 tcontext=u:object_r:sysfs:s0 tclass=file permissive=0
```

(5) selinux avc 权限配置信息添加位置

```
device/rockchip/common/sepolicy/vendor/
```

例如，这里是在该目录下的 system_server.te 文件添加。此外,还需要对对应api等级的相同文件进行一样的修改：

```
system/sepolicy/prebuilts/api/30.0/private/coredomain.te
```

### 三、编译及验证
(1) 编译

在根目录下编译 /system/sepolicy/ 中的文件，编译命令如下：

```shell
mmm /system/sepolicy/
```

(2) 验证

将编译好的文件从电脑推送到Android设备，以下推送命令（注意目录下存在mapping的需要删掉）：

```shell
adb push odm/etc/selinux/* odm/etc/selinux
adb push product/etc/selinux/* product/etc/selinux
adb push system/etc/selinux/* system/etc/selinux
adb push system_ext/etc/selinux/* system_ext/etc/selinux
adb push vendor/etc/selinux/* vendor/etc/selinux
adb reboot
```

### 四、常见编译错误

例如：

```
libsepol.report_failure: neverallow on line 99 of system/sepolicy/private/coredomain.te (or line 36611 of policy.conf) violated by allow system_server sysfs:file { read write open };

libsepol.check_assertions: 1 neverallow failures occurred
Error while expanding policy
```

即上述修改的权限被 neverallow，具体位置在 /system/sepolicy/private/coredomain.te 中第99行，对以上报错的修改如下：

```diff
--- a/sepolicy/private/coredomain.te
+++ b/sepolicy/private/coredomain.te
@@ -111,6 +111,7 @@ full_treble_only(`
    # /sys
    neverallow {
    coredomain
     -init
     -ueventd
     -vold

+    -system_server
     -system_app
     } sysfs:file no_rw_file_perms;
```