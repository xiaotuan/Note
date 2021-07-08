[toc]

### 1. 报错信息

在编译展讯 Android R 源代码 OTA 时报如下错误：

```log
[ 99% 27755/27756] PRODUCT_SECURE_BOOT=SPRD
FAILED: out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837
/bin/bash -c "(mkdir -p out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/boot.img out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/boot.img -rfv ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/u-boot-sign.bin out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/uboot.img -rfv ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/u-boot-spl-16k-sign.bin out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/mmcblk0boot0.img -rfv ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/tos-sign.bin out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/trustos.img ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/sml-sign.bin out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/sml.img ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/teecfg-sign.bin out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/teecfg.img ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/s9863a1h10_go_32b.xml out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/partition.xml ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/socko.img out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/socko.img ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/odmko.img out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/odmko.img ; true ) && (echo \"secure_boot=SPRD\" >> out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/META/misc_info.txt ) && (rm -rf out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837.zip; 	    PATH=out/host/linux-x86/bin/:system/extras/ext4_utils/:\$PATH MKBOOTIMG=out/host/linux-x86/bin/mkbootimg 	    out/host/linux-x86/bin/add_img_to_target_files -a -v -p out/host/linux-x86 out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837 ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/vbmeta_system.img out/target/product/s9863a1h10_go_32b/vbmeta_system.img -rfv ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/vbmeta_vendor.img out/target/product/s9863a1h10_go_32b/vbmeta_vendor.img -rfv ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/vbmeta_product.img out/target/product/s9863a1h10_go_32b/vbmeta_product.img -rfv ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/vbmeta_system_ext.img out/target/product/s9863a1h10_go_32b/vbmeta_system_ext.img -rfv ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/vbmeta-sign.img out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/vbmeta.img ; true ) && (prebuilts/build-tools/linux-x86/bin/acp out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/dtbo.img out/target/product/s9863a1h10_go_32b/dtbo.img ; true ) && (find out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/META | sort >out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837.zip.list ) && (find out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837 -path out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/META -prune -o -print | sort >>out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837.zip.list ) && (out/soong/host/linux-x86/bin/soong_zip -d -o out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837.zip -C out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837 -l out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837.zip.list ) && (echo \"Rebuild super fs image after target pkg: out/target/product/s9863a1h10_go_32b/super.img\" ) && (PATH=out/host/linux-x86/bin/:\$PATH 	    out/host/linux-x86/bin/build_super_image -v out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837 out/target/product/s9863a1h10_go_32b/super.img )"
    'out/target/product/s9863a1h10_go_32b/boot.img' --> 'out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/IMAGES/boot.img'
acp: cannot create 'out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/uboot.img': No such file or directory
acp: cannot create 'out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/mmcblk0boot0.img': No such file or directory
acp: cannot create 'out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/trustos.img': No such file or directory
acp: cannot create 'out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/sml.img': No such file or directory
acp: cannot create 'out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/teecfg.img': No such file or directory
acp: cannot create 'out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1625290837/RADIO/partition.xml': No such file or directory
2021-07-03 13:44:18 - common.py - WARNING : Failed to read SYSTEM/etc/build.prop
2021-07-03 13:44:18 - common.py - WARNING : Failed to read VENDOR/etc/build.prop
```

### 2. 报错分析

提展讯 CRP 后回复：请问modem bin有正确放置到modem_bins目录下吗？

经确认该代码并没有拷贝 modem bin 到 modem_bins 目录下，拷贝 modem bin 文件到 modem_bins 目录下后编译通过。

### 3. 解决方法

modem bin 配置文件位于 `vendor/sprd/release/pac_config` 目录下，请根据自己项目的实际 modem 查看对应的 ini 文件。比如我的工程使用的是 `s9863a1h10_go_32b.ini` 文件。文件内容如下：

```ini
[Setting]
PacVer=BP_R2.0.1
PAC_PRODUCT=s9863a1h10
ProductAlias=s9863a1h10
ProductVer=MocorDroidR
Mode=0
FlashType=1
NandStrategy=0
NandPageType=0
NvBackup=1
OmaDmProductFlag=0
OmaDM=1
IsPreload=1

[partition]
carrier_partition=
sparse=Super
ota_build_backup=

ota_partition=
    Modem_LTE:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_modem.img
    DSP_LTE_GGE:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_gdsp.img
    DSP_LTE_LTE:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_ldsp.img
    DFS:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/pm_sys.img
    NV_LTE:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv1.img
    Modem_WCN:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/wcnmodem.img
    Modem_LTE_DELTANV:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_deltanv.img
    GPS_BD:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/gpsbd.img
    GPS_GL:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/gpsgl.img
    NV_LTE:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv2.img
[project]
s9863a1h10_go_32b_2g-userdebug-gms=
    SHARKL3_R11:ota
s9863a1h10_go_32b_2g-user-gms=
    SHARKL3_R11:ota

[SHARKL3_R11]
CONFILE=./out/target/product/s9863a1h10_go_32b/s9863a1h10_go_32b.xml
FDL=1@./out/target/product/s9863a1h10_go_32b/fdl1-sign.bin
FDL2=1@./out/target/product/s9863a1h10_go_32b/fdl2-sign.bin
NV_LTE=1@./vendor/sprd/release/unisoc_bin/nv_wb/U863JR200_G4+W1258+F1357820+T38394041(100M)+singleSIM_201207/sharkl3_pubcp_nvitem.bin
ProdNV=1@./out/target/product/s9863a1h10_go_32b/prodnv.img
PhaseCheck=1@
EraseUBOOT=1@
EraseUBOOTLOG=1@
SPLLoader=1@./out/target/product/s9863a1h10_go_32b/u-boot-spl-16k-sign.bin
Modem_LTE=1@./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/SC9600_sharkl3_pubcp_modem.dat
Modem_LTE_DELTANV=1@./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_deltanv.bin
DSP_LTE_LTE=1@./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_LTEA_DSP.bin
DSP_LTE_GGE=1@./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_DM_DSP.bin
DFS=1@./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_cm4_builddir/sharkl3_cm4.bin
DTBO=1@./out/target/product/s9863a1h10_go_32b/dtbo.img
Modem_WCN=1@./vendor/sprd/release/unisoc_bin/marlin2_18a/sharkl3_cm4_v2_builddir/PM_sharkl3_cm4_v2.bin
BOOT=1@./out/target/product/s9863a1h10_go_32b/boot.img
GPS_BD=1@./vendor/sprd/release/unisoc_bin/gnss_20a/greeneye2_cm4_bds_builddir/gnssbdmodem.bin
GPS_GL=1@./vendor/sprd/release/unisoc_bin/gnss_20a/greeneye2_cm4_glonass_builddir/gnssmodem.bin
Super=1@./out/target/product/s9863a1h10_go_32b/super.img
UserData=1@./out/target/product/s9863a1h10_go_32b/userdata.img
BootLogo=1@./vendor/sprd/release/bmp/unisoc_bmp/unisoc_HD_600_1024.bmp
Fastboot_Logo=1@./vendor/sprd/release/bmp/unisoc_bmp/unisoc_HD_600_1024.bmp
Socko=1@./out/target/product/s9863a1h10_go_32b/socko.img
Odmko=1@./out/target/product/s9863a1h10_go_32b/odmko.img
FLASH_LTE=1@
EraseMisc=1@
EraseMetadata=1@
SML=1@./out/target/product/s9863a1h10_go_32b/sml-sign.bin
UBOOTLoader=1@./out/target/product/s9863a1h10_go_32b/u-boot-sign.bin
Persist=1@./out/target/product/s9863a1h10_go_32b/persist.img
Trustos=1@./out/target/product/s9863a1h10_go_32b/tos-sign.bin
EraseSysdumpdb=1@
Teecfg=1@./out/target/product/s9863a1h10_go_32b/teecfg-sign.bin
VBMETA=1@./out/target/product/s9863a1h10_go_32b/vbmeta-sign.img
VBMETA_SYSTEM=1@./out/target/product/s9863a1h10_go_32b/vbmeta_system.img
VBMETA_SYSTEM_EXT=1@./out/target/product/s9863a1h10_go_32b/vbmeta_system_ext.img
VBMETA_VENDOR=1@./out/target/product/s9863a1h10_go_32b/vbmeta_vendor.img
VBMETA_PRODUCT=1@./out/target/product/s9863a1h10_go_32b/vbmeta_product.img
Cache=1@./out/target/product/s9863a1h10_go_32b/cache.img
```

具体操作如下：

1. 使用 `[partition]` 下的 `ota_partition=` 的前缀，在 `[SHARKL3_R11]` 下搜索对应的值。比如 `ota_partition=` 下的 `DSP_LTE_LTE` 前缀对应 `[SHARKL3_R11]` 下的值是 `DSP_LTE_LTE=1@./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_LTEA_DSP.bin`。
2. 将 `[SHARKL3_R11]` 下的值对应的路径的文件拷贝到 `ota_partition=` 下的对应文件中即可。
3. 一直将 `ota_partition=` 下的所有文件都拷贝成功位置。

> 注意：
>
> 在 `ota_partition=` 中有两个 `NV_LTE` 值，它们分别对应 `./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv1.img` 和 `./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv2.img`， 而在 `[SHARKL3_R11]` 下只有一个 `NV_LTE`。因此将  `[SHARKL3_R11]` 下只有一个 `NV_LTE` 文件拷贝到 l_fixnv1.img 和 l_fixnv2.img 中。

例如，以拷贝 DSP_LTE_LTE 的文件为例：

`[SHARKL3_R11]` 下的值指示要拷贝的文件路径，`DSP_LTE_LTE ` 的文件路径是 ./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_LTEA_DSP.bin。

`[partition]` 下的 `ota_partition=` 的值表示目标文件的路径，也就是说要将 ./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_LTEA_DSP.bin 文件拷贝到 ./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins 目录中，并将其重命名为 l_ldsp.img。

