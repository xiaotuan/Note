[toc]

### 1. 微步

#### 1.1 MTK 平台

##### 1.1.1 mt8766_r

1. 首先查看 `vendor/partner_gms/gms.mk` 文件，看最终使用的是那个 mk 文件。从文件中可以看出非 GO 项目使用的是 `vendor/partner_gms/products/gms.mk` ，GO 项目使用的使用 `vendor/partner_gms/products/gms_go.mk`.
2. 查看 `gms.mk` 或 `gms_go.mk` 文件，看最终使用的是那个桌面布局覆盖应用。从文件中可以看到非 GO 项目使用的是 `GmsSampleIntegration`，GO 项目使用的是 `GmsSampleIntegrationGo` 。
3. 再查看 `GmsSampleIntegration` 和 `GmsSampleIntegrationGo` 的 `Android.mk` 文件，以了解它们使用的是那个资源文件夹。从文件中可以看到 `GmsSampleIntegration` 应用使用的是 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_full` 文件夹中的资源，而 `GmsSampleIntegrationGo` 使用的是 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go` 文件夹中的资源。
4. 因此修改 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_full/xml/partner_default_layout.xml` 文件或 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go/xml/partner_default_layout.xml` 文件即可。

