[toc]

### 1. MTK

#### 1.1 MT8781

##### 1.1.1 Android T

通过修改 `sys/packages/apps/Launcher3/src/com/android/launcher3/util/DisplayController.java` 文件中 `isTablet()` 方法返回值为 `false` 后，桌面使用了错误的布局文件。通过跟踪代码发现，在 `sys/packages/apps/Launcher3/src/com/android/launcher3/InvariantDeviceProfile.java` 文件中，`InvariantDeviceProfile` 类通过调用 `getDeviceType()` 方法获取设备类型，来初始化桌面布局文件。

在 `getDeviceType()` 方法中调用了 `DisplayController.java` 类中的 `isTablet()` 方法来判断设备是否是平板：

```java
private static @DeviceType int getDeviceType(Info displayInfo) {
    int flagPhone = 1 << 0;
    int flagTablet = 1 << 1;

    int type = displayInfo.supportedBounds.stream()
            .mapToInt(bounds -> displayInfo.isTablet(bounds) ? flagTablet : flagPhone)
            .reduce(0, (a, b) -> a | b);
    if ((type == (flagPhone | flagTablet)) && ENABLE_TWO_PANEL_HOME.get()) {
        // device has profiles supporting both phone and table modes
        return TYPE_MULTI_DISPLAY;
    } else if (type == flagTablet) {
        return TYPE_TABLET;
    } else {
        return TYPE_PHONE;
    }
}
```

因此，`getDeviceType()` 将会返回 `TYPE_PHONE` 。而在 `sys/packages/apps/Launcher3/res/xml/device_profiles.xml` 文件中，配置的布局中的 `launcher:deviceCategory` 属性值为 `tablet`，因此， `InvariantDeviceProfile` 类会将其视为不可用布局。

因此要解决这个问题，可以将 `sys/packages/apps/Launcher3/res/xml/device_profiles.xml`  文件中 `launcher:deviceCategory` 属性的值设置为 `phone` 来解决。