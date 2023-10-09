[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/partner_gms/products/gms.mk` 文件的如下代码：

```diff
@@ -133,5 +133,5 @@ PRODUCT_PRODUCT_PROPERTIES += \
     setupwizard.theme=glif_v3_light \
        setupwizard.feature.checkin_timeout_enabled=false \
     ro.opa.eligible_device=true \
-    ro.com.google.clientidbase=android-skythtek \
+    ro.com.google.clientidbase=android-weibu \
     ro.com.google.gmsversion=$(GMS_PACKAGE_VERSION_ID)
```

如果工程是欧盟项目，则需要修改 `sys/vendor/partner_gms/products/eea_common.mk` 文件的对应代码。