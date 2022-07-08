[toc]

### 1. MTK

#### 1.1 MTK8768

##### 1.1.1 Android S

修改 `vendor/mediatek/proprietary/packages/overlay/vendor/FrameworkResOverlay/ago/res/values/config.xml` 文件的如下代码：

```diff
@@ -21,7 +21,7 @@
 
     <!-- Disable multiuser for AGO projects -->
     <integer name="config_multiuserMaximumUsers">4</integer>
-    <bool name="config_enableMultiUserUI">false</bool>
+    <bool name="config_enableMultiUserUI">true</bool>
 
     <!-- Launcher - enable gesture navigation -->
     <bool name="config_swipe_up_gesture_setting_available">false</bool>
@@ -32,5 +32,11 @@
 
     <!-- Launcher - configure 16-bit task snapshots -->
     <bool name="config_use16bittasksnapshotpixelformat">true</bool>
+       
+       <!-- Set to true to enable the user switcher on the keyguard. -->
+    <bool name="config_keyguardUserSwitcher">true</bool>
+
+    <!-- If true, show multiuser switcher by default unless the user specifically disables it. -->
+    <bool name="config_showUserSwitcherByDefault">true</bool>
 
 </resources>
```

