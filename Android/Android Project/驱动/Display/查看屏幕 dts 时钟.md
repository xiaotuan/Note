[toc]

### 1. MTK

#### 1.1 MT8768

##### 1.1.1 Android S

1. 通过 `weibu/tb8768p1_64_bsp/M960YC_SM_159/config/csci.ini` 文件找到项目使用的屏幕名称，例如：

   ```ini
   lcm.driver.name							m960y_jd9365d_jlt101bi25228p4032d01k_wxga			#所使用屏驱动
   ```

   其中 `m960y_jd9365d_jlt101bi25228p4032d01k_wxga` 就是所使用屏幕的名称。

2. 查看 `vendor/mediatek/proprietary/bootable/bootloader/lk/dev/lcm/mt6765/m960y_jd9365d_jlt101bi25228p4032d01k_wxga/m960y_jd9365d_jlt101bi25228p4032d01k_wxga.c` 中 `lcm_get_params(LCM_PARAMS *params)` 方法的如下代码：

   ```c
   params->dsi.PLL_CLOCK = 245;
   ```

   其中 245 就是屏幕 dts 时钟值。