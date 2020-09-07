`WiFiManager` 类的一些其他隐藏方法提供了更多关于 `Wi-Fi` 网络共享的信息。

```java
private WifiConfiguration getWifiApConfig() {
    WifiConfiguration wifiConfiguration = null;
    try {
        WifiManager wifiManager = (WifiManager) getSystemService(WIFI_SERVICE);
        Class clazz = WifiManager.class;
        Method getWifiApConfigurationMethod = clazz.getMethod("getWifiApConfiguration");
        return (WifiConfiguration) getWifiApConfigurationMathod.invoke(wifiManager);
    } catch (NoSuchMethodException e) {
        Log.e(TAG, "Cannot find method", e);
    } catch (IllegalAccessException e) {
        Log.e(TAG, "Cannot call method", e);
    } catch (InvocationTargetException e) {
        Log.e(TAG, "Cannot call method", e);
    }
    return wifiConfiguration;
}
```

上面的代码显示了如何为设备上的 Wi-Fi 网络共享设置检索 WifiConfiguration 对象。注意，调用这些方法需要应用程序具有 android.permission.ACCESS_WIFI_STATE 权限。然而，如果像前面的代码那样获取 Wi-Fi 网络共享设置的 WifiConfiguration 对象，会发现 preSharedKey 呈现的是明文密码。这样一来，当激活 Wi-Fi 网络共享时，应用程序可以获取创建的访问点的名字和密码。