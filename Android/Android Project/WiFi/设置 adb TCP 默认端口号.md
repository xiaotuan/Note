[toc]

### 1. MTK

#### 1.1 Android 12

##### 1.1.1 MT8788

修改 `device/mediateksample/tb8788p1_64_bsp_k419/device.mk` 文件的如下代码：

```diff
@@ -204,6 +204,8 @@ ifeq ($(strip $(MTK_HDMI_SUPPORT)), yes)
     DEVICE_MANIFEST_FILE += device/mediatek/common/project_manifest/manifest_hdmi.xml
 endif
 
+PRODUCT_SYSTEM_DEFAULT_PROPERTIES += service.adb.tcp.port=5555
+
 $(call inherit-product, device/mediatek/mt6771/device.mk)
 
 $(call inherit-product-if-exists, vendor/mediatek/libs/$(MTK_TARGET_PROJECT)/device-vendor.mk)
```

