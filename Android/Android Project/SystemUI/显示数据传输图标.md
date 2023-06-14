[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/config.xml` 文件如下代码：

```diff
diff --git a/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/config.xml b/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/config.xml
index 1a89f12e5c4..ecf028bceb9 100644
--- a/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/config.xml
+++ b/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/config.xml
@@ -334,7 +334,7 @@
     <bool name="config_enableNotificationShadeDrag">true</bool>
 
     <!-- Whether to show activity indicators in the status bar -->
-    <bool name="config_showActivity">false</bool>
+    <bool name="config_showActivity">true</bool>
 
     <!-- Whether or not the button to clear all notifications will be shown. -->
     <bool name="config_enableNotificationsClearAll">true</bool>
```

