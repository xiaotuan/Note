**问题描述：**

项目是 WIFI ONLY 项目，不带 SIM 卡槽，在开机进入开机向导后，会弹出 "连接到移动网络" 界面。

**问题原因：**

在配置 WIFI ONLY 项目时没有配置好，通话功能未去掉造成的。可以参考 `vendor/mediatek/release_note/MT8788/ReleaseNote_for_MT8788_alps-mp-s0.mp1.rc.xlsx` 文件检查项目配置。

**解决办法：**

修改 `device/mediateksample/tb8788p1_64_bsp_k419/android.hardware.telephony.gsm.xml` 文件的如下代码：

```diff
@@ -16,6 +16,6 @@
 
 <!-- This is the standard set of telephony features for a GSM phone. -->
 <permissions>
-    <feature name="android.hardware.telephony" />
-    <feature name="android.hardware.telephony.gsm" />
+    <!--feature name="android.hardware.telephony" />
+    <feature name="android.hardware.telephony.gsm" /-->
 </permissions>
```

