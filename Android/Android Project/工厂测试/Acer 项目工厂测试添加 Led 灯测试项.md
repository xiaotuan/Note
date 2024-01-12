[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

1. 修改 `u_sys/frameworks/base/services/core/java/com/android/server/lights/LightsService.java` 文件中 `setLightUnchecked(()` 方法的如下代码：

   ```diff
   @@ -270,9 +270,12 @@ public class LightsService extends SystemService {
        }
    
        private final class LightImpl extends LogicalLight {
   +        
   +        private Context mContext;
    
            private LightImpl(Context context, HwLight hwLight) {
                mHwLight = hwLight;
   +            mContext = context;
            }
    
            @Override
   @@ -392,6 +395,20 @@ public class LightsService extends SystemService {
                    int brightnessMode) {
                Trace.traceBegin(Trace.TRACE_TAG_POWER, "setLightState(" + mHwLight.id + ", 0x"
                        + Integer.toHexString(color) + ")");
   +
   +            boolean isFactoryTest = false;
   +            try {
   +                isFactoryTest = Settings.System.getInt(mContext.getContentResolver(), "factory_test_led", 0) == 1;
   +            } catch (Exception e) {
   +                android.util.Log.e("LightsService", "setLightLocked=>error: ", e);
   +            }
   +            android.util.Log.d("LightsService", "setLightLocked=>isFactoryTest: " + isFactoryTest + ", color: " + color);
   +            if (isFactoryTest) {
   +                if (mHwLight.id != LightsManager.LIGHT_ID_NOTIFICATIONS) {
   +                    return;
   +                }
   +            }
   +            
                try {
                    if (mVintfLights != null) {
                        HwLightState lightState = new HwLightState();
   ```

2. 修改 `u_sys/frameworks/base/services/core/java/com/android/server/notification/NotificationManagerService.java` 文件的如下代码：

   ```diff
   @@ -480,6 +480,15 @@ public class NotificationManagerService extends SystemService {
        static final String REVIEW_NOTIF_ACTION_REMIND = "REVIEW_NOTIF_ACTION_REMIND";
        static final String REVIEW_NOTIF_ACTION_DISMISS = "REVIEW_NOTIF_ACTION_DISMISS";
        static final String REVIEW_NOTIF_ACTION_CANCELED = "REVIEW_NOTIF_ACTION_CANCELED";
   +    
   +    // Add led test to FacotryTest by qty at 2023-04-14 {{&&
   +    public static final String NOTIFICATION_LIGHT_TEST_RED = "notification_light_test_red";
   +    public static final String NOTIFICATION_LIGHT_TEST_GREEN = "notification_light_test_green";
   +    public static final String NOTIFICATION_LIGHT_TEST_BLUE = "notification_light_test_blue";
   +    private int mRedTestARGB = 0xFFFF0000;
   +    private int mGreenTestARGB = 0xFF00FF00;
   +    private int mBlueTestARGB = 0xFF0000FF;
   +    // &&}}
    
        /**
         * Apps that post custom toasts in the background will have those blocked. Apps can
   @@ -1855,9 +1864,20 @@ public class NotificationManagerService extends SystemService {
                    }
                } else if (action.equals(Intent.ACTION_USER_PRESENT)) {
                    // turn off LED when user passes through lock screen
   +                // System control of LED lights is prohibited in factory test mode by qty at 2023-04-20 {{&&
   +                /*
                    if (mNotificationLight != null) {
                        mNotificationLight.turnOff();
                    }
   +                */
   +                if (Settings.System.getInt(context.getContentResolver(), "factory_test_led", 0) == 0) {
   +                    if (mNotificationLight != null) {
   +                        mNotificationLight.turnOff();
   +                    }
   +                } else {
   +                    android.util.Log.w("NMS", "onReceive=>Factory testing led.");
   +                }
   +                // &&}}
                } else if (action.equals(Intent.ACTION_USER_SWITCHED)) {
                    final int userId = intent.getIntExtra(Intent.EXTRA_USER_HANDLE, USER_NULL);
                    mUserProfiles.updateCache(context);
   @@ -1921,6 +1941,15 @@ public class NotificationManagerService extends SystemService {
            private final Uri LOCK_SCREEN_SHOW_NOTIFICATIONS
                    = Settings.Secure.getUriFor(Settings.Secure.LOCK_SCREEN_SHOW_NOTIFICATIONS);
    
   +        // Add led test to FacotryTest by qty at 2023-04-14 {{&&
   +        private final Uri NOTIFICATION_LIGHT_TEST_RED_URI
   +                = Settings.System.getUriFor(NOTIFICATION_LIGHT_TEST_RED);
   +        private final Uri NOTIFICATION_LIGHT_TEST_GREEN_URI
   +                = Settings.System.getUriFor(NOTIFICATION_LIGHT_TEST_GREEN);
   +        private final Uri NOTIFICATION_LIGHT_TEST_BLUE_URI
   +                = Settings.System.getUriFor(NOTIFICATION_LIGHT_TEST_BLUE);
   +        // &&}}
   +
            SettingsObserver(Handler handler) {
                super(handler);
            }
   @@ -1944,6 +1973,16 @@ public class NotificationManagerService extends SystemService {
                        false, this, UserHandle.USER_ALL);
                resolver.registerContentObserver(LOCK_SCREEN_SHOW_NOTIFICATIONS,
                        false, this, UserHandle.USER_ALL);
   +
   +            // Add led test to FacotryTest by qty at 2023-04-14 {{&&
   +            resolver.registerContentObserver(NOTIFICATION_LIGHT_TEST_RED_URI,
   +                    false, this, UserHandle.USER_ALL);
   +            resolver.registerContentObserver(NOTIFICATION_LIGHT_TEST_GREEN_URI,
   +                    false, this, UserHandle.USER_ALL);
   +            resolver.registerContentObserver(NOTIFICATION_LIGHT_TEST_BLUE_URI,
   +                    false, this, UserHandle.USER_ALL);
   +            // &&}}
   +
                update(null);
            }
    
   @@ -1991,6 +2030,27 @@ public class NotificationManagerService extends SystemService {
                if (uri == null || LOCK_SCREEN_SHOW_NOTIFICATIONS.equals(uri)) {
                    mPreferencesHelper.updateLockScreenShowNotifications();
                }
   +            
   +            // Add led test to FacotryTest by qty at 2023-04-14 {{&&
   +            if (uri == null || NOTIFICATION_LIGHT_TEST_RED_URI.equals(uri)) {
   +                boolean testRedEnabled = Settings.System.getIntForUser(resolver,
   +                        NOTIFICATION_LIGHT_TEST_RED, 0, UserHandle.USER_CURRENT) != 0;
   +                Log.d(TAG, "testRedEnabled: " + testRedEnabled);
   +                updateNotificationLedTest(testRedEnabled, mRedTestARGB);
   +            }
   +            if (uri == null || NOTIFICATION_LIGHT_TEST_GREEN_URI.equals(uri)) {
   +                boolean testGreenEnabled = Settings.System.getIntForUser(resolver,
   +                        NOTIFICATION_LIGHT_TEST_GREEN, 0, UserHandle.USER_CURRENT) != 0;
   +                Log.d(TAG, "testGreenEnabled: " + testGreenEnabled);
   +                updateNotificationLedTest(testGreenEnabled, mGreenTestARGB);
   +            }
   +            if (uri == null || NOTIFICATION_LIGHT_TEST_BLUE_URI.equals(uri)) {
   +                boolean testBlueEnabled = Settings.System.getIntForUser(resolver,
   +                        NOTIFICATION_LIGHT_TEST_BLUE, 0, UserHandle.USER_CURRENT) != 0;
   +                Log.d(TAG, "testBlueEnabled: " + testBlueEnabled);
   +                updateNotificationLedTest(testBlueEnabled, mBlueTestARGB);
   +            }
   +            // &&}}
            }
        }
    
   @@ -2500,6 +2560,21 @@ public class NotificationManagerService extends SystemService {
                    Context.RECEIVER_NOT_EXPORTED);
        }
    
   +    // Add led test to FacotryTest by qty at 2023-04-14 {{&&
   +    private void updateNotificationLedTest(boolean test, int ledcolor) {
   +        Log.d(TAG, "mScreenOn : " + mScreenOn);
   +        // Don't flash while we are in a call or screen is on
   +        if ( isInCall() || !mScreenOn || !test) {
   +            mNotificationLight.turnOff();
   +            Log.d(TAG, "tmNotificationLight.turnOff(): ");
   +        } else {
   +            Log.d(TAG, "mNotificationPulseEnabled: " + mNotificationPulseEnabled);
   +            Log.d(TAG, "ledcolor: " + ledcolor);
   +            mNotificationLight.setColor(ledcolor);
   +        }
   +    }
   +    // &&}}
   +
        /**
         * Cleanup broadcast receivers change listeners.
         */
   @@ -8420,9 +8495,13 @@ public class NotificationManagerService extends SystemService {
            }
            // Suppressed because it's a silent update
            final Notification notification = record.getNotification();
   +        // Add led test to FacotryTest by qty at 2023-04-14 {{&&
   +        /*
            if (record.isUpdate && (notification.flags & FLAG_ONLY_ALERT_ONCE) != 0) {
                return false;
            }
   +        */
   +        // &&}}
            // Suppressed because another notification in its group handles alerting
            if (record.getSbn().isGroup() && record.getNotification().suppressAlertingDueToGrouping()) {
                return false;
   @@ -9797,6 +9876,8 @@ public class NotificationManagerService extends SystemService {
            }
    
            // Don't flash while we are in a call or screen is on
   +        // System control of LED lights is prohibited in factory test mode by qty at 2023-04-20 {{&&
   +        /*
            if (ledNotification == null || isInCall() || mScreenOn) {
                mNotificationLight.turnOff();
            } else {
   @@ -9807,6 +9888,22 @@ public class NotificationManagerService extends SystemService {
                            light.onMs, light.offMs);
                }
            }
   +        */
   +        if (Settings.System.getInt(getContext().getContentResolver(), "factory_test_led", 0) == 0) {
   +            if (ledNotification == null || isInCall() || mScreenOn) {
   +                mNotificationLight.turnOff();
   +            } else {
   +                NotificationRecord.Light light = ledNotification.getLight();
   +                if (light != null && mNotificationPulseEnabled) {
   +                    // pulse repeatedly
   +                    mNotificationLight.setFlashing(light.color, LogicalLight.LIGHT_FLASH_TIMED,
   +                            light.onMs, light.offMs);
   +                }
   +            }
   +        } else {
   +            android.util.Log.d("NMS", "updateLightsLocked=>light led is in factory test.");
   +        }
   +        // &&}}
        }
    
        @GuardedBy("mNotificationLock")
   ```

3. 添加 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/src/com/mediatek/factorymode/led/Led.java` 文件：

   ```java
   package com.mediatek.factorymode.led;
   
   import android.app.Activity;
   import android.content.Intent;
   import android.content.SharedPreferences;
   import android.os.Bundle;
   import android.util.Log;
   import android.view.View;
   import android.view.WindowManager;
   import android.widget.Button;
   import android.provider.Settings;
   
   import java.io.File;
   import java.io.FileOutputStream;
   import java.io.OutputStream;
   
   import com.mediatek.factorymode.R;
   import com.mediatek.factorymode.Utils;
   
   public class Led extends Activity implements View.OnClickListener {
   
       private static final String TAG = "Led";
       
       public static final String NOTIFICATION_LIGHT_TEST_RED = "notification_light_test_red";
       public static final String NOTIFICATION_LIGHT_TEST_GREEN = "notification_light_test_green";
       public static final String NOTIFICATION_LIGHT_TEST_BLUE = "notification_light_test_blue";
   
       private Button mPassBtn;
       private Button mFailBtn;
       private Button mRedBtn;
       private Button mGreenBtn;
       private Button mBlueBtn;
       
       private SharedPreferences mSp;
   
       private boolean isRedButtonClick;
       private boolean isGreenButtonClick;
       private boolean isBlueButtonClick;
   
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           //getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
   
           setContentView(R.layout.activity_ledtest);
           
           mSp = getSharedPreferences("FactoryMode", 0);
   
           mPassBtn = findViewById(R.id.bt_ok);
           mFailBtn = findViewById(R.id.bt_failed);
           mRedBtn = findViewById(R.id.red_led);
           mGreenBtn = findViewById(R.id.green_led);
           mBlueBtn = findViewById(R.id.blue_led);
   
           mPassBtn.setOnClickListener(this);
           mFailBtn.setOnClickListener(this);
           mRedBtn.setOnClickListener(this);
           mGreenBtn.setOnClickListener(this);
           mBlueBtn.setOnClickListener(this);
   
           mPassBtn.setEnabled(false);
       }
       
       @Override
       protected void onStart() {
           super.onStart();
           Settings.System.putInt(getContentResolver(), "factory_test_led", 1);
       }
   
       @Override
       protected void onPause() {
           super.onPause();
           closeAllLed();
       }
       
       @Override
       protected void onStop() {
           super.onStart();
           Settings.System.putInt(getContentResolver(), "factory_test_led", 0);
       }
   
       @Override
       public void onClick(View v) {
           switch (v.getId()) {
               case R.id.bt_ok:
                   Utils.putInt(getApplicationContext(), "Led_Test", 1);
                   Utils.SetPreferences(this, mSp, R.string.led_name, "success");
                   finish();
                   Intent localIntent = new Intent(); 
                   localIntent.setClassName("com.mediatek.factorymode", "com.mediatek.factorymode.googlekey.googlekey");
                   localIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                   startActivity(localIntent);
                   break;
   
               case R.id.bt_failed:
                   Utils.SetPreferences(this, mSp, R.string.led_name, "failed");
                   finish();
                   break;
   
               case R.id.red_led:
                   testRed();
                   isRedButtonClick = true;
                   break;
   
               case R.id.green_led:
                   testGreen();
                   isGreenButtonClick = true;
                   break;
   
               case R.id.blue_led:
                   testBlue();
                   isBlueButtonClick = true;
                   break;
           }
           if (isRedButtonClick && isGreenButtonClick && isBlueButtonClick) {
               mPassBtn.setEnabled(true);
           }
       }
       
       private void testRed() {
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_GREEN, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_BLUE, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_RED, 1);
       }
   
       private void testGreen() {
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_RED, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_BLUE, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_GREEN, 1);
       }
   
       private void testBlue() {
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_RED, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_GREEN, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_BLUE, 1);
       }
   
       private void closeAllLed() {
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_RED, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_GREEN, 0);
           Settings.System.putInt(getContentResolver(), NOTIFICATION_LIGHT_TEST_BLUE, 0);
       }
   
   }
   ```

4. 添加 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/res/layout/activity_ledtest.xml` 文件:

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
       android:id="@+id/container"
       style="@style/info_layout">
       
       <include layout="@layout/mid_header"/>
   
       <LinearLayout
           android:layout_width="match_parent"
           android:layout_height="0dp"
           android:layout_weight="1"
           android:gravity="center"
           android:orientation="vertical">
   
           <Button
               android:id="@+id/red_led"
               android:layout_width="240dp"
               android:layout_height="96dp"
               android:layout_marginBottom="4dp"
               android:text="@string/red_led_title" />
   
           <Button
               android:id="@+id/green_led"
               android:layout_width="240dp"
               android:layout_height="96dp"
               android:layout_marginTop="4dp"
               android:layout_marginBottom="4dp"
               android:text="@string/green_led_title" />
   
           <Button
               android:id="@+id/blue_led"
               android:layout_width="240dp"
               android:layout_height="96dp"
               android:layout_marginTop="4dp"
               android:layout_marginBottom="8dp"
               android:text="@string/blue_led_title" />
   
       </LinearLayout>
   
       <include layout="@layout/mid_btns"/>
       
   </LinearLayout>
   ```

5. 修改 `vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/src/com/mediatek/factorymode/FactoryMode.java` 文件中的如下代码：

   ```diff
   @@ -81,8 +81,8 @@ public class FactoryMode extends Activity implements
                   R.string.version,
                   R.string.battery_name,
            R.string.hall_switch_test,
   +        R.string.led_name,^M
                   //R.string.flashlight,
   -               //R.string.led_name,
                   //R.string.fmradio_name,
                   //R.string.vibrator_name,               
                   //R.string.gsensorcali_name,
   @@ -116,6 +116,7 @@ public class FactoryMode extends Activity implements
                           Utils.putInt(getApplicationContext(), "Microphone_Test", 2);
                           Utils.putInt(getApplicationContext(), "Headset_Test", 2);
                Utils.putInt(getApplicationContext(), "Hall_switch_Test", 2);
   +            Utils.putInt(getApplicationContext(), "Led_Test", 2);^M
                           //Utils.putInt(getApplicationContext(), "TP_test", 2);
                           Intent intent = new Intent(Intent.ACTION_REQUEST_SHUTDOWN);
                           intent.putExtra(Intent.EXTRA_KEY_CONFIRM, false);
   @@ -172,7 +173,7 @@ public class FactoryMode extends Activity implements
                                                   (Utils.getInt(getApplicationContext(), "SubCamera_Test") == 1) && (Utils.getInt(getApplicationContext(), "Left_speaker_Test") == 1) &&
                                                   (Utils.getInt(getApplicationContext(), "Microphone_Test") == 1) && (Utils.getInt(getApplicationContext(), "Headset_Test") == 1) &&
                                                   (Utils.getInt(getApplicationContext(), "Old_Test") == 1) && (Utils.getInt(getApplicationContext(), "Reboot_Test") == 1) &&
   -                        (Utils.getInt(getApplicationContext(), "Hall_switch_Test") == 1)
   +                        (Utils.getInt(getApplicationContext(), "Hall_switch_Test") == 1) && (Utils.getInt(getApplicationContext(), "Led_Test") == 1)^M
                                           ){      
                                                   Log.d(TAG, "SetColor=>power off.");                                     
                                                   powerOff(this); 
   @@ -349,6 +350,7 @@ public class FactoryMode extends Activity implements
                                                           //Utils.putInt(getApplicationContext(), "TP_test", 0);
                                                           Utils.putInt(getApplicationContext(), "Version", 3);
                                Utils.putInt(getApplicationContext(), "Hall_switch_Test", 0);
   +                            Utils.putInt(getApplicationContext(), "Led_Test", 0);^M
                                                           Utils.SetPreferences(FactoryMode.this,mSp,arrayOfInt[i],"null");
                                                           mSp.edit().putBoolean("is_close_sequence_test", false).commit();
                                                           mSp.edit().remove("reboot_test_time").commit();
   @@ -459,8 +461,11 @@ public class FactoryMode extends Activity implements
                                   startActivity(localIntent);     
                }else if(str2.equals("com.mediatek.factorymode.sensor.HallSwitchTest") && ((Utils.getInt(getApplicationContext(), "Battery_Test") == 1 || Utils.getInt(getApplicationContext(), "Battery_Test") == 2) || isCloseSequenceTest)){
                                   localIntent.setClassName(this, str2);
   -                               startActivity(localIntent);     
   -                       }else if(str2.equals("com.mediatek.factorymode.googlekey.googlekey") && (Utils.getInt(getApplicationContext(), "Hall_switch_Test") == 1  || isCloseSequenceTest)){
   +                               startActivity(localIntent);^M
   +            }else if(str2.equals("com.mediatek.factorymode.led.Led") && ((Utils.getInt(getApplicationContext(), "Hall_switch_Test") == 1 || Utils.getInt(getApplicationContext(), "Hall_switch_Test") == 2) || isCloseSequenceTest)){^M
   +                localIntent.setClassName(this, str2);^M
   +                startActivity(localIntent);^M
   +                       }else if(str2.equals("com.mediatek.factorymode.googlekey.googlekey") && (Utils.getInt(getApplicationContext(), "Led_Test") == 1  || isCloseSequenceTest)){^M
                                   localIntent.setClassName(this, str2);
                                   startActivity(localIntent);     
                           // }else if(str2.equals("com.mediatek.factorymode.tp.TPTest")){
   ```

6. 修改 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/src/com/mediatek/factorymode/Utils.java` 文件如下代码：

   ```diff
   @@ -55,8 +55,8 @@ public class Utils{
                   R.string.version,
                   R.string.battery_name,
            R.string.hall_switch_test,
   +        R.string.led_name,^M
                   //R.string.flashlight,
   -               //R.string.led_name,
                   //R.string.fmradio_name,
                   //R.string.vibrator_name,               
                   //R.string.gsensorcali_name,
   @@ -99,8 +99,8 @@ public class Utils{
                   "ro.mid.version",
                   "ro.mid.battery_name",
            "ro.mid.hall_switch_test",
   +        "ro.mid.led_name",^M
                   //"ro.mid.flashlight",
   -               //"ro.mid.led_name",
                   //"ro.mid.fmradio_name",
                   //"ro.mid.vibrator_name",               
                   //"ro.mid.gsensorcali_name",
   ```

7. 在 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/res/values/strings.xml` 文件中添加如下代码：

   ```xml
   <string name="red_led_title">Red light</string>
   <string name="green_led_title">Green light</string>
   <string name="blue_led_title">Blue light</string>
   ```

8. 在 `u_sys/vendor/mediatek/proprietary/packages/apps/FactoryMode_Acer/res/values-zh-rCN/strings.xml` 文件中添加如下代码：

   ```xml
   <string name="red_led_title">红色灯</string>
   <string name="green_led_title">绿色灯</string>
   <string name="blue_led_title">蓝色灯</string>
   ```

   