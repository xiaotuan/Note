[toc]

### 1. MTK

#### 1.1 MT8788

##### 1.1.1 Android T

处理同时按下两个按键的类为 `sys/frameworks/base/services/core/java/com/android/server/policy/KeyCombinationManager.java`

解决这个问题的方法如下：

修改 `vendor/mediatek/proprietary/packages/apps/SettingsProvider/src/com/android/providers/settings/DatabaseHelper.java` 文件，在  `loadSecureSettings()` 方法中添加如下代码：

```diff
@@ -2410,6 +2410,10 @@ class DatabaseHelper extends SQLiteOpenHelper {
 
             loadIntegerSetting(stmt, Settings.Secure.SLEEP_TIMEOUT,
                     R.integer.def_sleep_timeout);
+                                       
+                       // Long press the volume up and down buttons to open the Talkback function by qty at 2023-04-17 {{&&
+                       loadSetting(stmt, Settings.Secure.ACCESSIBILITY_SHORTCUT_TARGET_SERVICE, "com.google.android.marvin.talkback/.TalkBackService");
+                       // &&}}
 
             /// M: Load MTK added Secure providers before Android M.
             mUtils.loadCustomSecureSettings(stmt);
```

