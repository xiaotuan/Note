1. 将 jar 文件放入 libs 文件夹中。

2. 在 Android.mk 文件中添加预编译库代码：

   ```makefile
   include $(CLEAR_VARS)
   
   LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := \
       zxing:libs/zxing-core-3.5.2.jar
       
   include $(BUILD_MULTI_PREBUILT)
   ```

3. 在目标模块中引入 jar

   ```makefile
   LOCAL_STATIC_JAVA_LIBRARIES := \
       zxing
   ```

例如：

```makefile
LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE_TAGS := optional

LOCAL_SRC_FILES := $(call all-subdir-java-files) \
    src/com/mediatek/FMRadio/IFMRadioService.aidl

LOCAL_PACKAGE_NAME := FactoryModeCC
LOCAL_JAVA_LIBRARIES := mediatek-framework telephony-common
LOCAL_STATIC_JAVA_LIBRARIES := \
    vendor.mediatek.hardware.nvram-V1.0-java \
    zxing
LOCAL_CERTIFICATE := platform
LOCAL_PRIVATE_PLATFORM_APIS := true
LOCAL_PRIVILEGED_MODULE := true
LOCAL_OVERRIDES_PACKAGES := FactoryModeWeibu FactoryTest FMRadio

ifeq ($(strip $(TRUSTKERNEL_TEE_PLATFORM_APP_SUPPORT)), yes)
LOCAL_JNI_SHARED_LIBRARIES := libFMcheckkeyjni
endif

#LOCAL_PRODUCT_MODULE := true

include $(BUILD_PACKAGE)

include $(CLEAR_VARS)

LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := \
    zxing:libs/zxing-core-3.5.2.jar
    
include $(BUILD_MULTI_PREBUILT)

# Use the folloing include to make our test apk.
include $(call all-makefiles-under,$(LOCAL_PATH))
```



