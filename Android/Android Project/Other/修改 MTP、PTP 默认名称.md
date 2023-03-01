[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/frameworks/base/media/java/android/mtp/MtpDatabase.java` 文件如下代码：

```diff
diff --git a/frameworks/base/media/java/android/mtp/MtpDatabase.java b/frameworks/base/media/java/android/mtp/MtpDatabase.java
index 20d711cf4c5..9c29af2a834 100755
--- a/frameworks/base/media/java/android/mtp/MtpDatabase.java
+++ b/frameworks/base/media/java/android/mtp/MtpDatabase.java
@@ -686,7 +686,10 @@ public class MtpDatabase implements AutoCloseable {
             case MtpConstants.DEVICE_PROPERTY_SYNCHRONIZATION_PARTNER:
             case MtpConstants.DEVICE_PROPERTY_DEVICE_FRIENDLY_NAME:
                 // writable string properties kept in shared preferences
-                value = mDeviceProperties.getString(Integer.toString(property), "");
+                               // Modify the MTP name by qty at 2023-02-25 {{&&
+                // value = mDeviceProperties.getString(Integer.toString(property), "");
+                               value = "G3 Tab";
+                               // &&}}
                 length = value.length();
                 if (length > 255) {
                     length = 255;
```

