[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

修改 `sys/vendor/partner_gms/overlay/gms_overlay/frameworks/base/core/res/res/values/config.xml` 文件的如下代码：

```diff
@@ -45,5 +45,5 @@
        <!-- Flag indicating whether we should enable smart battery. -->
     <bool name="config_smart_battery_available">true</bool>
        <!-- long press for Go to assistant -->
-       <integer name="config_longPressOnPowerBehavior">5</integer>
+       <integer name="config_longPressOnPowerBehavior">1</integer>
 </resources>
```

