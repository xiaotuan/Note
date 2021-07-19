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


### 2. MTK平台

#### 2.1 MTK8168 Android R

1. 在 `packages` 目录下创建一个名为 `thirdpart` 的目录用于存放第三方 apk。

   > 提示：
   >
   > 第三方 apk 文件放置路径可以放置任何你想要放置的位置，不一定是 `packages/thirdpart` 目录下。

2. 创建以 apk 应用名字相同的文件夹，然后将 apk 文件放入其中，以 com.joycool.deskmain_pad_app7_5.9.2_592.apk 为例，该 apk 的应用名称为 `Wana` ，所以创建的文件夹名称为 `Wana`。

3. 在 `Wana` 文件夹中创建 Android.mk 文件，如 apk 使用到 so 库，则其内容如下：

   ```makefile
   LOCAL_PATH := $(my-dir)
   
   my_archs := arm arm64 x86 x86_64
   my_src_arch := $(call get-prebuilt-src-arch, $(my_archs))
   
   include $(CLEAR_VARS)
   LOCAL_MODULE := Wana
   LOCAL_MODULE_CLASS := APPS
   LOCAL_MODULE_TAGS := optional
   LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
   #LOCAL_PRIVILEGED_MODULE :=
   LOCAL_PRODUCT_MODULE := true
   LOCAL_CERTIFICATE := PRESIGNED
   LOCAL_SRC_FILES := com.joycool.deskmain_pad_app7_5.9.2_592.apk
   include $(BUILD_PREBUILT)
   ```

   否则其内容为：

   ```makefile
   LOCAL_PATH := $(my-dir)
   
   include $(CLEAR_VARS)
   LOCAL_MODULE := Wana
   LOCAL_MODULE_CLASS := APPS
   LOCAL_MODULE_TAGS := optional
   LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
   #LOCAL_PRIVILEGED_MODULE :=
   LOCAL_PRODUCT_MODULE := true
   LOCAL_CERTIFICATE := PRESIGNED
   LOCAL_SRC_FILES := com.joycool.deskmain_pad_app7_5.9.2_592.apk
   #LOCAL_REQUIRED_MODULES :=
   include $(BUILD_PREBUILT)
   ```

   > 提示：
   >
   > 可以参照 `vendor/partner_gms/apps/` 下的内置 apk 的写法修改 Android.mk 文件。

4. 将 apk 添加到编译中去，可以修改 `build/make/target/product/base_system.mk` 文件，在其末尾添加如下代码：

   ```makefile
   PRODUCT_PACKAGES += \
   	Wana
   ```

   

