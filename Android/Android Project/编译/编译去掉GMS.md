[toc]

### 1. 展讯

#### 1. 修改 `device/sprd/mpool/module/mainline/mtype/gms/mversion/full/full.mk` 文件

将该文件内容全部注释掉即可。

#### 2. 修改 `device/sprd/mpool/module/mainline/mtype/gms/mversion/go/go.mk` 文件

将该文件内容全部注释掉即可。

#### 3. 修改 `device/sprd/mpool/product/mversion/full/mtype/gms/gms.mk` 文件

将该文件内容全部注释掉即可。

#### 4. 修改 `device/sprd/mpool/product/mversion/go/mtype/gms/gms.mk` 文件

将该文件内容全部注释掉即可。

> 提示：
>
> 1. 编译脚本不需要修改。
>
> 2. 去掉 GMS 后，系统编译会缺少图库和文件管理器，可以通过如下方法将其添加到编译中：
>
>    图库：[编译系统的图库.md](../图库/编译系统的图库.md)
>
>    文件管理器：[显示系统文件管理器.md](../文件管理器/显示系统文件管理器.md)

### 2. MTK 平台

#### 2.1 mt8766_r

修改 `device/mediateksample/工程名/ProjectConfig.mk` 文件，将 `BUILD_GMS` 宏设置为 `no` 即可，例如修改 `device/mediateksample/m863u_bsp_64/ProjectConfig.mk` 文件：

```makefile
BUILD_GMS = no
```

