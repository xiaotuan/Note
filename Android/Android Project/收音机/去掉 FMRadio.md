[toc]

### 1. MTK

#### 1.1 MT8788

##### 1.1.1 Android S

修改 `device/mediatek/system/common/device.mk` 文件的如下代码：

```diff
@@ -3809,9 +3809,9 @@ ifeq ($(strip $(MSSI_MTK_SYSTEM_UPDATE_SUPPORT)), yes)
   endif
 endif
 
-ifeq ($(strip $(MSSI_MTK_FM_SUPPORT)), yes)
-  PRODUCT_PACKAGES += FMRadio
-endif
+#ifeq ($(strip $(MSSI_MTK_FM_SUPPORT)), yes)
+#  PRODUCT_PACKAGES += FMRadio
+#endif
 
 ifeq ($(strip $(MTK_CAM_LOMO_SUPPORT)), yes)
   PRODUCT_PACKAGES += libjni_lomoeffect
```

