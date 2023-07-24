[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

1. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/res/xml/firmware_version.xml` 文件的如下代码：

   ```diff
   @@ -59,7 +59,6 @@
            android:key="kernel_version"
            android:title="@string/kernel_version"
            android:summary="@string/summary_placeholder"
   -        android:selectable="false"
            settings:enableCopying="true"
            settings:controller="com.android.settings.deviceinfo.firmwareversion.KernelVersionPreferenceController"/>
    
   ```

2. 修改 `sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/deviceinfo/firmwareversion/KernelVersionPreferenceController.java` 文件的如下代码：

   ```diff
   @@ -18,11 +18,24 @@ package com.android.settings.deviceinfo.firmwareversion;
    
    import android.content.Context;
    
   +import androidx.preference.Preference;
    import com.android.settings.core.BasePreferenceController;
    import com.android.settingslib.DeviceInfoUtils;
    
   -public class KernelVersionPreferenceController extends BasePreferenceController {
   +import android.app.Activity;
   +import android.content.Intent;
   +import android.text.TextUtils;
   +import com.android.settingslib.core.lifecycle.Lifecycle;
   +import com.android.settingslib.core.lifecycle.LifecycleObserver;
   +import com.android.settingslib.core.lifecycle.events.OnResume;
   +import com.android.settings.core.PreferenceControllerMixin;
    
   +public class KernelVersionPreferenceController extends BasePreferenceController implements
   +        PreferenceControllerMixin, LifecycleObserver, OnResume {
   +
   +    private static final String KEY_KERNEL_VERSION = "kernel_version";
   +
   +    private int mHitCountdown;
        public KernelVersionPreferenceController(Context context, String preferenceKey) {
            super(context, preferenceKey);
        }
   @@ -36,4 +49,33 @@ public class KernelVersionPreferenceController extends BasePreferenceController
        public CharSequence getSummary() {
            return DeviceInfoUtils.getFormattedKernelVersion(mContext);
        }
   +
   +    @Override
   +    public String getPreferenceKey() {
   +        return KEY_KERNEL_VERSION;
   +    }
   +
   +    @Override
   +    public void onResume() {
   +        android.util.Log.d("qty", "onResume()...");
   +        mHitCountdown = 5;
   +    }
   +
   +    @Override
   +    public boolean handlePreferenceTreeClick(Preference preference) {
   +        android.util.Log.d("qty", "handlePreferenceTreeClick=>key: " + preference.getKey() + ", count: " + mHitCountdown);
   +        if (!TextUtils.equals(preference.getKey(), KEY_KERNEL_VERSION)) {
   +            return false;
   +        }
   +        if(mHitCountdown > 0){
   +            mHitCountdown--;
   +        }else{
   +            Intent intent = new Intent("android.intent.action.MAIN");
   +            intent.setClassName("com.weibu.factorytest","com.weibu.factorytest.FactoryTest");
   +            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
   +            mContext.startActivity(intent);
   +        }
   +        return true;
   +    }
   +
    }
   ```

   