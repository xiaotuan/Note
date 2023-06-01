[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 修改 `sys/device/mediatek/system/common/mtklog/mtklog-config-basic-eng.prop`、`sys/device/mediatek/system/common/mtklog/mtklog-config-basic-user.prop`、`sys/device/mediatek/system/common/mtklog/mtklog-config-bsp-eng.prop` 和 `sys/device/mediatek/system/common/mtklog/mtklog-config-bsp-user.prop`  文件中 `mtklog_path = system_data`  为 `mtklog_path = device_storage`：

   ```diff
   diff --git a/device/mediatek/system/common/mtklog/mtklog-config-basic-eng.prop b/device/mediatek/system/common/mtklog/mtklog-config-basic-eng.prop
   index c7204ba0ceb..76fb4706edf 100644
   --- a/device/mediatek/system/common/mtklog/mtklog-config-basic-eng.prop
   +++ b/device/mediatek/system/common/mtklog/mtklog-config-basic-eng.prop
   @@ -1,5 +1,5 @@
    # mtk log path can be set as system_data or device_storage or portable_storage
   -mtklog_path = system_data
   +mtklog_path = device_storage
    com.mediatek.log.mobile.customer = MTK_Internal
    com.mediatek.log.mobile.AllMode = true
    
   diff --git a/device/mediatek/system/common/mtklog/mtklog-config-basic-user.prop b/device/mediatek/system/common/mtklog/mtklog-config-basic-user.prop
   index 0b0efb3cedc..7c9cc3e2106 100644
   --- a/device/mediatek/system/common/mtklog/mtklog-config-basic-user.prop
   +++ b/device/mediatek/system/common/mtklog/mtklog-config-basic-user.prop
   @@ -1,5 +1,5 @@
    # mtk log path can be set as system_data or device_storage or portable_storage
   -mtklog_path = system_data
   +mtklog_path = device_storage
    com.mediatek.log.mobile.customer = MTK_Internal
    com.mediatek.log.mobile.AllMode = true
    
   diff --git a/device/mediatek/system/common/mtklog/mtklog-config-bsp-eng.prop b/device/mediatek/system/common/mtklog/mtklog-config-bsp-eng.prop
   index c7204ba0ceb..76fb4706edf 100644
   --- a/device/mediatek/system/common/mtklog/mtklog-config-bsp-eng.prop
   +++ b/device/mediatek/system/common/mtklog/mtklog-config-bsp-eng.prop
   @@ -1,5 +1,5 @@
    # mtk log path can be set as system_data or device_storage or portable_storage
   -mtklog_path = system_data
   +mtklog_path = device_storage
    com.mediatek.log.mobile.customer = MTK_Internal
    com.mediatek.log.mobile.AllMode = true
    
   diff --git a/device/mediatek/system/common/mtklog/mtklog-config-bsp-user.prop b/device/mediatek/system/common/mtklog/mtklog-config-bsp-user.prop
   index 0b0efb3cedc..7c9cc3e2106 100644
   --- a/device/mediatek/system/common/mtklog/mtklog-config-bsp-user.prop
   +++ b/device/mediatek/system/common/mtklog/mtklog-config-bsp-user.prop
   @@ -1,5 +1,5 @@
    # mtk log path can be set as system_data or device_storage or portable_storage
   -mtklog_path = system_data
   +mtklog_path = device_storage
    com.mediatek.log.mobile.customer = MTK_Internal
    com.mediatek.log.mobile.AllMode = true
   ```

2. 修改 `sys/vendor/mediatek/proprietary/external/NetworkLogD/netdiag/src/full_test_data.cpp` 文件中 `isCustomerUserLoad()` 方法的如下代码：

   ```diff
   @@ -236,7 +236,10 @@ bool isCustomerUserLoad() {
        }
        LOGD("isCustomerUserLoad()? %d,internal = %s,buildtype =%s", result,
                internal, buildtype);
   -    return result;
   +    // The default MTKLog storage location is internal storage by qty {{&&
   +    // return result;
   +    return false;
   +    // &&}}
    }
    
    void full_test(char *local, char *action, char * NTLog_name, char * ping_flag) {
   ```

3. 修改 `sys/vendor/mediatek/proprietary/external/connsyslogD/SocketConnection.cpp` 文件中 `isCustomerUserLoad()` 方法的如下代码：

   ```diff
   @@ -222,7 +222,10 @@ bool socketconnection::isCustomerUserLoad() {
        }
        LOGD("isCustomerUserLoad()? %d,internal = %s,buildtype =%s",
             result, internal, buildtype );
   -    return result;
   +    // The default MTKLog storage location is internal storage by qty {{&&
   +    // return result;
   +    return false;
   +    // &&}}
    }
    
    extern bool setStoragePath(char* path);
   ```

4. 修改 `sys/vendor/mediatek/proprietary/external/mobile_log_d/config.c` 文件中 `load_type()` 方法的如下代码：

   ```diff
   @@ -794,5 +794,8 @@ int load_type() {
        property_get("ro.build.type", build_type, "");
        property_get("ro.vendor.mtklog_internal", internal_prpject, "");
        if (strcmp(build_type, "user") != 0 || strcmp(internal_prpject, "1") == 0) return 0;
   -    return 1;
   +    // The default MTKLog storage location is internal storage by qty {{&&
   +    // return 1;
   +    return 0;
   +    // &&}}
    }
   ```

5. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MTKLogger/src/com/debug/loggerui/utils/Utils.java` 文件中 `isCustomerUserLoad()` 方法的如下代码：

   ```diff
   @@ -413,7 +413,10 @@ public class Utils {
         * @return boolean
         */
        public static boolean isCustomerUserLoad() {
   -        return Utils.BUILD_TYPE.equals("user") && isCustomerLoad();
   +        // The default MTKLog storage location is internal storage by qty {{&&
   +        // return Utils.BUILD_TYPE.equals("user") && isCustomerLoad();
   +        return false;
   +        // &&}}
        }
    
        /**
   ```

   