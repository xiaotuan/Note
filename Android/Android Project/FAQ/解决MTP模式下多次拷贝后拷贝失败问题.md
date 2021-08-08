[toc]

### 1. 条件

平台：展讯 S9863A

系统：Android Go

内存：2GB

### 2. 问题复现步骤

1.1 使用 USB 线将设备连接电脑。

1.2 在设备上选择 MTP 模式。

1.3 将电脑上的文件拷贝到设备中，当拷贝完成后继续拷贝，多次执行后无法再拷贝文件。

> 注意：在拷贝文件的过程中，未操作设备和数据线，屏幕会在一段时间后灭屏。

### 3. 分析原因

经过分析日志，发现 MTP 服务被低内存杀死了。

```
M027042  07-25 11:01:52.060   290   290 I lowmemorykiller: Kill 'android.process.media' (2334), uid 10089, oom_adj 500 to free 24508kB; reason: device is not responding
M02A1CB  07-25 11:35:01.575   290   290 I lowmemorykiller: Kill 'android.process.media' (6488), uid 10089, oom_adj 500 to free 21372kB; reason: device is not responding
M02E4E0  07-25 12:29:04.224   290   290 I lowmemorykiller: Kill 'android.process.media' (9692), uid 10089, oom_adj 800 to free 38452kB; reason: device is not responding
```

MTP 服务日志如下：

```
M026C7D  07-25 10:59:32.818  2334 24260 D MtpServer: receive mRequest with operation: MTP_OPERATION_SEND_OBJECT
M026EDC  07-25 11:01:23.461  2334  7349 D MtpServer: sending event 4007 handle: 0214
M026EDD  07-25 11:01:23.461  2334  7349 E MtpServer: Mtp send event failed: Device or resource busy   //设备忙
M026EDE  07-25 11:01:23.463  2334  7349 D MtpServer: sending event 4007 handle: 0215
M026EDF  07-25 11:01:23.463  2334  7349 E MtpServer: Mtp send event failed: Device or resource busy
M026EE0  07-25 11:01:23.464  2334  7349 D MtpServer: sending event 4007 handle: 0214
M026EE1  07-25 11:01:23.464  2334  7349 E MtpServer: Mtp send event failed: Device or resource busy
M026EE2  07-25 11:01:23.464  2334  7349 D MtpServer: sending event 4007 handle: 0213
M026EE3  07-25 11:01:23.464  2334  7349 E MtpServer: Mtp send event failed: Device or resource busy
S027400  07-25 11:02:54.359   761  5829 W ActivityManager: Scheduling restart of crashed service com.android.mtp/.MtpService in 1931506ms for start-requested
S027400  07-25 11:02:54.359   761  5829 W ActivityManager: Scheduling restart of crashed service com.android.mtp/.MtpService in 1931506ms for start-requested
```

### 4. 解决方法

将 MTP 服务添加到白名单中，在低内存时尽量不杀死服务，代码修改如下所示：

4.1 修改 `frameworks/base/data/etc/Android.bp` 文件

在如下代码：

```
prebuilt_etc {
    name: "privapp_whitelist_com.sprd.ImsConnectionManager",
    system_ext_specific: true,
    sub_dir: "permissions",
    src: "com.sprd.ImsConnectionManager.xml",
    filename_from_src: true,
}

// 在此次修改代码

prebuilt_etc {
    name: "com.android.timezone.updater.xml",
    sub_dir: "permissions",
    src: "com.android.timezone.updater.xml",
}
```

中 `// 在此次修改代码` （源代码不包含这些字符）位置添加如下代码：

```
prebuilt_etc {
    name: "privapp_whitelist_com.android.mtp",
    sub_dir: "permissions",
    src: "com.android.mtp.xml",
    filename_from_src: true,
}
```

4.2 添加 `frameworks/base/data/etc/com.android.mtp.xml` 文件

文件内容如下所示：

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
  ~ Copyright (C) 2019 The Android Open Source Project
  ~
  ~ Licensed under the Apache License, Version 2.0 (the "License");
  ~ you may not use this file except in compliance with the License.
  ~ You may obtain a copy of the License at
  ~
  ~      http://www.apache.org/licenses/LICENSE-2.0
  ~
  ~ Unless required by applicable law or agreed to in writing, software
  ~ distributed under the License is distributed on an "AS IS" BASIS,
  ~ WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  ~ See the License for the specific language governing permissions and
  ~ limitations under the License
  -->
<permissions>
    <privapp-permissions package="com.android.mtp">
        <permission name="sprd.permission.PROTECT_PROCESS"/>
    </privapp-permissions>
</permissions>
```

4.3 修改 `packages/services/Mtp/Android.bp` 文件

在如下代码：

```
android_app {
    name: "MtpService",

    static_libs: [
        "androidx.appcompat_appcompat",
    ],
    // 在此处修改代码
    srcs: ["src/**/*.java"],
    platform_apis: true,
    certificate: "media",
    privileged: true,
    optimize: {
        proguard_flags_files: ["proguard.flags"],
    },
}
```

中 `// 在此次修改代码` （源代码不包含这些字符）位置添加如下代码：

```
libs: [
	"com.unisoc.sdk.common",
],
required: ["privapp_whitelist_com.android.mtp"],
```

最终代码如下所示：

```
android_app {
    name: "MtpService",

    static_libs: [
        "androidx.appcompat_appcompat",
    ],
    libs: [
        "com.unisoc.sdk.common",
    ],
    required: ["privapp_whitelist_com.android.mtp"],
    srcs: ["src/**/*.java"],
    platform_apis: true,
    certificate: "media",
    privileged: true,
    optimize: {
        proguard_flags_files: ["proguard.flags"],
    },
}
```

4.4 修改 `packages/services/Mtp/AndroidManifest.xml` 文件

在如下代码：

```xml
<application
             android:process="android.process.media"
             android:label="@string/app_label"
             android:allowBackup="false"
             android:usesCleartextTraffic="true">
    <!-- 在此处修改代码 -->
    <provider
              android:name=".MtpDocumentsProvider"
              android:authorities="com.android.mtp.documents"
              android:grantUriPermissions="true"
              android:exported="true"
              android:permission="android.permission.MANAGE_DOCUMENTS">
        <intent-filter>
            <action android:name="android.content.action.DOCUMENTS_PROVIDER" />
        </intent-filter>
    </provider>
```

中 `在此次修改代码` （源代码不包含这些字符）位置添加如下代码：

```xml
<uses-library android:name="com.unisoc.sdk.common" android:required="false"/>
```

4.5 如果存在 `vendor/sprd/tools/ussi_build` 目录，则需要修改下面文件

4.5.1 修改 `vendor/sprd/tools/ussi_build\artifacts.arm.go.gms.user.mk` 文件

在如下代码：

```makefile
system/etc/permissions/com.android.location.provider.xml \
system/etc/permissions/com.android.media.remotedisplay.xml \
system/etc/permissions/com.android.mediadrm.signer.xml \
# 在此处修改
system/etc/permissions/com.unisoc.sdk.common.xml \
system/etc/permissions/gms_express_feature.xml \
system/etc/permissions/javax.obex.xml \
```

在 `在此处修改`  处添加如下代码：

```makefile
system/etc/permissions/com.android.mtp.xml \
```

在如下代码：

```makefile
system/lib/libdisplayservicehidl.so \
system/lib/libdng_sdk.so \
system/lib/libdrmframework.so \
system/lib/libdrmframework_jni.so \
# 在此处修改
system/lib/libdumpstateaidl.so \
system/lib/libdumpstateutil.so \
system/lib/libdumputils.so \
```

在 `在此处修改`  处添加如下代码（如果已存在则不需要修改）：

```makefile
system/lib/libdrmframeworkcommon.so \
```

4.5.2 修改 `vendor/sprd/tools/ussi_build/` 目录下的`artifacts.arm.go.gms.userdebug.mk` 、`artifacts.arm64.full.gms.userdebug.mk` 和 `artifacts.arm64.full.gms.userdebug.mk` 文件，修改方法同 4.5.1 修改方法一样。

4.5.3 修改 `vendor/sprd/tools/ussi_build/whitelists.mk` 文件

在如下代码:

```makefile
system/bin/performancemanager \
system/etc/init/performancemanager.rc \
system/app/IfaaManagerService/IfaaManagerService.apk \
```

后面添加如下代码：

```makefile
system/etc/permissions/com.android.mtp.xml \
```



