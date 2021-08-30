[toc]

### 1. 展讯

#### 1.1 Android R(Android 11)

在 `device/sprd/mpool/modul/main.mk` 文件中有一个属性配置 WiFi 热点名称的配置（它的名字又叫 WiFi 直连），如下代码所示：

```makefile
PRODUCT_SYSTEM_EXT_PROPERTIES += persist.wb.wifi_direct_name=Magnum_Pro	
```

> 注意：名称不能包含空格，否则空格后面的字符将会被忽略。

### 2. Android 标准修改流程

修改 `frameworks/opt/net/wifi/service/java/com/android/server/wifi/WifiApConfigStore.java` 文件中 `getDefaultApConfiguration()` 方法的 `configBuilder.setSsid(mContext.getResources().getString(R.string.wifi_tether_configure_ssid_default) + "_" + getRandomIntForDefaultSsid());` 代码即可:

```java
private SoftApConfiguration getDefaultApConfiguration() {
    SoftApConfiguration.Builder configBuilder = new SoftApConfiguration.Builder();
    configBuilder.setBand(SoftApConfiguration.BAND_2GHZ);
    configBuilder.setSsid(mContext.getResources().getString(
        R.string.wifi_tether_configure_ssid_default) + "_" + getRandomIntForDefaultSsid());
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

例如将 `wifi` 热点默认名称改为 `Magnum Pro` ，修改后的代码如下所示：

```java
private SoftApConfiguration getDefaultApConfiguration() {
    SoftApConfiguration.Builder configBuilder = new SoftApConfiguration.Builder();
    configBuilder.setBand(SoftApConfiguration.BAND_2GHZ);
    configBuilder.setSsid("Magnum Pro");
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
