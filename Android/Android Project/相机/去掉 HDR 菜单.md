[tcoc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `vendor/mediatek/proprietary/packages/apps/Camera2/feature/setting/hdr/src/com/mediatek/camera/feature/setting/hdr/HdrEntry.java` 文件中 `isSupport(CameraApi currentCameraApi, Activity activity)` 方法的如下代码：

```diff
@@ -69,11 +69,16 @@ public class HdrEntry extends FeatureEntryBase {
 
     @Override
     public boolean isSupport(CameraApi currentCameraApi, Activity activity) {
+               // Remove Camera HDR option by qty {{&&
+               /*
         boolean support =(!isThirdPartyIntent(activity))
                 && (CameraUtil.getAppVersionLevel() != MTK_CAMERA_APP_VERSION_FOUR
                 && CameraUtil.getAppVersionLevel() != MTK_CAMERA_APP_VERSION_FIVE
                 && CameraUtil.getAppVersionLevel() != MTK_CAMERA_APP_VERSION_SIX);
         return support;
+               */
+               return false;
+               // &&}}
     }
 
     @Override
```

