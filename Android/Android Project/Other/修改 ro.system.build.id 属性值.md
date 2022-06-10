[toc]

### 1. MTK

#### 1.1 MT8768

##### 1.1.1 Android S

修改 `build/make/core/sysprop.mk` 文件的如下内容：

```diff
@@ -55,7 +55,11 @@ define generate-common-build-props
     echo "ro.$(1).build.date=`$(DATE_FROM_FILE)`" >> $(2);\
     echo "ro.$(1).build.date.utc=`$(DATE_FROM_FILE) +%s`" >> $(2);\
     echo "ro.$(1).build.fingerprint=$(BUILD_FINGERPRINT_FROM_FILE)" >> $(2);\
-    echo "ro.$(1).build.id=$(BUILD_ID)" >> $(2);\
+    $(if $(filter system,$(1)),\
+               echo "ro.system.build.id=GOV.V1_`$(DATE_FROM_FILE) +%Y%m%d`" >> $(2);\
+         ,\
+               echo "ro.$(1).build.id=$(BUILD_ID)" >> $(2);\
+       )\
     echo "ro.$(1).build.tags=$(BUILD_VERSION_TAGS)" >> $(2);\
     echo "ro.$(1).build.type=$(TARGET_BUILD_VARIANT)" >> $(2);\
     echo "ro.$(1).build.version.incremental=$(BUILD_NUMBER_FROM_FILE)" >> $(2);\
```

