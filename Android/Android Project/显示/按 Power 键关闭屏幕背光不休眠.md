[toc]

### 1. MTK平台

#### 1.1 MTK8766、Android R

##### 1.1.1 修改 `frameworks/base/services/core/java/com/android/server/power/PowerManagerService.java`

1. 定义变量

   ```java
   private LogicalLight mBacklight;
   ```

2. 初始化变量

   ```java
   public void systemReady(IAppOpsService appOps) {
    	synchronized (mLock) {
        	......
           mLightsManager = getLocalService(LightsManager.class);
           mAttentionLight = mLightsManager.getLight(LightsManager.LIGHT_ID_ATTENTION);
           mBacklight = mLightsManager.getLight(LightsManager.LIGHT_ID_BACKLIGHT);	// 添加该行代码
   
           // Initialize display power management.
           mDisplayManagerInternal.initPowerManagement(
                       mDisplayPowerCallbacks, mHandler, sensorManager);
       }
   }
   ```

3. 修改 `wakeUp()` 方法

   ```java
   @Override // Binder call
   public void wakeUp(long eventTime, @WakeReason int reason, String details,
                      String opPackageName) {
       if (eventTime > mClock.uptimeMillis()) {
           throw new IllegalArgumentException("event time must not be in the future");
       }
   
       mContext.enforceCallingOrSelfPermission(
           android.Manifest.permission.DEVICE_POWER, null);
   
       // 开始注释代码位置
       // final int uid = Binder.getCallingUid();
       // final long ident = Binder.clearCallingIdentity();
       // try {
       //     wakeUpInternal(eventTime, reason, details, uid, opPackageName, uid);
       // } finally {
       //     Binder.restoreCallingIdentity(ident);
       // }
       // 结束注释代码位置
       // 开始添加代码位置
       if (mBacklight != null) {
           final ContentResolver resolver = mContext.getContentResolver();
           int brightness = Settings.System.getIntForUser(resolver, Settings.System.SCREEN_BRIGHTNESS, 102,
                                                          UserHandle.USER_CURRENT);
           Settings.System.putIntForUser(resolver, "goto_sleep", 0, UserHandle.USER_CURRENT);
           mBacklight.setBrightness(brightness/255.0f);
           android.util.Log.d(TAG, "wakeUp=>brightness: " + brightness);
       } else {
           android.util.Log.e(TAG, "wakeUp=>Backlight is null.");
       }
       // 结束添加代码位置
   }
   ```

4. 修改 `goToSleep()` 方法

   ```java
   @Override // Binder call
   public void goToSleep(long eventTime, int reason, int flags) {
       if (eventTime > mClock.uptimeMillis()) {
           throw new IllegalArgumentException("event time must not be in the future");
       }
   
       mContext.enforceCallingOrSelfPermission(
           android.Manifest.permission.DEVICE_POWER, null);
       
   	// 开始添加代码位置
       if (mBacklight != null) {
           android.util.Log.d(TAG, "goToSleep=turn off.");
           final ContentResolver resolver = mContext.getContentResolver();
           Settings.System.putIntForUser(resolver, "goto_sleep", 1, UserHandle.USER_CURRENT);
           mBacklight.turnOff();
       } else {
           android.util.Log.e(TAG, "goToSleep=>Backlight is null.");
       }
       // 结束添加代码位置
   
       // 开始注释代码位置
       // final int uid = Binder.getCallingUid();
       // final long ident = Binder.clearCallingIdentity();
       // try {
       //     goToSleepInternal(eventTime, reason, flags, uid);
       // } finally {
       //     Binder.restoreCallingIdentity(ident);
       // }
       // 结束注释代码位置
   }
   ```

##### 1.1.2 修改 `frameworks/base/services/core/java/com/android/server/policy/PhoneWindowManager.java`

1. 修改 `interceptKeyBeforeQueueing()` 方法

   ```java
   @Override
   public int interceptKeyBeforeQueueing(KeyEvent event, int policyFlags) {
       if (!mSystemBooted) {
           // If we have not yet booted, don't let key events do anything.
           return 0;
       }
   
       // /M:add for IPO, when shut down, don't let key events do anything. ,@{
       String huStatus = SystemProperties.get("sys.hu.status", null);
       if(huStatus != null && huStatus.contains("shutdown")) {
           Slog.w(TAG, "IPO Shutdown skip ");
           return 0;
       }
       // /@}
   
       // 开始添加代码位置
       boolean isGotoSleep = Settings.System.getIntForUser(mContext.getContentResolver(), "goto_sleep", 0, UserHandle.USER_CURRENT) == 1;
       final boolean interactive = ((policyFlags & FLAG_INTERACTIVE) != 0) && !isGotoSleep;
       android.util.Log.d(TAG, "interceptKeyBeforeQueueing=>isGotoSleep: " + isGotoSleep 
                          + ", interactive: " + ((policyFlags & FLAG_INTERACTIVE) != 0));
      	// 结束添加代码位置
       // final boolean interactive = (policyFlags & FLAG_INTERACTIVE) != 0;	// 注释这行代码
       final boolean down = event.getAction() == KeyEvent.ACTION_DOWN;
       final boolean canceled = event.isCanceled();
       final int keyCode = event.getKeyCode();
       ......
   }
   ```

   

