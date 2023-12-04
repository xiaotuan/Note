[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 在 `sys/weibu/mssi_t_64_cn/M866YCR200_MDF_1077/config/SystemConfig.mk` （具体项目修改具体文件）文件中添加如下宏定义：

   ```makefile
   MTK_TB_WIFI_3G_MODE = 3GDATA_ONLY
   ```

2. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/Android.bp` 文件中如下代码，使用设置应用覆盖掉通话和短信应用：

   ```diff
   @@ -104,6 +104,15 @@ android_app {
        name: "MtkSettings",
        overrides: [
            "Settings",
   +        "Dialer",
   +        "MtkDialer",
   +        "messaging",
   +        "Mms",
   +        "MtkMms",
   +        "MessagesGo",
   +        "GoogleDialer",
   +        "Messages",
   +        "AndroidAutoStub",
        ],
        defaults: ["platform_app_defaults"],
        platform_apis: true,
   ```

3. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/res/values/config.xml` 文件的如下代码，去掉通话音量调节功能：

   ```diff
   @@ -355,7 +355,7 @@
        <bool name="config_show_alarm_volume">true</bool>
    
        <!-- Whether call_volume should be shown or not. -->
   -    <bool name="config_show_call_volume">true</bool>
   +    <bool name="config_show_call_volume">false</bool>
    
        <!-- Whether notification_volume should be shown or not. -->
        <bool name="config_show_notification_volume">true</bool>
   ```

4. 修改 `sys/frameworks/base/core/res/res/values/config.xml` 文件的如下代码，去掉通话和短信功能：

   ```diff
   @@ -2023,7 +2023,7 @@
             PackageManager.FEATURE_TELEPHONY system feature, which is
             available on *any* device with a telephony radio, even if the
             device is data-only. -->
   -    <bool name="config_voice_capable">true</bool>
   +    <bool name="config_voice_capable">false</bool>
    
        <!-- Flag indicating whether all audio streams should be mapped to
             one single stream. If true, all audio streams are mapped to
   @@ -2049,7 +2049,7 @@
    
             Note: Disable SMS also disable voicemail waiting sms,
                   cell broadcasting sms, and MMS. -->
   -    <bool name="config_sms_capable">true</bool>
   +    <bool name="config_sms_capable">false</bool>
    
        <!-- Default SMS Application. This will be the default SMS application when
             the phone first boots. The user can then change the default app to one
   ```

5. 修改 `sys/frameworks/base/core/res/res/values/strings.xml` 文件的如下代码，去掉通话字样（如需修改其他语言字符串同理）：

   ```diff
   @@ -5753,8 +5753,8 @@
        <!-- Notification action for editing a screenshot (drawing on it, cropping it, etc) -->
        <string name="screenshot_edit">Edit</string>
    
   -    <string name="volume_dialog_ringer_guidance_vibrate">Calls and notifications will vibrate</string>
   -    <string name="volume_dialog_ringer_guidance_silent">Calls and notifications will be muted</string>
   +    <string name="volume_dialog_ringer_guidance_vibrate">Notifications will vibrate</string>
   +    <string name="volume_dialog_ringer_guidance_silent">Notifications will be muted</string>
    
        <!-- Title for the notification channel notifying user of settings system changes. [CHAR LIMIT=NONE] -->
        <string name="notification_channel_system_changes">System changes</string>
   ```

6. 修改 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/res/values/strings.xml` 文件的如下代码，去掉通话字样：

   ```diff
   @@ -1187,7 +1187,7 @@
    
        <string name="volume_dialog_title">%s volume controls</string>
    
   -    <string name="volume_dialog_ringer_guidance_ring">Calls and notifications will ring (<xliff:g id="volume level" example="56">%1$s</xliff:g>)</string>
   +    <string name="volume_dialog_ringer_guidance_ring">Notifications will ring (<xliff:g id="volume level" example="56">%1$s</xliff:g>)</string>
    
        <!-- Name of special SystemUI debug settings -->
        <string name="system_ui_tuner">System UI Tuner</string>
   ```

7. 修改 `vnd/frameworks/native/data/etc/android.hardware.telephony.ims.xml` 文件中的如下代码，去掉 volte feature：

   ```diff
   @@ -16,5 +16,5 @@
    
    <!-- Feature for devices that support IMS via ImsService APIs. -->
    <permissions>
   -    <feature name="android.hardware.telephony.ims" />
   +    <!--<feature name="android.hardware.telephony.ims" />-->
    </permissions>
   ```

8. 修改 `vnd/device/mediateksample/tb8766p1_64_bsp/android.hardware.telephony.gsm.xml` 文件的如下代码，去掉通话 feature：

   ```diff
   @@ -16,6 +16,8 @@
    
    <!-- This is the standard set of telephony features for a GSM phone. -->
    <permissions>
   +    <!--
        <feature name="android.hardware.telephony" />
        <feature name="android.hardware.telephony.gsm" />
   +    -->
    </permissions>
   ```

9. 修改 `vnd/weibu/tb8766p1_64_bsp/M866YCR200_MDF_1077/config/ProjectConfig.mk` 文件如下代码，设置项目为 3GDATA_ONLY 项目：

   ```diff
   @@ -14,6 +14,7 @@ WEIBU_PRODUCT_SAMPLE_GMS=yes
    MTK_FACTORY_MODE_IN_GB2312 = no
    
    MTK_BESLOUDNESS_SUPPORT = yes
   +MTK_TB_WIFI_3G_MODE = 3GDATA_ONLY^M
    
    #Audio
    WB_AUDIO_EARPIECT_CLOSE=yes
   ```

10. 修改 `sys/vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_full/xml/partner_default_layout.xml`文件，修改桌面布局，下面是一个示例布局：

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <!-- Copyright (C) 2017 Google Inc. All Rights Reserved. -->
   <favorites>
     <!-- Hotseat (We use the screen as the position of the item in the hotseat) -->
     <!-- Dialer Messaging Calendar Contacts Camera -->
     <favorite container="-101" screen="0" x="0" y="0" packageName="com.google.android.youtube" className="com.google.android.youtube.app.honeycomb.Shell$HomeActivity"/>
     <favorite container="-101" screen="1" x="1" y="0" packageName="com.google.android.gm" className="com.google.android.gm.ConversationListActivityGmail"/>
     <favorite container="-101" screen="2" x="2" y="0" packageName="com.android.chrome" className="com.google.android.apps.chrome.Main"/>
     <favorite container="-101" screen="3" x="3" y="0" packageName="com.google.android.contacts" className="com.android.contacts.activities.PeopleActivity"/>
     <favorite container="-101" screen="4" x="4" y="0" packageName="com.mediatek.camera" className="com.mediatek.camera.CameraLauncher"/>
     <favorite container="-101" screen="5" x="5" y="0" packageName="com.google.android.apps.photos" className="com.google.android.apps.photos.home.HomeActivity"/>
     
     <!-- In Launcher3, workspaces extend infinitely to the right, incrementing from zero -->
     <!-- Google folder -->
     <!-- Google, Chrome, Gmail, Maps, YouTube, (Drive), (Music), (Movies), Duo, Photos -->
     <folder title="@string/google_folder_title" screen="0" x="0" y="4">
       <!-- favorite packageName="com.google.android.googlequicksearchbox" className="com.google.android.googlequicksearchbox.SearchActivity"/> -->
       <!--<favorite packageName="com.google.android.gm" className="com.google.android.gm.ConversationListActivityGmail"/>-->
       <favorite packageName="com.google.android.apps.maps" className="com.google.android.maps.MapsActivity"/>
       <!-- <favorite packageName="com.google.android.youtube" className="com.google.android.youtube.app.honeycomb.Shell$HomeActivity"/> -->
       <favorite packageName="com.google.android.apps.docs" className="com.google.android.apps.docs.app.NewMainProxyActivity"/>
       <favorite packageName="com.google.android.apps.youtube.music" className="com.google.android.apps.youtube.music.activities.MusicActivity"/>
       <favorite packageName="com.google.android.videos" className="com.google.android.youtube.videos.EntryPoint"/>
       <favorite packageName="com.google.android.videos" className="com.google.android.videos.GoogleTvEntryPoint"/>
       <!--<favorite packageName="com.google.android.apps.photos" className="com.google.android.apps.photos.home.HomeActivity"/>-->
       <favorite packageName="com.google.android.calendar" className="com.android.calendar.AllInOneActivity"/>
       <favorite packageName="com.google.android.apps.youtube.kids" className="com.google.android.apps.youtube.kids.browse.SplashScreenActivity"/>
       <favorite packageName="com.google.android.apps.books" className="com.google.android.apps.play.books.home.HomeActivity"/>
       <favorite packageName="com.google.android.apps.adm" className="com.google.android.apps.adm.activities.MainActivity"/>
     </folder>
     
     <favorite screen="0" x="1" y="4" packageName="com.google.android.apps.tachyon" className="com.google.android.apps.tachyon.MainActivity"/>
     <!-- <favorite screen="0" x="2" y="4" packageName="com.google.android.apps.kids.home" className="com.google.android.apps.kids.home.accountsetup.AccountSignInActivity"/> -->
     <favorite screen="0" x="2" y="4" packageName="com.google.android.googlequicksearchbox" className="com.google.android.googlequicksearchbox.SearchActivity"/>
     <favorite screen="0" x="3" y="4" packageName="com.google.android.apps.googleassistant" className="com.google.android.apps.googleassistant.AssistantActivity"/>
     <favorite screen="0" x="4" y="4" packageName="com.android.settings" className="com.android.settings.Settings"/>
     <favorite screen="0" x="5" y="4" packageName="com.android.vending" className="com.android.vending.AssetBrowserActivity"/>
   </favorites>
   ```

   