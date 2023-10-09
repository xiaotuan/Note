[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/weibu_sz/products/products.mk` 文件的如下代码：

```diff
@@ -33,6 +33,7 @@ PRODUCT_COPY_FILES += \
         
        
 PRODUCT_PACKAGES += YGPS
+PRODUCT_PACKAGES += GoogleKidsSpace^M
 
 PRODUCT_PACKAGES += EngineerMode
 PRODUCT_PACKAGES += libem_support_jni
```

