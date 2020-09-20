## Android mk 简介

### 什么是 mk 文件

Android.mk 文件用来告知 NDK Build 系统关于 Source 的信息。 它是GNU Makefile的一部分，且将被 Build System 解析一次或多次。

------

## 简单示例

首先我们先来看一下最简单的例子，编译一个普通的 apk。



```ruby
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# 是否开启混淆
LOCAL_PROGUARD_ENABLED := disabled

LOCAL_MODULE_TAGS := optional

# 使用 platform 签名
LOCAL_CERTIFICATE := platform


# 指定 src 目录               
LOCAL_SRC_FILES := $(call all-java-files-under, src)
# 指定 res 目录
LOCAL_RESOURCE_DIR += $(LOCAL_PATH)/res
# 指定 apk 编译 
LOCAL_PACKAGE_NAME := AppDemo

include $(BUILD_PACKAGE)
```

### 解释说明

- LOCAL_PATH := $(call my-dir)

每个Android.mk文件必须以定义LOCAL_PATH为开始。它用于在开发tree中查找源文件。

- include $(CLEAR_VARS)

CLEAR_VARS 变量由Build System提供。并指向一个指定的GNU Makefile，由它负责清理很多LOCAL_xxx.

例如：LOCAL_MODULE, LOCAL_SRC_FILES, LOCAL_STATIC_LIBRARIES等等。但不清理LOCAL_PATH.

- LOCAL_MODULE_TAGS :

表示在什么版本情况下会编译该版本



```java
LOCAL_MODULE_TAGS ：=user eng tests optional
user: 指该模块只在user版本下才编译
eng: 指该模块只在eng版本下才编译
tests: 指该模块只在tests版本下才编译
optional:指该模块在所有版本下都编译
```

- include $(BUILD_PACKAGE) 表示生成一个 apk，它可以多多种类型



```bash
BUILD_SHARED_LIBRARY #生成一个动态库
BUILD_STATIC_LIBRARY #生成一个静态的库
BUILD_PACKAGE #生成一个APK
```

------

## 指定生成的 apk 存放的目录

### 默认情况

不指定 apk 生成目录时，默认的目录为 system/app/{LOCAL_PACKAGE_NAME}/{LOCAL_PACKAGE_NAME}.apk.

比如，我们上面的例子 LOCAL_PACKAGE_NAME 为 AppDemo，这样生成的 apk 目录为



```undefined
system/app/AppDemo/AppDemo.apk
```

### 指定目录

如果想指定生成的 apk 目录，我们可以通过 LOCAL_MODULE_PATH  来配置，比如，我们想指定生成的 aok 目录为 system/vendor/operator/app，我们可以这样配置



```cpp
LOCAL_MODULE_PATH := $(TARGET_OUT)/vendor/operator/app
```

$(TARGET_OUT) 代表 /system ,这样在 、system/vendor/operator/app 可以看到我们生成的 apk。

**假如我们想让我们生成的 apk 放到 system/priv-app 目录下，有什么方法呢？**

第一种方法，指定 LOCAL_MODULE_PATH ，在上面的讲解中，我们已经知道  $(TARGET_OUT) 代表 /system，那么生成的 apk 想放到 system/priv-app，我们可以这样配置。



```javascript
LOCAL_MODULE_PATH := $(TARGET_OUT)/priv-app
```

第二种方法，我们也可以直接这样配置，这样生成的 apk 也会放到 system/priv-app



```go
LOCAL_PRIVILEGED_MODULE := true
```

**假如我们想让我们生成的 apk 放到 data/app 目录下，有什么方法呢？**

我们可以直接这样指定，这样生成的 apk 就会放到 data/app 目录下



```java
LOCAL_MODULE_PATH := $(TARGET_OUT_DATA_APPS)/
```

------

## 引用第三方 jar 包

### 引用一个 jar 包

比如，我们当前目录下的 libs 有 CommonUtil.jar  jar 包，我们想引用它，需要两个步骤

第一步， 声明我们 jar 包所在的目录

LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := CommonUtil:/libs/CommonUtil.jar  这行代码的意思大概可以理解成这样，声明一个变量 CommonUtil，它的 value 是 /libs/CommonUtil.jar



```ruby
include $(CLEAR_VARS)
LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := CommonUtil:/libs/CommonUtil.jar 
include $(BUILD_MULTI_PREBUILT)
```

第二步. 引用我们声明 jar 包的变量

引用我们上面声明的 CommonUtil



```go
LOCAL_STATIC_JAVA_LIBRARIES := CommonUtil
```

### 引用多个 jar 包

引用多个 jar 包的方式其实跟引用 一个 jar 包的方式是一样的，只不过我们需要注意一下语法而已。

第一步：先声明多个  jar 包的位置



```jsx
include $(CLEAR_VARS)

LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := CloudHelper:/libs/CommonUtil.jar \
                                        BaiduLBS:/libs/BaiduLBS_Android.jar \
                                        logger:/libs/logger.jar
                                        

include $(BUILD_MULTI_PREBUILT)
```

第二步：引用我们声明的多个 jar 包的变量



```go
LOCAL_STATIC_JAVA_LIBRARIES := CommonUtil \
                               BaiduLBS \
                               logger
```

**为了方便大家理解，这里先贴出部分 mk 文件**



```ruby
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# 是否开启混淆
LOCAL_PROGUARD_ENABLED := disabled

LOCAL_MODULE_TAGS := optional

# 使用 platform 签名
LOCAL_CERTIFICATE := platform


# 指定 src 目录               
LOCAL_SRC_FILES := $(call all-java-files-under, src)
# 指定 res 目录
LOCAL_RESOURCE_DIR += $(LOCAL_PATH)/res
# 本地编译目录
LOCAL_PACKAGE_NAME := AppDemo

LOCAL_STATIC_JAVA_LIBRARIES := CommonUtil \
                               BaiduLBS \
                               logger

include $(BUILD_PACKAGE)


include $(CLEAR_VARS)

LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES := CommonUtil:/libs/CommonUtil.jar \
                                        BaiduLBS:/libs/BaiduLBS_Android.jar \
                                        logger:/libs/logger.jar
                                        

include $(BUILD_MULTI_PREBUILT)
```

------

## 引用 so 库

假如我们当前目录下的 lib 目录下 有 armeabi-v7a，arm64-v8a 目录，里面分别有 libBaiduMapSDK_base_v4_2_1.so， libBaiduMapSDK_base_v4_2_1.so 。如果我们在编译 apk 的时候，想把这些 so 库 打包进去，在 mk 文件中要怎样配置呢？

一般来说，会有以下两种写法

### 第一种写法

第一步，直接在 mk 文件中配置以下内容，配置我们 so 库文件的所在位置，可以在文件的开头或者结尾。



```go
#====================================================

include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := .so
LOCAL_MODULE := libBaiduMapSDK_base_v4_2_1
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_SRC_FILES :=libs/armeabi-v7a/libBaiduMapSDK_base_v4_2_1.so
include $(BUILD_PREBUILT)
#====================================================

#====================================================

include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := .so
LOCAL_MODULE := libBaiduMapSDK_base_v4_2_1
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_SRC_FILES_arm :=libs/armeabi-v7a/libBaiduMapSDK_base_v4_2_1.so
LOCAL_SRC_FILES_arm64 :=libs/arm64-v8a/libBaiduMapSDK_base_v4_2_1.so
LOCAL_MODULE_TARGET_ARCHS:= arm arm64
LOCAL_MULTILIB := both
include $(BUILD_PREBUILT)
#====================================================

#====================================================
include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := .so
LOCAL_MODULE := libBaiduMapSDK_map_v4_2_1
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_SRC_FILES_arm :=libs/armeabi-v7a/libBaiduMapSDK_map_v4_2_1.so
LOCAL_SRC_FILES_arm64 :=libs/arm64-v8a/libBaiduMapSDK_map_v4_2_1.so
LOCAL_MODULE_TARGET_ARCHS:= arm arm64
LOCAL_MULTILIB := both
include $(BUILD_PREBUILT)
```

第二步：  引用我们的 so 库

在include ![(CLEAR_VARS) 和 include](https://math.jianshu.com/math?formula=(CLEAR_VARS)%20%E5%92%8C%20include)(BUILD_PACKAGE) 之间添加以下内容



```go
LOCAL_REQUIRED_MODULES := libBaiduMapSDK_base_v4_2_1 \
                          libBaiduMapSDK_map_v4_2_1 \
                         

LOCAL_JNI_SHARED_LIBRARIES := libBaiduMapSDK_base_v4_2_1\
                              libBaiduMapSDK_map_v4_2_1\
```

**配置完以后 mk 文件的形式大概是这样的**



```ruby
include $(CLEAR_VARS)

----   

# 省略若干内容

LOCAL_REQUIRED_MODULES := libBaiduMapSDK_base_v4_2_1 \
                          libBaiduMapSDK_map_v4_2_1 \
                         

LOCAL_JNI_SHARED_LIBRARIES := libBaiduMapSDK_base_v4_2_1\
                              libBaiduMapSDK_map_v4_2_1\

include $(BUILD_PACKAGE)
```

### 第二种写法

第二种写法其实跟第一种写法差不多，只不过是将 so 库的 声明提取出来而已

第一步：比如我们将下面的代码提取到 lib/baidumap.mk mk 文件



```go
#====================================================

include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := .so
LOCAL_MODULE := libBaiduMapSDK_base_v4_2_1
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_SRC_FILES_arm :=libs/armeabi-v7a/libBaiduMapSDK_base_v4_2_1.so
LOCAL_SRC_FILES_arm64 :=libs/arm64-v8a/libBaiduMapSDK_base_v4_2_1.so
LOCAL_MODULE_TARGET_ARCHS:= arm arm64
LOCAL_MULTILIB := both
include $(BUILD_PREBUILT)
#====================================================

#====================================================
include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := .so
LOCAL_MODULE := libBaiduMapSDK_map_v4_2_1
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_SRC_FILES_arm :=libs/armeabi-v7a/libBaiduMapSDK_map_v4_2_1.so
LOCAL_SRC_FILES_arm64 :=libs/arm64-v8a/libBaiduMapSDK_map_v4_2_1.so
LOCAL_MODULE_TARGET_ARCHS:= arm arm64
LOCAL_MULTILIB := both
include $(BUILD_PREBUILT)
```

第二步，在原来的  Android.mk 文件中增加以下语句，表示将 /lib/baidumap.mk 文件 include 进来



```ruby
include $(LOCAL_PATH)/lib/baidumap.mk
```

第三步： 引用我们 的 so 库



```ruby
include $(CLEAR_VARS)

----   

# 省略若干内容

LOCAL_REQUIRED_MODULES := libBaiduMapSDK_base_v4_2_1 \
                          libBaiduMapSDK_map_v4_2_1 \
                         

LOCAL_JNI_SHARED_LIBRARIES := libBaiduMapSDK_base_v4_2_1\
                              libBaiduMapSDK_map_v4_2_1\

include $(BUILD_PACKAGE)
```

其实第一种写法和第二种写法并没有多大区别，第二种方法相对于第一种方法而言，只是将 so 库文件的配置独立到 mk 文件中。不过，我更推荐使用第二种方法，毕竟更符合面向对象的思维，以后复用以比较方便。

------

## 引用 aar 包

第一步：先声明 aar 包的位置



```ruby
include $(CLEAR_VARS)

LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES += inveno_ui_sdk:libs/sdk-release_201709291605.aar
LOCAL_PREBUILT_STATIC_JAVA_LIBRARIES += inveno_detail_info_sdk:libs/detail_info_sdk-release.aar

include $(BUILD_MULTI_PREBUILT)
```

第二步：引用我们声明的  aar 变量



```undefined
LOCAL_STATIC_JAVA_AAR_LIBRARIES += inveno_ui_sdk
LOCAL_STATIC_JAVA_AAR_LIBRARIES += inveno_detail_info_sdk
```

第三步：添加引用的  aar 包里面的资源



```cpp
LOCAL_AAPT_FLAGS += \
         --auto-add-overlay \
         --extra-packages com.inveno.basics \
         --extra-packages com.inveno.detailinfosdk \
```

------

## Android mk 文件配置签名

我们知道在  build/target/product/security 目录中有四组默认签名供，Android.mk在编译APK使用：

- 1、testkey：普通APK，默认情况下使用。
- 2、platform：该APK完成一些系统的核心功能。经过对系统中存在的文件夹的访问测试，
   这种方式编译出来的APK所在进程的UID为system。
- 3、shared：该APK需要和home/contacts进程共享数据。
- 4、media：该APK是media/download系统中的一环。

举例说明一下。



```go
系统中所有使用android.uid.system作为共享UID的APK，
都会首先在manifest节点中增加android:sharedUserId="android.uid.system"，
然后在Android.mk中增加LOCAL_CERTIFICATE := platform。可以参见Settings等

系统中所有使用android.uid.shared作为共享UID的APK，
都会在manifest节点中增加android:sharedUserId="android.uid.shared"，
然后在Android.mk中增加LOCAL_CERTIFICATE := shared。可以参见Launcher等

系统中所有使用android.media作为共享UID的APK，
都会在manifest节点中增加android:sharedUserId="android.media"，
然后在Android.mk中增加LOCAL_CERTIFICATE := media。可以参见Gallery等。
```



作者：stormjun94
链接：https://www.jianshu.com/p/e19e0d3bf13a
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。