[toc]

### 1. 微步

#### 1.1 展讯平台

1.1.1 确定项目的 `out` 文件夹名称，可以通过 `auto-compile-android-src-code.sh` 脚本进行确认，也可以通过查看 `out` 文件夹的名称确认。

+ 通过 `auto-compile-android-src-code.sh` 进行确认：

  ```shell
  #borad is SC9863A/T618/SC9832E, default SC9863A
  STEP0_BOARD_IS_SC9863A=1
  STEP0_BOARD_IS_T618=0
  STEP0_BOARD_IS_SC9832E=0
  
  #borad is 64bit or 32bit, default 64bit
  STEP0_BOARD_IS_64BIT=0
  
  # lunch target
  if [ $STEP0_BOARD_IS_SC9863A -ne 0 ];then
      if [ $STEP0_BOARD_IS_64BIT -ne 0 ];then
          MY_BOARD=s9863a3h10_Natv
          OUT_TARGET_DIR=s9863a3h10
          CHIP_TAG=SC9863A
      else
          MY_BOARD=s9863a1h10_go_32b_2g
          OUT_TARGET_DIR=s9863a1h10_go_32b
          CHIP_TAG=SC9863A_GO
      fi
      IMAGE_DIR=SHARKL3_R11
  elif [ $STEP0_BOARD_IS_T618 -ne 0 ];then
        MY_BOARD=ums512_1h10_Natv
        OUT_TARGET_DIR=ums512_1h10
        CHIP_TAG=T618
        IMAGE_DIR=SHARKL5PRO_SUPER_R
  elif [ $STEP0_BOARD_IS_SC9832E -ne 0 ];then
        MY_BOARD=sp9832e_1h10_go2g
        OUT_TARGET_DIR=sp9832e_1h10_go
        CHIP_TAG=SC9832E_GO
        IMAGE_DIR=SHARKLE_R
  else
      if [ $STEP0_BOARD_IS_64BIT -ne 0 ];then
          MY_BOARD=s9863a3h10_Natv
          OUT_TARGET_DIR=s9863a3h10
          CHIP_TAG=SC9863A
      else
          MY_BOARD=s9863a1h10_go_32b_2g
          OUT_TARGET_DIR=s9863a1h10_go_32b
          CHIP_TAG=SC9863A_GO
      fi
      IMAGE_DIR=SHARKL3_R11
  fi
  ```

+ 通过 `out` 文件夹名称进行确认：

  ```
  out/target/product/s9863a1h10_go_32b/
  ```

  其中 `s9863a1h10_go_32b` 就是文件夹的名称。

1.1.2 在 `vendor/sprd/release/pac_config` 目录下找到与 `out 文件夹名称.ini` 文件，比如上面的 `s9863a1h10_go_32b.ini` 文件, 在文件中找到 `BootLogo` 这一项：

```
BootLogo=1@./vendor/sprd/release/bmp/unisoc_bmp/unisoc_HD_800_1280.bmp
```

从它的值，我们可以知道该项目使用的 Logo 文件是 `vendor/sprd/release/bmp/unisoc_bmp/unisoc_HD_800_1280.bmp`。所以要修改 Logo 图片，可以直接使用新的 Logo 文件替换掉该文件即可。

> 注意：通常开机 Logo 和 Fastboot Logo 是一样的，所以在设置开机 Logo 的时候也需要同时修改 Fastboot Logo。修改方法一样，在 `s9863a1h10_go_32b.ini` 文件中找到 Fastboot_Logo 这项，使用新的 Logo 替换掉该项值对应的文件即可。

#### 1.2 MTK 平台

##### 1.2.1 mt8766_r

1. 查看 `device/mediateksample/项目名/ProjectConfig.mk` 文件中的 `BOOT_LOGO` 的值，例如：`device/mediateksample/m863u_bsp_64/ProjectConfig.mk`：

   ```makefile
   BOOT_LOGO = wxga
   ```

2. 替换 `vendor/mediatek/proprietary/bootable/bootloader/lk/dev/logo/BOOT_LOGO的值/` 目录下的 `BOOT_LOGO的值_kernel.bmp` 和 `BOOT_LOGO的值_uboot.bmp` 图片，例如 `vendor/mediatek/proprietary/bootable/bootloader/lk/dev/logo/wxga/` 目录下的 `wxga_kernel.bmp` 和 `wxga_uboot.bmp` 文件。

