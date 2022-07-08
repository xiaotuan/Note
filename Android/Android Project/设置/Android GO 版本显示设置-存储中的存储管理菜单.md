[toc]

### 1. MTK

#### 1.1 MTK8768

##### 1.1.1 Android S

修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/deviceinfo/storage/AutomaticStorageManagementSwitchPreferenceController.java` 文件中的如下代码：

```diff
@@ -70,7 +70,7 @@ public class AutomaticStorageManagementSwitchPreferenceController extends
         if (!mContext.getResources().getBoolean(R.bool.config_show_smart_storage_toggle)) {
             return UNSUPPORTED_ON_DEVICE;
         }
-        return !ActivityManager.isLowRamDeviceStatic() ? AVAILABLE : UNSUPPORTED_ON_DEVICE;
+        return AVAILABLE;      // !ActivityManager.isLowRamDeviceStatic() ? AVAILABLE : UNSUPPORTED_ON_DEVICE;
     }
 
     @Override
```

