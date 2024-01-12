[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

修改 `u_sys/frameworks/base/core/res/res/values/config.xml` 文件的如此代码：

```diff
@@ -1375,7 +1375,7 @@
     <integer name="config_notificationsBatteryLedOn">125</integer>
 
     <!-- Is the notification LED intrusive? Used to decide if there should be a disable option -->
-    <bool name="config_intrusiveNotificationLed">false</bool>
+    <bool name="config_intrusiveNotificationLed">true</bool>
 
     <!-- De we do icon badges? Used to decide if there should be a disable option-->
     <bool name="config_notificationBadging">true</bool>
```

