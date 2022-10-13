[toc]

### 1. MTK 平台

#### 1.1 MT8766

##### 1.1.1 Android 12

去掉 Settings -> System -> Reset options -> Erase downloaded SIMs 选项代码如下：

```diff
--- a/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/network/EraseEuiccDataController.java
+++ b/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/network/EraseEuiccDataController.java
@@ -50,6 +50,9 @@ public class EraseEuiccDataController extends BasePreferenceController {
 
     @Override
     public int getAvailabilityStatus() {
-        return AVAILABLE_UNSEARCHABLE;
+               // Hide Erase downloaded SIMs item by qty at 2022-10-13 {{&&
+        // return AVAILABLE_UNSEARCHABLE;
+               return UNSUPPORTED_ON_DEVICE;
+               // &&}}
     }
 }
```

