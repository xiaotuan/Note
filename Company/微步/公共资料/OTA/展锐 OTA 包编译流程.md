[toc]

### 步骤 1 

下载项目中 `AP` 部分的代码。 

### 步骤 2 

通过以下命令设置编译环境。 

```shell
source build/envsetup.sh l
unch 
kheader
```

 ### 步骤 3 

通过 `make` 命令全编整个工程。 

### 步骤 4 

进入 `device/sprd/mpool/module/modem/msoc/sharkle/` 目录，手动建立 `modem_bins` 子目录。 

### 步骤 5 

将展锐发布的对应 `AP` 版本的 `modem bins` 按照 `device/sprd/mpool/module/modem/msoc/sharkle/ build.mk` 中的规定名字改名后拷贝到 `device/sprd/mpool/module/modem/msoc/sharkle/modem_bins/` 目录下。以下是 `SC9832E` 平台示例： 

```shel 
ifneq ($(strip $(PRODUCT_MODEM_COPY_LIST)),) 
	MODEM_COPY_LIST := $(PRODUCT_MODEM_COPY_LIST) 
else 
	MODEM_COPY_LIST := l_modem l_gdsp l_ldsp pm_sys wcnmodem l_deltanv \ gpsgl gpsbd
```

 改名对应规则请参考 [展讯 Modem bins 改名映射](./展讯 Modem bins 改名映射.md) 改名映射。 

> 说明：
> + `modem_bins` 目录中，镜像文件名称的后缀应该以 `.img` 结尾。
> + 主 `modem` 以 `.dat` 为后缀的文件，也要改为以 `.img` 为后缀的文件。
> + `modem bins` 文件中放入的 `image`，要使用签过名的 `image` 文件。

### 步骤 6 

通过命令 `make otapackage` 编译 `OTA` 整包。此命令运行完后会产生版本 `target` 包和 `OTA` 整包。 整包目录：`out/target/product/spXXXX/spXXXX-ota-*.zip`。 为了以后在版本升级时可以使用差分升级，要保留此版本对应的 `target` 文件。路径为： `out/target/product/spXXXX/obj/PACKAGING/target_files_intermediates/*-target_files-*.zip`

### 步骤 7

如果要制作版本 `PAC` 包，请在此时执行命令生成 `PAC` 包。

> 注意：
>
> 请务必在执行完 make otapackage 后做 PAC 包，因为 make otapackage 命令会对很多 img 重新编 译，只有在此步骤后做的 PAC 包才与 target 包严格对应。

### 参考资料

[33017_Android11.0OTA升级指导手册V1.1.pdf](https://unisupport.unisoc.com/file/index?fileid=33017)

