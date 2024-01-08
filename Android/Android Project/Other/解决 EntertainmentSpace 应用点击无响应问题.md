[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

点击 EntertainmentSpace 娱乐负一屏中的按钮，系统报如下错误：
```shell
E ActivityTaskManager: Abort background activity starts from 10043
```

可以通过修改 `u_sys/frameworks/base/services/core/java/com/android/server/wm/BackgroundActivityStartController.java` 文件中 `checkBackgroundActivityStart()` 方法的如下代码解决：

```diff
@@ -215,6 +215,11 @@ public class BackgroundActivityStartController {
                 return logStartAllowedAndReturnCode(BAL_ALLOW_ALLOWLISTED_UID, /*background*/ false,
                         callingUid, realCallingUid, intent, "Important callingUid");
             }
+            
+            // Allow special application to start activities
+            if (callingPackage.equals("com.google.android.apps.mediahome.launcher")) {
+                return logStartAllowedAndReturnCode(BAL_ALLOW_PERMISSION,false, callingUid, realCallingUid, intent,"Special app");
+            }
 
             // Always allow home application to start activities.
             if (isHomeApp(callingUid, callingPackage)) {
```

也可以通过在应用中添加 `android.permission.START_ACTIVITIES_FROM_BACKGROUND` 权限来解决，但是这是谷歌应用无法修改源代码。