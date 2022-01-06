[toc]

### 1. MTK 平台

#### 1.1 MT8766

##### 1.1.1 Android R

修改 `device/mediatek/system/mssi_t_64_cn/sys_mssi_t_64_cn.mk` 文件中 `PRODUCT_AAPT_PREF_CONFIG` 的值为 xhdpi：

```makefile
PRODUCT_AAPT_PREF_CONFIG := xhdpi
```

> 提示：
>
> 屏幕密度对应的 dpi 如下：
>
> + 160dpi -> mdpi
> + 240dpi -> hdpi
> + 320dpi -> xhdpi
> + 480dpi -> xxhdpi
> + 640dpi -> xxxhdpi

