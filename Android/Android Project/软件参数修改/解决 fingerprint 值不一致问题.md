**问题现象：**

设备 fingerprint 值如下：

```
$ adb shell getprop | grep fingerprint
[ro.bootimage.build.fingerprint]: [CPSpeed/full_tb8788p1_64_bsp/tb8788p1_64_bsp:11/RP1A.200720.011/1644540016:user/relea
se-keys]
[ro.build.fingerprint]: [CPSpeed/CPS_TAB_01/CPS_TAB_01:11/RP1A.200720.011/1644540016:user/release-keys]
[ro.build.version.preview_sdk_fingerprint]: [REL]
[ro.odm.build.fingerprint]: [CPSpeed/full_tb8788p1_64_bsp/tb8788p1_64_bsp:11/RP1A.200720.011/1644540016:user/release-key
s]
[ro.product.build.fingerprint]: [CPSpeed/full_tb8788p1_64_bsp/tb8788p1_64_bsp:11/RP1A.200720.011/1644540016:user/release
-keys]
[ro.system.build.fingerprint]: [CPSpeed/full_tb8788p1_64_bsp/tb8788p1_64_bsp:11/RP1A.200720.011/1644540016:user/release-
keys]
[ro.system_ext.build.fingerprint]: [CPSpeed/full_tb8788p1_64_bsp/tb8788p1_64_bsp:11/RP1A.200720.011/1644540016:user/rele
ase-keys]
[ro.vendor.build.fingerprint]: [CPSpeed/full_tb8788p1_64_bsp/tb8788p1_64_bsp:11/RP1A.200720.011/1644540016:user/release-
keys]
```

从上面的日志中可以看到，只有 ro.build.fingerprint 的值是正确的，其他值都不正确。

**问题分析：**

从 `build/core/Makefile` 文件中找到 fingerprint 的值定义如下：

```
BUILD_FINGERPRINT := $(PRODUCT_BRAND)/$(PRODUCT_SYSTEM_NAME)/$(PRODUCT_SYSTEM_DEVICE):$(PLATFORM_VERSION)/$(BUILD_ID)/$(BF_BUILD_NUMBER):$(TARGET_BUILD_VARIANT)/$(BUILD_VERSION_TAGS)
```

从中可以看出不正确的地方是 PRODUCT_SYSTEM_NAME 和 PRODUCT_SYSTEM_DEVICE 的值。

**解决方法：**

在 `device/mediateksample/项目名/vnd_项目名.mk` 文件中添加如下代码：

```makefile
PRODUCT_SYSTEM_NAME := CPS_TAB_01
PRODUCT_SYSTEM_DEVICE := CPS_TAB_01
```

