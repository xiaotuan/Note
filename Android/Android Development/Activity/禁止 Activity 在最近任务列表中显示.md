在 `AndroidManifest.xml` 文件注册 `Activity` 时，添加如下属性：

```xml
android:excludeFromRecents="true"
```

例如：

```xml
<activity
    android:name="com.mediatek.factorymode.FactoryReset"
    android:exported="false"
    android:label="@string/reboot_name"
    android:screenOrientation="portrait"
    android:excludeFromRecents="true" />
```

