[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android S

修改 `sys/packages/modules/Wifi/service/java/com/android/server/wifi/ClientModeImpl.java` 文件中 `retrieveFactoryMacAddressAndStoreIfNecessary()` 方法的如下代码：

```diff
@@ -6616,9 +6616,11 @@ public class ClientModeImpl extends StateMachine implements ClientMode {
                 mWifiGlobals.isSaveFactoryMacToConfigStoreEnabled();
         if (saveFactoryMacInConfigStore) {
             // Already present, just return.
-            String factoryMacAddressStr = mSettingsConfigStore.get(WIFI_STA_FACTORY_MAC_ADDRESS);
-            if (factoryMacAddressStr != null) return MacAddress.fromString(factoryMacAddressStr);
-        }
+                       // WiFi Mac addresses can be modified using Nvram by qty at 2023-02-07 {{&&
+            // String factoryMacAddressStr = mSettingsConfigStore.get(WIFI_STA_FACTORY_MAC_ADDRESS);
+            // if (factoryMacAddressStr != null) return MacAddress.fromString(factoryMacAddressStr);
+                       // &&}}
+               }
         MacAddress factoryMacAddress = mWifiNative.getStaFactoryMacAddress(mInterfaceName);
         if (factoryMacAddress == null) {
             // the device may be running an older HAL (version < 1.3).
```

