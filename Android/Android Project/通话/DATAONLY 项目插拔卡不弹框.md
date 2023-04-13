[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/frameworks/base/core/res/res/values/config.xml` 文件的如下代码：

```diff
@@ -1281,7 +1281,7 @@
     <bool name="config_enableLockScreenRotation">false</bool>
 
     <!-- Is the device capable of hot swapping an UICC Card -->
-    <bool name="config_hotswapCapable">false</bool>
+    <bool name="config_hotswapCapable">true</bool>
 
     <!-- Component name of the ICC hotswap prompt for restart dialog -->
     <string name="config_iccHotswapPromptForRestartDialogComponent" translatable="false">@null</string>
```

