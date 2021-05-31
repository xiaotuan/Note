在源码中的 `android.mk`
`aar` 文件包含 `Android` 的资源文件，如：布局、样式、图片等，按照一般的jar方式编译会出现错误，无法使用。

这里使用 `recyclerview-v7-23.0.0.aar` 为例子简洁的讲解书写格式：

下面是我开发的一个主页，并在 `android` 系统源码中编译使用到的依赖文件，我把其他的 `jar` 删除了，只剩下 `recyclerview` 便于观看

```mk
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

LOCAL_PACKAGE_NAME := launcher

LOCAL_MODULE_TAGS := optional

LOCAL_CERTIFICATE := platform
LOCAL_PROGUARD_FLAG_FILES := proguard.flags
LOCAL_OVERRIDES_PACKAGES := Home Launcher2

LOCAL_SRC_FILES := \
    $(call all-java-files-under, java) \
    $(call all-renderscript-files-under, java)

LOCAL_STATIC_JAVA_LIBRARIES := \
    recyclerview-v7-23.0.0 \
LOCAL_STATIC_JAVA_AAR_LIBRARIES := recyclerview-v7-23.0.0 \

LOCAL_AAPT_FLAGS := \
--auto-add-overlay \
--extra-packages android.support.v7.recyclerview \

LOCAL_JAVA_LIBRARIES := \
    services \       
LOCAL_MANIFEST_FILE := AndroidManifest.xml 

include $(BUILD_PACKAGE)

include $(CLEAR_VARS)
LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := \
    recyclerview-v7-23.0.0:recyclerview-v7-23.0.0.aar \
include $(BUILD_MULTI_PREBUILT)

include $(call all-makefiles-under,$(LOCAL_PATH))
```

主要代码
这里是引用 `aar` 的包,其他的 `jar` 也写在这里。

```mk
LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := \
    recyclerview-v7-23.0.0:recyclerview-v7-23.0.0.aar \
```

`recyclerview-v7-23.0.0` 是在下面的代码中定义的名称

```mk
LOCAL_STATIC_JAVA_AAR_LIBRARIES ：= 名称
```

注意 `aar` 的编译要用 `BUILD_MULTI_PREBUILT:`

```mk
include $(CLEAR_VARS)
LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := \
    recyclerview-v7-23.0.0:recyclerview-v7-23.0.0.aar \
include $(BUILD_MULTI_PREBUILT)
```

如果需要使用到 `R` 文件的话，需要在 `LOCAL_AAPT_FLAGS` 变量后面添加 `AAR` 包中的包名，这 `AAR` 打包过程中，会有一个清单文件打包进去，只需要拷贝清单文件中 `package` 的包名并赋值给 `LOCAL_AAPT_FLAGS` 就可以了。

```mk
LOCAL_AAPT_FLAGS := \
--auto-add-overlay \
--extra-packages android.support.v7.recyclerview \
```

基本上就是这些，没什么复杂的，照用上面的代码修改为自己的 `aar` 就行了。