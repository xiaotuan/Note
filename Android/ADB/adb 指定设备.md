可以使用如下格式指定 adb 操作的设备：

```shell
adb -s 设备序列号 shell
```

例如：

```shell
$ adb devices
List of devices attached
C1NGA1E7A3103718        device
$ adb -s C1NGA1E7A3103718 shell
```

