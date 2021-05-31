在 Android 源码编译中，如果源码中存在 aidl 文件，则需要将其明确指定到编译源文件中。例如：

```mak
LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_STATIC_JAVA_LIBRARIES  := SWStbParamService_sd_SWDeveloplib

LOCAL_MODULE_TAGS := optional

LOCAL_SRC_FILES := $(call all-java-files-under, src)
LOCAL_SRC_FILES += \
	src/com/certus/ottstb/bestv/aidl/IStbParmService.aidl

LOCAL_RESOURCE_DIR := $(LOCAL_PATH)/res

LOCAL_MANIFEST_FILE := AndroidManifest.xml

LOCAL_PACKAGE_NAME := SWStbParamService_sd
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

LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := SWStbParamService_sd_SWDeveloplib:extlibs/SWDeveloplib-1.0.16.jar

include $(BUILD_MULTI_PREBUILT)
```

