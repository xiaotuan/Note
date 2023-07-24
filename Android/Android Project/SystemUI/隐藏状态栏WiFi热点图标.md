[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/android/systemui/statusbar/phone/PhoneStatusBarPolicy.java` 文件如下代码：

```diff
@@ -307,7 +307,10 @@ public class PhoneStatusBarPolicy
         // hotspot
         mIconController.setIcon(mSlotHotspot, R.drawable.stat_sys_hotspot,
                 mResources.getString(R.string.accessibility_status_bar_hotspot));
-        mIconController.setIconVisibility(mSlotHotspot, mHotspot.isHotspotEnabled());
+        // Hide the WiFi hotspot icon by qty {{&&
+        // mIconController.setIconVisibility(mSlotHotspot, mHotspot.isHotspotEnabled());
+        mIconController.setIconVisibility(mSlotHotspot, false);
+        // &&}}
 
         // managed profile
         updateManagedProfile();
@@ -606,7 +609,10 @@ public class PhoneStatusBarPolicy
     private final HotspotController.Callback mHotspotCallback = new HotspotController.Callback() {
         @Override
         public void onHotspotChanged(boolean enabled, int numDevices) {
-            mIconController.setIconVisibility(mSlotHotspot, enabled);
+            // Hide the WiFi hotspot icon by qty {{&&
+            // mIconController.setIconVisibility(mSlotHotspot, enabled);
+            mIconController.setIconVisibility(mSlotHotspot, false);
+            // &&}}
         }
     };
 
```

