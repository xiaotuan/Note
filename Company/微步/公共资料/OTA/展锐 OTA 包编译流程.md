[toc]

### 1. 修改代码

   1.1 请确保 `prebuilts/sdk/30/unisoc/aip/` 目录下的 `current.txt` 和 `unisoc-hidden-current.txt` 文件内容与 `frameworks/base/api/` 目录下的  `current.txt` 和 `unisoc-hidden-current.txt` 文件内容保持一致。

   移植红石 Fota 代码

   1.2 修改 `build/make/core/Makefile` 文件

   1.2.1 在如下代码：
   ```makefile
   # Accepts a whitespace separated list of product locales such as
   # (en_US en_AU en_GB...) and returns the first locale in the list with
   # underscores replaced with hyphens. In the example above, this will
   # return "en-US".
   define get-default-product-locale
   $(strip $(subst _,-, $(firstword $(1))))
   endef
   
   # TARGET_BUILD_FLAVOR and ro.build.flavor are used only by the test
   # harness to distinguish builds. Only add _asan for a sanitized build
   # if it isn't already a part of the flavor (via a dedicated lunch
   # config for example).
   TARGET_BUILD_FLAVOR := $(TARGET_PRODUCT)-$(TARGET_BUILD_VARIANT)
   ifneq (, $(filter address, $(SANITIZE_TARGET)))
   ifeq (,$(findstring _asan,$(TARGET_BUILD_FLAVOR)))
   TARGET_BUILD_FLAVOR := $(TARGET_BUILD_FLAVOR)_asan
   endif
   endif
   ```

   的后面添加如下代码：
   ```makefile
   ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
   	REDSTONE_BUILDINFO_SH :=   packages/apps/Rsota/sh/redstonebuildinfo.sh
   endif
   ```

   1.2.2 在如下代码：

   ```makefile
   INSTALLED_RECOVERYIMAGE_TARGET :=
   ifdef BUILDING_RECOVERY_IMAGE
   ifneq ($(BOARD_USES_RECOVERY_AS_BOOT),true)
   INSTALLED_RECOVERYIMAGE_TARGET := $(PRODUCT_OUT)/recovery.img
   endif
   endif
   
   $(INSTALLED_BUILD_PROP_TARGET): $(intermediate_system_build_prop)
   	@echo "Target build info: $@"
   	$(hide) grep -v 'ro.product.first_api_level' $(intermediate_system_build_prop) > $@
   ```

   的后面添加如下代码：

   ```makefile
   ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
   	bash $(REDSTONE_BUILDINFO_SH) $@ $(REDSTONE_FOTA_APK_KEY) $(REDSTONE_FOTA_APK_CHANNELID) >> $@
   endif
   ```

   1.3 修改 `build/make/target/product/base_system.mk` 文件，在其末尾添加如下代码：

   ```makefile
   #ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
   PRODUCT_PACKAGES += \
          Rsota
   #endi
   ```

   1.4 修改 `device/sprd/mpool/module/fota/main.mk` 文件，将下面代码：

   ```makefile
   #redstone fota
   REDSTONE_FOTA_SUPPORT := false
   REDSTONE_FOTA_APK_ICON := no
   REDSTONE_FOTA_APK_KEY := none
   REDSTONE_FOTA_APK_CHANNELID := none
   #end
   ```

   修改成如下代码：

   ```makefile
   #redstone fota
   REDSTONE_FOTA_SUPPORT := yes
   REDSTONE_FOTA_APK_ICON := no
   REDSTONE_FOTA_IS_AB = yes
   REDSTONE_FOTA_APK_KEY := none
   REDSTONE_FOTA_APK_CHANNELID := none
   #end
   ```

   1.5 将红石升级应用（Rsota）文件放到 `packages/apps/` 目录下。

   1.6 修改 `system/sepolicy/prebuilts/api/30.0/public/platform_app.te` 文件，在该文件末尾添加如下代码：

   ```
   #redstone
   allow platform_app system_app_data_file:dir r_dir_perms;
   allow platform_app system_app_data_file:file r_file_perms;
   ```

   1.7 修改 `system/sepolicy/prebuilts/api/30.0/public/system_app.te` 文件，在该文件末尾添加如下代码：

   ```
   #redstone
   allow system_app cache_file:dir { create add_name write ioctl open search };
   allow system_app cache_file:file {create open write ioctl };
   allow system_app cache_recovery_file:dir { create add_name write ioctl open search read setattr getattr remove_name};
   allow system_app cache_recovery_file:file {create open write read unlink setattr getattr };
   allow system_app ota_package_file:dir { create add_name write ioctl open search read setattr getattr remove_name};
   allow system_app ota_package_file:file {create open write read unlink setattr getattr };
   #redstone
   ```

   1.8 修改 `system/sepolicy/prebuilts/api/30.0/public/uncrypt.te` 文件，在该文件末尾添加如下代码：

   ```
   #redstone
   allow uncrypt system_app_data_file:dir {read getattr };
   allow uncrypt system_app_data_file:file {read getattr };
   ```

   1.9 将 `system/sepolicy/prebuilts/api/30.0/public/` 目录下的 `platform_app.te` 、`system_app.te` 和 `uncrypt.te` 文件拷贝到 `system/sepolicy/public/` 目录下，覆盖对应的文件。

   1.10 修改 `bsp/kernel/kernel4.14/sprd-diffconfig/androidr/sharkl3/arm/go_google_diff_config` 文件，将文件中 `ADD:CONFIG_DM_ANDROID_VERITY_AT_MOST_ONCE_DEFAULT_ENABLED` 行删除掉，如果文件中只有这一行，则可以将该文件直接删除掉。

### 2. 修改编译脚本

   2.1 执行 `make -j8` 命令全编工程

   2.2 执行 `cp_sign` 命令拷贝并签名文件

   2.3 按照 `out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/pac.ini` 文件对应关系，将 `[pac_list]` 下面的文件拷贝到 `ota_partion` 变量中的文件中，例如：在 `ota_partition` 中有如下值:

   ```
   Modem_LTE:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_modem.img
   ```

   我们在 `[pac_list]` 可以找到 `Modem_LTE` 对应的值，如下所示：

   ```
   Modem_LTE=1@./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/SC9600_sharkl3_pubcp_modem.dat
   ```

   最后，我们使用 `cp` 命令将  `[pac_list]` 下的文件拷贝到 `ota_partition` 中对应路径的文件，例如，在源代码根目录下执行如下命令拷贝：

   ```shell
   cp ./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/SC9600_sharkl3_pubcp_modem.dat ./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_modem.img
   ```

   下面给出一个拷贝的脚本：

   ```shell
   copy_modem_bins() {
       Modem_LTE="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_modem.img"
       Modem_LTE_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/SC9600_sharkl3_pubcp_modem.dat"
   
       DSP_LTE_GGE="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_gdsp.img"
       DSP_LTE_GGE_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/sharkl3_pubcp_DM_DSP.bin"
   
       DSP_LTE_LTE="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_ldsp.img"
       DSP_LTE_LTE_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/sharkl3_pubcp_LTEA_DSP.bin"
   
       DFS="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/pm_sys.img"
       DFS_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/sharkl3_cm4.bin"
   
       NV_LTE1="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv1.img"
       NV_LTE2="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv2.img"
       NV_LTE_FROM="./vendor/sprd/release/unisoc_bin/nv_wb/U863JR200-J44L_G4+W25+F247828_TSX_SingleSIM/sharkl3_pubcp_nvitem.bin"
   
       Modem_WCN="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/wcnmodem.img"
       Modem_WCN_FROM="./vendor/sprd/release/unisoc_bin/marlin2_18a/sharkl3_cm4_v2_builddir/PM_sharkl3_cm4_v2.bin"
   
       Modem_LTE_DELTANV="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_deltanv.img"
       Modem_LTE_DELTANV_FROM="./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_deltanv.bin"
   
       GPS_BD="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/gpsbd.img"
       GPS_BD_FROM="./vendor/sprd/release/unisoc_bin/gnss_20a/greeneye2_cm4_bds_builddir/gnssbdmodem.bin"
   
       GPS_GL="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/gpsgl.img"
       GPS_GL_FROM="./vendor/sprd/release/unisoc_bin/gnss_20a/greeneye2_cm4_glonass_builddir/gnssmodem.bin"
   
       cd unisoc_all_11_0_2021_07_14_13_14_59
   
       rm -rf ./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/
       mkdir ./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/
   
       cp $Modem_LTE_FROM $Modem_LTE
       cp $DSP_LTE_GGE_FROM $DSP_LTE_GGE
       cp $DSP_LTE_LTE_FROM $DSP_LTE_LTE
       cp $DFS_FROM $DFS
       cp $NV_LTE_FROM $NV_LTE1
       cp $NV_LTE_FROM $NV_LTE2
       cp $Modem_WCN_FROM $Modem_WCN
       cp $Modem_LTE_DELTANV_FROM $Modem_LTE_DELTANV
       cp $GPS_BD_FROM $GPS_BD
       cp $GPS_GL_FROM $GPS_GL
   }
   ```

   2.4 执行 `make otapackage -j8` 命令编译 ota

   2.5 执行 `make otatools` 命令生成用于生成差分包的工具

   2.6 执行 `makepac` 命令生成 pac 文件

   2.7 执行 `copy_out_imagefiles` 命令拷贝镜像文件。

   下面给出一个完成的编译脚本：

   ```shell
   if [ $STEP0_MAKE_ALL_IMG -ne 0 ];then
   
       echo -e "\033[;33m
   
   	start to make all img -j$TASK_NUM ...
   
       \033[0m"
   
       source build/envsetup.sh
       choosecombo release $MY_BOARD $BUILD_VER gms
   
       if [ ! -d out/target/product/$OUT_TARGET_DIR/vendor ];then
           echo "IDH out not exist copy them now !!"
           if [ ! -d out/target/product/$OUT_TARGET_DIR ];then
              rm -rf bsp/out
              rm -rf out
           fi
           cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/bsp .
           cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/out .
       fi
   
       make -j$TASK_NUM
       if [ $? -eq 0 ]; then
           echo "Build images ok!"
       else
           echo "Build images failed!"
           exit 1
       fi
   
       cp_sign
       copy_modem_bins
       make otapackage -j$TASK_NUM
       make otatools
       makepac
   
       copy_out_imagefiles
   
       echo "make all img -j$TASK_NUM finished"
       date "+%Y-%m-%d %H:%M:%S"
   fi
   ```

### 4. 制作差分包

4.1 执行下面命令将 `out` 目录下的 `otatools` 文件夹拷贝到源代码根目录下：

```shell
cp out/target/product/s9863a1h10_go_32b/otatools ./
```

> 注意：必须在 Linux 下拷贝，如果在 Windows 下拷贝将会导致文件夹中的文件权限改变，从而导致生成差分包失败。

4.2 将生成的两个 target 包，例如 `V1.zip` 和 `V2.zip` 拷贝到源代码根目录下的 `otatools` 文件夹中。（V1.zip 是基础包，V2.zip 是目的包）

```shell
cp out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1627279500.zip ./otatools/V1.zip
```

4.3 进入到源代码根目录下的 `otatools` 文件夹中执行如下命令生成差分包：

4.3.1 `user` 版本生成差分包命令如下：

```shell
./build/make/tools/releasetools/ota_from_target_files -k ./build/target/product/security/release/releasekey --block -v -i V1.zip V2.zip update.zip
```

4.3.2 `userdebug` 版本生成差分包命令如下：

```shell
./build/make/tools/releasetools/ota_from_target_files -k ./build/target/product/security/testkey --block -v -i V1.zip V2.zip update.zip
```



