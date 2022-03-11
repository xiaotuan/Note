[toc]

### 1. Android 

修改 `frameworks/base/packages/SettingsProvider/res/values/defaults.xml` 文件， 将 `def_wifi_on` 的值设置成 `false` 即可，例如：

```xml
<bool name="def_wifi_on">false</bool>
```

### 2. 微步

#### 2.1 MTK 平台

##### 2.1.1 mt8766_r

修改 `vendor/mediatek/proprietary/packages/apps/SettingsProvider/res/values/defaults.xml` 文件，将 `def_wifi_on` 的值设置成 `false` 即可，例如：

```xml
<bool name="def_wifi_on">false</bool>
```

> 注意：
>
> 如果系统带开机向导，则会在开机向导界面重新打开 wifi。这时可以使用如下修改解决：
>
> 修改 `frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java` 文件中的 `broadcastIntentLocked()` 方法，在如下位置添加修改代码：
>
> ```java
> // Verify that protected broadcasts are only being sent by system code,
> // and that system code is only sending protected broadcasts.
> final boolean isProtectedBroadcast;
> try {
> isProtectedBroadcast = AppGlobals.getPackageManager().isProtectedBroadcast(action);
> } catch (RemoteException e) {
> Slog.w(TAG, "Remote exception", e);
> return ActivityManager.BROADCAST_SUCCESS;
> }
> 
> // 添加代码开始位置
> if (intent != null && intent.getAction() != null && intent.getAction().equals(Intent.ACTION_PACKAGE_CHANGED)) { 
>     String data =intent.getDataString();
>     if (data != null && data.length() != 0) {
>         if (data.endsWith("setupwizard")) {
>             if (android.provider.Settings.Global.getInt(mContext.getContentResolver(), android.provider.Settings.Global.WIFI_ON, 0) == 0) {
>                 android.net.wifi.WifiManager mWifiManager =(android.net.wifi.WifiManager) mContext.getSystemService(Context.WIFI_SERVICE);
>                 int state =mWifiManager.getWifiState();	
>                 if(state == android.net.wifi.WifiManager.WIFI_STATE_ENABLED){
>                     mWifiManager.setWifiEnabled(false);
>                 }
>             }
>         }
>     }
> }
> // 添加代码位置结束
> 
> final boolean isCallerSystem;
> switch (UserHandle.getAppId(callingUid)) {
> ```