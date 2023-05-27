[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `vendor/mediatek/proprietary/packages/apps/SystemUI/shared/src/com/android/systemui/shared/recents/utilities/Utilities.java` 类中 `isTablet()` 方法的如下代码：

```diff
@@ -133,7 +133,8 @@ public class Utilities {
 
         float smallestWidth = dpiFromPx(Math.min(bounds.width(), bounds.height()),
                 context.getResources().getConfiguration().densityDpi);
-        return smallestWidth >= TABLET_MIN_DPS;
+        //return smallestWidth >= TABLET_MIN_DPS;
+               return false;
     }
 
     public static float dpiFromPx(float size, int densityDpi) {
```

