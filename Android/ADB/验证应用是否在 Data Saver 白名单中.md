通过如下代码可以查看应用是否在 `Data Saver` 白名单中：

```shell
adb shell "dumpsys package [Package_Name] | grep userId"
adb shell "cmd netpolicy list restrict-background-whitelist"
```

例如：

```shell
$ adb shell "dumpsys package com.dti.xw | grep userId"
    userId=10117

$ adb shell "cmd netpolicy list restrict-background-whitelist"
Restrict background whitelisted UIDs: 10039 10117 10118 10121
```

