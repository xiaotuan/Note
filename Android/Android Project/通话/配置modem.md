[toc]

### 1. MTK 平台

#### 1. MTK8766、Android R

1. 将 `modem` 文件夹拷贝到 `vendor/mediatek/proprietary/modem` 目录下。

2. 修改 `device/mediateksample/项目名/ProjectConfig.xmk` 文件，将 `CUSTOM_MODEM` 宏的值设置成 `modem` 文件夹的名称，例如：

   ```makefile
   CUSTOM_MODEM = M863U_HanTianXia_Lamei_GSM235_W245_L2345712171366_20210917_V197_4
   ```

   

