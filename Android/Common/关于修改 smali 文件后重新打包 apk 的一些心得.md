1. 添加代码

   在 `smali` 文件中添加代码需要注意的是，不能重新定义新的变量名，但是可以使用已有的变量名，例如：

   ```
   .line 162
       invoke-virtual {p0}, Lkr/hwangti/batterylog/ui/MenuFragment;->getActivity()Landroid/support/v4/app/FragmentActivity;
   
       move-result-object v0
   
       new-instance v1, Landroid/content/Intent;
   
       const-string v2, "kr.hwangti.batterylog.BatteryLogService"
   
       invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V
   
       invoke-virtual {v0, v1}, Landroid/support/v4/app/FragmentActivity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;
   ```

   如果需要再上面添加代码，例如给 v1 Intent 对象设置包名，修改代码如下：

   ```
   .line 162
       invoke-virtual {p0}, Lkr/hwangti/batterylog/ui/MenuFragment;->getActivity()Landroid/support/v4/app/FragmentActivity;
   
       move-result-object v0
   
       new-instance v1, Landroid/content/Intent;
   
       const-string v2, "kr.hwangti.batterylog.BatteryLogService"
   
       invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V
       
       const-string v2, "kr.hwangti.batterylog"
       
       invoke-virtual {v1, v2}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;
   
       invoke-virtual {v0, v1}, Landroid/support/v4/app/FragmentActivity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;
   ```

   原先我通过定义一个 v3 变量来实现：

   ```
   .line 162
       invoke-virtual {p0}, Lkr/hwangti/batterylog/ui/MenuFragment;->getActivity()Landroid/support/v4/app/FragmentActivity;
   
       move-result-object v0
   
       new-instance v1, Landroid/content/Intent;
   
       const-string v2, "kr.hwangti.batterylog.BatteryLogService"
   
       invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V
       
       const-string v2, "kr.hwangti.batterylog"
       
       invoke-virtual {v1, v3}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;
   
       invoke-virtual {v0, v1}, Landroid/support/v4/app/FragmentActivity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;
   ```

   重新打包后安装 apk 运行报如下错误：

   ```
   11-24 05:38:37.115 23048 23048 E AndroidRuntime: FATAL EXCEPTION: main
   11-24 05:38:37.115 23048 23048 E AndroidRuntime: Process: kr.hwangti.batterylog, PID: 23048
   11-24 05:38:37.115 23048 23048 E AndroidRuntime: java.lang.VerifyError: Verifier rejected class kr.hwangti.batterylog.ui.MenuFragment: void kr.hwangti.batterylog.ui.MenuFragment.onClick(android.view.View) failed to verify: void kr.hwangti.batterylog.ui.MenuFragment.onClick(android.view.View): [0x3E] 'this' argument 'Precise Reference: java.lang.String' not instance of 'Reference: android.support.v4.app.Fragment' (declaration of 'kr.hwangti.batterylog.ui.MenuFragment' appears in /data/app/~~zTOk1o6t5Jp5O_bqNF_8-Q==/kr.hwangti.batterylog-cAAckvFhm_sd_d65wa-7jg==/base.apk)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at java.lang.Class.newInstance(Native Method)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.support.v4.app.Fragment.instantiate(Fragment.java:402)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.support.v4.app.Fragment.instantiate(Fragment.java:377)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.support.v4.app.FragmentActivity.onCreateView(FragmentActivity.java:283)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.tryCreateView(LayoutInflater.java:1085)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.createViewFromTag(LayoutInflater.java:1009)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.createViewFromTag(LayoutInflater.java:973)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.rInflate(LayoutInflater.java:1152)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.rInflateChildren(LayoutInflater.java:1113)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.inflate(LayoutInflater.java:694)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.inflate(LayoutInflater.java:538)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.view.LayoutInflater.inflate(LayoutInflater.java:485)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at com.android.internal.policy.PhoneWindow.setContentView(PhoneWindow.java:475)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.Activity.setContentView(Activity.java:3679)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at kr.hwangti.batterylog.MainActivity.onCreate(MainActivity.java:25)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.Activity.performCreate(Activity.java:8595)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.Activity.performCreate(Activity.java:8573)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1456)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:3805)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3963)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.servertransaction.LaunchActivityItem.execute(LaunchActivityItem.java:103)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.servertransaction.TransactionExecutor.executeCallbacks(TransactionExecutor.java:139)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.servertransaction.TransactionExecutor.execute(TransactionExecutor.java:96)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.ActivityThread$H.handleMessage(ActivityThread.java:2484)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.os.Handler.dispatchMessage(Handler.java:106)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.os.Looper.loopOnce(Looper.java:205)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.os.Looper.loop(Looper.java:294)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at android.app.ActivityThread.main(ActivityThread.java:8225)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at java.lang.reflect.Method.invoke(Native Method)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:573)
   11-24 05:38:37.115 23048 23048 E AndroidRuntime:        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1049)
   11-24 05:40:44.452 23399 23399 D AndroidRuntime: Shutting down VM
   ```

   