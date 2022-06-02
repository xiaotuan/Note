[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

修改 `frameworks/opt/net/wifi/service/java/com/android/server/wifi/WifiApConfigStore.java` 类中 `getDefaultApConfiguration()` 方法：

```java
private SoftApConfiguration getDefaultApConfiguration() {
    SoftApConfiguration.Builder configBuilder = new SoftApConfiguration.Builder();
    configBuilder.setBand(SoftApConfiguration.BAND_2GHZ);
    /* 注释如下代码
    // configBuilder.setSsid(mContext.getResources().getString(
    // R.string.wifi_tether_configure_ssid_default) + "_" + getRandomIntForDefaultSsid());
    */
    configBuilder.setSsid("Elite_T8Plus");	// 添加该行代码
    if (ApConfigUtil.isWpa3SaeSupported(mContext)) {
        configBuilder.setPassphrase(generatePassword(),
                                    SoftApConfiguration.SECURITY_TYPE_WPA3_SAE_TRANSITION);
    } else {
        configBuilder.setPassphrase(generatePassword(),
                                    SoftApConfiguration.SECURITY_TYPE_WPA2_PSK);
    }
    return configBuilder.build();
}
```

#### 1.2 MTK8765

##### 1.2.1 Android S

修改`packages/modules/Wifi/service/java/com/android/server/wifi/WifiApConfigStore.java` 文件中的 `getDefaultApConfiguration()` 方法的如下代码：

```java
configBuilder.setSsid(mContext.getResources().getString(
                R.string.wifi_tether_configure_ssid_default) + "_" + getRandomIntForDefaultSsid());
```

将其修改为需要设置的 WiFi 热点名称，例如：

```java
configBuilder.setSsid("E8765");
```

> 注意：该方法在 GMS 项目中修改无效，因为改模块已经被 `vendor/partner_modules/WiFiPrebuilt` 模块覆盖了。询问 MTK 后，MTK 说 WiFiPrebuilt 模块不是必须的，可以替换成 MTK 模块，只是不建议而已。替换成 MTK 模块的方法是修改 `device/mediatek/system/common/device.mk` 文件中的如下代码：
>
> ```diff
> @@ -3915,7 +3915,7 @@ ifneq ($(wildcard vendor/partner_modules/build),)
>              # FBE is mandatory for Q new launching device
>              # Mainline partner build config - updatable APEX
>              PRODUCT_SYSTEM_PROPERTIES += ro.apex.updatable=true
> -            MAINLINE_INCLUDE_WIFI_MODULE := true
> +            MAINLINE_INCLUDE_WIFI_MODULE := false
>              MAINLINE_COMPRESS_APEX_ART := true
>              MAINLINE_COMPRESS_APEX_MEDIAPROVIDER := true
>              $(call inherit-product, vendor/partner_modules/build/mainline_modules.mk)
> ```



> 提示：可以参考 `device/google/coral/rro_overlays/WifiOverlay/`  资源覆盖示例，覆盖 `wifi_tether_configure_ssid_default` 资源的值。
