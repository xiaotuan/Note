[toc]

### 1. MTK

#### 1.1 MTK8768

##### 1.1.1 Android S

1. 修改 `vendor/mediatek/proprietary/packages/apps/EngineerMode/Android.mk` 文件如下代码：

   ```diff
   @@ -64,75 +64,75 @@ LOCAL_STATIC_JAVA_LIBRARIES += vendor.mediatek.hardware.mtkradioex-V3.0-java
    endif
    
    # Files only for eng/user_debug load
   -ifeq ($(TARGET_BUILD_VARIANT), user)
   -    ENG_ONLY_TEL_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/amrwb) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/sbp) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/u3phy) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/simswitch) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/modemfilter) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/iatype) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/lte) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/mdmdiagnosticinfo) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/epdgconfig) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/fastdormancy) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/hspainfo) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/spc) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/npt) \
   -                         $(JAVA_SRC_DIR)/GPRS.java \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/gwsd) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/xpxtaging) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/dsdamonitor) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/multisimswitch) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/vodata) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/nrmapconfigure) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/data/NetworkSliceActivity.java) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/mdthermal) \
   -                         $(call all-java-files-under, $(JAVA_SRC_DIR)/divdualpolar)
   -
   -
   -    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_TEL_FILE), $(LOCAL_SRC_FILES))
   -
   -    ENG_ONLY_CONN_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/wfdsettings) \
   -                          $(JAVA_SRC_DIR)/wifi/WiFiMcr.java \
   -                          $(JAVA_SRC_DIR)/wifi/WiFiEeprom.java \
   -                          $(JAVA_SRC_DIR)/wifi/WiFiRFCR.java \
   -                          $(JAVA_SRC_DIR)/wifi/WifiEmCfgActivity.java \
   -                          $(call all-java-files-under, $(JAVA_SRC_DIR)/csreevaluation)
   -
   -    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_CONN_FILE), $(LOCAL_SRC_FILES))
   -
   -    ENG_ONLY_HARDWARE_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/memory) \
   -                              $(call all-java-files-under, $(JAVA_SRC_DIR)/power) \
   -                              $(call all-java-files-under, $(JAVA_SRC_DIR)/usb) \
   -                              $(call all-java-files-under, $(JAVA_SRC_DIR)/aoltest) \
   -                              $(JAVA_SRC_DIR)/UsbSuperSpeedSwitch.java \
   -                              $(JAVA_SRC_DIR)/AalSetting.java \
   -                              $(JAVA_SRC_DIR)/UartUsbSwitch.java
   -
   -    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_HARDWARE_FILE), $(LOCAL_SRC_FILES))
   -
   -    ENG_ONLY_LOCATION_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/cwtest) \
   -                              $(call all-java-files-under, $(JAVA_SRC_DIR)/desenseat) \
   -                              $(call all-java-files-under, $(JAVA_SRC_DIR)/clkqualityat) \
   -                              $(call all-java-files-under, $(JAVA_SRC_DIR)/dcbcalibration) \
   -                              $(call all-java-files-under, $(JAVA_SRC_DIR)/mnlconfigeditor)
   -
   -    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_LOCATION_FILE), $(LOCAL_SRC_FILES))
   -
   -    ENG_ONLY_LOG_DEBUG_FILE := $(JAVA_SRC_DIR)/BatteryLog.java \
   -                               $(call all-java-files-under, $(JAVA_SRC_DIR)/modemwarning) \
   -                               $(call all-java-files-under, $(JAVA_SRC_DIR)/modemresetdelay) \
   -                               $(call all-java-files-under, $(JAVA_SRC_DIR)/wcncoredump)
   -
   -    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_LOG_DEBUG_FILE), $(LOCAL_SRC_FILES))
   -
   -    ENG_ONLY_OTHERS_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/swla) \
   -                            $(call all-java-files-under, $(JAVA_SRC_DIR)/usbacm) \
   -                            $(JAVA_SRC_DIR)/carrierexpress/CarrierExpressActivity.java \
   -                            $(JAVA_SRC_DIR)/cip/CipPropContentActivity.java
   -
   -    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_OTHERS_FILE), $(LOCAL_SRC_FILES))
   -endif
   +#ifeq ($(TARGET_BUILD_VARIANT), user)
   +#    ENG_ONLY_TEL_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/amrwb) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/sbp) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/u3phy) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/simswitch) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/modemfilter) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/iatype) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/lte) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/mdmdiagnosticinfo) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/epdgconfig) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/fastdormancy) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/hspainfo) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/spc) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/npt) \
   +#                         $(JAVA_SRC_DIR)/GPRS.java \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/gwsd) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/xpxtaging) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/dsdamonitor) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/multisimswitch) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/vodata) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/nrmapconfigure) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/data/NetworkSliceActivity.java) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/mdthermal) \
   +#                         $(call all-java-files-under, $(JAVA_SRC_DIR)/divdualpolar)
   +#
   +#
   +#    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_TEL_FILE), $(LOCAL_SRC_FILES))
   +#
   +#    ENG_ONLY_CONN_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/wfdsettings) \
   +#                          $(JAVA_SRC_DIR)/wifi/WiFiMcr.java \
   +#                          $(JAVA_SRC_DIR)/wifi/WiFiEeprom.java \
   +#                          $(JAVA_SRC_DIR)/wifi/WiFiRFCR.java \
   +#                          $(JAVA_SRC_DIR)/wifi/WifiEmCfgActivity.java \
   +#                          $(call all-java-files-under, $(JAVA_SRC_DIR)/csreevaluation)
   +#
   +#    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_CONN_FILE), $(LOCAL_SRC_FILES))
   +#
   +#    ENG_ONLY_HARDWARE_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/memory) \
   +#                              $(call all-java-files-under, $(JAVA_SRC_DIR)/power) \
   +#                              $(call all-java-files-under, $(JAVA_SRC_DIR)/usb) \
   +#                              $(call all-java-files-under, $(JAVA_SRC_DIR)/aoltest) \
   +#                              $(JAVA_SRC_DIR)/UsbSuperSpeedSwitch.java \
   +#                              $(JAVA_SRC_DIR)/AalSetting.java \
   +#                              $(JAVA_SRC_DIR)/UartUsbSwitch.java
   +#
   +#    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_HARDWARE_FILE), $(LOCAL_SRC_FILES))
   +#
   +#    ENG_ONLY_LOCATION_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/cwtest) \
   +#                              $(call all-java-files-under, $(JAVA_SRC_DIR)/desenseat) \
   +#                              $(call all-java-files-under, $(JAVA_SRC_DIR)/clkqualityat) \
   +#                              $(call all-java-files-under, $(JAVA_SRC_DIR)/dcbcalibration) \
   +#                              $(call all-java-files-under, $(JAVA_SRC_DIR)/mnlconfigeditor)
   +#
   +#    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_LOCATION_FILE), $(LOCAL_SRC_FILES))
   +#
   +#    ENG_ONLY_LOG_DEBUG_FILE := $(JAVA_SRC_DIR)/BatteryLog.java \
   +#                               $(call all-java-files-under, $(JAVA_SRC_DIR)/modemwarning) \
   +#                               $(call all-java-files-under, $(JAVA_SRC_DIR)/modemresetdelay) \
   +#                               $(call all-java-files-under, $(JAVA_SRC_DIR)/wcncoredump)
   +#
   +#    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_LOG_DEBUG_FILE), $(LOCAL_SRC_FILES))
   +#
   +#    ENG_ONLY_OTHERS_FILE := $(call all-java-files-under, $(JAVA_SRC_DIR)/swla) \
   +#                            $(call all-java-files-under, $(JAVA_SRC_DIR)/usbacm) \
   +#                            $(JAVA_SRC_DIR)/carrierexpress/CarrierExpressActivity.java \
   +#                            $(JAVA_SRC_DIR)/cip/CipPropContentActivity.java
   +#
   +#    LOCAL_SRC_FILES := $(filter-out $(ENG_ONLY_OTHERS_FILE), $(LOCAL_SRC_FILES))
   +#endif
    
    ifeq (,$(filter $(MSSI_MTK_TELEPHONY_ADD_ON_POLICY),1))
    
   ```

2. 修改 `vendor/mediatek/proprietary/packages/apps/EngineerMode/src/com/mediatek/engineermode/FeatureSupport.java` 文件的如下代码：

   ```diff
   @@ -199,11 +199,11 @@ public class FeatureSupport {
    
        public static boolean isUserLoad() {
            Elog.i(TAG, "FK_BUILD_TYPE:" + SystemProperties.get(FK_BUILD_TYPE));
   -        return USER_LOAD.equals(SystemProperties.get(FK_BUILD_TYPE));
   +        return false; //USER_LOAD.equals(SystemProperties.get(FK_BUILD_TYPE));
        }
    
        public static boolean isUserDebugLoad() {
   -        return USERDEBUG_LOAD.equals(SystemProperties.get(FK_BUILD_TYPE));
   +        return true;//USERDEBUG_LOAD.equals(SystemProperties.get(FK_BUILD_TYPE));
        }
    
        public static boolean isSupportWfc() {
   ```

   