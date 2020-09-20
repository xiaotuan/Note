```mak
LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_STATIC_JAVA_LIBRARIES  := SWDM_swlib  SWDM_terminal_sdk               
LOCAL_JNI_SHARED_LIBRARIES := libSWDMmt

LOCAL_MODULE_TAGS := optional

LOCAL_SRC_FILES := $(call all-java-files-under, src)

LOCAL_RESOURCE_DIR := $(LOCAL_PATH)/res

LOCAL_MANIFEST_FILE := AndroidManifest.xml

LOCAL_PACKAGE_NAME := SWDM
ALL_DEFAULT_INSTALLED_MODULES += $(LOCAL_PACKAGE_NAME)
LOCAL_CERTIFICATE := platform
#LOCAL_PRIVILEGED_MODULE := true

#LOCAL_MODULE_CLASS := APPS

LOCAL_PROGUARD_ENABLED := disabled

LOCAL_AAPT_FLAGS += -c zz_ZZ


#LOCAL_MODULE_TAGS := tests

include $(BUILD_PACKAGE)

# Use the folloing include to make our test apk.
include $(call all-makefiles-under,$(LOCAL_PATH))

 
include $(CLEAR_VARS)

LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := SWDM_swlib:libs/swlib-1.0.16.jar  SWDM_terminal_sdk:libs/terminal_sdk-v1.1.1_release_jdk1.7.jar


include $(BUILD_MULTI_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := .so
LOCAL_MODULE := libSWDMmt
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_SRC_FILES := libs/armeabi-v7a/libmt-jni.so
include $(BUILD_PREBUILT)
```

