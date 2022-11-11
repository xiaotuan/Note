[toc]

### 1. MTK

#### 1.1 Android 12

##### 1.1.1 MT8788

修改 `weibu/tb8788p1_64_bsp_k419/M100BS_CC_261/config/csci.ini` 文件如下代码：

```diff
@@ -41,7 +41,7 @@ touchpanel.gsl.x.reverse                                          0       #触摸屏x轴左右相反
 touchpanel.gsl.y.reverse                                           0       #触摸屏y轴上下相反
 touchpanel.gsl.xy.deal                                             0       #触摸屏交换分辨率
 
-
+ro.qq.camera.sensor                                 3    #开启自动旋转,QQ视频, 逆时针旋转90时：0 顺时针旋转90度时：
 ro.sf.lcd_density                                                          240     #像素密度
 ro.vendor.physical.orientation                      0       #旋转方向 0:0  1；90  2；180  3；270 跟MTK_LCM_PHYSICAL_ROTATION等效
 ro.vendor.fake.orientation                          1       #假横屏方案 0:不使用假横屏  1；使用假横屏方案
```

