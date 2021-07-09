[toc]

### 1. 展讯平台

#### 1.1 Android R

修改 `frameworks\base\packages\SettingsProvider\res\values\defaults.xml` 文件中的 `def_wifi_on` 的值为 `false` 即可。

```xml
<bool name="def_wifi_on">false</bool>
```

> 提示：
>
> 如果系统带开机向导，则会在开机向导界面重新打开 wifi。这时可以使用如下修改解决：
>
> 修改 `\frameworks\base\services\core\java\com\android\server\am\ActivityManagerService.java` 文件中的 `broadcastIntentLocked()` 方法，在如下位置添加修改代码：
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
> if(intent != null && intent.getAction() != null &&intent.getAction().equals(Intent.ACTION_PACKAGE_CHANGED)){ 
> String data =intent.getDataString();
> if(data.endsWith("setupwizard")){
>   if("false".equalsIgnoreCase(SystemProperties.get("ro.wb.wifi_on", "false"))){
>       WifiManager mWifiManager =(WifiManager) mContext.getSystemService(Context.WIFI_SERVICE);
>       int state =mWifiManager.getWifiState();	
>       if(state == WifiManager.WIFI_STATE_ENABLED){
>           mWifiManager.setWifiEnabled(false);
>       }
>   }
> }
> }
> // 添加代码位置结束
> 
> final boolean isCallerSystem;
> switch (UserHandle.getAppId(callingUid)) {
> case ROOT_UID:
> case SYSTEM_UID:
> case PHONE_UID:
> case BLUETOOTH_UID:
> case NFC_UID:
> case SE_UID:
> case NETWORK_STACK_UID:
>   isCallerSystem = true;
>   break;
> default:
>   isCallerSystem = (callerApp != null) && callerApp.isPersistent();
>   break;
> }
> ```
>
> 记得导入下列包：
>
> ```java
> import android.net.wifi.WifiManager;
> ```
>
> 并在 `device\sprd\mpool\module\main.mk` 文件中添加如下代码：
>
> ```makefile
> PRODUCT_SYSTEM_EXT_PROPERTIES += ro.wb.wifi_on=false
> ```



