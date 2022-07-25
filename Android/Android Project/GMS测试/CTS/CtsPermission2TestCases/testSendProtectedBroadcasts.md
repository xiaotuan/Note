[toc]

### 1. 测试命令

```shell
$ run cts -m CtsPermission2TestCases -t android.permission2.cts.ProtectedBroadcastsTest#testSendProtectedBroadcasts
```

### 2. 报错项列表

#### 2.1 修改默认关闭 wifi 功能导致的

1. 报错信息

   ```
   java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.endsWith(java.lang.String)' on a null object reference
   	at android.os.Parcel.createExceptionOrNull(Parcel.java:2379)
   	at android.os.Parcel.createException(Parcel.java:2357)
   	at android.os.Parcel.readException(Parcel.java:2340)
   	at android.os.Parcel.readException(Parcel.java:2282)
   	at android.app.IActivityManager$Stub$Proxy.broadcastIntentWithFeature(IActivityManager.java:5565)
   	at android.app.ContextImpl.sendBroadcast(ContextImpl.java:1115)
   	at android.permission2.cts.ProtectedBroadcastsTest.testSendProtectedBroadcasts(ProtectedBroadcastsTest.java:97)
   	at java.lang.reflect.Method.invoke(Native Method)
   	at junit.framework.TestCase.runTest(TestCase.java:168)
   	at junit.framework.TestCase.runBare(TestCase.java:134)
   	at junit.framework.TestResult$1.protect(TestResult.java:115)
   	at androidx.test.internal.runner.junit3.AndroidTestResult.runProtected(AndroidTestResult.java:73)
   	at junit.framework.TestResult.run(TestResult.java:118)
   	at androidx.test.internal.runner.junit3.AndroidTestResult.run(AndroidTestResult.java:51)
   	at junit.framework.TestCase.run(TestCase.java:124)
   	at androidx.test.internal.runner.junit3.NonLeakyTestSuite$NonLeakyTest.run(NonLeakyTestSuite.java:62)
   	at androidx.test.internal.runner.junit3.AndroidTestSuite$2.run(AndroidTestSuite.java:101)
   	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:462)
   	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
   	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1167)
   	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:641)
   	at java.lang.Thread.run(Thread.java:923)
   ```

2. 错误分析

   客户要求默认关闭 wifi，但是在开机向导中，开机向导应用会打开 wifi，导致开完机后，wifi 是打开状态的。为了达到默认关闭 wifi 效果，修改了 `frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java` 文件 `broadcastIntentLocked()` 方法的如下代码：

   ```java
   // Verify that protected broadcasts are only being sent by system code,
   // and that system code is only sending protected broadcasts.
   final boolean isProtectedBroadcast;
   try {
   isProtectedBroadcast = AppGlobals.getPackageManager().isProtectedBroadcast(action);
   } catch (RemoteException e) {
       Slog.w(TAG, "Remote exception", e);
       return ActivityManager.BROADCAST_SUCCESS;
   }
   
   // 添加代码开始位置
   if (intent != null && intent.getAction() != null && intent.getAction().equals(Intent.ACTION_PACKAGE_CHANGED)) { 
   	String data =intent.getDataString();
       if (data.endsWith("setupwizard")) {
           android.net.wifi.WifiManager mWifiManager =(android.net.wifi.WifiManager) mContext.getSystemService(Context.WIFI_SERVICE);
           int state =mWifiManager.getWifiState();	
           if(state == android.net.wifi.WifiManager.WIFI_STATE_ENABLED){
               mWifiManager.setWifiEnabled(false);
           }
       }
   }
   // 添加代码位置结束
   
   final boolean isCallerSystem;
   switch (UserHandle.getAppId(callingUid)) {
   ```
   
   在上面的修改中，没有对 data 变量进行判空操作，导致当 data 为 null 时报错。

3. 解决方法

   对上面代码中 data 变量进行判空操作即可：
   
   ```java
   // Verify that protected broadcasts are only being sent by system code,
   // and that system code is only sending protected broadcasts.
   final boolean isProtectedBroadcast;
   try {
   isProtectedBroadcast = AppGlobals.getPackageManager().isProtectedBroadcast(action);
   } catch (RemoteException e) {
   Slog.w(TAG, "Remote exception", e);
   return ActivityManager.BROADCAST_SUCCESS;
   }
   
   // 添加代码开始位置
   if (intent != null && intent.getAction() != null && intent.getAction().equals(Intent.ACTION_PACKAGE_CHANGED)) { 
   	String data =intent.getDataString();
       if (data != null && data.length() != 0) {
           if (data.endsWith("setupwizard")) {
               android.net.wifi.WifiManager mWifiManager =(android.net.wifi.WifiManager) mContext.getSystemService(Context.WIFI_SERVICE);
               int state =mWifiManager.getWifiState();	
               if(state == android.net.wifi.WifiManager.WIFI_STATE_ENABLED){
                   mWifiManager.setWifiEnabled(false);
               }
           }
       }
   }
   // 添加代码位置结束
   
   final boolean isCallerSystem;
   switch (UserHandle.getAppId(callingUid)) {
   ```
   
   