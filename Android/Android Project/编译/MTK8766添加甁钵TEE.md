[toc]

### 1. 申请甁钵TEE

申请网址和账号信息请参阅《[甁钵TEE申请网站账号信息](C:\WorkSpace\GitSpace\Xiaotuan\Notes\Company\微步\公司资料\甁钵TEE申请网站账号信息.md)》，申请指南请参阅《[TrustKernel_OSS说明V2.0 20181217.pdf](C:\WorkSpace\Backup\甁钵TEE申请指南\TrustKernel_OSS说明V2.0 20181217.pdf)》。

### 2. 修改代码

#### 2.1 修改 `device/mediateksample/m863u_bsp_64/ProjectConfig.mk`文件

添加如下宏或修改宏的值为如下值：

```makefile
#TrustKernel add
MTK_PERSIST_PARTITION_SUPPORT = yes
MTK_TEE_SUPPORT = yes
TRUSTKERNEL_TEE_SUPPORT = yes
```

#### 2.2 修改 `kernel-4.14/arch/arm64/configs/m863u_bsp_64_debug_defconfig` 文件

添加如下宏或修改宏的值为如下值：

```makefile
#TrustKernel add
CONFIG_TRUSTKERNEL_TEE_SUPPORT=y
CONFIG_TRUSTKERNEL_TEE_FP_SUPPORT=y
CONFIG_TRUSTKERNEL_TEE_RPMB_SUPPORT=y
```

#### 2.3 修改 `kernel-4.14/arch/arm64/configs/m863u_bsp_64_defconfig` 文件

添加如下宏或修改宏的值为如下值：

```makefile
#TrustKernel add
CONFIG_TRUSTKERNEL_TEE_SUPPORT=y
CONFIG_TRUSTKERNEL_TEE_FP_SUPPORT=y
CONFIG_TRUSTKERNEL_TEE_RPMB_SUPPORT=y
```

#### 2.4 修改 `vendor/mediatek/proprietary/bootable/bootloader/preloader/custom/m863u_bsp_64/m863u_bsp_64.mk` 文件

添加如下宏或修改宏的值为如下值：

```makefile
#TrustKernel add
MTK_TEE_SUPPORT = yes
TRUSTKERNEL_TEE_SUPPORT = yes
```

在 `export` 行末尾添加 `空格+TRUSTKERNEL_TEE_SUPPORT` 

#### 2.5 修改 `vendor/mediatek/proprietary/trustzone/custom/build/project/m863u_bsp_64.mk` 文件

添加如下宏或修改宏的值为如下值：

```makefile
#TrustKernel add
MTK_TEE_SUPPORT = yes
TRUSTKERNEL_TEE_SUPPORT = yes
MTK_TEE_DRAM_SIZE = 0x2400000
TRUSTKERNEL_TEE_VERSION=20
```

#### 2.6 在 `vendor/mediatek/proprietary/trustzone/trustkernel/source/build/m863u_bsp_64/` 目录下添加 `array.c` 文件

`array.c` 文件可以在甁钵TEE申请网站下载。

> 注意：MT8781 芯片放置位置为 `vendor/mediatek/proprietary/trustzone/trustkernel/source/build/hal_mgvi_t_64_armv82/array.c`。

#### 2.7 将在甁钵TEE网站生成的 `dat` 证书文件替换掉 `vendor/mediatek/proprietary/trustzone/trustkernel/source/build/m863u_bsp_64/cert.dat` 文件

证书文件可以在甁钵申请网站上获得。

> 注意：MT8781 芯片放置位置为 `vendor/mediatek/proprietary/trustzone/trustkernel/source/build/hal_mgvi_t_64_armv82/cert.dat`。

#### 2.8 最后需要将申请到的 keybox 压缩包文件上传到甁钵网站

keybox 文件为第三方申请后获得的，需要将其上传到甁钵TEE申请网站上。

> 注意：
>
> 1. 在甁钵网站上创建工程后需要 @王昌彦 ，让其帮忙审核通过。
> 2. 在甁钵网站上添加 Keybox 文件后，如果需要验证软件是否没有问题，需要 @王昌彦 ，让其帮忙将其激活为测试阶段。



