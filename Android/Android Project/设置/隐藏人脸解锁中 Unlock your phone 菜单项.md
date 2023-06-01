[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/biometrics/combination/BiometricSettingsKeyguardPreferenceController.java` 文件中 `getAvailabilityStatus()` 方法的如下代码：

   ```diff
   @@ -63,10 +63,15 @@ public class BiometricSettingsKeyguardPreferenceController extends TogglePrefere
    
        @Override
        public int getAvailabilityStatus() {
   +        // Hide the Unlock your phone menu by qty {{&&
   +        /*
            if (!Utils.isMultipleBiometricsSupported(mContext)) {
                return UNSUPPORTED_ON_DEVICE;
            }
            return getRestrictingAdmin() != null ? DISABLED_FOR_USER : AVAILABLE;
   +        */
   +        return DISABLED_FOR_USER;
   +        // &&}}
        }
    
        @Override
   ```

2. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/biometrics/face/FaceSettingsKeyguardPreferenceController.java` 文件中 `getAvailabilityStatus()` 方法的如下代码：

   ```diff
   @@ -71,7 +71,10 @@ public class FaceSettingsKeyguardPreferenceController extends FaceSettingsPrefer
        @Override
        public int getAvailabilityStatus() {
            // When the device supports multiple biometrics auth, this preference will be unavailable.
   -        return Utils.isMultipleBiometricsSupported(mContext) ? UNSUPPORTED_ON_DEVICE : AVAILABLE;
   +        // Hide the Unlock your phone menu by qty {{&&
   +        // return Utils.isMultipleBiometricsSupported(mContext) ? UNSUPPORTED_ON_DEVICE : AVAILABLE;
   +        return UNSUPPORTED_ON_DEVICE;
   +        // &&}}
        }
    
        @Override
   ```

