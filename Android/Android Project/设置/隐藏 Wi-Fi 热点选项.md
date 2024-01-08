[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/wifi/tether/WifiTetherSettings.java` 文件中的如下代码：

```diff
@@ -315,7 +315,10 @@ public class WifiTetherSettings extends RestrictedDashboardFragment
 
         @Override
         protected boolean isPageSearchEnabled(Context context) {
-            return !FeatureFlagUtils.isEnabled(context, FeatureFlags.TETHER_ALL_IN_ONE);
+            // The Wi-Fi hotspot function is disabled by qty {{&&
+            // return !FeatureFlagUtils.isEnabled(context, FeatureFlags.TETHER_ALL_IN_ONE);
+            return false;
+            // &&||
         }
 
         @Override
```

##### 1.1.2 Android U

修改 `u_sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/wifi/WifiUtils.java` 文件中 `checkShowWifiHotspot()` 方法的如下代码：

```diff
@@ -259,6 +259,8 @@ public class WifiUtils extends com.android.settingslib.wifi.WifiUtils {
      * @return true if Wi-Fi hotspot settings can be displayed
      */
     public static boolean checkShowWifiHotspot(Context context) {
+        return false;
+        /*
         if (context == null) return false;
 
         boolean showWifiHotspotSettings =
@@ -285,6 +287,7 @@ public class WifiUtils extends com.android.settingslib.wifi.WifiUtils {
             return false;
         }
         return true;
+        */
     }
 
     /**
```

