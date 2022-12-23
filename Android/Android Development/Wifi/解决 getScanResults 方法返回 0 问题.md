在 Android 6.0 及以上版本，调用 `WifiManager.getScanResults()` 方法返回的列表长度为 0 ，解决这个问题的办法是在清单文件中添加如下权限：

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

