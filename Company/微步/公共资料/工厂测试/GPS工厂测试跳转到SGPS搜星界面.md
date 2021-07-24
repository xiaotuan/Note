1. 修改 `vendor/sprd/platform/packages/apps/ValidationTools/src/com/sprd/validationtools/itemstest/gps/GpsTestActivity.java` 文件，将其修改为如下代码：

   ```java
   package com.sprd.validationtools.itemstest.gps;
   
   import java.util.Iterator;
   import java.util.Timer;
   import java.util.TimerTask;
   
   import android.content.Context;
   import android.location.GpsSatellite;
   import android.location.GpsStatus;
   import android.location.Location;
   import android.location.LocationListener;
   import android.location.LocationManager;
   import android.os.Bundle;
   import android.os.Handler;
   import android.provider.Settings;
   import android.util.Log;
   import android.view.View;
   import android.view.WindowManager;
   import android.widget.Button;
   import android.widget.TextView;
   import android.widget.Toast;
   import android.content.Intent;
   import android.content.ComponentName;
   
   import com.sprd.validationtools.BaseActivity;
   import com.sprd.validationtools.R;
   
   public class GpsTestActivity extends BaseActivity {
       private static final String TAG = "GpsTestActivity";
       
       /** the text view object for show gps not enabled message */
       private TextView txtGpsMsg = null;
       private TextView mSatelliteInfo;
       
       /** location manager object */
       private LocationManager manager = null;
   
       @Override
       public void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           getWindow().setFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON,
                   WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
           setContentView(R.layout.gps_test_main);
           setTitle(R.string.gps_test);
           getWindow().addFlags(WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED);
   
           txtGpsMsg = (TextView) findViewById(R.id.txt_gps_not_enabled);
           mSatelliteInfo = (TextView) findViewById(R.id.txt_gps_satellite_info);
           mSatelliteInfo.setText("\n\n");
   
           manager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
           setTitle(R.string.gps_title_text);
           if (isGpsEnabled()) {
               Settings.Secure.setLocationProviderEnabled(getContentResolver(),
           LocationManager.GPS_PROVIDER, true);
               try {
                   Intent intent = new Intent();
                   intent.putExtra("tab_tag", "Satellites");
                   intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                   intent.setComponent(new ComponentName("com.spreadtrum.sgps",
                           "com.spreadtrum.sgps.SgpsActivity"));
                   startActivity(intent);
                   mPassButton.setVisibility(View.VISIBLE);
               } catch (Exception e) {
                   Log.d(TAG, e.getMessage());
               }
           } else {
               mPassButton.setVisibility(View.INVISIBLE);
           }
       }
   
       @Override
       public void onResume() {
           super.onResume();
           showGpsMsg();
       }
       
       @Override
       public void onStop() {
           if (isGpsEnabled()) {
               Settings.Secure.setLocationProviderEnabled(getContentResolver(),
           LocationManager.GPS_PROVIDER, false);
           }
           super.onStop();
       }
   
       @Override
       protected void onDestroy() {
           super.onDestroy();
       }
   
       private boolean isGpsEnabled() {
           if (manager == null) {
               return false;
           }
   
           return manager.isProviderEnabled(PROVIDER);
       }
   
       private void showGpsMsg() {
           if (!isGpsEnabled()) {
               // gps not enabled
               txtGpsMsg.setText(getString(R.string.gps_not_enabled_msg));
           } else {
               txtGpsMsg.setText("");
           }
       }
   
       @Override
       public void onBackPressed() {
           return ;
       }
   
   }
   ```

2. 修改 `vendor/sprd/platform/packages/apps/SGPS/src/com/spreadtrum/sgps/SgpsActivity` 文件，处理在启动该 Activity 后跳转到搜星界面，修改如下：

   2.1 导入 `CountDownTimer`

   ```java
   import android.os.CountDownTimer;
   ```

   2.2 定义如下变量

   ```java
   private String mTabTag = null;
   private CountDownTimer mTimer;
   ```

   2.3 在 `onCreate` 方法末尾添加如下代码：

   ```java
   android.util.Log.d("SgpsActivity", "onCreate=>intent: " + getIntent());
   if (getIntent() != null) {
       mTabTag = getIntent().getStringExtra("tab_tag");
       android.util.Log.d("SgpsActivity", "onCreate=>tag: " + mTabTag);
   }
   ```

   2.4 在 `onResume` 方法末尾添加如下代码：

   ```java
   android.util.Log.d("SgpsActivity", "onResume=>tag: " + mTabTag);
   if ("Satellites".equals(mTabTag)) {
       mTimer = new CountDownTimer(20000, 100) {
           @Override
           public void onTick(long millisUntilFinished) {
               android.util.Log.d("SgpsActivity", "onTick=>hNMEAtabMenu: " + hNMEAtabMenu);
               if (hNMEAtabMenu != null) {
                   String tagId = getString(R.string.satellites);
                   getTabHost().setCurrentTabByTag(tagId);
                   mTabTag = null;
                   mTimer.cancel();
               }
           }
   
           @Override
           public void onFinish() {
               // do something
           }
       };
       mTimer.start();
   }
   ```

   

