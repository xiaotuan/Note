[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

修改 `vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/android/systemui/util/sensors/ProximitySensor.java` 文件：

```diff
@@ -35,7 +35,7 @@ import java.util.concurrent.atomic.AtomicBoolean;
 import java.util.function.Consumer;
 
 import javax.inject.Inject;
-
+import android.os.SystemProperties;
 /**
  * Simple wrapper around SensorManager customized for the Proximity sensor.
  */
@@ -81,8 +81,14 @@ public class ProximitySensor {
             }
         }
         if (sensor == null) {
-            sensor = sensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);
-            if (sensor != null) {
+                       int kernel_ps = SystemProperties.getInt("ro.wb.custom.kernel.ps",0);    //jnier 20220110
+                       if (kernel_ps == 1) {
+                               sensor = null;
+                       } else {
+                               sensor = sensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);
+                       }
+
+               if (sensor != null) {
                 threshold = sensor.getMaximumRange();
             }
         }
```

