[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android S

1. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/res/xml/system_dashboard_fragment.xml` 文件

   ```diff
   @@ -42,6 +42,16 @@
            android:order="-240"
            android:fragment="com.android.settings.datetime.DateTimeSettings"
            settings:controller="com.android.settings.datetime.DateTimePreferenceController"/>
   +               
   +       <Preference
   +        android:key="system_certification_settings"
   +        android:title="@string/system_certification_settings_title"
   +        android:icon="@drawable/ic_certification_icon"
   +        android:order="-60"
   +        settings:keywords="@string/keywords_system_certification_settings"
   +        settings:controller="com.android.settings.system.SystemCertificationPreferenceController">
   +        <intent android:action="android.settings.SYSTEM_CERTIFICATION_SETTINGS"/>
   +    </Preference>
    
        <!-- System updates -->
        <Preference
   ```

2. 添加 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/system/SystemCertificationPreferenceController.java` 文件

   ```java
   /*
    * Copyright (C) 2016 The Android Open Source Project
    *
    * Licensed under the Apache License, Version 2.0 (the "License");
    * you may not use this file except in compliance with the License.
    * You may obtain a copy of the License at
    *
    *      http://www.apache.org/licenses/LICENSE-2.0
    *
    * Unless required by applicable law or agreed to in writing, software
    * distributed under the License is distributed on an "AS IS" BASIS,
    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    * See the License for the specific language governing permissions and
    * limitations under the License.
    */
   package com.android.settings.system;
   
   import android.content.Context;
   import android.content.Intent;
   import android.os.Build;
   import android.os.Bundle;
   import android.os.PersistableBundle;
   import android.text.TextUtils;
   import android.util.Log;
   
   import androidx.preference.Preference;
   import androidx.preference.PreferenceScreen;
   
   import com.android.settings.R;
   import com.android.settings.Utils;
   import com.android.settings.core.BasePreferenceController;
   
   public class SystemCertificationPreferenceController extends BasePreferenceController {
   
       private static final String TAG = "SysCertPrefContr";
   
       private static final String KEY_SYSTEM_CERTIFICATION_SETTINGS = "system_certification_settings";
   
       public SystemCertificationPreferenceController(Context context) {
           super(context, KEY_SYSTEM_CERTIFICATION_SETTINGS);
       }
   
       @Override
       public int getAvailabilityStatus() {
                   /*
           return mContext.getResources().getBoolean(R.bool.config_show_system_update_settings)
                   && mUm.isAdminUser()
                   ? AVAILABLE
                   : UNSUPPORTED_ON_DEVICE;
                   */
                   return AVAILABLE;
       }
   
       @Override
       public void displayPreference(PreferenceScreen screen) {
           super.displayPreference(screen);
           if (isAvailable()) {
               Utils.updatePreferenceToSpecificActivityOrRemove(mContext, screen,
                       getPreferenceKey(),
                       Utils.UPDATE_PREFERENCE_FLAG_SET_TITLE_TO_MATCHING_ACTIVITY);
           }
       }
   
       @Override
       public boolean handlePreferenceTreeClick(Preference preference) {
           // always return false here because this handler does not want to block other handlers.
           return false;
       }
   
       @Override
       public CharSequence getSummary() {
           return "";
       }
   
   }
   ```

3. 添加 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/system/CertificationActivity.java` 文件

   ```java
   package com.android.settings.system;
   
   import android.app.Activity;
   import android.os.Bundle;
   import android.view.MenuItem;
   
   import com.android.settings.R;
   
   public class CertificationActivity extends Activity {
   
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_certification);
   
                   if (getActionBar() != null) {
               getActionBar().setDisplayHomeAsUpEnabled(true);
           }
       }
   
           @Override
       public boolean onOptionsItemSelected(MenuItem item) {
           switch (item.getItemId()) {
               case android.R.id.home:
                   finish();
                   break;
           }
           return super.onOptionsItemSelected(item);
       }
   }
   ```

4. 添加 `vendor/mediatek/proprietary/packages/apps/MtkSettings/res/layout/activity_certification.xml` 文件

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
       android:layout_width="match_parent"
       android:layout_height="match_parent"
           android:background="@android:color/white"
       android:orientation="vertical">
   
       <ImageView
           android:layout_width="wrap_content"
           android:layout_height="wrap_content"
           android:scaleType="centerInside"
           android:src="@drawable/certification" />
   
   </LinearLayout>
   ```

5. 认证信息图标文件内容

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
       android:layout_width="match_parent"
       android:layout_height="match_parent"
           android:background="@android:color/white"
       android:orientation="vertical">
   
       <ImageView
           android:layout_width="wrap_content"
           android:layout_height="wrap_content"
           android:scaleType="centerInside"
           android:src="@drawable/certification" />
   
   </LinearLayout>qintuanye@WB-SVR-27:~/work02/mtk/12/8766/A/mt8766_s$ cat vendor/mediatek/proprietary/packages/apps/MtkSettings/res/drawable/ic_certification_icon.xml
   <?xml version="1.0" encoding="utf-8"?>
   <vector xmlns:android="http://schemas.android.com/apk/res/android" android:tint="?android:attr/colorControlNormal" android:height="24dp" android:width="24dp" android:viewportWidth="24" android:viewportHeight="24">
       <path android:fillColor="#ffffffff" android:pathData="M9.3,12.9l2.7,-1.6l2.7,1.6l-0.7,-3.1l2.3,-2.1l-3.1,-0.3l-1.2,-2.9l-1.2,2.9l-3.2,0.3l2.4,2.1z"/>
       <path android:fillColor="#ffffffff" android:pathData="M20,9c0,-4.5 -3.6,-8.2 -8,-8.2S4,4.5 4,9c0,2.5 1.1,4.8 2.9,6.3v7.8l5,-3.1l5,3.1v-7.7C18.8,14 20,11.6 20,9zM5.7,9c0,-3.5 2.8,-6.4 6.3,-6.4s6.3,2.9 6.3,6.4s-2.8,6.4 -6.3,6.4S5.7,12.6 5.7,9z"/>
   </vector>
   ```

6. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/res/values/themes.xml` 文件

   ```diff
   @@ -265,4 +265,23 @@
            <item name="colorPrimary">@*android:color/primary_device_default_settings_light</item>
            <item name="colorAccent">@*android:color/accent_device_default_light</item>
        </style>
   +  
   +       <style name="Certification" parent="Theme.SettingsBase">
   +               <item name="android:windowBackground">@*android:color/white</item>
   +               <item name="colorPrimaryDark">@*android:color/primary_dark_device_default_settings_light</item>
   +        <item name="android:windowLightStatusBar">true</item>
   +        <item name="android:navigationBarDividerColor">@*android:color/ripple_material_light</item>
   +        <!-- Homepage should follow device default design, the values is same as device default theme.-->
   +        <item name="android:navigationBarColor">@android:color/white</item>
   +        <item name="android:statusBarColor">?attr/colorPrimaryDark</item>
   +    </style>
    </resources>
   ```

7. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/res/values-night/themes.xml` 文件

   ```diff
   @@ -49,4 +49,22 @@
            <item name="colorPrimary">@*android:color/primary_dark_device_default_settings</item>
            <item name="colorAccent">@*android:color/accent_device_default_dark</item>
        </style>
   +         
   +       <style name="Certification" parent="Theme.SettingsBase">
   +               <item name="colorPrimary">@*android:color/primary_device_default_settings</item>
   +        <item name="colorPrimaryDark">@*android:color/primary_dark_device_default_settings</item>
   +        <item name="android:colorBackground">?android:attr/colorPrimaryDark</item>
   +        <!-- Homepage should follow device default design, the values is same as device default theme.-->
   +        <item name="android:navigationBarColor">@android:color/black</item>
   +        <item name="android:statusBarColor">?attr/colorPrimaryDark</item>
   +    </style>
    </resources>
   ```

8. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/AndroidManifest.xml` 文件

   ```diff
   @@ -4161,6 +4161,30 @@
                    <action android:name="com.mediatek.common.carrierexpress.operator_config_changed" />
                </intent-filter>
            </receiver>
   +               
   +               <activity
   +            android:name=".system.CertificationActivity"
   +            android:label="@string/system_certification_settings_title"
   +            android:exported="true"
   +                       android:theme="@style/Certification"
   +            android:icon="@drawable/ic_certification_icon">
   +            <intent-filter>
   +                <action android:name="android.settings.SYSTEM_CERTIFICATION_SETTINGS" />
   +                <category android:name="android.intent.category.DEFAULT" />
   +            </intent-filter>
   +        </activity>
            <!-- This is the longest AndroidManifest.xml ever. -->
        </application>
    </manifest>
   ```

   