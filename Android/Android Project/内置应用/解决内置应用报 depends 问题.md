**报错信息：**

```
[100% 569/569] writing build rules ...
FAILED: 
vendor/mediatek/kernel_modules/connectivity/bt/mt66xx/Android.mk:11: warning: warning for parse error in an unevaluated line: *** commands commence before first target.
build/make/core/base_rules.mk:579: warning: overriding commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/android.hardware.security.keymint-service.trustonic.xml'
build/make/core/base_rules.mk:579: warning: ignoring old commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/android.hardware.security.keymint-service.trustonic.xml'
build/make/core/base_rules.mk:579: warning: overriding commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/android.hardware.security.sharedsecret-service.trustonic.xml'
build/make/core/base_rules.mk:579: warning: ignoring old commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/android.hardware.security.sharedsecret-service.trustonic.xml'
build/make/core/base_rules.mk:579: warning: overriding commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/android.hardware.security.secureclock-service.trustonic.xml'
build/make/core/base_rules.mk:579: warning: ignoring old commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/android.hardware.security.secureclock-service.trustonic.xml'
build/make/core/base_rules.mk:579: warning: overriding commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/bluetooth_audio.xml'
build/make/core/base_rules.mk:579: warning: ignoring old commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/bluetooth_audio.xml'
build/make/core/base_rules.mk:579: warning: overriding commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/gnss-default.xml'
build/make/core/base_rules.mk:579: warning: ignoring old commands for target `out/target/product/mssi_t_64_cn_datasms/vendor/etc/vintf/manifest/gnss-default.xml'
vendor/mediatek/proprietary/packages/modules/Bluetooth/system/Android.mk:101: warning: overriding commands for target `out/host/linux-x86/obj/PACKAGING/bluetooth_cert_src_and_bin_intermediates/bluetooth_cert_src_and_bin.zip'
packages/modules/Bluetooth/system/Android.mk:100: warning: ignoring old commands for target `out/host/linux-x86/obj/PACKAGING/bluetooth_cert_src_and_bin_intermediates/bluetooth_cert_src_and_bin.zip'
vendor/mediatek/proprietary/packages/modules/Bluetooth/system/Android.mk:129: warning: overriding commands for target `out/host/linux-x86/obj/PACKAGING/bluetooth_cert_tests_py_package_intermediates/bluetooth_cert_tests.zip'
packages/modules/Bluetooth/system/Android.mk:128: warning: ignoring old commands for target `out/host/linux-x86/obj/PACKAGING/bluetooth_cert_tests_py_package_intermediates/bluetooth_cert_tests.zip'
build/make/core/app_prebuilt_internal.mk:188: error: real file "out/target/product/mssi_t_64_cn_datasms/obj/APPS/Solitaire_intermediates/package.apk" depends on PHONY target "Calm.apk"
15:26:39 ckati failed with: exit status 1
b8a567a276a34433b0cd692a236f3bf9:         0.2%

#### failed to build some targets (02:54 (mm:ss)) ####
```

**解决办法：**

这是因为 apk 文件名包含空格造成的，该报错 apk 的名字为 `Solitaire Calm.apk`， 在 Android.mk 文件中配置如下：

```makefile
LOCAL_REPLACE_PREBUILT_APK_INSTALLED := $(LOCAL_PATH)/Solitaire Calm.apk
```

因为空格问题导致编译系统认为要编译的 apk 是 Calm.apk。将 apk 文件名称中的空格使用 `_` 替换，修改 Android.mk 文件内容为：

```makefile
LOCAL_REPLACE_PREBUILT_APK_INSTALLED := $(LOCAL_PATH)/Solitaire_Calm.apk
```

即可解决问题。