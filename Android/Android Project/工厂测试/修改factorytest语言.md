[toc]

### 1. 展讯平台

#### 1.1 Android R

修改 `vendor/sprd/proprietories-source/factorytest/Android.mk`文件，将文件中如下代码：

```makefile
LOCAL_CFLAGS += -DLANGUAGE_CN
```

注释或者去掉即可。

### 2. MTK 平台

#### 2.1 MTK8766、Android R

修改 `device/mediateksample/m863u_bsp_64/ProjectConfig.mk` 中 `MTK_FACTORY_MODE_IN_GB2312` 宏的值为 `no` 即可。

```diff
@@ -240,7 +240,7 @@ MTK_EXTERNAL_SIM_ONLY_SLOTS = 0
 MTK_EXTERNAL_SIM_SUPPORT = no
 MTK_EXTMD_NATIVE_DOWNLOAD_SUPPORT = no
 MTK_FACEBEAUTY_SUPPORT = yes
-MTK_FACTORY_MODE_IN_GB2312 = yes
+MTK_FACTORY_MODE_IN_GB2312 = no
 MTK_FACTORY_RESET_PROTECTION_SUPPORT = yes
 MTK_FAN5402_SUPPORT = no
 MTK_FAN5405_SUPPORT = no
```

