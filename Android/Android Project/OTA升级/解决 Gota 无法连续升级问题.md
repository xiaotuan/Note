**平台：** MTK

**芯片：**MT8766

**系统版本：**Android R

**报错信息：**

```
E: Error opening trace file: No such file or directory(2)
Supported API: 3
Finding update package...
Verifying update package...
Update package verification took 0.5 s (result 0).
Installing update...
Source: Masstel/Masstel_Tab8_Edu/Masstel_Tab8_Edu:11/RP1A.200720.011/1641879956:user/release-keys
Target: Masstel/Masstel_Tab8_Edu/Masstel_Tab8_Edu:11/RP1A.200720.011/1642151673:user/release-keys
Verifying current system...
E3001: Package expects build fingerprint of Masstel/Masstel_Tab8_Edu/Masstel_Tab8_Edu:11/RP1A.200720.011/1641879956:user/release-keys or Masstel/Masstel_Tab8_Edu/Masstel_Tab8_Edu:11/RP1A.200720.011/1642151673:user/release-keys; this device has Masstel/Masstel_Tab8_Edu/Masstel_Tab8_Edu:11/RP1A.200720.011/1640591398:user/release-keys.
E:Error in /cache/update.zip (status 1)

Installation aborted.
```

**原因分析：**

Recovery 模式下，系统获取到的 fingerprint  的值为老版本软件的 fingerprint，与要升级的升级包 fingerprint 值不一致导致的。

**解决办法：**

**1. 完全解决方法**

在 `device/mediateksample/m863u_bsp_64/device.mk` 文件中添加如下代码：

```makefile
BOARD_USES_FULL_RECOVERY_IMAGE = true
```

**2. 临时解决办法**

在做升级包时，去掉 fingerprint 判断条件。代码修改如下：

**build/make/tools/releasetools/ota_from_target_files.py**

```diff
diff --git a/build/make/tools/releasetools/ota_from_target_files.py b/build/make/tools/releasetools/ota_from_target_files.py
index 3b68439d8fd..417d6261e28 100755
--- a/build/make/tools/releasetools/ota_from_target_files.py
+++ b/build/make/tools/releasetools/ota_from_target_files.py
@@ -1477,7 +1477,7 @@ else if get_stage("%(bcb_dev)s") != "3/3" then
 
   device_specific.IncrementalOTA_VerifyBegin()
 
-  WriteFingerprintAssertion(script, target_info, source_info)
+  # WriteFingerprintAssertion(script, target_info, source_info)
 
   # Check the required cache size (i.e. stashed blocks).
   required_cache_sizes = [diff.required_cache for diff in
```
