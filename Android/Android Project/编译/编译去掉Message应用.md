[toc]

### 1. 微步

#### 1.1 MTK 平台

##### 1.1.2 mt8766_r

2. 修改 `device/mediatek/system/common/device.mk` 文件，去掉 `messaging` 和 `MtkMms`，以及 `MtkMmsAppService`。
3. 修改 `vendor/partner_gms/products/google_comms_suite.mk` 文件，去掉  `Messages`；如果是 GO 项目，则修改 `vendor/partner_gms/products/google_go_comms_suite.mk` 文件，去掉 `MessagesGo`。

