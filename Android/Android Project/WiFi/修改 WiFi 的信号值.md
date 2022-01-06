[toc]

### 1. MTK 平台

#### 1.1 MT8766

##### 1.1.1 Android R

修改 `frameworks/base/wifi/java/android/net/wifi/WifiManager.java` 文件中的 `calculateSignalLevel(int rssi, int numLevels)` 和 `int calculateSignalLevel(int rssi)` 方法：

```diff
@@ -2959,6 +2959,12 @@ public class WifiManager {
      */
     @Deprecated
     public static int calculateSignalLevel(int rssi, int numLevels) {
+        if (rssi > MIN_RSSI && rssi < MAX_RSSI) {
+            rssi += 8;
+            if (rssi >= MAX_RSSI) {
+                rssi = MAX_RSSI;
+            }
+        }
         if (rssi <= MIN_RSSI) {
             return 0;
         } else if (rssi >= MAX_RSSI) {
@@ -2980,6 +2986,12 @@ public class WifiManager {
      */
     @IntRange(from = 0)
     public int calculateSignalLevel(int rssi) {
+        if (rssi > MIN_RSSI && rssi < MAX_RSSI) {
+            rssi += 8;
+            if (rssi >= MAX_RSSI) {
+                rssi = MAX_RSSI;
+            }
+        }
         try {
             return mService.calculateSignalLevel(rssi);
         } catch (RemoteException e) {
```

