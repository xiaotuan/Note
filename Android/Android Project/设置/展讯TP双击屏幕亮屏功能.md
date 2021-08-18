

[toc]

### 1. 展讯平台

> 提示：修改位置：`设置应用 -> 智能控制 -> 黑屏唤醒`，将原先使用重力传感器实现的双击亮屏修改为由 TP 实现的双击亮屏。

1. 修改 `packages/apps/Settings/src_unisoc/com/unisoc/settings/smartcontrols/SmartWakePreferenceController.java` 文件，将原先的开关改为控制 TP 双击亮屏功能的开关。

   1. 导入类

      ```java
      import android.util.Log;
      import java.io.File;
      import java.io.FileOutputStream;
      import java.io.FileInputStream;
      ```

   2. 添加变量

      ```java
      private static final String TAG = "SmartWakePreferenceController";
      public static final String WAKE_GESTURE_ENABLED = "double_tap_wakeup";
      private static final String SMART_WAKE_PATH = "sys/sileadinc/tpgesture_func";
      ```

   3. 修改 `displayPreference()` 方法，将原先的代码修改成如下代码：

      ```java
      @Override
      public void displayPreference(PreferenceScreen screen) {
          super.displayPreference(screen);
          if (isAvailable()) {
              mSmartWakePreference = (SmartSwitchPreference) screen.findPreference(KEY_SMART_WAKE);
      
              mSmartWakePreference.setOnViewClickedListener(new OnViewClickedListener() {
                  @Override
                  public void OnViewClicked(View v) {
                      int setting = Settings.Secure.getInt(mContext.getContentResolver(),
                                                           WAKE_GESTURE_ENABLED, 0);
                      setSmartWakeup(setting == 0 ? 1 : 0);
                      Settings.Secure.putInt(mContext.getContentResolver(), WAKE_GESTURE_ENABLED, setting == 0 ? 1 : 0);
                      updateState(null);
                  }
      
              });
      
              mSmartWakePreference.setOnPreferenceSwitchCheckedListener(new OnPreferenceSwitchChangeListener() {
                  @Override
                  public void onPreferenceSwitchChanged(boolean checked) {
                      setSmartWakeup(checked ? 1 : 0);
                      Settings.Secure.putInt(mContext.getContentResolver(), WAKE_GESTURE_ENABLED, checked ? 1 : 0);
                  }
              });
          }
      }
      ```

   4. 添加如下方法

      ```java
      // 0: closed, 1: opened
      public static void setSmartWakeup(int value) {
          Log.d(TAG, "setSmartWakeup=>value " + value);
          if (value != 0 && value != 1) {
              Log.e(TAG, "setSmartWakeup=>Value must be 0 or 1.");
              return;
          }
          File file = new File(SMART_WAKE_PATH);
          FileOutputStream fos = null;
          try {
              fos = new FileOutputStream(file);
              fos.write(value);
              fos.flush();
          } catch (Exception e) {
              Log.e(TAG, "setSmartWakeup=>error: ", e);
          } finally {
              if (fos != null) {
                  try { fos.close(); } catch (Exception ignore) {}
                  fos = null;
              }
          }
      }
      
      public static boolean isSmartWakeOpened() {
          boolean result = false;
          File file = new File(SMART_WAKE_PATH);
          FileInputStream fis = null;
          try {
              fis = new FileInputStream(file);
              int value = fis.read();
              Log.d(TAG, "isSmartWakeOpened=>value: " + value);
              result = (value == 1);
          } catch (Exception e) {
              Log.e(TAG, "isSmartWakeOpened=>error: ", e);
          } finally {
              if (fis != null) {
                  try { fis.close(); } catch (Exception ignore) {}
              }
              fis = null;
          }
          return result;
      }
      ```

2. 修改 `frameworks/base/services/core/java/com/android/server/policy/PhoneWindowManager.java` 文件

   1. 导入类

      ```java
      import java.io.FileOutputStream;
      import java.io.FileInputStream;
      ```

   2. 在 `screenTurnedOn()` 方法中添加如下代码：

      ```java
      int setting = Settings.Secure.getIntForUser(mContext.getContentResolver(), "double_tap_wakeup", 0, mCurrentUserId);
      setSmartWakeup(setting);
      ```

   3. 在 `systemReady()` 方法中添加如下代码：

      ```java
      if (isScreenOn()) {
          int setting = Settings.Secure.getIntForUser(mContext.getContentResolver(), "double_tap_wakeup", 0, mCurrentUserId);
          setSmartWakeup(setting);
      }
      ```

   4. 添加如下方法

      ```java
      // 0: closed, 1: opened
      public void setSmartWakeup(int value) {
          Log.d(TAG, "setSmartWakeup=>value " + value);
          if (value != 0 && value != 1) {
              Log.e(TAG, "setSmartWakeup=>Value must be 0 or 1.");
              return;
          }
          File file = new File("sys/sileadinc/tpgesture_func");
          FileOutputStream fos = null;
          try {
              fos = new FileOutputStream(file);
              fos.write(value);
              fos.flush();
          } catch (Exception e) {
              Log.e(TAG, "setSmartWakeup=>error: ", e);
          } finally {
              if (fos != null) {
                  try { fos.close(); } catch (Exception ignore) {}
                  fos = null;
              }
          }
      }
      ```

      

