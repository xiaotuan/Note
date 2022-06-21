### 1. Android S

修改 `vendor/partner_gms/products/gms.mk b/vendor/partner_gms/products/gms.mk` 文件，添加如下代码：

```diff
@@ -120,6 +120,7 @@ endif
 PRODUCT_PRODUCT_PROPERTIES += \
     ro.setupwizard.rotation_locked=true \
     setupwizard.theme=glif_v3_light \
+    setupwizard.feature.checkin_timeout_enabled = false \
     ro.opa.eligible_device=true \
     ro.com.google.clientidbase=android-skythtek \
     ro.com.google.gmsversion=12_202204
```

