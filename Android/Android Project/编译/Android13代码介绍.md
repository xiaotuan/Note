[toc]

### 1、拉取代码

```shell
$ git clone --recurse-submodules git@192.168.0.24:mtk/mtk_sp_t0.git
$ cd mtk_sp_t0
$ git submodule foreach git checkout master
```

整个代码有3个仓库：

+ `mtk_sp_t0/.git`： 主仓库，只管理编译脚本等⽂件

+ `mtk_sp_t0/vnd/.git`： `vendor`⼦仓库，就是我们维护的仓库 对应地址
  `git@192.168.0.24:mtk/mt8766_s.git`

+ `mtk_sp_t0/sys/.git`： `mssi` ⼦仓库 ，就是最新释放的 `system` 仓库 对应地址
  `git@192.168.0.24:mtk/mtk_t_mssi.git`

### 2、更新代码
+ `cd mtk_sp_t0; git pull --rebase`： 更新主仓库脚本类

+ `cd mtk_sp_t0/vnd;git pull --rebase`： 更新vendor仓库

+ `cd mtk_sp_t0/sys;git pull --rebase`： 更新mssi仓库

每个仓库提交互相不影响

### 3. 编译

```
Split Build 1.0 ( MT8321 MT8765 MT8766 MT8768 MT8183 MT8788 适⽤)
```

#### 3.1 编译 kernel 及 vnd

```shell
cd vnd ; source build/envsetup.sh && export OUT_DIR=out && lunch vnd_tb8766p1_64_bsp-userdebug M869YCR100_YM_546 && make krn_images vnd_images
```

WB_PROJECT对应vnd/weibu/tb8766p1_64_bsp/M866YA_WB_420，如果不存在则报错

#### 3.2 编译 mssi

```shell
cd sys ; source build/envsetup.sh && export OUT_DIR=out && lunch sys_mssi_t_64_cn-userdebug M869YCR100_YM_536-MMI && m api-stubs-docs-non-updatable-update-current-api && make -j24 sys_images
```

```shell
source build/envsetup.sh && export OUT_DIR=out && lunch sys_mssi_t_64_cn-userd M869YCR100_YM_536-MMI

source build/envsetup.sh && export OUT_DIR=out && lunch sys_mssi_t_64_cn_datasms-userdebug M869YCR100_YM_537-MMI
```



WB_PROJECT对应vnd/weibu/mssi_t_64_cn/M866YA_WB_420-MMI，如果不存在则报错

#### 3.3 合成固件

```shell
cd mtk_sp_t0 ; python vendor/mediatek/proprietary/scripts/releasetools/split_build.py --system-dir sys/out/target/product/mssi_t_64_cn/images --vendor-dir vnd/out/target/product/tb8768p1_64_bsp/images --kernel-dir vnd/out/target/product/tb8768p1_64_bsp/images --output-dir ./tb8768p1_64_bsp
```

### 4、固定组合

| Vendor project        | MSSI project             |                   |
| --------------------- | ------------------------ | ----------------- |
| tb8321p3_bsp          | mssi_t_32_ago_ww_armv7   | go 32bit          |
| tb8765ap1_bsp_1g_k419 | mssi_t_32_ago_ww         | go 32bit          |
| tb8765ap1_bsp_1g_k419 | mssi_t_32_ww             | ⾮go 32bit        |
| tb8766p1_64_bsp       | mssi_t_64_cn             | ⾮go 64bit        |
| tb8766p1_bsp_1g       | mssi_t_32_ago_ww         | go 32bit          |
| tb8768p1_64_bsp       | mssi_t_64_cn             | ⾮go 64bit        |
| tb8768p1_bsp          | mssi_t_32_ago_h_ww       | go 32bit          |
| tb8781p1_64           | mssi_t_64_cn_armv82      | ⾮go 64bit        |
| tb8781p1_64_wifi      | mssi_t_64_cn_armv82_wifi | ⾮go 单wifi       |
| tb8788p1_64_bsp_k419  | mssi_t_64_cn             | ⾮go 64bit        |
| tb8788p1_64_wifi_k419 | mssi_t_64_cn_wifi        | ⾮go 64bit 单wifi |
| tb8791p1_64           | mssi_t_64_cn_armv82      | ⾮go 64bit        |
| tb8791p1_64_wifi      | mssi_t_64_cn_armv82_wifi | ⾮go 64bit 单wifi |
| tb8797p1_64_k419      | mssi_t_64_cn_armv82      | ⾮go 64bit        |
| tb8797p2_64_k419_wifi | mssi_t_64_cn_armv82_wifi | ⾮go 64bit 单wifi |

### 5、编译脚本
+ `./split_build.sh vnd`： 编译vnd_images 编译完后不打包

+ `./split_build.sh krn`： 编译 krn_images 编译完后不打包

+ `./split_build.sh krn vnd`： 编译 krn_images vnd_images编译完后不打包

+ `./split_build.sh mer`： 合成固件到merged

+ `./split_build.sh pac`： 打包发布固件

Split Build 2.0 ( MT8781 适⽤)