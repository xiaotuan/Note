[toc]

### 1. 微步

#### 1.1 MTK 平台

##### 1.1.2 mt8766_r

1. 修改 `build/make/target/product/telephony_product.mk` 文件，去掉 `Dialer`。
2. 修改 `device/mediatek/system/common/device.mk` 文件，去掉 `Dialer` 和 `MtkDialer`。
3. 修改 `vendor/partner_gms/products/google_comms_suite.mk` 文件，去掉  `GoogleDialer`；如果是 GO 项目，则修改 `vendor/partner_gms/products/google_go_comms_suite.mk` 文件，去掉 `GoogleDialerGo`。

