[toc]

### 1. MTK

#### 1.1 MTK8768

##### 1.1.1 Android S

1. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/res/values/arrays.xml` 文件中的如下代码：

   ```diff
   @@ -1282,8 +1282,8 @@
        </string-array>
    
        <string-array name="wifi_privacy_entries">
   -        <item>Use randomized MAC (default)</item>
   -        <item>Use device MAC</item>
   +        <item>Use device MAC (default)</item>
   +               <item>Use randomized MAC</item>
        </string-array>
    
        <string-array name="wifi_hidden_entries">
   @@ -1298,8 +1298,8 @@
        </string-array>
    
        <string-array name="wifi_privacy_values" translatable="false">
   -        <item>1</item>
            <item>0</item>
   +               <item>1</item>
        </string-array>
    
        <!-- Titles for ui dark mode preference. -->
   ```

   > 注意：这里只列出默认语言的修改，如果需要修改其他语言字符串，请自行修改对应文件中对应的字符串。

2. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/wifi/details2/WifiPrivacyPreferenceController2.java` 文件中的如下代码：

   ```diff
   @@ -109,7 +109,7 @@ public class WifiPrivacyPreferenceController2 extends BasePreferenceController i
         * @return index value of preference
         */
        public static int translateMacRandomizedValueToPrefValue(int macRandomized) {
   -        return (macRandomized == WifiEntry.PRIVACY_RANDOMIZED_MAC)
   +        return (macRandomized == WifiEntry.PRIVACY_DEVICE_MAC)
                ? PREF_RANDOMIZATION_PERSISTENT : PREF_RANDOMIZATION_NONE;
        }
    
   @@ -120,7 +120,7 @@ public class WifiPrivacyPreferenceController2 extends BasePreferenceController i
         * @return mac randomized value
         */
        public static int translatePrefValueToMacRandomizedValue(int prefMacRandomized) {
   -        return (prefMacRandomized == PREF_RANDOMIZATION_PERSISTENT)
   +        return (prefMacRandomized == PREF_RANDOMIZATION_NONE)
                ? WifiEntry.PRIVACY_RANDOMIZED_MAC : WifiEntry.PRIVACY_DEVICE_MAC;
        }
    
   ```

   