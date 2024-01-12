[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

修改 `u_sys/frameworks/base/core/res/res/values/config.xml` 文件的如下代码：

```xml
<!-- Default value for led color when battery is low on charge -->
<integer name="config_notificationsBatteryLowARGB">0xFFFF0000</integer>

<!-- Default value for led color when battery is medium charged -->
<integer name="config_notificationsBatteryMediumARGB">0xFFFFFF00</integer>

<!-- Default value for led color when battery is fully or nearly fully charged -->
<integer name="config_notificationsBatteryFullARGB">0xFF00FF00</integer>
```

