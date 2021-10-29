[toc]

### 1. MTK 平台

#### 1.1 MTK8766、Android R

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

