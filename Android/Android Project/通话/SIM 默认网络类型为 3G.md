[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/frameworks/base/telephony/java/com/android/internal/telephony/RILConstants.java` 文件的如下代码：

```diff
@@ -253,10 +253,11 @@ public interface RILConstants {
     int NETWORK_MODE_NR_LTE_TDSCDMA_CDMA_EVDO_GSM_WCDMA = 33;
 
     @UnsupportedAppUsage
-    int PREFERRED_NETWORK_MODE = Optional.of(TelephonyProperties.default_network())
-            .filter(list -> !list.isEmpty())
-            .map(list -> list.get(0))
-            .orElse(NETWORK_MODE_WCDMA_PREF);
+    int PREFERRED_NETWORK_MODE = NETWORK_MODE_WCDMA_ONLY;
+    //int PREFERRED_NETWORK_MODE = Optional.of(TelephonyProperties.default_network())
+            //.filter(list -> !list.isEmpty())
+            //.map(list -> list.get(0))
+            //.orElse(NETWORK_MODE_WCDMA_PREF);
 
     int BAND_MODE_UNSPECIFIED = 0;      //"unspecified" (selected by baseband automatically)
     int BAND_MODE_EURO = 1;             //"EURO band" (GSM-900 / DCS-1800 / WCDMA-IMT-2000)
```

