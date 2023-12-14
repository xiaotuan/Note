可以通过下面命令在 Android 14 系统上安装低版本 apk：

```shell
adb install --bypass-low-target-sdk-block APK路径
```

例如：

```shell
$ adb install --bypass-low-target-sdk-block batterylog.apk
Performing Streamed Install
Success
```

