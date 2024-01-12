[toc]

去掉 Settings -> Network & internet -> Internet -> Add network 界面中，当 Security 选中 WPA/WPA2/WPA3-Enterprise 选项时，去掉 EAP method 下拉列表中的 `SIM/AKA/AKA'` 选项。

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/wifi/WifiConfigController2.java` 文件中 `showSecurityFields()` 方法的如下代码：

```diff
@@ -1044,7 +1044,7 @@ public class WifiConfigController2 implements TextWatcher,
         if (refreshEapMethods) {
             ArrayAdapter<CharSequence> eapMethodSpinnerAdapter;
             if (mWifiEntrySecurity == WifiEntry.SECURITY_EAP_SUITE_B) {
-                eapMethodSpinnerAdapter = getSpinnerAdapter(R.array.wifi_eap_method);
+                eapMethodSpinnerAdapter = getSpinnerAdapter(R.array.eap_method_without_sim_auth);
                 mEapMethodSpinner.setAdapter(eapMethodSpinnerAdapter);
                 // WAP3-Enterprise 192-bit only allows EAP method TLS
                 mEapMethodSpinner.setSelection(Eap.TLS);
@@ -1056,7 +1056,7 @@ public class WifiConfigController2 implements TextWatcher,
                 mEapMethodSpinner.setEnabled(true);
             } else {
                 eapMethodSpinnerAdapter = getSpinnerAdapterWithEapMethodsTts(
-                        R.array.wifi_eap_method);
+                        R.array.eap_method_without_sim_auth);
                 mEapMethodSpinner.setAdapter(eapMethodSpinnerAdapter);
                 mEapMethodSpinner.setEnabled(true);
             }
```

