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

   