[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/services/Telephony/src/com/android/phone/SpecialCharSequenceMgr.java` 文件中 `showDeviceIdPanel()` 方法的如下代码：

```diff
@@ -305,7 +305,18 @@ public class SpecialCharSequenceMgr {
 
         Phone phone = PhoneGlobals.getPhone();
         int labelId = TelephonyCapabilities.getDeviceIdLabel(phone);
-        String deviceId = phone.getDeviceId();
+               // Add all imei and serial number by qty {{&&
+        // String deviceId = phone.getDeviceId();
+               String deviceId = "";
+               TelephonyManager telephonyManager =
+                       (TelephonyManager) context.getSystemService(Context.TELEPHONY_SERVICE);
+               for (int slot = 0; slot < telephonyManager.getPhoneCount(); slot++) {
+            String imei = telephonyManager.getDeviceId(slot);
+                       deviceId += "IMEI " + (slot + 1) + ": " + imei + "\n";
+               }
+               deviceId += "Serial Number: " + android.os.Build.getSerial();
+               android.util.Log.d("qty", "showDeviceIdPanel=>deviceId: " + deviceId);
+               // &&}}
 
         AlertDialog alert = FrameworksUtils.makeAlertDialogBuilder(context)
                 .setTitle(labelId)
```

