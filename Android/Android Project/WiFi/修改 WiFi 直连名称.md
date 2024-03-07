### 1. MTK

#### 1.1 Android S

##### 1.1.1 MT8788

修改 `packages/modules/Wifi/service/java/com/android/server/wifi/p2p/WifiP2pServiceImpl.java` 文件中 `getPersistedDeviceName()` 方法的如下代码：

```diff
@@ -4086,7 +4086,7 @@ public class WifiP2pServiceImpl extends IWifiP2pManager.Stub {
                 postfix = id.substring(0, 4);
             }
             logd("the default device name: " + prefix + postfix);
-            return prefix + postfix;
+            return "K-M10P"; // prefix + postfix;
         }
 
         private boolean setAndPersistDeviceName(String devName) {
```

