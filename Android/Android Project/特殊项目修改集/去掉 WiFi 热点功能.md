[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/res/values/strings.xml` 文件的如下代码：

   ```diff
   @@ -3088,7 +3088,7 @@
        <!-- Tethering controls, item title to go into the tethering settings when USB and Bluetooth tethering are available [CHAR LIMIT=25]-->
        <string name="tether_settings_title_usb_bluetooth">Tethering</string>
        <!-- Tethering controls, item title to go into the tethering settings when USB, Bluetooth and Wifi tethering are available [CHAR LIMIT=60]-->
   -    <string name="tether_settings_title_all">Hotspot &amp; tethering</string>
   +    <string name="tether_settings_title_all">Tethering</string>
        <!-- Tethering setting summary when both Wi-Fi hotspot and tether are turned on [CHAR LIMIT=NONE]-->
        <string name="tether_settings_summary_hotspot_on_tether_on">Hotspot on, tethering</string>
        <!-- Tethering setting summary when Wi-Fi hotspot is on and tether is off [CHAR LIMIT=NONE]-->
   @@ -6894,7 +6894,7 @@
        <!-- Summary for Network and Internet settings, explaining it contains mobile, wifi setting and data usage settings [CHAR LIMIT=NONE]-->
        <string name="network_dashboard_summary_mobile">Mobile, Wi\u2011Fi, hotspot</string>
        <!-- Summary for Network and Internet settings, explaining it contains wifi and data usage setting [CHAR LIMIT=NONE]-->
   -    <string name="network_dashboard_summary_no_mobile">Wi\u2011Fi, hotspot</string>
   +    <string name="network_dashboard_summary_no_mobile">Wi\u2011Fi</string>
    
        <!-- Title for setting tile leading to Connected devices settings [CHAR LIMIT=40]-->
        <string name="connected_devices_dashboard_title">Connected devices</string>
   ```

2. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/wifi/WifiUtils.java` 文件中 `checkShowWifiHotspot(Context context)` 方法的如下代码：

   ```diff
   @@ -259,6 +259,8 @@ public class WifiUtils extends com.android.settingslib.wifi.WifiUtils {
         * @return true if Wi-Fi hotspot settings can be displayed
         */
        public static boolean checkShowWifiHotspot(Context context) {
   +        return false;
   +        /*
            if (context == null) return false;
    
            boolean showWifiHotspotSettings =
   ```

3. 修改 `sys/frameworks/base/packages/SettingsLib/src/com/android/settingslib/wifi/WifiEnterpriseRestrictionUtils.java` 文件中 `isWifiTetheringAllowed(Context context)` 方法的如下代码：

   ```diff
   @@ -36,7 +36,7 @@ public class WifiEnterpriseRestrictionUtils {
         * @return whether the device is permitted to use Wi-Fi Tethering
         */
        public static boolean isWifiTetheringAllowed(Context context) {
   -        if (!hasUserRestrictionFromT(context, UserManager.DISALLOW_WIFI_TETHERING)) return true;
   +        //if (!hasUserRestrictionFromT(context, UserManager.DISALLOW_WIFI_TETHERING)) return true;
            Log.w(TAG, "Wi-Fi Tethering isn't available due to user restriction.");
            return false;
        }
   ```

4. 修改 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/config.xml` 文件的如下代码：

   ```diff
   @@ -91,7 +91,7 @@
    
        <!-- Tiles native to System UI. Order should match "quick_settings_tiles_default" -->
        <string name="quick_settings_tiles_stock" translatable="false">
   -        internet,bt,flashlight,dnd,alarm,airplane,controls,wallet,rotation,battery,screenshot,cast,screenrecord,mictoggle,cameratoggle,readmode,location,hotspot,inversion,saver,dark,work,night,reverse,reduce_brightness,qr_code_scanner,onehanded,color_correction,dream,font_scaling
   +        internet,bt,flashlight,dnd,alarm,airplane,controls,wallet,rotation,battery,cast,screenrecord,mictoggle,cameratoggle,location,inversion,saver,dark,work,night,reverse,reduce_brightness,qr_code_scanner,onehanded,color_correction,dream,font_scaling
        </string>
    
        <!-- The tiles to display in QuickSettings -->
   ```

5. 如果在下拉状态栏默认显示 WiFi 热点的项目，还需要修改 `sys/vendor/partner_gms/overlay/gms_overlay/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/config.xml` 文件中 `quick_settings_tiles_default` 的值。