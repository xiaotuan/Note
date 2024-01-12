[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

修改 `u_sys/frameworks/base/core/res/res/values/config.xml` 文件的如下代码：

```xml
<!-- LED behavior when battery is low.
     Color for solid is taken from config_notificationsBatteryLowARGB
      0 - default, solid when charging, flashing when not charging
      1 - always solid when battery is low
      2 - always flashing when battery is low -->
<integer name="config_notificationsBatteryLowBehavior">0</integer>
```

> 提示：
>
> 固态的颜色取自config_notificationsBatteryLowARGB
> 0 -默认，充电时固态，不充电时闪烁
> 1 -电池电量低时始终保持固态
> 2 -电池电量低时始终闪烁