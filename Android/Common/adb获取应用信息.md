可以使用下面命令获取已安装应用信息：

```shell
adb shell dumpsys package packagename
```

例如：

```shell
$ adb shell dumpsys package com.android.provision       
Activity Resolver Table:
  Non-Data Actions:
      android.intent.action.MAIN:
        418afc38 com.android.provision/.DefaultActivity filter 41c95a70
          Action: "android.intent.action.MAIN"
          Category: "android.intent.category.HOME"
          Category: "android.intent.category.DEFAULT"
          mPriority=1, mHasPartialTypes=false
        41c284a8 com.android.provision/.DefaultActivity filter 41b28f38
          Action: "android.intent.action.MAIN"
          Category: "android.intent.category.HOME"
          Category: "android.intent.category.DEFAULT"
          mPriority=1, mHasPartialTypes=false

Key Set Manager:
  [com.android.provision]
      Signing KeySets: 1

Packages:
  Package [com.android.provision] (41986af8):
    userId=10013 gids=[]
    pkg=Package{41f316e8 com.android.provision}
    codePath=/system/app/Provision_signed.apk
    resourcePath=/system/app/Provision_signed.apk
    nativeLibraryPath=/data/app-lib/Provision_signed
    versionCode=19 targetSdk=19
    versionName=4.4.2-eng.liangyangyang.20201231.151823
    applicationInfo=ApplicationInfo{41ec0490 com.android.provision}
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    dataDir=/data/data/com.android.provision
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2008-08-01 20:00:00
    firstInstallTime=2008-08-01 20:00:00
    lastUpdateTime=2008-08-01 20:00:00
    signatures=PackageSignatures{418982a0 [419d7600]}
    permissionsFixed=false haveGids=true installStatus=1
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    User 0:  installed=true blocked=false stopped=false notLaunched=false enabled=3
      lastDisabledCaller: shell:0
    grantedPermissions:
      android.permission.WRITE_SECURE_SETTINGS
      android.permission.WRITE_SETTINGS
```

