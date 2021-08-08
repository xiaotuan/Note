[toc]

> 注意：下面的修改是基于展讯 SC9863A 芯片、Android R 版本进行修改的。

### 1. 修改展讯代码

1.1 请确保 `prebuilts/sdk/30/unisoc/aip/` 目录下的 `current.txt` 和 `unisoc-hidden-current.txt` 文件内容与 `frameworks/base/api/` 目录下的  `current.txt` 和 `unisoc-hidden-current.txt` 文件内容保持一致。

1.2 修改 `bsp/kernel/kernel4.14/sprd-diffconfig/androidr/sharkl3/arm/go_google_diff_config` 文件，将文件中 `ADD:CONFIG_DM_ANDROID_VERITY_AT_MOST_ONCE_DEFAULT_ENABLED` 行删除掉，如果文件中只有这一行有效，则必须将该文件直接删除掉，否则编译可能会报错。

> 注意：只有在使用 target 包做差分包时才需要执行这一步。

1.3 修改 `packages/apps/Settings/src_unisoc/com/android/settings/deviceinfo/LocalSystemUpdatePreferenceController.java` 文件，将所有 Dialog 都添加禁止点击屏幕外隐藏设置：

```java
dialog.setCancelable(false);
dialog.setCanceledOnTouchOutside(false);
```

最终代码如下所示：

```java
package com.android.settings.deviceinfo;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.res.Resources;
import android.os.AsyncTask;
import android.os.Environment;
import android.os.EnvironmentEx;
import android.os.Handler;
import android.os.PowerManager;
import android.os.RecoverySystem;
import android.os.SystemProperties;
import android.os.UpdateEngine;
import android.os.UpdateEngineCallback;
import android.os.UserHandle;
import android.provider.Settings;
import android.util.Log;
import android.view.WindowManager;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.preference.DialogPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceScreen;
import com.android.internal.util.Preconditions;
import com.android.settings.R;
import com.android.settings.core.PreferenceControllerMixin;
import com.android.settingslib.Utils;
import com.android.settingslib.core.lifecycle.Lifecycle;
import com.android.settingslib.core.lifecycle.LifecycleObserver;
import com.android.settingslib.core.lifecycle.events.OnDestroy;
import com.android.settingslib.core.AbstractPreferenceController;

import java.util.ArrayList;
import java.util.List;
import java.io.File;
import java.io.IOException;

public class LocalSystemUpdatePreferenceController extends AbstractPreferenceController
            implements PreferenceControllerMixin, LifecycleObserver {
    private static final String TAG = "LocalSystemUpdate";
    private static final String KEY_RECOVERY_SYSTEM_UPDATE = "RecoverySystemUpdate";
    private static final String UPDATE_FILE_PATH = "/update.zip";
    private static final String INTERNAL_STORAGE_PHY_PATH = "data/media/0";
    private static final String INTERNAL_STORAGE_MOUNT_PATH = "storage/emulated/0";
    private static final String OTA_PACKAGE_PATH = "data/ota_package";
    private static final String REBOOT_REASON = "reboot-ab-update";
    private static final String DATABASE_KEY_INSTALL_IN_PROGRESS = "install_in_progress";
    private static final String ERROR_NEED_REBOOT = "An update already applied, waiting for reboot";
    private static final int MINIMUM_LEVEL_POWER = 35;
    private static final boolean SD_UDPATE_SUPPORTED = true;

    private final UpdateEngine mUpdateEngine = new UpdateEngine();
    private final OtaUpdateEngineCallback mOtaUpdateEngineCallback = new OtaUpdateEngineCallback();
    // Add for bug1413281， support Non-A/B feature
    private final boolean mIsVirtualAbSupported = SystemProperties.getBoolean("ro.build.ab_update", false);

    private boolean mInternalUpdateFileExist = false;
    private boolean mSdUpdateFileExist = false;
    private boolean mOtaUpdateFileExist = false;
    private int mUserChoice = 0;

    private List<File> mUpdateItems = new ArrayList<File>();
    private PowerManager mPowerManager;
    private ProgressDialog mProgressDialog;
    private boolean mInstallationInProgress = false;

    private DialogInterface.OnClickListener mDialogClickListener = new DialogInterface.OnClickListener() {
        public void onClick(DialogInterface arg0, int arg1) {
            checkUpdatePackage();
        }
    };

    public LocalSystemUpdatePreferenceController(Context context) {
        super(context);
        mPowerManager = (PowerManager) mContext.getSystemService(Context.POWER_SERVICE);
        mInstallationInProgress = Settings.Global.getInt(mContext.getContentResolver(),
                DATABASE_KEY_INSTALL_IN_PROGRESS, 0) == 1;
    }

    public void checkUpdatePackage() {
        Log.d(TAG, "mIsVirtualAbSupported:" + mIsVirtualAbSupported);
        mUpdateItems.clear();
        checkInteralStorage();
         // Add for bug1413281， support Non-A/B feature
        if (mIsVirtualAbSupported) {
            checkOtaPackage();
        }
        if (SD_UDPATE_SUPPORTED) {
            checkExternalStorage();
        }
        showOperateDialog();
    }

    public void showOperateDialog() {
        final String [] items = mContext.getResources().getStringArray(R.array.update_choice);
        boolean internalFlag = false;
        boolean sdFlag = false;
        if (mUpdateItems.size() == 3) {
            showSingleChoiceDialog(items);
        } else if (mUpdateItems.size() > 0) {
            int size = mUpdateItems.size();
            String [] item_temp = new String[size];
            for (int i = 0; i < size; i++) {
                if (mInternalUpdateFileExist && !internalFlag) {
                    item_temp[i] = items[0];
                    internalFlag = true;
                    continue;
                }
                if (mSdUpdateFileExist && !sdFlag) {
                    item_temp[i] = items[1];
                    sdFlag = true;
                    continue;
                }
                if (mOtaUpdateFileExist) {
                    item_temp[i] = items[2];
                    continue;
                }
            }
            showSingleChoiceDialog(item_temp);
        } else {
            if (SD_UDPATE_SUPPORTED) {
                Toast.makeText(mContext, R.string.recovery_no_update_package, Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(mContext, R.string.recovery_no_update_package_internal_only, Toast.LENGTH_LONG).show();
            }
        }
    }

    public void checkOtaPackage() {
        // update.zip path: data/ota_package
        mOtaUpdateFileExist = false;
        File otaFile = new File(OTA_PACKAGE_PATH + UPDATE_FILE_PATH);
        if (otaFile.exists()) {
            mOtaUpdateFileExist = true;
            mUpdateItems.add(otaFile);
        }
    }

    public void checkInteralStorage() {
        // Ota does not recognize the internal storage mount path
        // "storage/emulated/0", only the physical path"data/media/0" is recognized.
        mInternalUpdateFileExist = false;
        File checkFile = new File(INTERNAL_STORAGE_MOUNT_PATH + UPDATE_FILE_PATH);
        File internalFile = new File(INTERNAL_STORAGE_PHY_PATH + UPDATE_FILE_PATH);
        if (checkFile.exists()) {
            mInternalUpdateFileExist = true;
            if (mIsVirtualAbSupported) {
                mUpdateItems.add(checkFile);
            } else {
                mUpdateItems.add(internalFile);
            }
        }
    }

    public void checkExternalStorage() {
        //external sdcard
        mSdUpdateFileExist = false;
        String storageState = EnvironmentEx.getExternalStoragePathState();
        String storageDirectory = EnvironmentEx.getExternalStoragePath().getAbsolutePath();
        if (storageState.equals(Environment.MEDIA_MOUNTED)) {
            File file = new File(storageDirectory + UPDATE_FILE_PATH);
            if (file.exists()) {
                mSdUpdateFileExist = true;
                mUpdateItems.add(file);
            }
        }
    }

    @Override
    public boolean handlePreferenceTreeClick(Preference preference) {
        int messageId = SD_UDPATE_SUPPORTED ? R.string.recovery_update_message : R.string.recovery_update_message_internal_only;
        if (getPreferenceKey().equals(preference.getKey())) {
            AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
            builder.setMessage(mContext.getResources().getString(messageId));
            builder.setPositiveButton(android.R.string.ok, mDialogClickListener);
            builder.setNegativeButton(android.R.string.cancel, null);
            AlertDialog dialog = builder.create();
            dialog.setCancelable(false);
            dialog.setCanceledOnTouchOutside(false);
            dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
            dialog.show();
            return true;
        }
        return super.handlePreferenceTreeClick(preference);
    }

    @Override
    public boolean isAvailable() {
        return mContext.getResources().getBoolean(R.bool.config_support_otaupdate)
                && isAdminUser();
    }

    @Override
    public String getPreferenceKey() {
        return KEY_RECOVERY_SYSTEM_UPDATE;
    }

    @Override
    public void displayPreference(PreferenceScreen screen) {
        super.displayPreference(screen);
        if (isAvailable()) {
            final Preference preference = initLocalSystemUpdatePreference();
            screen.addPreference(preference);
        }
    }

    public boolean isLowBatteryLevel() {
        Intent batteryBroadcast = mContext.registerReceiver(null,
                new IntentFilter(Intent.ACTION_BATTERY_CHANGED));
        final int batteryLevel = Utils.getBatteryLevel(batteryBroadcast);
        return batteryLevel < MINIMUM_LEVEL_POWER;
    }

    public boolean isAdminUser() {
        return UserHandle.myUserId() == UserHandle.USER_OWNER;
    }

    public Preference initLocalSystemUpdatePreference() {
        Preference preference = new Preference (mContext);
        preference.setTitle(R.string.recovery_update_title);
        preference.setKey(KEY_RECOVERY_SYSTEM_UPDATE);
        preference.setOrder(0);
        return preference;
    }

    public void showSingleChoiceDialog(String [] items) {
        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
        builder.setSingleChoiceItems(items, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                mUserChoice = which;
            }
        });
        builder.setTitle(R.string.choice_dialog_title);
        builder.setPositiveButton(R.string.update_choice_dialog_ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                File file = mUpdateItems.get(mUserChoice);
                if (mIsVirtualAbSupported) {
                    startVirtualAbUpdateProgress(file);
                } else {
                    startNormalUpdateProgress(items[mUserChoice], file);
                }
            }
        });
        AlertDialog dialog = builder.create();
        dialog.setCancelable(false);
        dialog.setCanceledOnTouchOutside(false);
        dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
        dialog.show();
    }

    /** ------------------------------------------------Normal Ota Update Progress start ------------------------------------------------------------ */
    /**  Add for bug1413281， support Non-A/B feature start @{ */
    public void startNormalUpdateProgress(String message, File file) {
        if (mUserChoice >= 0) {
            Toast.makeText(mContext, message, Toast.LENGTH_SHORT).show();
            tryToRecoverySystem(file);
        }
    }

    public void tryToRecoverySystem(File file) {
        if (isLowBatteryLevel()) {
            Toast.makeText(mContext, R.string.recovery_update_level, Toast.LENGTH_LONG).show();
        } else {
            try {
                RecoverySystem.installPackage(mContext, file);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    /** @} */
    /** ------------------------------------------------Normal Ota Update Progress end -------------------------------------------------------------- */


    /** ------------------------------------------------VAB Ota Update Progress start --------------------------------------------------------------- */
    public void startVirtualAbUpdateProgress(File file) {
        if (mInstallationInProgress) {
            showInstallationInProgress();
        } else if (mUserChoice >= 0) {
            try {
                new UpdateVerifier().execute(file);
            } catch (Exception ex) {
                Log.e(TAG, ex.getMessage());
                Toast.makeText(mContext, R.string.recovery_update_package_verify_failed, Toast.LENGTH_SHORT).show();
            }
        }
    }

    private void showInstallationInProgress() {
        mInstallationInProgress = true;
        showStatus(R.string.recovery_update_package_install_title, R.string.recovery_update_package_download_in_progress);
        mUpdateEngine.bind(mOtaUpdateEngineCallback, new Handler(mContext.getMainLooper()));
    }

    private void showStatus(int titleId, int messageId) {
        if (mProgressDialog != null && mProgressDialog.isShowing()) {
            mProgressDialog.setTitle(titleId);
            mProgressDialog.setMessage(mContext.getResources().getString(messageId));
        } else {
            mProgressDialog = getProgressDialog();
            mProgressDialog.setTitle(titleId);
            mProgressDialog.setMessage(mContext.getResources().getString(messageId));
            mProgressDialog.setCancelable(false);
            mProgressDialog.setCanceledOnTouchOutside(false);
            mProgressDialog.show();
        }
    }

    private ProgressDialog getProgressDialog() {
        ProgressDialog progressDialog = new ProgressDialog(mContext);
        progressDialog.setIndeterminate(true);
        return progressDialog;
    }

    private void dismissProgressDialog() {
        if (mProgressDialog != null && mProgressDialog.isShowing()) {
            // Add for bug1413124,Avoid the exception of dissmiss dialog when the context has been recycled.
            try {
                mProgressDialog.dismiss();
            } catch (Exception ex) {
                Log.e(TAG, ex.getMessage());
            } finally {
                mProgressDialog = null;
            }
        }
    }

    /** Ota upgrade is complete, pop up the dialog to confirm whether to restart the phone immediately */
    public void showConfirmRebootDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
        builder.setTitle(mContext.getResources().getString(R.string.recovery_update_package_install_title));
        builder.setMessage(mContext.getResources().getString(R.string.recovery_update_rebooting));
        builder.setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                rebootNow();
            }
        });
        builder.setNegativeButton(android.R.string.cancel, null);
        AlertDialog dialog = builder.create();
        dialog.setCancelable(false);
        dialog.setCanceledOnTouchOutside(false);
        dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
        dialog.show();
    }

    /** A dialog pops up to confirm whether to upgrade */
    public void showConfirmInstallDialog(final UpdateParser.ParsedUpdate parsedUpdate) {
        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
        builder.setTitle(mContext.getResources().getString(R.string.recovery_update_package_install_title));
        builder.setMessage(mContext.getResources().getString(R.string.recovery_update_install_ready));
        builder.setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                showInstallationInProgress();
                Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 1);
                installUpdate(parsedUpdate);
            }
        });
        builder.setNegativeButton(android.R.string.cancel, null);
        AlertDialog dialog = builder.create();
        dialog.setCancelable(false);
        dialog.setCanceledOnTouchOutside(false);
        dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
        dialog.show();
    }

    /** Send ota package data to updateEngine for upgrade */
    private void installUpdate(UpdateParser.ParsedUpdate parsedUpdate) {
        Log.d(TAG, "mUrl:" + parsedUpdate.mUrl + ",mOffset:" + parsedUpdate.mOffset
                + ",mSize:" + parsedUpdate.mSize + ",mProps:" + parsedUpdate.mProps);
        try {
            mUpdateEngine.applyPayload(
                    parsedUpdate.mUrl, parsedUpdate.mOffset, parsedUpdate.mSize, parsedUpdate.mProps);
        } catch (Exception ex) {
            mInstallationInProgress = false;
            Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 0);
            //Modify for bug1420894, no need to show toast if update succeed
            String message = ex.getMessage();
            Log.e(TAG, message);
            if (!ERROR_NEED_REBOOT.equals(message)) {
                Toast.makeText(mContext, R.string.recovery_update_package_install_failed, Toast.LENGTH_SHORT).show();
            }
        }
    }

    /** Reboot the system. */
    private void rebootNow() {
        Log.i(TAG, "Rebooting Now.");
        mPowerManager.reboot(REBOOT_REASON);
    }

    /** Handle events from the UpdateEngine. */
    public class OtaUpdateEngineCallback extends UpdateEngineCallback {
        @Override
        public void onStatusUpdate(int status, float percent) {
            switch (status) {
                case UpdateEngine.UpdateStatusConstants.UPDATED_NEED_REBOOT:
                    mInstallationInProgress = false;
                    Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 0);
                    dismissProgressDialog();
                    Log.d(TAG, "Before show reboot dialog");
                    showConfirmRebootDialog();
                    break;
                case UpdateEngine.UpdateStatusConstants.DOWNLOADING:
                    Log.d(TAG, "downloading progress:" + ((int) (percent * 100) + "%"));
                    if (mProgressDialog != null && mProgressDialog.isShowing()) {
                        String message = mContext.getResources().getString(R.string.recovery_update_package_download_in_progress);
                        String progessMessage = message + ((int) (percent * 100) + "%");
                        mProgressDialog.setMessage(progessMessage);
                    }
                    break;
                // Add install progress display for bug1397771
                case UpdateEngine.UpdateStatusConstants.FINALIZING:
                    Log.d(TAG, "finalizing progress:" + ((int) (percent * 100) + "%"));
                    if (mProgressDialog != null && mProgressDialog.isShowing()) {
                        String message = mContext.getResources().getString(R.string.recovery_update_package_install_in_progress);
                        String progessMessage = message + ((int) (percent * 100) + "%");
                        mProgressDialog.setMessage(progessMessage);
                    }
                default:
                    // do nothing
            }
        }

        @Override
        public void onPayloadApplicationComplete(int errorCode) {
            mInstallationInProgress = false;
            Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 0);
            dismissProgressDialog();
            Log.w(TAG, String.format("onPayloadApplicationComplete %d", errorCode));
            int messageId = (errorCode == UpdateEngine.ErrorCodeConstants.SUCCESS) ? R.string.recovery_update_package_install_success : R.string.recovery_update_package_install_failed;
            Toast.makeText(mContext, messageId, Toast.LENGTH_SHORT).show();
        }
    }

    /** Verify the validity of the ota upgrade package */
    private class UpdateVerifier extends AsyncTask<File, Void, UpdateParser.ParsedUpdate> {
        @Override
        protected UpdateParser.ParsedUpdate doInBackground(File... files) {
            Preconditions.checkArgument(files.length > 0, "No file specified");
            File file = files[0];
            try {
                return UpdateParser.parse(file);
            } catch (IOException e) {
                Log.e(TAG, String.format("For file %s", file), e);
                return null;
            }
        }

        @Override
        protected void onPostExecute(UpdateParser.ParsedUpdate result) {
            if (result == null) {
                Toast.makeText(mContext, R.string.recovery_update_package_verify_failed, Toast.LENGTH_SHORT).show();
                Log.e(TAG, String.format("Failed verification %s", result));
                return;
            }
            if (!result.isValid()) {
                Toast.makeText(mContext, R.string.recovery_update_package_verify_failed, Toast.LENGTH_SHORT).show();
                Log.e(TAG, String.format("Failed verification %s", result));
                return;
            }
            Log.d(TAG, "package verifier success");
            if (isLowBatteryLevel()) {
                Toast.makeText(mContext, R.string.recovery_update_level, Toast.LENGTH_LONG).show();
            } else {
                showConfirmInstallDialog(result);
            }
        }
    }
    /* ------------------------------------------------VAB Ota Update Progress end ----------------------------------------------------------------- */
}
```

> 注意：这一步只是不允许用户点击屏幕外或按返回键和 HOME 键取消升级对话框，用于解决用户来回点击升级造成无响应问题。



### 2. 移植红石 Fota 代码

2.1 修改 `build/make/core/Makefile` 文件

2.1.1 在如下代码：

   ```makefile
   # Accepts a whitespace separated list of product locales such as
   # (en_US en_AU en_GB...) and returns the first locale in the list with
   # underscores replaced with hyphens. In the example above, this will
   # return "en-US".
   define get-default-product-locale
   $(strip $(subst _,-, $(firstword $(1))))
   endef
   
   # TARGET_BUILD_FLAVOR and ro.build.flavor are used only by the test
   # harness to distinguish builds. Only add _asan for a sanitized build
   # if it isn't already a part of the flavor (via a dedicated lunch
   # config for example).
   TARGET_BUILD_FLAVOR := $(TARGET_PRODUCT)-$(TARGET_BUILD_VARIANT)
   ifneq (, $(filter address, $(SANITIZE_TARGET)))
   ifeq (,$(findstring _asan,$(TARGET_BUILD_FLAVOR)))
   TARGET_BUILD_FLAVOR := $(TARGET_BUILD_FLAVOR)_asan
   endif
   endif
   ```

   的后面添加如下代码：
   ```makefile
   ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
   	REDSTONE_BUILDINFO_SH :=   packages/apps/Rsota/sh/redstonebuildinfo.sh
   endif
   ```

2.1.2 在如下代码：

   ```makefile
   INSTALLED_RECOVERYIMAGE_TARGET :=
   ifdef BUILDING_RECOVERY_IMAGE
   ifneq ($(BOARD_USES_RECOVERY_AS_BOOT),true)
   INSTALLED_RECOVERYIMAGE_TARGET := $(PRODUCT_OUT)/recovery.img
   endif
   endif
   
   $(INSTALLED_BUILD_PROP_TARGET): $(intermediate_system_build_prop)
   	@echo "Target build info: $@"
   	$(hide) grep -v 'ro.product.first_api_level' $(intermediate_system_build_prop) > $@
   ```

   的后面添加如下代码：

   ```makefile
   ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
   	bash $(REDSTONE_BUILDINFO_SH) $@ $(REDSTONE_FOTA_APK_KEY) $(REDSTONE_FOTA_APK_CHANNELID) >> $@
   endif
   ```

2.2 修改 `build/make/target/product/base_system.mk` 文件，在其末尾添加如下代码：

   ```makefile
   #ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
   PRODUCT_PACKAGES += \
          Rsota
   #endi
   ```

2.3 修改 `device/sprd/mpool/module/fota/main.mk` 文件，将下面代码：

   ```makefile
   #redstone fota
   REDSTONE_FOTA_SUPPORT := false
   REDSTONE_FOTA_APK_ICON := no
   REDSTONE_FOTA_APK_KEY := none
   REDSTONE_FOTA_APK_CHANNELID := none
   #end
   ```

   修改成如下代码：

   ```makefile
   #redstone fota
   REDSTONE_FOTA_SUPPORT := yes
   REDSTONE_FOTA_APK_ICON := no
   REDSTONE_FOTA_IS_AB = yes
   REDSTONE_FOTA_APK_KEY := none
   REDSTONE_FOTA_APK_CHANNELID := none
   #end
   ```

2.4 将红石升级应用（Rsota）文件放到 `packages/apps/` 目录下。

2.5 修改 `system/sepolicy/prebuilts/api/30.0/public/platform_app.te` 文件，在该文件末尾添加如下代码：

   ```
   #redstone
   allow platform_app system_app_data_file:dir r_dir_perms;
   allow platform_app system_app_data_file:file r_file_perms;
   ```

2.6 修改 `system/sepolicy/prebuilts/api/30.0/public/system_app.te` 文件，在该文件末尾添加如下代码：

   ```
   #redstone
   allow system_app cache_file:dir { create add_name write ioctl open search };
   allow system_app cache_file:file {create open write ioctl };
   allow system_app cache_recovery_file:dir { create add_name write ioctl open search read setattr getattr remove_name};
   allow system_app cache_recovery_file:file {create open write read unlink setattr getattr };
   allow system_app ota_package_file:dir { create add_name write ioctl open search read setattr getattr remove_name};
   allow system_app ota_package_file:file {create open write read unlink setattr getattr };
   #redstone
   ```

2.7 修改 `system/sepolicy/prebuilts/api/30.0/public/uncrypt.te` 文件，在该文件末尾添加如下代码：

   ```
   #redstone
   allow uncrypt system_app_data_file:dir {read getattr };
   allow uncrypt system_app_data_file:file {read getattr };
   ```

2.8 将 `system/sepolicy/prebuilts/api/30.0/public/` 目录下的 `platform_app.te` 、`system_app.te` 和 `uncrypt.te` 文件拷贝到 `system/sepolicy/public/` 目录下，覆盖对应的文件。

> 警告：禁止两个位置的文件都是通过拷贝的方式进行修改，必须是修改 `system/sepolicy/prebuilts/api/30.0/public/` 下的文件，再将修改的文件拷贝到 `system/sepolicy/public/` 目录下，否则编译会报错。

2.9 修改 `Settings` 代码

2.9.1 修改 `packages/apps/Settings/res/xml/my_device_info.xml` 文件，在如下代码：

   ```xml
   <PreferenceScreen
       xmlns:android="http://schemas.android.com/apk/res/android"
       xmlns:settings="http://schemas.android.com/apk/res-auto"
       android:key="my_device_info_pref_screen"
       android:title="@string/about_settings">
   
       <com.android.settingslib.widget.LayoutPreference
           android:key="my_device_info_header"
           android:order="0"
           android:layout="@layout/settings_entity_header"
           android:selectable="false"
           settings:isPreferenceVisible="false"/>
   ```

后面添加如下代码：

   ```xml
   <!--Redstone add for OTA-->
   <Preference android:key="redstone_updates"
               android:order="8"
               android:title="System Update"
               android:summary=""
               >
       <intent android:action="android.intent.action.MAIN"
               android:targetPackage="com.abfota.systemUpdate"
              android:targetClass="com.redstone.ota.ui.activity.RsMainActivity" />
   </Preference>
   <!--Redstone add end for OTA-->
   ```

2.9.2 修改 `packages/apps/Settings/src/com/android/settings/deviceinfo/aboutphone/MyDeviceInfoFragment.java` 文件，导入如下类：

```java
//strat by redstone
import com.android.settings.deviceinfo.RsAdditionalSystemUpdatePreferenceController;
//end by redstone
```

在如下代码：

```java
private static List<AbstractPreferenceController> buildPreferenceControllers(
            Context context, MyDeviceInfoFragment fragment, Lifecycle lifecycle) {
	final List<AbstractPreferenceController> controllers = new ArrayList<>();
```

后面添加如下代码：

```java
//start by redstone
controllers.add(new RsAdditionalSystemUpdatePreferenceController(context));
//end by redstone
```

2.9.3 在 `packages/apps/Settings/src/com/android/settings/deviceinfo` 目录下添加 `RsAdditionalSystemUpdatePreferenceController.java` 文件，文件内容如下所示：

```java
/*
 * Copyright (C) 2016 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.android.settings.deviceinfo;

import android.content.Context;
import androidx.preference.Preference;
import androidx.preference.PreferenceScreen;
import android.util.Log;
import com.android.settings.Utils;
import android.content.pm.PackageInfo;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;

import com.android.settings.core.PreferenceControllerMixin;
import com.android.settingslib.core.AbstractPreferenceController;
public class RsAdditionalSystemUpdatePreferenceController extends AbstractPreferenceController implements
        PreferenceControllerMixin {

    private static final String KEY_UPDATE_SETTING = "redstone_updates";
        private static final String PACKAGE_NAME = "com.abfota.systemUpdate";
Context mContext;
    public RsAdditionalSystemUpdatePreferenceController(Context context) {
        super(context);
                mContext = context;
    }

        private boolean isApkExist(String packageName){
                PackageManager pm = mContext.getPackageManager();
                PackageInfo pInfo = null;
                try{
                        pInfo = pm.getPackageInfo(packageName,PackageManager.GET_ACTIVITIES);
                        Log.e("FotaUpdate","FotaApk found..");
                }catch(PackageManager.NameNotFoundException e){
                        Log.e("FotaUpdate","FotaApk not found..");
                        return false;
                }catch(Exception xe){
                        return false;
                }


                return true;

        }
        private String getApkName(String packageName){
                PackageManager pm = mContext.getPackageManager();
                ApplicationInfo aInfo = null;
                try{
                        aInfo = pm.getApplicationInfo(packageName,PackageManager.GET_ACTIVITIES);

                }catch(PackageManager.NameNotFoundException e){
                        Log.e("FotaUpdate","FotaApk not found..");
                }catch(Exception xe){
                        aInfo = null;
                }


                return (String)pm.getApplicationLabel(aInfo);

        }
   // @Override
   // public void displayPreference(PreferenceScreen screen) {
   //     if (isAvailable()) {
   //         Utils.updatePreferenceToSpecificActivityOrRemove(mContext, screen,
  //                  KEY_UPDATE_SETTING,
  //                  Utils.UPDATE_PREFERENCE_FLAG_SET_TITLE_TO_MATCHING_ACTIVITY);
  //      } else {
  //          removePreference(screen, KEY_UPDATE_SETTING);
  //      }
 //   }
        @Override
        public void  updateState(Preference preference){
                super.updateState(preference);
                String title = getApkName(PACKAGE_NAME);
                if(title != null&& !title.equals("")){
                        preference.setTitle(title);
                        Log.e("FotaUpdate","preference  set preference title :" + title);
                }else{
                        Log.e("FotaUpdate","preference  set preference title null");
                }
                //super.displayPreference(screen);
        }
    @Override
    public boolean isAvailable() {
                String packageName = PACKAGE_NAME;
                boolean isAvi = false;
                if(isApkExist(packageName))
                        return true;
                else
                        return false;
       // return mContext.getResources().getBoolean(
           //         com.android.settings.R.bool.config_redstone_system_update_setting_enable);
    }

    @Override
    public String getPreferenceKey() {
        return KEY_UPDATE_SETTING;
    }
}
```

   1.12 修改 `packages/apps/Settings/src_unisoc/com/android/settings/deviceinfo/LocalSystemUpdatePreferenceController.java` 文件，将所有 Dialog 都添加禁止点击屏幕外隐藏设置：

```java
dialog.setCancelable(false);
dialog.setCanceledOnTouchOutside(false);
```

最终代码如下所示：

```java
package com.android.settings.deviceinfo;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.res.Resources;
import android.os.AsyncTask;
import android.os.Environment;
import android.os.EnvironmentEx;
import android.os.Handler;
import android.os.PowerManager;
import android.os.RecoverySystem;
import android.os.SystemProperties;
import android.os.UpdateEngine;
import android.os.UpdateEngineCallback;
import android.os.UserHandle;
import android.provider.Settings;
import android.util.Log;
import android.view.WindowManager;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.preference.DialogPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceScreen;
import com.android.internal.util.Preconditions;
import com.android.settings.R;
import com.android.settings.core.PreferenceControllerMixin;
import com.android.settingslib.Utils;
import com.android.settingslib.core.lifecycle.Lifecycle;
import com.android.settingslib.core.lifecycle.LifecycleObserver;
import com.android.settingslib.core.lifecycle.events.OnDestroy;
import com.android.settingslib.core.AbstractPreferenceController;

import java.util.ArrayList;
import java.util.List;
import java.io.File;
import java.io.IOException;

public class LocalSystemUpdatePreferenceController extends AbstractPreferenceController
            implements PreferenceControllerMixin, LifecycleObserver {
    private static final String TAG = "LocalSystemUpdate";
    private static final String KEY_RECOVERY_SYSTEM_UPDATE = "RecoverySystemUpdate";
    private static final String UPDATE_FILE_PATH = "/update.zip";
    private static final String INTERNAL_STORAGE_PHY_PATH = "data/media/0";
    private static final String INTERNAL_STORAGE_MOUNT_PATH = "storage/emulated/0";
    private static final String OTA_PACKAGE_PATH = "data/ota_package";
    private static final String REBOOT_REASON = "reboot-ab-update";
    private static final String DATABASE_KEY_INSTALL_IN_PROGRESS = "install_in_progress";
    private static final String ERROR_NEED_REBOOT = "An update already applied, waiting for reboot";
    private static final int MINIMUM_LEVEL_POWER = 35;
    private static final boolean SD_UDPATE_SUPPORTED = true;

    private final UpdateEngine mUpdateEngine = new UpdateEngine();
    private final OtaUpdateEngineCallback mOtaUpdateEngineCallback = new OtaUpdateEngineCallback();
    // Add for bug1413281， support Non-A/B feature
    private final boolean mIsVirtualAbSupported = SystemProperties.getBoolean("ro.build.ab_update", false);

    private boolean mInternalUpdateFileExist = false;
    private boolean mSdUpdateFileExist = false;
    private boolean mOtaUpdateFileExist = false;
    private int mUserChoice = 0;

    private List<File> mUpdateItems = new ArrayList<File>();
    private PowerManager mPowerManager;
    private ProgressDialog mProgressDialog;
    private boolean mInstallationInProgress = false;

    private DialogInterface.OnClickListener mDialogClickListener = new DialogInterface.OnClickListener() {
        public void onClick(DialogInterface arg0, int arg1) {
            checkUpdatePackage();
        }
    };

    public LocalSystemUpdatePreferenceController(Context context) {
        super(context);
        mPowerManager = (PowerManager) mContext.getSystemService(Context.POWER_SERVICE);
        mInstallationInProgress = Settings.Global.getInt(mContext.getContentResolver(),
                DATABASE_KEY_INSTALL_IN_PROGRESS, 0) == 1;
    }

    public void checkUpdatePackage() {
        Log.d(TAG, "mIsVirtualAbSupported:" + mIsVirtualAbSupported);
        mUpdateItems.clear();
        checkInteralStorage();
         // Add for bug1413281， support Non-A/B feature
        if (mIsVirtualAbSupported) {
            checkOtaPackage();
        }
        if (SD_UDPATE_SUPPORTED) {
            checkExternalStorage();
        }
        showOperateDialog();
    }

    public void showOperateDialog() {
        final String [] items = mContext.getResources().getStringArray(R.array.update_choice);
        boolean internalFlag = false;
        boolean sdFlag = false;
        if (mUpdateItems.size() == 3) {
            showSingleChoiceDialog(items);
        } else if (mUpdateItems.size() > 0) {
            int size = mUpdateItems.size();
            String [] item_temp = new String[size];
            for (int i = 0; i < size; i++) {
                if (mInternalUpdateFileExist && !internalFlag) {
                    item_temp[i] = items[0];
                    internalFlag = true;
                    continue;
                }
                if (mSdUpdateFileExist && !sdFlag) {
                    item_temp[i] = items[1];
                    sdFlag = true;
                    continue;
                }
                if (mOtaUpdateFileExist) {
                    item_temp[i] = items[2];
                    continue;
                }
            }
            showSingleChoiceDialog(item_temp);
        } else {
            if (SD_UDPATE_SUPPORTED) {
                Toast.makeText(mContext, R.string.recovery_no_update_package, Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(mContext, R.string.recovery_no_update_package_internal_only, Toast.LENGTH_LONG).show();
            }
        }
    }

    public void checkOtaPackage() {
        // update.zip path: data/ota_package
        mOtaUpdateFileExist = false;
        File otaFile = new File(OTA_PACKAGE_PATH + UPDATE_FILE_PATH);
        if (otaFile.exists()) {
            mOtaUpdateFileExist = true;
            mUpdateItems.add(otaFile);
        }
    }

    public void checkInteralStorage() {
        // Ota does not recognize the internal storage mount path
        // "storage/emulated/0", only the physical path"data/media/0" is recognized.
        mInternalUpdateFileExist = false;
        File checkFile = new File(INTERNAL_STORAGE_MOUNT_PATH + UPDATE_FILE_PATH);
        File internalFile = new File(INTERNAL_STORAGE_PHY_PATH + UPDATE_FILE_PATH);
        if (checkFile.exists()) {
            mInternalUpdateFileExist = true;
            if (mIsVirtualAbSupported) {
                mUpdateItems.add(checkFile);
            } else {
                mUpdateItems.add(internalFile);
            }
        }
    }

    public void checkExternalStorage() {
        //external sdcard
        mSdUpdateFileExist = false;
        String storageState = EnvironmentEx.getExternalStoragePathState();
        String storageDirectory = EnvironmentEx.getExternalStoragePath().getAbsolutePath();
        if (storageState.equals(Environment.MEDIA_MOUNTED)) {
            File file = new File(storageDirectory + UPDATE_FILE_PATH);
            if (file.exists()) {
                mSdUpdateFileExist = true;
                mUpdateItems.add(file);
            }
        }
    }

    @Override
    public boolean handlePreferenceTreeClick(Preference preference) {
        int messageId = SD_UDPATE_SUPPORTED ? R.string.recovery_update_message : R.string.recovery_update_message_internal_only;
        if (getPreferenceKey().equals(preference.getKey())) {
            AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
            builder.setMessage(mContext.getResources().getString(messageId));
            builder.setPositiveButton(android.R.string.ok, mDialogClickListener);
            builder.setNegativeButton(android.R.string.cancel, null);
            AlertDialog dialog = builder.create();
            dialog.setCancelable(false);
            dialog.setCanceledOnTouchOutside(false);
            dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
            dialog.show();
            return true;
        }
        return super.handlePreferenceTreeClick(preference);
    }

    @Override
    public boolean isAvailable() {
        return mContext.getResources().getBoolean(R.bool.config_support_otaupdate)
                && isAdminUser();
    }

    @Override
    public String getPreferenceKey() {
        return KEY_RECOVERY_SYSTEM_UPDATE;
    }

    @Override
    public void displayPreference(PreferenceScreen screen) {
        super.displayPreference(screen);
        if (isAvailable()) {
            final Preference preference = initLocalSystemUpdatePreference();
            screen.addPreference(preference);
        }
    }

    public boolean isLowBatteryLevel() {
        Intent batteryBroadcast = mContext.registerReceiver(null,
                new IntentFilter(Intent.ACTION_BATTERY_CHANGED));
        final int batteryLevel = Utils.getBatteryLevel(batteryBroadcast);
        return batteryLevel < MINIMUM_LEVEL_POWER;
    }

    public boolean isAdminUser() {
        return UserHandle.myUserId() == UserHandle.USER_OWNER;
    }

    public Preference initLocalSystemUpdatePreference() {
        Preference preference = new Preference (mContext);
        preference.setTitle(R.string.recovery_update_title);
        preference.setKey(KEY_RECOVERY_SYSTEM_UPDATE);
        preference.setOrder(0);
        return preference;
    }

    public void showSingleChoiceDialog(String [] items) {
        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
        builder.setSingleChoiceItems(items, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                mUserChoice = which;
            }
        });
        builder.setTitle(R.string.choice_dialog_title);
        builder.setPositiveButton(R.string.update_choice_dialog_ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                File file = mUpdateItems.get(mUserChoice);
                if (mIsVirtualAbSupported) {
                    startVirtualAbUpdateProgress(file);
                } else {
                    startNormalUpdateProgress(items[mUserChoice], file);
                }
            }
        });
        AlertDialog dialog = builder.create();
        dialog.setCancelable(false);
        dialog.setCanceledOnTouchOutside(false);
        dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
        dialog.show();
    }

    /** ------------------------------------------------Normal Ota Update Progress start ------------------------------------------------------------ */
    /**  Add for bug1413281， support Non-A/B feature start @{ */
    public void startNormalUpdateProgress(String message, File file) {
        if (mUserChoice >= 0) {
            Toast.makeText(mContext, message, Toast.LENGTH_SHORT).show();
            tryToRecoverySystem(file);
        }
    }

    public void tryToRecoverySystem(File file) {
        if (isLowBatteryLevel()) {
            Toast.makeText(mContext, R.string.recovery_update_level, Toast.LENGTH_LONG).show();
        } else {
            try {
                RecoverySystem.installPackage(mContext, file);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    /** @} */
    /** ------------------------------------------------Normal Ota Update Progress end -------------------------------------------------------------- */


    /** ------------------------------------------------VAB Ota Update Progress start --------------------------------------------------------------- */
    public void startVirtualAbUpdateProgress(File file) {
        if (mInstallationInProgress) {
            showInstallationInProgress();
        } else if (mUserChoice >= 0) {
            try {
                new UpdateVerifier().execute(file);
            } catch (Exception ex) {
                Log.e(TAG, ex.getMessage());
                Toast.makeText(mContext, R.string.recovery_update_package_verify_failed, Toast.LENGTH_SHORT).show();
            }
        }
    }

    private void showInstallationInProgress() {
        mInstallationInProgress = true;
        showStatus(R.string.recovery_update_package_install_title, R.string.recovery_update_package_download_in_progress);
        mUpdateEngine.bind(mOtaUpdateEngineCallback, new Handler(mContext.getMainLooper()));
    }

    private void showStatus(int titleId, int messageId) {
        if (mProgressDialog != null && mProgressDialog.isShowing()) {
            mProgressDialog.setTitle(titleId);
            mProgressDialog.setMessage(mContext.getResources().getString(messageId));
        } else {
            mProgressDialog = getProgressDialog();
            mProgressDialog.setTitle(titleId);
            mProgressDialog.setMessage(mContext.getResources().getString(messageId));
            mProgressDialog.setCancelable(false);
            mProgressDialog.setCanceledOnTouchOutside(false);
            mProgressDialog.show();
        }
    }

    private ProgressDialog getProgressDialog() {
        ProgressDialog progressDialog = new ProgressDialog(mContext);
        progressDialog.setIndeterminate(true);
        return progressDialog;
    }

    private void dismissProgressDialog() {
        if (mProgressDialog != null && mProgressDialog.isShowing()) {
            // Add for bug1413124,Avoid the exception of dissmiss dialog when the context has been recycled.
            try {
                mProgressDialog.dismiss();
            } catch (Exception ex) {
                Log.e(TAG, ex.getMessage());
            } finally {
                mProgressDialog = null;
            }
        }
    }

    /** Ota upgrade is complete, pop up the dialog to confirm whether to restart the phone immediately */
    public void showConfirmRebootDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
        builder.setTitle(mContext.getResources().getString(R.string.recovery_update_package_install_title));
        builder.setMessage(mContext.getResources().getString(R.string.recovery_update_rebooting));
        builder.setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                rebootNow();
            }
        });
        builder.setNegativeButton(android.R.string.cancel, null);
        AlertDialog dialog = builder.create();
        dialog.setCancelable(false);
        dialog.setCanceledOnTouchOutside(false);
        dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
        dialog.show();
    }

    /** A dialog pops up to confirm whether to upgrade */
    public void showConfirmInstallDialog(final UpdateParser.ParsedUpdate parsedUpdate) {
        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
        builder.setTitle(mContext.getResources().getString(R.string.recovery_update_package_install_title));
        builder.setMessage(mContext.getResources().getString(R.string.recovery_update_install_ready));
        builder.setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                showInstallationInProgress();
                Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 1);
                installUpdate(parsedUpdate);
            }
        });
        builder.setNegativeButton(android.R.string.cancel, null);
        AlertDialog dialog = builder.create();
        dialog.setCancelable(false);
        dialog.setCanceledOnTouchOutside(false);
        dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
        dialog.show();
    }

    /** Send ota package data to updateEngine for upgrade */
    private void installUpdate(UpdateParser.ParsedUpdate parsedUpdate) {
        Log.d(TAG, "mUrl:" + parsedUpdate.mUrl + ",mOffset:" + parsedUpdate.mOffset
                + ",mSize:" + parsedUpdate.mSize + ",mProps:" + parsedUpdate.mProps);
        try {
            mUpdateEngine.applyPayload(
                    parsedUpdate.mUrl, parsedUpdate.mOffset, parsedUpdate.mSize, parsedUpdate.mProps);
        } catch (Exception ex) {
            mInstallationInProgress = false;
            Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 0);
            //Modify for bug1420894, no need to show toast if update succeed
            String message = ex.getMessage();
            Log.e(TAG, message);
            if (!ERROR_NEED_REBOOT.equals(message)) {
                Toast.makeText(mContext, R.string.recovery_update_package_install_failed, Toast.LENGTH_SHORT).show();
            }
        }
    }

    /** Reboot the system. */
    private void rebootNow() {
        Log.i(TAG, "Rebooting Now.");
        mPowerManager.reboot(REBOOT_REASON);
    }

    /** Handle events from the UpdateEngine. */
    public class OtaUpdateEngineCallback extends UpdateEngineCallback {
        @Override
        public void onStatusUpdate(int status, float percent) {
            switch (status) {
                case UpdateEngine.UpdateStatusConstants.UPDATED_NEED_REBOOT:
                    mInstallationInProgress = false;
                    Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 0);
                    dismissProgressDialog();
                    Log.d(TAG, "Before show reboot dialog");
                    showConfirmRebootDialog();
                    break;
                case UpdateEngine.UpdateStatusConstants.DOWNLOADING:
                    Log.d(TAG, "downloading progress:" + ((int) (percent * 100) + "%"));
                    if (mProgressDialog != null && mProgressDialog.isShowing()) {
                        String message = mContext.getResources().getString(R.string.recovery_update_package_download_in_progress);
                        String progessMessage = message + ((int) (percent * 100) + "%");
                        mProgressDialog.setMessage(progessMessage);
                    }
                    break;
                // Add install progress display for bug1397771
                case UpdateEngine.UpdateStatusConstants.FINALIZING:
                    Log.d(TAG, "finalizing progress:" + ((int) (percent * 100) + "%"));
                    if (mProgressDialog != null && mProgressDialog.isShowing()) {
                        String message = mContext.getResources().getString(R.string.recovery_update_package_install_in_progress);
                        String progessMessage = message + ((int) (percent * 100) + "%");
                        mProgressDialog.setMessage(progessMessage);
                    }
                default:
                    // do nothing
            }
        }

        @Override
        public void onPayloadApplicationComplete(int errorCode) {
            mInstallationInProgress = false;
            Settings.Global.putInt(mContext.getContentResolver(), DATABASE_KEY_INSTALL_IN_PROGRESS, 0);
            dismissProgressDialog();
            Log.w(TAG, String.format("onPayloadApplicationComplete %d", errorCode));
            int messageId = (errorCode == UpdateEngine.ErrorCodeConstants.SUCCESS) ? R.string.recovery_update_package_install_success : R.string.recovery_update_package_install_failed;
            Toast.makeText(mContext, messageId, Toast.LENGTH_SHORT).show();
        }
    }

    /** Verify the validity of the ota upgrade package */
    private class UpdateVerifier extends AsyncTask<File, Void, UpdateParser.ParsedUpdate> {
        @Override
        protected UpdateParser.ParsedUpdate doInBackground(File... files) {
            Preconditions.checkArgument(files.length > 0, "No file specified");
            File file = files[0];
            try {
                return UpdateParser.parse(file);
            } catch (IOException e) {
                Log.e(TAG, String.format("For file %s", file), e);
                return null;
            }
        }

        @Override
        protected void onPostExecute(UpdateParser.ParsedUpdate result) {
            if (result == null) {
                Toast.makeText(mContext, R.string.recovery_update_package_verify_failed, Toast.LENGTH_SHORT).show();
                Log.e(TAG, String.format("Failed verification %s", result));
                return;
            }
            if (!result.isValid()) {
                Toast.makeText(mContext, R.string.recovery_update_package_verify_failed, Toast.LENGTH_SHORT).show();
                Log.e(TAG, String.format("Failed verification %s", result));
                return;
            }
            Log.d(TAG, "package verifier success");
            if (isLowBatteryLevel()) {
                Toast.makeText(mContext, R.string.recovery_update_level, Toast.LENGTH_LONG).show();
            } else {
                showConfirmInstallDialog(result);
            }
        }
    }
    /* ------------------------------------------------VAB Ota Update Progress end ----------------------------------------------------------------- */
}
```

### 3. 修改编译脚本

3.1 执行 `make -j8` 命令全编工程

3.2 执行 `cp_sign` 命令拷贝并签名文件

3.3 按照 `out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/pac.ini` 文件对应关系，将 `[pac_list]` 下面的文件拷贝到 `ota_partion` 变量中的文件中，例如：在 `ota_partition` 中有如下值:

   ```
   Modem_LTE:./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_modem.img
   ```

我们在 `[pac_list]` 可以找到 `Modem_LTE` 对应的值，如下所示：

   ```
   Modem_LTE=1@./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/SC9600_sharkl3_pubcp_modem.dat
   ```

最后，我们使用 `cp` 命令将  `[pac_list]` 下的文件拷贝到 `ota_partition` 中对应路径的文件，例如，在源代码根目录下执行如下命令拷贝：

   ```shell
   cp ./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/SC9600_sharkl3_pubcp_modem.dat ./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_modem.img
   ```

下面给出一个拷贝的脚本：

   ```shell
   copy_modem_bins() {
       Modem_LTE="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_modem.img"
       Modem_LTE_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/SC9600_sharkl3_pubcp_modem.dat"
   
       DSP_LTE_GGE="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_gdsp.img"
       DSP_LTE_GGE_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/sharkl3_pubcp_DM_DSP.bin"
   
       DSP_LTE_LTE="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_ldsp.img"
       DSP_LTE_LTE_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/sharkl3_pubcp_LTEA_DSP.bin"
   
       DFS="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/pm_sys.img"
       DFS_FROM="./out/target/product/s9863a1h10_go_32b/cp_sign/SHARKL3_R11/sharkl3_cm4.bin"
   
       NV_LTE1="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv1.img"
       NV_LTE2="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_fixnv2.img"
       NV_LTE_FROM="./vendor/sprd/release/unisoc_bin/nv_wb/U863JR200-J44L_G4+W25+F247828_TSX_SingleSIM/sharkl3_pubcp_nvitem.bin"
   
       Modem_WCN="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/wcnmodem.img"
       Modem_WCN_FROM="./vendor/sprd/release/unisoc_bin/marlin2_18a/sharkl3_cm4_v2_builddir/PM_sharkl3_cm4_v2.bin"
   
       Modem_LTE_DELTANV="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/l_deltanv.img"
       Modem_LTE_DELTANV_FROM="./vendor/sprd/release/unisoc_bin/4g_modem_20a/9863a/sharkl3_pubcp_builddir/sharkl3_pubcp_deltanv.bin"
   
       GPS_BD="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/gpsbd.img"
       GPS_BD_FROM="./vendor/sprd/release/unisoc_bin/gnss_20a/greeneye2_cm4_bds_builddir/gnssbdmodem.bin"
   
       GPS_GL="./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/gpsgl.img"
       GPS_GL_FROM="./vendor/sprd/release/unisoc_bin/gnss_20a/greeneye2_cm4_glonass_builddir/gnssmodem.bin"
   
       cd unisoc_all_11_0_2021_07_14_13_14_59
   
       rm -rf ./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/
       mkdir ./device/sprd/mpool/module/modem/msoc/sharkl3/modem_bins/
   
       cp $Modem_LTE_FROM $Modem_LTE
       cp $DSP_LTE_GGE_FROM $DSP_LTE_GGE
       cp $DSP_LTE_LTE_FROM $DSP_LTE_LTE
       cp $DFS_FROM $DFS
       cp $NV_LTE_FROM $NV_LTE1
       cp $NV_LTE_FROM $NV_LTE2
       cp $Modem_WCN_FROM $Modem_WCN
       cp $Modem_LTE_DELTANV_FROM $Modem_LTE_DELTANV
       cp $GPS_BD_FROM $GPS_BD
       cp $GPS_GL_FROM $GPS_GL
   }
   ```

3.4 执行 `make otapackage -j8` 命令编译 ota

3.5 执行 `make otatools` 命令生成用于生成差分包的工具

3.6 执行 `makepac` 命令生成 pac 文件

3.7 执行 `copy_out_imagefiles` 命令拷贝镜像文件。

下面给出一个完成的编译脚本：

   ```shell
   if [ $STEP0_MAKE_ALL_IMG -ne 0 ];then
   
       echo -e "\033[;33m
   
   	start to make all img -j$TASK_NUM ...
   
       \033[0m"
   
       source build/envsetup.sh
       choosecombo release $MY_BOARD $BUILD_VER gms
   
       if [ ! -d out/target/product/$OUT_TARGET_DIR/vendor ];then
           echo "IDH out not exist copy them now !!"
           if [ ! -d out/target/product/$OUT_TARGET_DIR ];then
              rm -rf bsp/out
              rm -rf out
           fi
           cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/bsp .
           cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/out .
       fi
   
       make -j$TASK_NUM
       if [ $? -eq 0 ]; then
           echo "Build images ok!"
       else
           echo "Build images failed!"
           exit 1
       fi
   
       cp_sign
       copy_modem_bins
       make otapackage -j$TASK_NUM
       make otatools
       makepac
   
       copy_out_imagefiles
   
       echo "make all img -j$TASK_NUM finished"
       date "+%Y-%m-%d %H:%M:%S"
   fi
   ```

### 4. 制作差分包

4.1 执行下面命令将 `out` 目录下的 `otatools` 文件夹拷贝到源代码根目录下：

```shell
cp out/target/product/s9863a1h10_go_32b/otatools ./
```

> 注意：必须在 Linux 下拷贝，如果在 Windows 下拷贝将会导致文件夹中的文件权限改变，从而导致生成差分包失败。

4.2 将生成的两个 target 包，例如 `V1.zip` 和 `V2.zip` 拷贝到源代码根目录下的 `otatools` 文件夹中。（V1.zip 是基础包，V2.zip 是目的包）

```shell
cp out/target/product/s9863a1h10_go_32b/obj/PACKAGING/target_files_intermediates/s9863a1h10_go_32b_2g-target_files-1627279500.zip ./otatools/V1.zip
```

4.3 进入到源代码根目录下的 `otatools` 文件夹中执行如下命令生成差分包：

4.3.1 `user` 版本生成差分包命令如下：

```shell
./build/make/tools/releasetools/ota_from_target_files -k ./build/target/product/security/release/releasekey --block -v -i V1.zip V2.zip update.zip
```

4.3.2 `userdebug` 版本生成差分包命令如下：

```shell
./build/make/tools/releasetools/ota_from_target_files -k ./build/target/product/security/testkey --block -v -i V1.zip V2.zip update.zip
```



