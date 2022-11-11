[toc]

### 1. MTK 平台

#### 1.1 MT8788

##### 1.1.1 Android S

修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/mediatek/settings/deviceinfo/CustomizeSoftwareUpdatePreferenceController.java` 文件如下代码：

```diff
diff --git a/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/mediatek/settings/deviceinfo/CustomizeSoftwareUpdatePreferenceController.java b/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/mediatek/settings/deviceinfo/CustomizeSoftwareUpdatePreferenceController.java
index 4a660b06bc4..2530b266836 100755
--- a/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/mediatek/settings/deviceinfo/CustomizeSoftwareUpdatePreferenceController.java
+++ b/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/mediatek/settings/deviceinfo/CustomizeSoftwareUpdatePreferenceController.java
@@ -42,11 +42,11 @@ public class CustomizeSoftwareUpdatePreferenceController extends AbstractPrefere
 
     @Override
     public boolean isAvailable() {
-        return true;//mUm.isAdminUser() && isCustomizedSoftwareUpdateAvalible();
+        return false;//mUm.isAdminUser() && isCustomizedSoftwareUpdateAvalible();
     }
 
     public static boolean isCustomizedSoftwareUpdateAvalible() {
-        return true;//FeatureOption.MTK_MDM_SCOMO || FeatureOption.MTK_SCOMO_ENTRY;
+        return false;//FeatureOption.MTK_MDM_SCOMO || FeatureOption.MTK_SCOMO_ENTRY;
     }
 
     @Override
```

