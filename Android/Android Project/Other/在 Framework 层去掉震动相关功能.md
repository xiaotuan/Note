[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 修改 `sys/frameworks/base/core/java/android/os/CombinedVibration.java` 文件中的如下代码：

   ```diff
   @@ -341,7 +341,10 @@ public abstract class CombinedVibration implements Parcelable {
            /** @hide */
            @Override
            public boolean hasVibrator(int vibratorId) {
   -            return true;
   +            // Remove vibration function {{&&
   +            // return true;
   +            return false;
   +            // &&}}
            }
    
            @Override
   @@ -473,7 +476,10 @@ public abstract class CombinedVibration implements Parcelable {
            /** @hide */
            @Override
            public boolean hasVibrator(int vibratorId) {
   -            return mEffects.indexOfKey(vibratorId) >= 0;
   +            // Remove vibration function {{&&
   +            // return mEffects.indexOfKey(vibratorId) >= 0;
   +            return false;
   +            // &&}}
            }
    
            @Override
   @@ -649,6 +655,11 @@ public abstract class CombinedVibration implements Parcelable {
            /** @hide */
            @Override
            public boolean hasVibrator(int vibratorId) {
   +            // Remove vibration function {{&&
   +            if (true) {
   +                return false;
   +            }
   +            // &&}}
                final int effectCount = mEffects.size();
                for (int i = 0; i < effectCount; i++) {
                    if (mEffects.get(i).hasVibrator(vibratorId)) {
   ```

2. 修改 `sys/frameworks/base/core/java/android/os/SystemVibrator.java` 文件中 `hasVibrator` 方法的如下代码：

   ```diff
   @@ -110,6 +110,11 @@ public class SystemVibrator extends Vibrator {
                Log.w(TAG, "Failed to check if vibrator exists; no vibrator manager.");
                return false;
            }
   +        // Remove vibration function {{&&
   +        if (true) {
   +            return false;
   +        }
   +        // &&}}
            return mVibratorManager.getVibratorIds().length > 0;
        }
    
   ```

3. 修改 `sys/frameworks/base/core/java/android/os/SystemVibratorManager.java` 文件中 `hasVibrator` 方法的如下代码：

   ```diff
   @@ -199,7 +199,10 @@ public class SystemVibratorManager extends VibratorManager {
    
            @Override
            public boolean hasVibrator() {
   -            return true;
   +            // Remove vibration function {{&&
   +            // return true;
   +            return false;
   +            // &&}}
            }
    
            @Override
   ```

4. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/res/values/strings.xml` 文件的如下代码：

   ```diff
   @@ -2836,7 +2836,7 @@
        <skip/>
        <string name="display_settings_title">Display</string>
        <!-- Sound and vibration settings screen heading. [CHAR LIMIT=30] -->
   -    <string name="sound_settings">Sound &amp; vibration</string>
   +    <string name="sound_settings">Sound</string>
        <!-- DO NOT TRANSLATE Summary placeholder -->
        <string name="summary_placeholder" translatable="false">&#160;</string>
        <!-- DO NOT TRANSLATE Summary placeholder reserving 2 lines -->
   @@ -8513,7 +8513,7 @@
        <string name="sound_settings_summary">Ring &amp; notification volume at <xliff:g id="percentage" example="2%">%1$s</xliff:g></string>
    
        <!-- Summary for sound settings, explaining a few important settings under it [CHAR LIMIT=NONE]-->
   -    <string name="sound_dashboard_summary">Volume, vibration, Do Not Disturb</string>
   +    <string name="sound_dashboard_summary">Volume, Do Not Disturb</string>
    
        <!-- Sound: Dashboard summary indicating the volume of ringtone when at 0% with vibrate enabled. [CHAR LIMIT=100] -->
        <string name="sound_settings_summary_vibrate">Ringer set to vibrate</string>
   @@ -8585,7 +8585,7 @@
        <string name="screen_locking_sounds_title">Screen locking sound</string>
    
        <!-- Sound: Other sounds: Title for the option enabling charging sounds and vibration. [CHAR LIMIT=50] -->
   -    <string name="charging_sounds_title">Charging sounds and vibration</string>
   +    <string name="charging_sounds_title">Charging sounds</string>
    
        <!-- Sound: Other sounds: Title for the option enabling docking sounds. [CHAR LIMIT=30] -->
        <string name="docking_sounds_title">Docking sounds</string>
   ```

5. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/notification/VibrateIconPreferenceController.java` 文件的如下代码：

   ```diff
   @@ -37,6 +37,6 @@ public class VibrateIconPreferenceController extends SettingPrefController {
    
        @Override
        public boolean isAvailable() {
   -        return true;
   +        return false;
        }
    }
   ```

   