[toc]

### 1. 发送错误代码

```java
public synchronized void checkAccess(LicenseCheckerCallback callback) {
    // If we have a valid recent LICENSED response, we can skip asking
    // Market.
    if (mPolicy.allowAccess()) {
        Log.i(TAG, "Using cached license response");
        callback.allow(Policy.LICENSED);
    } else {
        LicenseValidator validator = new LicenseValidator(mPolicy, new NullDeviceLimiter(),
                                                          callback, generateNonce(), mPackageName, mVersionCode);

        if (mService == null) {
            Log.i(TAG, "Binding to licensing service.");
            try {
                boolean bindResult = mContext
                    .bindService(
                    new Intent(
                        new String(
                            Base64.decode("Y29tLmFuZHJvaWQudmVuZGluZy5saWNlbnNpbmcuSUxpY2Vuc2luZ1NlcnZpY2U="))),	// 该行报错
                    this, // ServiceConnection.
                    Context.BIND_AUTO_CREATE);

                if (bindResult) {
                    mPendingChecks.offer(validator);
                } else {
                    Log.e(TAG, "Could not bind to service.");
                    handleServiceConnectionError(validator);
                }
            } catch (SecurityException e) {
                callback.applicationError(LicenseCheckerCallback.ERROR_MISSING_PERMISSION);
            } catch (Base64DecoderException e) {
                e.printStackTrace();
            }
        } else {
            mPendingChecks.offer(validator);
            runChecks();
        }
    }
}
```

### 2. 报错信息

```
2021-11-19 16:59:48.311 10363-10363/net.zenconsult.android.chucknorris E/AndroidRuntime: FATAL EXCEPTION: main
    Process: net.zenconsult.android.chucknorris, PID: 10363
    java.lang.IllegalArgumentException: Service Intent must be explicit: Intent { act=com.android.vending.licensing.ILicensingService }
        at android.app.ContextImpl.validateServiceIntent(ContextImpl.java:1531)
        at android.app.ContextImpl.bindServiceCommon(ContextImpl.java:1675)
        at android.app.ContextImpl.bindService(ContextImpl.java:1624)
        at android.content.ContextWrapper.bindService(ContextWrapper.java:698)
        at com.google.android.vending.licensing.LicenseChecker.checkAccess(LicenseChecker.java:150)
        at net.zenconsult.android.chucknorris.ChuckNorrisFactsActivity$1.onClick(ChuckNorrisFactsActivity.java:71)
        at android.view.View.performClick(View.java:6608)
        at com.google.android.material.button.MaterialButton.performClick(MaterialButton.java:992)
        at android.view.View.performClickInternal(View.java:6585)
        at android.view.View.access$3100(View.java:782)
        at android.view.View$PerformClick.run(View.java:25945)
        at android.os.Handler.handleCallback(Handler.java:874)
        at android.os.Handler.dispatchMessage(Handler.java:100)
        at android.os.Looper.loop(Looper.java:198)
        at android.app.ActivityThread.main(ActivityThread.java:6729)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:493)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:858)
```

### 3. 解决方法

跟了一下源码，发现在ContextImpl中有如下的判断：

```java
@Override
public boolean bindService(Intent service, ServiceConnection conn,
            int flags) {
    warnIfCallingFromSystemProcess();
    return bindServiceCommon(service, conn, flags, mMainThread.getHandler(),
            Process.myUserHandle());
}
private boolean bindServiceCommon(Intent service, ServiceConnection conn, int flags, Handler
            handler, UserHandle user) {
    ...
    validateServiceIntent(service);
    ...
}

private void validateServiceIntent(Intent service) {
    if (service.getComponent() == null && service.getPackage() == null) {
        if (getApplicationInfo().targetSdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
            IllegalArgumentException ex = new IllegalArgumentException(
                        "Service Intent must be explicit: " + service);
            throw ex;
        } else {
            Log.w(TAG, "Implicit intents with startService are not safe: " + service
                    + " " + Debug.getCallers(2, 3));
        }
    }
}
```

由此可见，在Android5.0中增加了对intent的判断，因为intent是通过设置action得到的，因此没有Component对象的实例，也没有包名，故而报错。原因找到，增加了一个设置包名的步骤，而且需要是App的包名，而不是Service类所在包的包名，即可顺利解决，代码如下：

```java
 boolean bindResult = mContext
                    .bindService(
                    new Intent(
                        new String(
                            Base64.decode("Y29tLmFuZHJvaWQudmVuZGluZy5saWNlbnNpbmcuSUxpY2Vuc2luZ1NlcnZpY2U=")))
     				.setPackage("com.android.vending"),
                    this, // ServiceConnection.
                    Context.BIND_AUTO_CREATE);
```

