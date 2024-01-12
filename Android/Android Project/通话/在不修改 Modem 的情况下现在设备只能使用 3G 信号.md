[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 修改 `device/mediateksample/tb8766p1_64_bsp/ProjectConfig.mk` 文件中的如下代码：

   ```diff
   @@ -232,8 +232,8 @@ MTK_PQ_VIDEO_WHITELIST_SUPPORT = no
    MTK_PRIVACY_PROTECTION_LOCK = yes
    MTK_PRODUCT_LINE = tablet
    MTK_PRODUCT_LINE_PLATFORM = MT8766
   -MTK_PROTOCOL1_RAT_CONFIG = Lf/Lt/W/G
   -MTK_PROTOCOL2_RAT_CONFIG = L/W/G
   +MTK_PROTOCOL1_RAT_CONFIG = W
   +MTK_PROTOCOL2_RAT_CONFIG = W
    MTK_PROTOCOL3_RAT_CONFIG = G
    MTK_PUMP_EXPRESS_PLUS_20_SUPPORT = no
    MTK_PUMP_EXPRESS_PLUS_SUPPORT = no
   ```

2. 修改 `sys/vendor/mediatek/proprietary/bootable/bootloader/lk/project/tb8766p1_64_bsp.mk` 文件中的如下代码：

   ```diff
   @@ -35,7 +35,7 @@ MTK_TINYSYS_SCP_SUPPORT = yes
    MTK_TINYSYS_SSPM_SUPPORT = yes
    #DEFINES += NO_POWER_OFF=y
    #DEFINES += FPGA_BOOT_FROM_LK=y
   -MTK_PROTOCOL1_RAT_CONFIG = Lf/Lt/W/G
   +MTK_PROTOCOL1_RAT_CONFIG = W
    MTK_GOOGLE_TRUSTY_SUPPORT = no
    MTK_EFUSE_WRITER_SUPPORT = no
    MTK_SMC_ID_MGMT = yes
   ```

3. 修改 `sys/vendor/mediatek/proprietary/scripts/check_dep/android_dep_rule.mak` 文件的如下代码：

   ```diff
   @@ -250,7 +250,8 @@ endif
    ###############################################################
    RAT_CONFIG := Lf/Lt/W/T/G Lf/Lt/W/G Lf/W/G Lt/T/G Lf/Lt/T/G W/T/G W/G T/G G \
                  C/Lf C/Lf/Lt/W/T/G C/Lf/Lt/W/G C/Lf/W/G C/Lf/Lt/G C/W/G Lf Lf/Lt no \
   -              N/C/Lf/Lt/W/T/G N/Lf/Lt/W/T/G N/Lf/Lt/W/G N/C/Lf/Lt/W/G N/C/Lt/T/G N/Lf/Lt
   +              N/C/Lf/Lt/W/T/G N/Lf/Lt/W/T/G N/Lf/Lt/W/G N/C/Lf/Lt/W/G N/C/Lt/T/G N/Lf/Lt \
   +              W
    ifneq (,$(strip $(MTK_PROTOCOL1_RAT_CONFIG)))
      ifeq (,$(filter $(strip $(RAT_CONFIG)),$(strip $(MTK_PROTOCOL1_RAT_CONFIG))))
        $(call dep-err-common, MTK_PROTOCOL1_RAT_CONFIG = $(MTK_PROTOCOL1_RAT_CONFIG) is invalid, \
   ```

   

