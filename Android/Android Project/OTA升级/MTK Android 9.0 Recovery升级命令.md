```shell
adb push update_data.zip /data
adb shell uncrypt /data/update_data.zip /cache/recovery/block.map
adb shell "echo \"--update_package=@/cache/recovery/block.map\" > /cache/recovery/command"
adb reboot recovery
```

