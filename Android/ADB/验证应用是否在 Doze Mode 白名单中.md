通过如下命令可以查看应用是否在 `Doze Mode` 白名单中：

```shell
$ adb shell dumpsys deviceidle
```

例如：

```shell
$ adb shell dumpsys deviceidle
  Settings:
    flex_time_short=+1m0s0ms
    light_after_inactive_to=+4m0s0ms
    light_idle_to=+5m0s0ms
    light_idle_factor=2.0
    light_max_idle_to=+15m0s0ms
    light_idle_maintenance_min_budget=+1m0s0ms
    light_idle_maintenance_max_budget=+5m0s0ms
    min_light_maintenance_time=+5s0ms
    min_deep_maintenance_time=+30s0ms
    inactive_to=+30m0s0ms
    sensing_to=+4m0s0ms
    locating_to=+30s0ms
    location_accuracy=20.0m
    motion_inactive_to=+10m0s0ms
    motion_inactive_to_flex=+1m0s0ms
    idle_after_inactive_to=+30m0s0ms
    idle_pending_to=+5m0s0ms
    max_idle_pending_to=+10m0s0ms
    idle_pending_factor=2.0
    quick_doze_delay_to=+1m0s0ms
    idle_to=+1h0m0s0ms
    max_idle_to=+6h0m0s0ms
    idle_factor=2.0
    min_time_to_alarm=+30m0s0ms
    max_temp_app_allowlist_duration_ms=+5m0s0ms
    mms_temp_app_allowlist_duration_ms=+1m0s0ms
    sms_temp_app_allowlist_duration_ms=+20s0ms
    notification_allowlist_duration_ms=+30s0ms
    wait_for_unlock=true
    pre_idle_factor_long=1.67
    pre_idle_factor_short=0.33
    use_window_alarms=true
  Idling history:
         normal: -1h32m6s870ms (screen)
     light-idle: -1h11m5s626ms
    light-maint: -1h5m5s626ms
     light-idle: -1h4m49s994ms
    light-maint: -53m49s988ms
     light-idle: -53m44s918ms
    light-maint: -37m44s912ms
     light-idle: -37m39s858ms
    light-maint: -21m39s848ms
         normal: -20m16s139ms (charging)
     light-idle: -10m0s605ms
         normal: -9m25s249ms (unlocked)
  Whitelist (except idle) system apps:
    com.huub.everyday
    com.android.providers.calendar
    com.android.providers.downloads
    com.google.android.apps.safetyhub
    com.android.vending
    com.google.android.gms
    com.google.android.ims
    com.android.proxyhandler
    com.dti.xw
    com.google.android.apps.turbo
    com.aura.oobe.sliide
    com.android.shell
    com.android.emergency
    com.google.android.cellbroadcastreceiver
    com.android.providers.contacts
    us.sliide.puma
  Whitelist system apps:
    com.huub.everyday
    com.android.providers.calendar
    com.android.providers.downloads
    com.google.android.apps.safetyhub
    com.google.android.gms
    com.google.android.ims
    com.dti.xw
    com.aura.oobe.sliide
    com.android.shell
    com.android.emergency
    com.google.android.cellbroadcastreceiver
    us.sliide.puma
  Whitelist user apps:
    com.android.phone
  Whitelist (except idle) all app ids:
    1001
    2000
    10039
    10041
    10044
    10046
    10047
    10049
    10059
    10113
    10114
    10115
    10117
    10118
    10121
    10155
    10168
  Whitelist user app ids:
    1001
  Whitelist all app ids:
    1001
    2000
    10039
    10041
    10044
    10046
    10059
    10115
    10117
    10118
    10121
    10155
    10168
  mLightEnabled=true  mDeepEnabled=true
  mForceIdle=false
  mUseMotionSensor=true mMotionSensor=null
  mScreenOn=false
  mScreenLocked=true
  mNetworkConnected=true
  mCharging=true
  mMotionActive=false
  mNotMoving=false
  mMotionListener.activatedTimeElapsed=0
  mLastMotionEventElapsed=0
  3 stationary listeners registered
  mLocating=false mHasGps=false mHasNetwork=false mLocated=false
  mState=ACTIVE mLightState=ACTIVE
  mInactiveTimeout=+30m0s0ms
  mNextLightIdleDelay=+5m0s0ms
  mCurLightIdleBudget=+1m0s0ms
```

