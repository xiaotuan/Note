```shell
adb push update.zip data/
adb shell uncrypt data/update.zip cache/recovery/block.map
adb shell "echo \"--update_package=@/cache/recovery/block.map\" > /cache/recovery/command"
adb reboot recovery
```

