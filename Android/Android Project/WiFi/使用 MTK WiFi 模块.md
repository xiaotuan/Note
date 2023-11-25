[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android S

修改 `sys/device/mediatek/system/common/device.mk` 文件中的如下代码：

```diff
@@ -3931,7 +3931,7 @@ ifneq ($(wildcard vendor/partner_modules/build),)
     MAINLINE_COMPRESS_APEX_ALL := false
     # any one of these two can be changed but additional patches might be required
     # check the known issues section below.
-    MAINLINE_INCLUDE_WIFI_MODULE := true
+    MAINLINE_INCLUDE_WIFI_MODULE := false
     MAINLINE_INCLUDE_UWB_MODULE := true
 
     ifneq ($(strip $(MTK_GMO_RAM_OPTIMIZE)), yes)
```

