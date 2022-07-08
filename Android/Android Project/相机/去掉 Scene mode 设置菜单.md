[toc]

### 1. MTK 平台

#### 1.1 MTK8768

##### 1.1.1 Android S

修改 `vendor/mediatek/proprietary/packages/apps/Camera2/common/src/com/mediatek/camera/common/loader/FeatureLoader.java` 如下代码：

```diff
@@ -375,10 +375,12 @@ public class FeatureLoader {
         IFeatureEntry aisEntry = new AISEntry(context, context.getResources());
         aisEntry.setDeviceSpec(deviceSpec);
         entries.put(AIS, aisEntry);
-
+               
+               /*
         IFeatureEntry sceneModeEntry = new SceneModeEntry(context, context.getResources());
         sceneModeEntry.setDeviceSpec(deviceSpec);
         entries.put(SCENE_MODE, sceneModeEntry);
+               */
 
         IFeatureEntry whiteBalanceEntry = new WhiteBalanceEntry(context, context.getResources());
         whiteBalanceEntry.setDeviceSpec(deviceSpec);
```

