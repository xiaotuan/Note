[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

1. 修改 `u_sys/frameworks/base/services/core/java/com/android/server/policy/PhoneWindowManager.java` 文件中 `notifyLidSwitchChanged()` 和 `applyLidSwitchState()` 方法的如下代码：

   ```diff
   @@ -3909,6 +3943,13 @@ public class PhoneWindowManager implements WindowManagerPolicy {
            if (newLidState == mDefaultDisplayPolicy.getLidState()) {
                return;
            }
   +        
   +        // Hall factory test to obtain Hall switch status by qty at 2023-02-07 {{&&
   +        Settings.System.putIntForUser(mContext.getContentResolver(),
   +                                "lid_state",
   +                                newLidState,
   +                                UserHandle.USER_CURRENT_OR_SELF);
   +        // &&}}
    
            mDefaultDisplayPolicy.setLidState(newLidState);
            applyLidSwitchState();
   @@ -5635,7 +5696,15 @@ public class PhoneWindowManager implements WindowManagerPolicy {
    
        private void applyLidSwitchState() {
            final int lidState = mDefaultDisplayPolicy.getLidState();
   -        if (lidState == LID_CLOSED) {
   +        // Hall Factory test does not allow off screen by qty at 2023-02-07 {{&&
   +        // if (lidState == LID_CLOSED) {
   +        final boolean isFactoryTest = Settings.System.getIntForUser(
   +                                mContext.getContentResolver(),
   +                                "factory_test_hall",
   +                                /* def= */ 0,
   +                                UserHandle.USER_CURRENT) == 1;
   +        if (!isFactoryTest && (lidState == LID_CLOSED)) {
   +        // &&}}
                int lidBehavior = getLidBehavior();
                switch (lidBehavior) {
                    case LID_BEHAVIOR_LOCK:
   ```

2. 修改 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/AndroidManifest.xml` 文件的如下代码：

   ```diff
   @@ -301,6 +301,11 @@
                android:excludeFromRecents="true"
                android:label="@string/device_info"
                android:screenOrientation="portrait" />
   +        <activity^M
   +            android:name="com.mediatek.factorymode.sensor.HallSwitchTest"^M
   +            android:excludeFromRecents="true"^M
   +            android:label="@string/hall_switch_test"^M
   +            android:screenOrientation="portrait" />^M
    
    
            <!--  -->
   ```

3. 添加 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/res/layout/test_result_hall_switch.xml` 文件：

   ```xml
   @@ -0,0 +1,15 @@
   <?xml version="1.0" encoding="utf-8"?>
   <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
       android:id="@+id/container"
       style="@style/info_layout">
       <include layout="@layout/mid_header"/>
        <TextView
           android:id="@+id/txt_value_hall"
           android:layout_width="fill_parent"
           android:layout_height="0dp"
           android:layout_weight="1"
           android:gravity="center"
           android:textSize="25dip"
           />
       <include layout="@layout/mid_btns"/>
   </LinearLayout>
   ```

4. 修改 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/res/values-zh-rCN/strings.xml` 文件添加如下内容：

   ```xml
   <string name="hall_switch_test"> 霍尔开关 </string>
   <string name="hall_is_open">"霍尔测试成功"</string>
   <string name="hall_toast">"请合上皮套进行测试\n当屏幕变成蓝色的时候Hall测试成功"</string>
   ```

5. 修改 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/res/values/strings.xml` 文件添加如下内容：

   ```xml
   <string name="hall_switch_test"> Hall Switch </string>
   <string name="hall_toast">"Please close the leather case for testing\nThe Hall test worked when the screen turned blue"</string>
   <string name="hall_is_open">Hall test is successful!</string>
   ```

6. 修改 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/src/com/mediatek/factorymode/BatteryLog.java` 文件如下代码：

   ```diff
   @@ -189,7 +189,7 @@ public class BatteryLog extends Activity implements View.OnClickListener {
                finish();
                Intent intent = new Intent();
                // intent.setClassName("com.mediatek.factorymode", "com.mediatek.factorymode.sdcard.SDCard");
   -                       intent.setClassName("com.mediatek.factorymode", "com.mediatek.factorymode.googlekey.googlekey");
   +                       intent.setClassName("com.mediatek.factorymode", "com.mediatek.factorymode.sensor.HallSwitchTest");^M
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                startActivity(intent);
            }
   ```

7. 修改 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/src/com/mediatek/factorymode/FactoryMode.java` 文件如下代码：

   ```diff
   @@ -80,6 +80,7 @@ public class FactoryMode extends Activity implements
                   R.string.device_info,
                   R.string.version,
                   R.string.battery_name,
   +        R.string.hall_switch_test,^M
                   //R.string.flashlight,
                   //R.string.led_name,
                   //R.string.fmradio_name,
   @@ -114,6 +115,7 @@ public class FactoryMode extends Activity implements
                           Utils.putInt(getApplicationContext(), "Right_peaker_Test", 2);
                           Utils.putInt(getApplicationContext(), "Microphone_Test", 2);
                           Utils.putInt(getApplicationContext(), "Headset_Test", 2);
   +            Utils.putInt(getApplicationContext(), "Hall_switch_Test", 2);^M
                           //Utils.putInt(getApplicationContext(), "TP_test", 2);
                           Intent intent = new Intent(Intent.ACTION_REQUEST_SHUTDOWN);
                           intent.putExtra(Intent.EXTRA_KEY_CONFIRM, false);
   @@ -169,7 +171,8 @@ public class FactoryMode extends Activity implements
                                                   (Utils.getInt(getApplicationContext(), "Lsensor_Test") == 1) && (Utils.getInt(getApplicationContext(), "Right_speaker_Test") == 1) &&
                                                   (Utils.getInt(getApplicationContext(), "SubCamera_Test") == 1) && (Utils.getInt(getApplicationContext(), "Left_speaker_Test") == 1) &&
                                                   (Utils.getInt(getApplicationContext(), "Microphone_Test") == 1) && (Utils.getInt(getApplicationContext(), "Headset_Test") == 1) &&
   -                                               (Utils.getInt(getApplicationContext(), "Old_Test") == 1) && (Utils.getInt(getApplicationContext(), "Reboot_Test") == 1)
   +                                               (Utils.getInt(getApplicationContext(), "Old_Test") == 1) && (Utils.getInt(getApplicationContext(), "Reboot_Test") == 1) &&^M
   +                        (Utils.getInt(getApplicationContext(), "Hall_switch_Test") == 1)^M
                                           ){      
                                                   Log.d(TAG, "SetColor=>power off.");                                     
                                                   powerOff(this); 
   @@ -345,6 +348,7 @@ public class FactoryMode extends Activity implements
                                                           Utils.putInt(getApplicationContext(), "Device_Info", 0);
                                                           //Utils.putInt(getApplicationContext(), "TP_test", 0);
                                                           Utils.putInt(getApplicationContext(), "Version", 3);
   +                            Utils.putInt(getApplicationContext(), "Hall_switch_Test", 0);^M
                                                           Utils.SetPreferences(FactoryMode.this,mSp,arrayOfInt[i],"null");
                                                           mSp.edit().putBoolean("is_close_sequence_test", false).commit();
                                                           mSp.edit().remove("reboot_test_time").commit();
   @@ -453,7 +457,10 @@ public class FactoryMode extends Activity implements
                           }else if(str2.equals("com.mediatek.factorymode.BatteryLog") && ((Utils.getInt(getApplicationContext(), "Version") == 1 || Utils.getInt(getApplicationContext(), "Version") == 2) || isCloseSequenceTest)){
                                   localIntent.setClassName(this, str2);
                                   startActivity(localIntent);     
   -                       }else if(str2.equals("com.mediatek.factorymode.googlekey.googlekey") && (Utils.getInt(getApplicationContext(), "Battery_Test") == 1  || isCloseSequenceTest)){
   +            }else if(str2.equals("com.mediatek.factorymode.sensor.HallSwitchTest") && ((Utils.getInt(getApplicationContext(), "Battery_Test") == 1 || Utils.getInt(getApplicationContext(), "Battery_Test") == 2) || isCloseSequenceTest)){^M
   +                               localIntent.setClassName(this, str2);^M
   +                               startActivity(localIntent);     ^M
   +                       }else if(str2.equals("com.mediatek.factorymode.googlekey.googlekey") && (Utils.getInt(getApplicationContext(), "Hall_switch_Test") == 1  || isCloseSequenceTest)){^M
                                   localIntent.setClassName(this, str2);
                                   startActivity(localIntent);     
                           // }else if(str2.equals("com.mediatek.factorymode.tp.TPTest")){
   ```

8. 修改 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/src/com/mediatek/factorymode/Utils.java` 文件如下代码：

   ```diff
   @@ -54,6 +54,7 @@ public class Utils{
                   R.string.device_info,
                   R.string.version,
                   R.string.battery_name,
   +        R.string.hall_switch_test,^M
                   //R.string.flashlight,
                   //R.string.led_name,
                   //R.string.fmradio_name,
   @@ -97,6 +98,7 @@ public class Utils{
                   "ro.mid.device_info",
                   "ro.mid.version",
                   "ro.mid.battery_name",
   +        "ro.mid.hall_switch_test",^M
                   //"ro.mid.flashlight",
                   //"ro.mid.led_name",
                   //"ro.mid.fmradio_name",
   @@ -206,6 +208,8 @@ public class Utils{
                           pkg = "com.mediatek.factorymode.version.version";
                   else if (res.getString(R.string.flashlight).equals(str1)) 
                           pkg = "com.mediatek.factorymode.flashlight.FlashLight";
   +        else if (res.getString(R.string.hall_switch_test).equals(str1)) ^M
   +                       pkg = "com.mediatek.factorymode.sensor.HallSwitchTest";^M
                   else if (res.getString(R.string.googlekey).equals(str1)) 
                           pkg = "com.mediatek.factorymode.googlekey.googlekey";
            else if (res.getString(R.string.agingtest).equals(str1))
   ```

9. 添加 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/src/com/mediatek/factorymode/sensor/HallSwitchTest.java` 文件：

   ```java
   package com.mediatek.factorymode.sensor;
   
   import android.app.Activity;
   import android.database.ContentObserver;
   import android.content.Intent;
   import android.content.SharedPreferences;
   import android.net.Uri;
   import android.os.Bundle;
   import android.os.Handler;
   import android.provider.Settings;
   import android.widget.TextView;
   import android.widget.Button;
   import android.view.View;
   import android.view.View.OnClickListener;
   import android.view.WindowManager;
   import android.graphics.Color;
   import android.util.Log;
   
   import com.mediatek.factorymode.R;
   import com.mediatek.factorymode.Utils;
   
   
   public class HallSwitchTest extends Activity implements OnClickListener {
   
       private static final String TAG = "HallSwitchTest";
       public static int HallTestStatus = 0;
       protected static boolean mCreateFirstTime;
       private TextView hallTv;
       private Button mBtFailed;
       private Button mBtOk;
   
       private View mContainerView;
       private TextView hallTextView;
       
       private SharedPreferences mSp;
   
       @Override
       protected void onCreate(Bundle bundle) {
           super.onCreate(bundle);
           this.getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
           setContentView(R.layout.test_result_hall_switch);
           
           mSp = getSharedPreferences("FactoryMode", 0);
   
           mContainerView = findViewById(R.id.container);
           hallTextView = findViewById(R.id.txt_value_hall);
           hallTextView.setText(R.string.hall_toast);
           
           mBtOk = (Button)findViewById(R.id.bt_ok);
           this.mBtOk.setOnClickListener(this);
           mBtOk.setEnabled(false);
           mBtFailed = (Button)findViewById(R.id.bt_failed);
           this.mBtFailed.setOnClickListener(this);
   
           Settings.System.putInt(getContentResolver(), "factory_test_hall", 1);
           getContentResolver().registerContentObserver(Settings.System.getUriFor("lid_state"), false, mObserver);
       }
   
       @Override
       protected void onResume() {
           super.onResume();
           updateHallState();
       }
   
       @Override
       protected void onDestroy() {
           getContentResolver().unregisterContentObserver(mObserver);
           Settings.System.putInt(getContentResolver(), "factory_test_hall", 0);
           super.onDestroy();
       }
   
       private void updateHallState() {
           boolean closed = Settings.System.getInt(getContentResolver(),
                   "lid_state", -1) == 0;
           if (closed) {
               hallTextView.setText(R.string.hall_is_open);
               mContainerView.setBackgroundColor(Color.BLUE);
               mBtOk.setEnabled(true);
           } else {
               hallTextView.setText(R.string.hall_toast);
           }
       }
   
       private ContentObserver mObserver = new ContentObserver(new Handler()) {
           @Override
           public void onChange(boolean selfChange, Uri uri) {
               updateHallState();
           }
       };
       
       public void onClick(View arg0) {
           if(arg0.getId() == mBtOk.getId()){
               HallTestStatus = 1;
               Utils.putInt(getApplicationContext(), "Hall_switch_Test", 1);
               Utils.SetPreferences(this, mSp, R.string.hall_switch_test, "success");
               finish();
               Intent localIntent = new Intent(); 
               localIntent.setClassName("com.mediatek.factorymode", "com.mediatek.factorymode.googlekey.googlekey");
               localIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
               startActivity(localIntent);
           } else{
               HallTestStatus = -1;
               Utils.SetPreferences(this, mSp, R.string.hall_switch_test, "failed");
               finish();
           }
       }
   
   }
   ```

   