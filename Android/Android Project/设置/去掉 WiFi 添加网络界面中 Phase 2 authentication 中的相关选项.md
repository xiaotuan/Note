[toc]

去掉 Settings -> Network & internet -> Internet -> Add network 界面中，当 Security 选中 WPA/WPA2/WPA3-Enterprise 选项时，去掉 Phase 2 authentication 下拉列表中的 `SIM/AKA/AKA'` 选项。

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/wifi/WifiConfigController2.java` 文件中 `initWifiConfigController2()` 方法的如下代码：

```diff
@@ -269,7 +269,7 @@ public class WifiConfigController2 implements TextWatcher,
             mPhase2PeapAdapter = getSpinnerAdapter(R.array.wifi_peap_phase2_entries);
         } else {
             mPhase2PeapAdapter = getSpinnerAdapterWithEapMethodsTts(
-                R.array.wifi_peap_phase2_entries_with_sim_auth);
+                R.array.wifi_peap_phase2_entries);
         }
 
         mPhase2TtlsAdapter = getSpinnerAdapter(R.array.wifi_ttls_phase2_entries);
```

