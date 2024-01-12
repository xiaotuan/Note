[toc]

去掉 Settings -> Network & internet -> Internet -> Add network 界面中 Security 下拉列表中的 `Enhanced Open` 选项。

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/mediatek/settings/wifi/WifiConfigControllerExt.java` 文件中 `addWifiItems(ArrayAdapter<String> spinnerAdapter, int idx)` 方法的如下代码：

```diff
@@ -313,10 +313,12 @@ public class WifiConfigControllerExt {
         Log.d(TAG, Log.getStackTraceString(new Exception()));
         spinnerAdapter.add(mContext.getString(R.string.wifi_security_none));
         mController.mSecurityInPosition[idx++] = WifiEntry.SECURITY_NONE;
+        /*
         if (mWifiManager.isEnhancedOpenSupported()) {
             spinnerAdapter.add(mContext.getString(R.string.wifi_security_owe));
             mController.mSecurityInPosition[idx++] = WifiEntry.SECURITY_OWE;
         }
+        */
                    spinnerAdapter.add(mContext.getString(R.string.wifi_security_wep));
                    mController.mSecurityInPosition[idx++] = WifiEntry.SECURITY_WEP;
                    spinnerAdapter.add(mContext.getString(R.string.wifi_security_wpa_wpa2));
```

