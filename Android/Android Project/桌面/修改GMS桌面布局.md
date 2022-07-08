[toc]

### 1. 微步

#### 1.1 MTK 平台

##### 1.1.1 mt8766_r

1. 首先查看 `vendor/partner_gms/gms.mk` 文件，看最终使用的是那个 mk 文件。从文件中可以看出非 GO 项目使用的是 `vendor/partner_gms/products/gms.mk` ，GO 项目使用的使用 `vendor/partner_gms/products/gms_go.mk`.
2. 查看 `gms.mk` 或 `gms_go.mk` 文件，看最终使用的是那个桌面布局覆盖应用。从文件中可以看到非 GO 项目使用的是 `GmsSampleIntegration`，GO 项目使用的是 `GmsSampleIntegrationGo` 。
3. 再查看 `GmsSampleIntegration` 和 `GmsSampleIntegrationGo` 的 `Android.mk` 文件，以了解它们使用的是那个资源文件夹。从文件中可以看到 `GmsSampleIntegration` 应用使用的是 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_full` 文件夹中的资源，而 `GmsSampleIntegrationGo` 使用的是 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go` 文件夹中的资源。
4. 因此修改 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_full/xml/partner_default_layout.xml` 文件或 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go/xml/partner_default_layout.xml` 文件即可。

> 注意：2GB GO 项目的桌面布局位置为：`vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go_2gb/xml/partner_default_layout.xml`。

#### 2. 展讯平台

##### 2.1 s9863a1h10、Android R

1. 查看 `vendor/partner_gms/products/` 目录下的 `gms.mk`（非 GO 项目）、`gms_go_2gb.mk`（2GB 内存的 GO 项目）和 `gms_go.mk` （其他 GO 项目）文件，查看具体使用的是那个 `GmsSampleIntegration` 应用。从文件中可以看出，`gms.mk` 使用的是 `SearchLauncherQuickStep`，`gms_go_2gb.mk` 使用的是 `GmsSampleIntegrationGo_2GB`，`gms_go.mk` 使用的是 `GmsSampleIntegrationGo`。

2. 查看 `vendor/partner_gms/apps/GmsSampleIntegration/Android.mk` 文件，找到上面对应的应用名称，比如 2GB GO版本的是 `GmsSampleIntegrationGo_2GB`，在文件中可以看到如下代码：

   ```makefile
   # GmsSampleIntegrationGo_2GB
   include $(CLEAR_VARS)
   LOCAL_PACKAGE_NAME := GmsSampleIntegrationGo_2GB
   LOCAL_MODULE_OWNER := google
   LOCAL_MODULE_TAGS := optional
   LOCAL_PRODUCT_MODULE := true
   LOCAL_CERTIFICATE := platform
   LOCAL_SRC_FILES := $(call all-java-files-under, src)
   LOCAL_RESOURCE_DIR := $(LOCAL_PATH)/res_dhs_go_2gb $(LOCAL_PATH)/res
   LOCAL_SDK_VERSION := current
   include $(BUILD_PACKAGE)
   ```

   从上面的代码中可以看出，2GB GO 版本使用的使用 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go_2gb/` 目录下的资源文件，在该目录下找到 `partner_default_layout.xml`，修改它即可。

   

