**1. `adb shell dumpsys package <packagename> | grep userId=`**

```shell
$ adb shell dumpsys package com.huawei.stb.tm | grep userId=
    userId=10025 gids=[3003, 1028, 1015]
```

**2. `adb shell cat /proc/<pid>/status | grep Uid`**

可以通过下面命令获取应用的 pid。

```shell
adb shell ps | grep <packagename>
```

```shell
$ adb shell ps | grep com.predict.horoscope.daily.zodiac.sign
u0_a96    1061  199   1614212 95232 ffffffff 00000000 S com.predict.horoscope.daily.zodiac.sign
```

第二列的值 1061 就是 PID。代入到获取 UID 的命令中的结果如下：

```shell
$ adb shell cat /proc/1061/status | grep Uid

Uid:	10096	10096	10096	10096 
```

**3. `adb shell cat /data/system/packages.xml | grep <packagename>`**

依次执行以下命令：

```shell
$ adb root
$ adb remount
$ adb shell cat /data/system/packages.xml | grep <packagename>
```

