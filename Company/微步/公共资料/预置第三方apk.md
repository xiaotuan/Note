[toc]

### 1. 展讯平台

#### 1.1 Android R

1. 将第三方 APK 放到 `vendor/sprd/partner/prebuilt_apps/` 目录下。

2. 在 `vendor/sprd/partner/prebuilt_apps/` 目录下创建 `Android.mk` 文件。`Android.mk` 文件内容参照如下：

   ```makefile
   LOCAL_PATH:= $(call my-dir)
   
   #举例
   #include $(CLEAR_VARS)
   #LOCAL_MODULE_TAGS := optional
   # module 名字
   #LOCAL_MODULE := weixin
   #该预置为预置 apk
   #LOCAL_MODULE_CLASS := APPS 
   #签名方式
   #LOCAL_CERTIFICATE := PRESIGNED
   #安装位置 1.可删除可恢复目录---------- 预置到preloadapp目录下：$(TARGET_OUT)/preloadapp  预置到vital-app目录下：$(TARGET_OUT)/vital-app  
   #         2.不可删除---------预置到 system/app目录下：$(TARGET_OUT)/app     预置到/system/priv-app目录下： $(TARGET_OUT)/priv-app
   #LOCAL_MODULE_PATH := $(TARGET_OUT)/app  
   #apk 源文件位置
   #LOCAL_SRC_FILES := app/weixin.apk
   
   #include $(CLEAR_VARS)
   #LOCAL_MODULE_TAGS := optional
   #LOCAL_MODULE := sogou
   #LOCAL_MODULE_STEM := sogou.apk
   #LOCAL_MODULE_CLASS := APPS
   #LOCAL_CERTIFICATE := PRESIGNED
   #LOCAL_MODULE_PATH := $(TARGET_OUT)/vital-app
   #LOCAL_MODULE_PATH := $(PRODUCT_OUT)/$(TARGET_COPY_OUT_PRODUCT)/app
   #LOCAL_SRC_FILES := ./app/sogou.apk
   #LOCAL_PREBUILT_JNI_LIBS := ./lib/glupad/lib/armeabi/libnative-lib.so \
                              ./lib/glupad/lib/armeabi/libyzstts.so 
   			   
   #include $(BUILD_PREBUILT)
   
   include $(CLEAR_VARS)
   LOCAL_MODULE := Facebook
   LOCAL_MODULE_TAGS := optional
   LOCAL_SRC_FILES :=$(LOCAL_MODULE).apk
   LOCAL_MODULE_CLASS := APPS
   DONT_DEXPREOPT_PREBUILTS := true
   LOCAL_PRODUCT_MODULE := true
   LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
   LOCAL_CERTIFICATE := PRESIGNED
   include $(BUILD_PREBUILT)
   
   include $(CLEAR_VARS)
   LOCAL_MODULE := Netflix
   LOCAL_MODULE_TAGS := optional
   LOCAL_SRC_FILES :=$(LOCAL_MODULE).apk
   LOCAL_MODULE_CLASS := APPS
   LOCAL_PRODUCT_MODULE := true
   LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
   LOCAL_CERTIFICATE := PRESIGNED
   include $(BUILD_PREBUILT)
   
   include $(CLEAR_VARS)
   LOCAL_MODULE := Skype
   LOCAL_MODULE_TAGS := optional
   LOCAL_SRC_FILES :=$(LOCAL_MODULE).apk
   LOCAL_MODULE_CLASS := APPS
   LOCAL_PRODUCT_MODULE := true
   LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
   LOCAL_CERTIFICATE := PRESIGNED
   LOCAL_MULTILIB := 32
   include $(BUILD_PREBUILT)
   
   include $(CLEAR_VARS)
   LOCAL_MODULE := Twitter
   LOCAL_MODULE_TAGS := optional
   LOCAL_SRC_FILES :=$(LOCAL_MODULE).apk
   LOCAL_MODULE_CLASS := APPS
   LOCAL_PRODUCT_MODULE := true
   LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
   LOCAL_CERTIFICATE := PRESIGNED
   LOCAL_MULTILIB := 32
   include $(BUILD_PREBUILT)
   
   include $(call all-makefiles-under,$(LOCAL_PATH))
   ```

   