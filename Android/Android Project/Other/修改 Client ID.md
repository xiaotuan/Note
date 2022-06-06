[toc]

### 1. MTK

#### 1.1 MT8768

##### 1.1.1 Android S

1. 如果项目是非 GO 版本，则修改 `vendor/partner_gms/products/gms.mk` 文件中的如下代码:

   ```diff
   @@ -121,5 +121,5 @@ PRODUCT_PRODUCT_PROPERTIES += \
        ro.setupwizard.rotation_locked=true \
        setupwizard.theme=glif_v3_light \
        ro.opa.eligible_device=true \
   -    ro.com.google.clientidbase=android-skythtek \
   +    ro.com.google.clientidbase=android-multilaser \
        ro.com.google.gmsversion=12_202204
   ```

2. 如果项目是 2G 内存的 GO 版本，则修改 `vendor/partner_gms/products/gms_go_2gb.mk` 文件中的如下代码：

   ```diff
   @@ -119,5 +119,5 @@ PRODUCT_PRODUCT_PROPERTIES += \
        setupwizard.theme=glif_v3_light \
        setupwizard.feature.checkin_timeout_enabled=false \
        ro.opa.eligible_device=true \
   -    ro.com.google.clientidbase=android-skythtek \
   +    ro.com.google.clientidbase=android-multilaser \
        ro.com.google.gmsversion=12_202204.go
   ```

3. 如果项目是 1G 内存的 GO 版本，则修改 `vendor/partner_gms/products/gms_go.mk` 文件中的如下代码：

   ```diff
   @@ -103,5 +103,5 @@ PRODUCT_PRODUCT_PROPERTIES += \
        setupwizard.theme=glif_v3_light \
        setupwizard.feature.checkin_timeout_enabled=false \
        ro.opa.eligible_device=true \
   -    ro.com.google.clientidbase=android-skythtek \
   +    ro.com.google.clientidbase=android-multilaser \
        ro.com.google.gmsversion=12_202204.go
   ```

   

