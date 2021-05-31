可以使用下面的语法格式在 Android.mk 文件中执行 Shell 脚本：

```makefile
$(shell 要执行的 Shell 脚本)
```

例如：

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
```

