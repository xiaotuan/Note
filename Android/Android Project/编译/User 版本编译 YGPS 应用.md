[toc]

### 1. MTK 平台

#### 1.1 MTK8766、Android R

##### 1.1.1 方法一

修改 `device/mediateksample/tb8788p1_64_bsp/ProjectConfig.mk` 文件中 MTK_AGPS_APP 宏的值为 yes:

```makfile
MTK_AGPS_APP = yes
```

##### 1.1.2 方法二

修改 `device/mediatek/system/common/device.mk` 文件：

```diff
@@ -3738,9 +3738,9 @@ endif
 ifneq ($(wildcard vendor/mediatek/internal/em_enable),)
   PRODUCT_PACKAGES += YGPS
 else
-  ifneq ($(filter $(TARGET_BUILD_VARIANT),eng userdebug),)
+  # ifneq ($(filter $(TARGET_BUILD_VARIANT),eng userdebug),)
     PRODUCT_PACKAGES += YGPS
-  endif
+  # endif
 endif
 
 ifeq ($(strip $(MSSI_MTK_LIVEWALLPAPER_APP)), yes)
```

