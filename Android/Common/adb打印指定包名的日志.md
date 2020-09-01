下面以包名为 "net.sunniwell.app.swsettings" 所为示例：

1. 获取包名对应的应用的进程 PID:

```shell
$ adb shell ps | grep "net.sunniwell.app.swsettings"
system    2634  1572  539088 59752 ffffffff 4014480c S net.sunniwell.app.swsettings
```

> PID 为第2项的值，即 2634

2. 打印指定包名的日志：

```shell
$ adb logcat | grep -E "2634"
```

如果需要打印多个包名对应的日志，可以使用如下命令：

```shell
$ adb logcat | grep -E "2634|3425" # 多个 PID 使用 | 分隔
```

