```mak
LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE_TAGS := optional

LOCAL_SRC_FILES := $(call all-java-files-under, src)

LOCAL_RESOURCE_DIR := $(LOCAL_PATH)/res

LOCAL_MANIFEST_FILE := AndroidManifest.xml

LOCAL_PACKAGE_NAME := SWSettingsJump_sd
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
```

