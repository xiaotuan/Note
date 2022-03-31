[toc]

### 1. MTK 平台

#### 1.1 MTK8766、Android R

修改 `frameworks/base/core/res/res/values/config.xml` 文件中 `config_dozeComponent` 的值为 `com.android.systemui/com.android.systemui.doze.DozeService`：

```xml
<string name="config_dozeComponent" translatable="false">com.android.systemui/com.android.systemui.doze.DozeService</string>
```

#### 1.2 MTK8766、Android S

修改 `vendor/mediatek/proprietary/packages/overlay/vendor/FrameworkResOverlay/aod_support/res/values/config.xml` 文件的如下内容：

```diff
@@ -27,7 +27,7 @@
 
          Note that doze dreams are not subject to the same start conditions as ordinary dreams.
          Doze dreams will run whenever the power manager is in a dozing state. -->
-    <string name="config_dozeComponent" translatable="false">com.android.dreams.alwaysondisplay/.AlwaysOnDisplay</string>
+    <string name="config_dozeComponent" translatable="false">com.android.systemui/com.android.systemui.doze.DozeService</string>^M
 
     <!-- If true, the doze component is not started until after the screen has been
          turned off and the screen off animation has been performed. -->
```

