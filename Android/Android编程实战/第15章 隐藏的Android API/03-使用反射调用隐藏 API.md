使用反射调用隐藏的 API 需要两步。首先，需要查找要调用的类和方法，并把它们的引用存到 Method 对象中。当持有了引用后，接下来可以调用对象的方法。下面的代码演示了查找检查 Wi-Fi 网络共享状态的方法的两个过程：

```java
public Method getWifiAPMethod(WifiManager wifiManager) {
    try {
        Class clazz = wifiManager.getClass();
        return clazz.getMethod("isWifiApEnabled");
    } catch (NoSuchMethodException e) {
        throw new RuntimeException(e);
    }
}

public boolean invokeIsWifiAPEnabled(WifiManager wifiManager, Method isWifiApEnabledMethod) {
    try {
        return (Boolean) isWifiApEnabledMethod.invoke(wifiManager);
    } catch (IllegalAccessException e) {
        throw new RuntimeException(e);
    } catch (InvocationTargetException e) {
        throw new RuntimeException(e);
    }
}
```

