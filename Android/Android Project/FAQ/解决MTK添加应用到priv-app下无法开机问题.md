[toc]

### 1. 条件

MTK8766、Android R

### 2. 复现条件

在 `packages/apps/` 目录下创建一个工程，`Android.mk` 文件内容如下：

```makefile
LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE_TAGS := optional

LOCAL_SRC_FILES := $(call all-java-files-under, src)

LOCAL_JAVA_LIBRARIES := telephony-common


LOCAL_PACKAGE_NAME := StressTest
LOCAL_CERTIFICATE := platform
LOCAL_PRIVILEGED_MODULE := true
LOCAL_DEX_PREOPT := false  
LOCAL_PRIVATE_PLATFORM_APIS = true
#LOCAL_SDK_VERSION := current
include $(BUILD_PACKAGE)
```

编译后 `apk` 将会在 `system/priv-app` 目录下生成。

### 3. 现象

使用编译后的软件刷机，系统停在开机动画上，无法进入系统，过段时间后系统重启后进入 factory 模式。

### 4. 日志

```
08-24 03:24:52.816  4387  4387 E System  : ******************************************
08-24 03:24:52.817  4387  4387 E System  : ************ Failure starting system services
08-24 03:24:52.817  4387  4387 E System  : java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {com.cghs.stresstest (/system/priv-app/StressTest): android.permission.MOUNT_UNMOUNT_FILESYSTEMS, com.cghs.stresstest (/syst
em/priv-app/StressTest): android.permission.WRITE_MEDIA_STORAGE, com.cghs.stresstest (/system/priv-app/StressTest): android.permission.WRITE_SECURE_SETTINGS}
08-24 03:24:52.817  4387  4387 E System  :      at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:4814)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.server.pm.permission.PermissionManagerService.access$500(PermissionManagerService.java:182)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:4897)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21718)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.server.SystemServer.startOtherServices(SystemServer.java:2236)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.server.SystemServer.run(SystemServer.java:623)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.server.SystemServer.main(SystemServer.java:429)
08-24 03:24:52.817  4387  4387 E System  :      at java.lang.reflect.Method.invoke(Native Method)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:612)
08-24 03:24:52.817  4387  4387 E System  :      at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:975)
08-24 03:24:52.817  4387  4387 D SystemServerTiming: MakePackageManagerServiceReady took to complete: 321ms
```

### 5. 解决办法

`MTK` 这个版本如果应用安装目录是 `priv-app`，且使用到了系统权限，需要在 `frameworks/base/data/etc/privapp-permissions-platform.xml` 文件中使用下面格式把报错的系统权限添加进去：

```xml
<privapp-permissions package="应用包名">
    <permission name="系统权限"/>
</privapp-permissions>
```

最终代码如下所示：

```xml
<privapp-permissions package="com.cghs.stresstest">
    <permission name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
    <permission name="android.permission.WRITE_MEDIA_STORAGE"/>
    <permission name="android.permission.WRITE_SECURE_SETTINGS"/>
</privapp-permissions>
```

