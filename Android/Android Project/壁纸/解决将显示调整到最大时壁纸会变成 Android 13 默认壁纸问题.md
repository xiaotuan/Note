[toc]

### 1. MTK

#### 1.1 MT8788

##### 1.1.1 Android T

在 Settings -> Display -> Display size and text 界面，将 Display size 调整到最大后，桌面壁纸将会变成 Android 13 默认样式。

解决办法：修改 `vendor/partner_gms/overlay/AndroidSGmsBetaOverlay/res/drawable-nodpi/default_wallpaper.png` 图片为默认壁纸即可。

