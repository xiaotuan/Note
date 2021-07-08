[toc]

### 1. 展讯

#### 1. Android R(Android 11)

修改 `frameworks\opt\net\wifi\service\java\com\android\server\wifi\WifiApConfigStore.java` 文件中 `getDefaultApConfiguration()` 方法的 `configBuilder.setSsid(mContext.getResources().getString(R.string.wifi_tether_configure_ssid_default) + "_" + getRandomIntForDefaultSsid());` 代码即可:

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

