[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/frameworks/base/services/core/java/com/android/server/pm/PackageManagerService.java` 文件中 `hasSystemFeature()` 方法的如下代码：

```diff
@@ -2814,6 +2814,20 @@ public class PackageManagerService implements PackageSender, TestUtilityService
     public boolean hasSystemFeature(String name, int version) {
         // allow instant applications
         synchronized (mAvailableFeatures) {
+                       // Allow SetupWizard app has telephony feature by qty {{&&
+                       if (!TextUtils.isEmpty(name) && name.equals("android.hardware.telephony")) {
+                int callingUid = Binder.getCallingUid();
+                Computer snapshot = snapshotComputer();
+                String[] names = snapshot.getPackagesForUid(callingUid);
+                if (names != null) {
+                    for (String str : names) {
+                        if ("com.google.android.setupwizard".equalsIgnoreCase(str)) {
+                            return true;
+                        }
+                    }
+                }
+            }
+                       // &&}}
             final FeatureInfo feat = mAvailableFeatures.get(name);
             if (feat == null) {
                 return false;
```

