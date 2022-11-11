[toc]

### 1. MTK 平台

#### 1.1 MT8788

##### 1.1.1 Android S

1. 在 `device/mediatek/vendor/common/connectivity/product_package/wlan_product_package.mk` 的如下代码：

   ```makefile
   ifneq ($(filter $(WLAN_GEN3_CHIPS), $(MTK_COMBO_CHIP)),)
   DUTINFO_NAME := 6631_gen3
   PRODUCT_PACKAGES += wlan_drv_gen3.ko
   PRODUCT_PROPERTY_OVERRIDES += ro.vendor.wlan.gen=gen3
   else ifneq ($(filter $(WLAN_GEN4M_CHIPS), $(MTK_COMBO_CHIP)),)
       ifneq ($(filter $(WLAN_BRANCH_5_SERIES) $(WLAN_BRANCH_3_SERIES), $(WLAN_CHIP_ID)),)
           DUTINFO_NAME := 6635_gen4m
       else
           DUTINFO_NAME := 6631_gen4m
       endif
   PRODUCT_PACKAGES += wlan_drv_gen4m.ko
   PRODUCT_PROPERTY_OVERRIDES += ro.vendor.wlan.standalone.log=y
   PRODUCT_PROPERTY_OVERRIDES += ro.vendor.wlan.gen=gen4m
   WIFI_HAL_INTERFACE_COMBINATIONS := {{{STA}, 2}}
   WIFI_HAL_INTERFACE_COMBINATIONS += ,{{{AP}, 2},}
   WIFI_HAL_INTERFACE_COMBINATIONS += ,{{{STA}, 1}, {{AP}, 1}}
   WIFI_HAL_INTERFACE_COMBINATIONS += ,{{{STA}, 1}, {{P2P}, 1}}
   WIFI_HAL_INTERFACE_COMBINATIONS += ,{{{STA}, 1}, {{NAN}, 1}}
   else ifneq ($(filter CONSYS_%, $(MTK_COMBO_CHIP)),)
   DUTINFO_NAME := 6625_gen2
   PRODUCT_PACKAGES += wlan_drv_gen2.ko
   PRODUCT_PROPERTY_OVERRIDES += ro.vendor.wlan.gen=gen2
   endif
   ```

   确认如下代码是否和上面代码一致：

   ```makefile
   WIFI_HAL_INTERFACE_COMBINATIONS += ,{{{STA}, 1}, {{AP}, 1}}
   ```

2. 修改 `device/mediateksample/tb8788p1_64_bsp_k419/BoardConfig.mk` 文件的如下代码：

   ```diff
   @@ -8,6 +8,9 @@ include device/mediatek/mt6771/BoardConfig.mk
    BOARD_ROOT_EXTRA_FOLDERS += metadata
    BOARD_USES_METADATA_PARTITION := true
    
   +# STA AP Concurrence config to overlay the BoardConfig
   +WIFI_HIDL_FEATURE_DUAL_INTERFACE := true
   +
    # ptgen
    MTK_PTGEN_CHIP := $(shell echo $(TARGET_BOARD_PLATFORM) | tr '[a-z]' '[A-Z]')
    -include vendor/mediatek/proprietary/tools/ptgen/common/ptgen.mk
   ```

3. 修改 `vendor/mediatek/proprietary/hardware/connectivity/wlan/wifi_hal/wifi_hal.cpp` 文件的如下代码：

   ```diff
   @@ -83,7 +83,9 @@ static int internal_no_seq_check(nl_msg *msg, void *arg);
    static int internal_valid_message_handler(nl_msg *msg, void *arg);
    static int wifi_get_multicast_id(wifi_handle handle, const char *name, const char *group);
    static int wifi_add_membership(wifi_handle handle, const char *group);
   -static wifi_error wifi_init_interfaces(wifi_handle handle);
   +// M: gen3 STA+SAP
   +//static wifi_error wifi_init_interfaces(wifi_handle handle);
   +wifi_error wifi_init_interfaces(wifi_handle handle);
    static wifi_error wifi_start_rssi_monitoring(wifi_request_id id, wifi_interface_handle
                            iface, s8 max_rssi, s8 min_rssi, wifi_rssi_event_handler eh);
    static wifi_error wifi_stop_rssi_monitoring(wifi_request_id id, wifi_interface_handle iface);
   ```

4. 修改 `hardware/libhardware_legacy/include/hardware_legacy/wifi_hal.h` 文件如下代码：

   ```diff
   @@ -896,6 +896,9 @@ typedef struct {
    wifi_error init_wifi_vendor_hal_func_table(wifi_hal_fn *fn);
    typedef wifi_error (*init_wifi_vendor_hal_func_table_t)(wifi_hal_fn *fn);
    
   +// M: gen3 STA+SAP
   +wifi_error wifi_init_interfaces(wifi_handle handle);
   +
    #ifdef __cplusplus
    }
    #endif
   ```

5. 修改 `hardware/interfaces/wifi/1.5/default/wifi_chip.cpp` 文件如下代码：

   ```diff
   @@ -961,6 +961,16 @@ WifiChip::createApIfaceInternal() {
        if (!canCurrentModeSupportIfaceOfTypeWithCurrentIfaces(IfaceType::AP)) {
            return {createWifiStatus(WifiStatusCode::ERROR_NOT_AVAILABLE), {}};
        }
   +       
   +       // M: Change firmware mode here for gen3
   +    std::array<char, PROPERTY_VALUE_MAX> buffer;
   +    property_get("ro.vendor.wlan.gen", buffer.data(), "");
   +    if (0 == strncmp(buffer.data(), "gen3", 4) &&
   +        isStaApConcurrencyAllowedInCurrentMode()) {
   +        mode_controller_.lock()->changeFirmwareMode(IfaceType::AP);
   +        legacy_hal_.lock()->refreshInterfaces();
   +    }
   +       
        std::string ifname = allocateApIfaceName();
        WifiStatus status = createVirtualApInterface(ifname);
        if (status.code != WifiStatusCode::SUCCESS) {
   @@ -1047,6 +1057,18 @@ WifiStatus WifiChip::removeApIfaceInternal(const std::string& ifname) {
            }
        }
        setActiveWlanIfaceNameProperty(getFirstActiveWlanIfaceName());
   +       
   +       // M: Change firmware mode here for gen3
   +    std::array<char, PROPERTY_VALUE_MAX> buffer;
   +    property_get("ro.vendor.wlan.gen", buffer.data(), "");
   +    if (0 == strncmp(buffer.data(), "gen3", 4) &&
   +        isStaApConcurrencyAllowedInCurrentMode() &&
   +            !sta_ifaces_.empty()) {
   +            LOG(INFO) << "[STA+SAP] Change firmware mode to STA when stopping SAP";
   +            mode_controller_.lock()->changeFirmwareMode(IfaceType::STA);
   +            legacy_hal_.lock()->refreshInterfaces();
   +    }
   +       
        return createWifiStatus(WifiStatusCode::SUCCESS);
    }
    
   @@ -1199,6 +1221,16 @@ WifiChip::createStaIfaceInternal() {
        if (!canCurrentModeSupportIfaceOfTypeWithCurrentIfaces(IfaceType::STA)) {
            return {createWifiStatus(WifiStatusCode::ERROR_NOT_AVAILABLE), {}};
        }
   +       
   +       // M: Change firmware mode here for gen3
   +    std::array<char, PROPERTY_VALUE_MAX> buffer;
   +    property_get("ro.vendor.wlan.gen", buffer.data(), "");
   +    if (0 == strncmp(buffer.data(), "gen3", 4) &&
   +            isStaApConcurrencyAllowedInCurrentMode()) {
   +            mode_controller_.lock()->changeFirmwareMode(IfaceType::STA);
   +            legacy_hal_.lock()->refreshInterfaces();
   +    }
   +
        std::string ifname = allocateStaIfaceName();
        legacy_hal::wifi_error legacy_status =
            legacy_hal_.lock()->createVirtualInterface(
   @@ -1216,6 +1248,14 @@ WifiChip::createStaIfaceInternal() {
                LOG(ERROR) << "Failed to invoke onIfaceAdded callback";
            }
        }
   +       
   +       // M: Change firmware mode here for gen3
   +    if (0 == strncmp(buffer.data(), "gen3", 4) && !ap_ifaces_.empty()) {
   +        LOG(INFO) << "[STA+SAP] Change firmware mode to AP when create STA";
   +        mode_controller_.lock()->changeFirmwareMode(IfaceType::AP);
   +        legacy_hal_.lock()->refreshInterfaces();
   +    }
   +       
        setActiveWlanIfaceNameProperty(getFirstActiveWlanIfaceName());
        return {createWifiStatus(WifiStatusCode::SUCCESS), iface};
    }
   @@ -1257,6 +1297,18 @@ WifiStatus WifiChip::removeStaIfaceInternal(const std::string& ifname) {
            }
        }
        setActiveWlanIfaceNameProperty(getFirstActiveWlanIfaceName());
   +       
   +       // M: Change firmware mode here for gen3
   +    std::array<char, PROPERTY_VALUE_MAX> buffer;
   +    property_get("ro.vendor.wlan.gen", buffer.data(), "");
   +    if (0 == strncmp(buffer.data(), "gen3", 4) &&
   +        isStaApConcurrencyAllowedInCurrentMode() &&
   +            !ap_ifaces_.empty()) {
   +             LOG(INFO) << "[STA+SAP] Change firmware mode to AP when stopping STA";
   +             mode_controller_.lock()->changeFirmwareMode(IfaceType::AP);
   +            legacy_hal_.lock()->refreshInterfaces();
   +    }
   +
        return createWifiStatus(WifiStatusCode::SUCCESS);
    }
    
   ```

6. 修改 `hardware/interfaces/wifi/1.5/default/wifi_legacy_hal.cpp` 文件如下代码：

   ```diff
   @@ -1452,6 +1452,21 @@ wifi_error WifiLegacyHal::setCountryCode(const std::string& iface_name,
                                                        code_str.c_str());
    }
    
   +// M: gen3 STA+SAP
   +wifi_error WifiLegacyHal::refreshInterfaces() {
   +    wifi_error status = wifi_init_interfaces(global_handle_);
   +    if (status != WIFI_SUCCESS) {
   +        LOG(ERROR) << "Failed to retrieve wifi interfaces";
   +        return status;
   +    }
   +    status = retrieveIfaceHandles();
   +    if (status != WIFI_SUCCESS || iface_name_to_handle_.empty()) {
   +        LOG(ERROR) << "Failed to retrieve wlan interface handle";
   +        return status;
   +    }
   +    return WIFI_SUCCESS;
   +}
   +
    wifi_error WifiLegacyHal::retrieveIfaceHandles() {
        wifi_interface_handle* iface_handles = nullptr;
        int num_iface_handles = 0;
   ```

7. 修改 `hardware/interfaces/wifi/1.5/default/wifi_legacy_hal.h` 文件如下代码：

   ```diff
   @@ -670,6 +670,9 @@ class WifiLegacyHal {
        // AP functions.
        wifi_error setCountryCode(const std::string& iface_name,
                                  std::array<int8_t, 2> code);
   +                                                         
   +       // M: gen3 STA+SAP
   +    wifi_error refreshInterfaces();
    
        // interface functions.
        virtual wifi_error createVirtualInterface(const std::string& ifname,
   ```

   