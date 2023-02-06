在 Android 13 中，桌面底部图标在竖屏状态下显示不全，解决方法如下：

修改 `sys/packages/apps/Launcher3/res/xml/device_profiles.xml` 文件如下代码：

```xml
@@ -197,7 +197,7 @@
             launcher:allAppsBorderSpaceHorizontal="8"
             launcher:allAppsBorderSpaceVertical="16"
             launcher:allAppsBorderSpaceLandscape="16"
-            launcher:hotseatBorderSpace="58"
+            launcher:hotseatBorderSpace="47"
             launcher:hotseatBorderSpaceLandscape="50.4"
             launcher:canBeDefault="true" />
```

