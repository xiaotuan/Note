[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

> 提示：修改方法是在`sys/device/` 和 `vnd/device/` 目录下搜索 `DONT_DEXPREOPT_PREBUILTS` 宏定义，将其值都修改为 `false` 即可。

在下面文件中搜索 `DONT_DEXPREOPT_PREBUILTS` 宏，将其值都修改为 `false`：

````
sys/device/mediatek/system/common/BoardConfig.mk
sys/device/mediatek/vendor/common/BoardConfig.mk
sys/device/mediatek/common/BoardConfig.mk
vnd/device/mediatek/system/common/BoardConfig.mk
vnd/device/mediatek/vendor/common/BoardConfig.mk
vnd/device/mediatek/common/BoardConfig.mk
````

