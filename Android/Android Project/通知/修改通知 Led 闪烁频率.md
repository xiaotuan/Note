[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

修改 `u_sys/frameworks/base/core/res/res/values/config.xml` 文件中的如下代码：

```xml
<!-- Default LED on time for notification LED in milliseconds. -->
<integer name="config_defaultNotificationLedOn">500</integer>

<!-- Default LED off time for notification LED in milliseconds. -->
<integer name="config_defaultNotificationLedOff">2000</integer>
```

