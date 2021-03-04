### 1. 提取 so 文件

如果 apk 中存在 so 文件，则需要解压缩 apk ，拿到 apk 的 so 文件。

### 2. 添加 Android.mk 文件

```makefile
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

# Module name should match apk name to be installed
LOCAL_MODULE := SD_YD_Launcher
LOCAL_MODULE_TAGS := optional
LOCAL_SRC_FILES := $(LOCAL_MODULE).apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_CERTIFICATE := platform
LOCAL_MODULE_PATH := $(TARGET_OUT)/app

$(shell cp -rf $(LOCAL_PATH)/lib/armeabi/libgifimage.so $(PRODUCT_OUT)/system/lib)
$(shell cp -rf $(LOCAL_PATH)/lib/armeabi/libimagepipeline.so $(PRODUCT_OUT)/system/lib)
$(shell cp -rf $(LOCAL_PATH)/lib/armeabi/libX86Bridge.so $(PRODUCT_OUT)/system/lib)
$(shell if [ ! -d $(TARGET_OUT)/app/$(LOCAL_MODULE)/lib/arm ]; then mkdir -p $(TARGET_OUT)/app/$(LOCAL_MODULE)/lib/arm; fi)
$(shell cp -rf $(LOCAL_PATH)/lib/armeabi/libgifimage.so $(PRODUCT_OUT)/system/app/$(LOCAL_MODULE)/lib/arm)
$(shell cp -rf $(LOCAL_PATH)/lib/armeabi/libimagepipeline.so $(PRODUCT_OUT)/system/app/$(LOCAL_MODULE)/lib/arm)
$(shell cp -rf $(LOCAL_PATH)/lib/armeabi/libX86Bridge.so $(PRODUCT_OUT)/system/app/$(LOCAL_MODULE)/lib/arm)

include $(BUILD_PREBUILT)

# Use the folloing include to make our test apk.
#include $(call all-makefiles-under,$(LOCAL_PATH))
```

