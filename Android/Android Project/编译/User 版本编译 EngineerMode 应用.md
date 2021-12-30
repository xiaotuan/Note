[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

修改 `device/mediatek/system/common/device.mk` 文件：

```diff
@@ -3688,13 +3688,13 @@ ifeq ($(strip $(MSSI_MTK_ENGINEERMODE_APP)), yes)
     PRODUCT_PACKAGES += libem_wifi_jni
     PRODUCT_PACKAGES += libem_audio_jni
   else
-    ifneq ($(filter $(TARGET_BUILD_VARIANT),eng userdebug),)
+    # ifneq ($(filter $(TARGET_BUILD_VARIANT),eng userdebug),)
       PRODUCT_PACKAGES += EngineerMode
       PRODUCT_PACKAGES += libem_support_jni
       PRODUCT_PACKAGES += libem_usb_jni
       PRODUCT_PACKAGES += libem_wifi_jni
       PRODUCT_PACKAGES += libem_audio_jni
-    endif
+    # endif
   endif
```

