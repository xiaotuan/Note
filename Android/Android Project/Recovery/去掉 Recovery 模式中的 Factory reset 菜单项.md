[toc]

### 1. MTK

#### 1.1 MTK8768

#### 1.1.1 Android S

修改 `bootable/recovery/recovery_ui/device.cpp` 文件的如下代码：

```diff
@@ -32,7 +32,7 @@ static std::vector<std::pair<std::string, Device::BuiltinAction>> g_menu_actions
   { "Enter fastboot", Device::ENTER_FASTBOOT },
   { "Apply update from ADB", Device::APPLY_ADB_SIDELOAD },
   { "Apply update from SD card", Device::APPLY_SDCARD },
-  { "Wipe data/factory reset", Device::WIPE_DATA },
+//  { "Wipe data/factory reset", Device::WIPE_DATA },
   { "Wipe cache partition", Device::WIPE_CACHE },
   { "Mount /system", Device::MOUNT_SYSTEM },
   { "View recovery logs", Device::VIEW_RECOVERY_LOGS },
```

