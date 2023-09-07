[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `packages/apps/Launcher3/quickstep/src/com/android/launcher3/taskbar/TaskbarNavButtonController.java` 文件如下代码：

```diff
@@ -51,6 +51,11 @@ import java.io.PrintWriter;
 import java.lang.annotation.Retention;
 import java.lang.annotation.RetentionPolicy;
 
+// Add vibration effects to Home and Recent by qty {{&&
+import android.content.Context;
+import com.android.quickstep.util.VibratorWrapper;
+// &&}}
+
 /**
  * Controller for 3 button mode in the taskbar.
  * Handles all the functionality of the various buttons, making/routing the right calls into
@@ -65,6 +70,10 @@ public class TaskbarNavButtonController implements TaskbarControllers.LoggableTa
 
     private long mLastScreenPinLongPress;
     private boolean mScreenPinned;
+       
+       // Add vibration effects to Home and Recent by qty {{&&
+       private Context mContext;
+       // &&}}
 
     @Override
     public void dumpLogs(String prefix, PrintWriter pw) {
@@ -240,6 +249,9 @@ public class TaskbarNavButtonController implements TaskbarControllers.LoggableTa
 
     public void init(TaskbarControllers taskbarControllers) {
         mStatsLogManager = taskbarControllers.getTaskbarActivityContext().getStatsLogManager();
+               // Add vibration effects to Home and Recent by qty {{&&
+               mContext = taskbarControllers.getTaskbarActivityContext();
+               // &&}}
     }
 
     public void onDestroy() {
@@ -256,12 +268,22 @@ public class TaskbarNavButtonController implements TaskbarControllers.LoggableTa
 
     private void navigateHome() {
         mService.getOverviewCommandHelper().addCommand(OverviewCommandHelper.TYPE_HOME);
+               // Add vibration effects to Home and Recent by qty {{&&
+               if (mContext != null) {
+                       VibratorWrapper.INSTANCE.get(mContext).vibrate(VibratorWrapper.EFFECT_CLICK);
+               }
+               // &&}}
     }
 
     private void navigateToOverview() {
         if (mScreenPinned) {
             return;
         }
+               // Add vibration effects to Home and Recent by qty {{&&
+               if (mContext != null) {
+                       VibratorWrapper.INSTANCE.get(mContext).vibrate(VibratorWrapper.EFFECT_CLICK);
+               }
+        // &&}}
         TestLogging.recordEvent(TestProtocol.SEQUENCE_MAIN, "onOverviewToggle");
         TaskUtils.closeSystemWindowsAsync(CLOSE_SYSTEM_WINDOWS_REASON_RECENTS);
         mService.getOverviewCommandHelper().addCommand(OverviewCommandHelper.TYPE_TOGGLE);
```

