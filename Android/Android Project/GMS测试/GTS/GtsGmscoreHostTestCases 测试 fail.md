[toc]

### 1. com.google.android.gts.devicepolicy.managedprovisioning.DeviceOwnerProvisioningHostsideTest#testRequiredAppsInManagedDevice 和 com.google.android.gts.devicepolicy.managedprovisioning.DeviceOwnerProvisioningHostsideTest#testRequiredAppsInManagedUser 测试 Fail

#### 1. 报错信息

```
java.lang.AssertionError: Should have at least one packages to handle Intent { act=android.intent.action.DIAL }, found []
```

#### 2. 报错原因

项目是 WiFi-only 项目，需要去掉拨号应用。

#### 3. 解决办法

查看测试源码后发现，该项测试是根据 `android.software.connectionservice` 功能进行检测的，当发现设备存在该功能，则会检测该项测试。因此去掉该功能即可。

拷贝 `frameworks/native/data/etc/handheld_core_hardware.xml` 文件至 `/device/mediateksample/tb8768p1_64_bsp/` 目录下，并去掉该文件中的 `<feature name="android.software.connectionservice" />` 项即可。

