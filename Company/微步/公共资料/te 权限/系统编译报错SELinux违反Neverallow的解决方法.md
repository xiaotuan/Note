[toc]

### 一、违反neverallow规则

SeLinux 的 `*.te` 文件路径：

```
p9.0.0.0\device\fsl\imx8q\sepolicy
p9.0.0.0\system\sepolicy
```

其中为了给串口增加权限，修改了一些*.te的权限配置文件，修改完之后系统编译报错。

报错信息如下：

```
FAILED: out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/sepolicy_neverallows 
/bin/bash -c "(rm -f out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/sepolicy_neverallows ) && (ASAN_OPTIONS=detect_leaks=0 out/host/linux-x86/bin/checkpolicy -M -c 		30 -o out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/sepolicy_neverallows out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/policy.conf )"
libsepol.report_failure: neverallow on line 31 of system/sepolicy/private/domain.te (or line 26746 of policy.conf) violated by allow system_app sysfs:file { read write create setattr open };
libsepol.report_failure: neverallow on line 507 of system/sepolicy/public/app.te (or line 8383 of policy.conf) violated by allow system_app sysfs:file { write };
libsepol.check_assertions: 2 neverallow failures occurred
Error while expanding policy
out/host/linux-x86/bin/checkpolicy:  loading policy configuration from out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/policy.conf
```

错误分析：system/sepolicy/private/domain.te 和 system/sepolicy/public/app.te 违反了neverallows规则

解决办法：

#### 1. 修改 system/sepolicy/private/domain.te 文件中的：

```
# /sys
neverallow {
    coredomain
    -init
    -ueventd
    -vold
} sysfs:file no_rw_file_perms;
```

修改为：

```
# /sys
neverallow {
    coredomain
    -init
    -ueventd
    -vold
    -appdomain		//排除appdomain
} sysfs:file no_rw_file_perms;
```

绝对不允许 app 对 sysfs:file 进行文件读写操作，改为：可以允许 app 对 sysfs:file 进行文件读写操作。

#### 2. 修改修改 system\sepolicy\public\app.te 文件中的：

```
# Write to various pseudo file systems.
neverallow { appdomain -bluetooth -nfc }
    sysfs:dir_file_class_set write;
neverallow appdomain
    proc:dir_file_class_set write;
```

改为：

```
# Write to various pseudo file systems.
#neverallow { appdomain -bluetooth -nfc }
#    sysfs:dir_file_class_set write;
neverallow appdomain
    proc:dir_file_class_set write;
```

即注释掉 neverallow { appdomain -bluetooth -nfc } sysfs:dir_file_class_set write;

解除 Neverallow 的限制。

### 二、system/sepolicy/prebuilts/api/28.0/private和system/sepolicy/private文件不一致

```
system/sepolicy/prebuilts/api/28.0/private和system/sepolicy/private下面的文件
system/sepolicy/prebuilts/api/28.0/public和system/sepolicy/public下面的文件，必须保持一致
```

否则会报错误：

```
[  0% 1/321] build out/target/product/mek_8q/obj/ETC/sepolicy_freeze_test_intermediates/sepolicy_freeze_test
FAILED: out/target/product/mek_8q/obj/ETC/sepolicy_freeze_test_intermediates/sepolicy_freeze_test 
/bin/bash -c "(diff -rq system/sepolicy/prebuilts/api/28.0/public system/sepolicy/public ) && (diff -rq system/sepolicy/prebuilts/api/28.0/private system/sepolicy/private ) && (touch out/target/product/mek_8q/obj/ETC/sepolicy_freeze_test_intermediates/sepolicy_freeze_test )"
Files system/sepolicy/prebuilts/api/28.0/public/app.te and system/sepolicy/public/app.te differ
[  2% 7/321] Merging KERNEL config
Using /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx/arch/arm64/configs/android_car_defconfig as base
Merging /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx
sed: read error on /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx: Is a directory
cat: /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx: Is a directory
make[1]: Entering directory `/home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/out/target/product/mek_8q/obj/KERNEL_OBJ'
  GEN     ./Makefile
````

```
/bin/bash -c "(diff -rq system/sepolicy/prebuilts/api/28.0/public system/sepolicy/public ) && (diff -rq system/sepolicy/prebuilts/api/28.0/private system/sepolicy/private ) && (touch out/target/product/mek_8q/obj/ETC/sepolicy_freeze_test_intermediates/sepolicy_freeze_test )"
Files system/sepolicy/prebuilts/api/28.0/private/domain.te and system/sepolicy/private/domain.te differ
[  0% 2/315] build out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/plat_pub_policy.cil
out/host/linux-x86/bin/checkpolicy:  loading policy configuration from out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/plat_pub_policy.conf
out/host/linux-x86/bin/checkpolicy:  policy configuration loaded
out/host/linux-x86/bin/checkpolicy:  writing CIL to out/target/product/mek_8q/obj/ETC/sepolicy_neverallows_intermediates/plat_pub_policy.cil.tmp
[  1% 6/315] Merging KERNEL config
Using /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx/arch/arm64/configs/android_car_defconfig as base
Merging /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx
sed: read error on /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx: Is a directory
cat: /home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/vendor/nxp-opensource/kernel_imx: Is a directory
make[1]: Entering directory `/home/sunxl/imx8_p9.0.0_2.1.0_auto_ga/android9.0.0/out/target/product/mek_8q/obj/KERNEL_OBJ'
  GEN     ./Makefile
scripts/kconfig/conf  --alldefconfig Kconfig
```