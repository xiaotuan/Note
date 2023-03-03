[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 前提条件

   项目 MTK_TB_WIFI_3G_MODE 宏的值为 3GDATA_SMS 或 3GDATA_ONLY

2. 报错信息

   ```
   02-28 10:15:58.418839  1660  1660 D MobileNetworkUtils: launchMobileNetworkSettings for subId: 1
   02-28 10:15:58.503446  1247  2809 I game_scn: collectForegroundAppList packName=com.android.phone, actName=com.mediatek.settings.network.MobileNetworkSettings, pid=1642, uid=1001, state:RESUMED
   02-28 10:15:58.553369  1642  1642 D MobileNetworkSettings: onCreate
   
   02-28 10:15:58.723293  1642  1642 I NetworkSettings: updatePhone, subId=1, sir={id=1 iccId=898601178[-2YN9R0IAqVJUZ84_3k46YRlrD4] simSlotIndex=0 carrierId=1436 displayName=CU carrierName=CU nameSource=0 iconTint=-16746133 number=+86 dataRoaming=0 iconBitmap=null mcc=460 mnc=01 countryIso=cn isEmbedded=false nativeAccessRules=null cardString=898601178[-2YN9R0IAqVJUZ84_3k46YRlrD4] cardId=0 portIndex=-1 isOpportunistic=false groupUUID=null isGroupDisabled=false profileClass=-1 ehplmns=[46001] hplmns=[46001, 46009, 46001, 46009] subscriptionType=0 groupOwner=null carrierConfigAccessRules=null areUiccApplicationsEnabled=true usageSetting=0}
   02-28 10:15:58.723713  1642  1642 D NetworkSettings: updatePhone, imsMgr=com.mediatek.ims.internal.MtkImsManager@fcf042a
   
   02-28 10:16:00.391697  1642  1642 D NetworkSettings: onPreferenceTreeClick, preference=Advanced
   02-28 10:16:00.396167   617   617 I BufferQueueProducer: [com.android.phone/com.mediatek.settings.network.MobileNetworkSettings#165](this:0xb400006f38c506b8,id:-1,api:0,p:-1,c:617) queueBuffer: fps=17.52 dur=1141.52 max=789.08 min=16.36
   
   \debuglogger\mobilelog\APLog_2023_0228_101557__4\crash_log_5__2023_0228_101629
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime: FATAL EXCEPTION: main
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime: Process: com.android.phone, PID: 1642
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime: java.lang.IllegalStateException: Unexpected phone type: 0
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime:     at com.mediatek.settings.network.MobileNetworkSettings$MobileNetworkFragment.updateEnabledNetworksEntries(MobileNetworkSettings.java:2429)
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime:     at com.mediatek.settings.network.MobileNetworkSettings$MobileNetworkFragment.updateBodyAdvancedFields(MobileNetworkSettings.java:1403)
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime:     at com.mediatek.settings.network.MobileNetworkSettings$MobileNetworkFragment.updateBody(MobileNetworkSettings.java:1333)
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime:     at com.mediatek.settings.network.MobileNetworkSettings$MobileNetworkFragment.onPreferenceTreeClick(MobileNetworkSettings.java:729)
   02-28 10:16:00.526545  1642  1642 E AndroidRuntime:     at android.preference.Preference.performClick(Preference.java:1174)
   ```

3. 解决办法

   修改 `sys/frameworks/base/telephony/java/android/telephony/TelephonyManager.java` 文件如下代码：

   ```diff
   diff --git a/frameworks/base/telephony/java/android/telephony/TelephonyManager.java b/frameworks/base/telephony/java/android/telephony/TelephonyManager.java
   index b6f86527b74..39c5d11f6f4 100644
   --- a/frameworks/base/telephony/java/android/telephony/TelephonyManager.java
   +++ b/frameworks/base/telephony/java/android/telephony/TelephonyManager.java
   @@ -2594,7 +2594,10 @@ public class TelephonyManager {
         * @see #PHONE_TYPE_SIP
         */
        public int getPhoneType() {
   -        if (!isVoiceCapable()) {
   +               // Solve the error of obtaining telephone type for 3GDATAONLY and 3GDATASMS project by qty at 2023-03-01 {{&&
   +        // if (!isVoiceCapable()) {
   +               if (!isVoiceCapable() && !isSmsCapable() && !isDataCapable()) {
   +               // &&}}
                return PHONE_TYPE_NONE;
            }
            return getCurrentPhoneType();
   ```

   