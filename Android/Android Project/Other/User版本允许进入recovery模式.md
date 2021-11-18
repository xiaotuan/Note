[toc]

在 `User` 版本中按住音量加键，然后在按 Power 键就可以进入选择模式界面。在选择模式界面中选择 Recovery 模式后，系统重启后显示 No Command 界面，没有能进入 Recovery 模式。

### 1. MTK 平台

#### 1.1 MTK8766、Android R

1. 修改 `bootable/recovery/recovery.cpp` 文件中 `IsRoDebuggable()` 函数，使其返回 `true`。

   ```diff
   @@ -121,7 +121,7 @@ const char* reason = nullptr;
     */
    
    static bool IsRoDebuggable() {
   -  return android::base::GetBoolProperty("ro.debuggable", false);
   +  return true;//android::base::GetBoolProperty("ro.debuggable", false);
    }
    
    // Clear the recovery command and prepare to boot a (hopefully working) system,
   ```

2. 修改 `bootable/recovery/recovery_main.cpp` 文件中 `IsRoDebuggable()` 函数，使其返回 `true`。

   ```diff
   @@ -66,7 +66,7 @@ static constexpr const char* LOCALE_FILE = "/cache/recovery/last_locale";
    static RecoveryUI* ui = nullptr;
    
    static bool IsRoDebuggable() {
   -  return android::base::GetBoolProperty("ro.debuggable", false);
   +  return true;//android::base::GetBoolProperty("ro.debuggable", false);
    }
    
    static bool IsDeviceUnlocked() {
   ```

   

