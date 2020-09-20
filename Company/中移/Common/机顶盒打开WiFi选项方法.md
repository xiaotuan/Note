**朝歌盒子打开 WiFi**

```shell
$ adb shell settings put secure hide_settings_wifi_cfg 0
```

**长虹盒子打开 WiFi**

1. 检查盒子是否支持 WiFi

   ```shell
   $ cat /sys/bus/sdio/devices/*/uevent | grep SDIO_ID
   ```

   在 `adb shell` 里面执行下这个命令，看看有没有值
   如果有值，就表示有模块，没有值，就表示没有模块

2. 支持` WiFi` 的如何打开？
   网络设置界面上，按 8 次遥控器左键，就能显示出选项