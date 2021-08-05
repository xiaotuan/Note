[toc]

### 1. 修改 `build/make/core/Makefile` 文件

1.1 在如下代码：

```makefile
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

后面添加如下代码：

```makefile
ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
	REDSTONE_TARGETFILE_SH := packages/apps/Rsota/sh/redstonetargetfile.sh
	REDSTONE_BUILDINFO_SH := packages/apps/Rsota/sh/redstonebuildinfo.sh
endif
```

1.2 在如下代码：

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

后面添加如下代码：

```makefile
ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
	bash $(REDSTONE_BUILDINFO_SH) $@ $(REDSTONE_FOTA_APK_KEY) $(REDSTONE_FOTA_APK_CHANNELID) >> $@
endif
```

1.3 在如下代码：

```makefile
ifeq ($(BUILD_QEMU_IMAGES),true)
	$(hide) AVBTOOL=$(AVBTOOL) $(MK_VBMETA_BOOT_KERNEL_CMDLINE_SH) $(zip_root)/IMAGES/vbmeta.img \
	    $(zip_root)/IMAGES/system.img $(zip_root)/IMAGES/VerifiedBootParams.textproto
endif
	@# Zip everything up, preserving symlinks and placing META/ files first to
	@# help early validation of the .zip file while uploading it.
	$(hide) find $(zip_root)/META | sort >$@.list
	$(hide) find $(zip_root) -path $(zip_root)/META -prune -o -print | sort | sed -e 's/\[/\\\[/g' -e 's/\]/\\\]/g' >>$@.list
	$(hide) $(SOONG_ZIP) -d -o $@ -C $(zip_root) -l $@.list
```

后面添加如下代码：

```makefile
ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
	@echo "Package redstone-fota-Package"
	$(hide) echo $(OTATOOLS) >> $(PRODUCT_OUT)/otatools_list
	$(hide) bash $(REDSTONE_TARGETFILE_SH) $(PRODUCT_OUT)/otatools_list $(PRODUCT_OUT) $(zip_root)
	rm $(PRODUCT_OUT)/otatools_list
	#$1 OTATOOLS
	#$2 PRODUCT_OUT
	#$3 $(zip_root)/META/misc_info.txt
endif
```

### 2. 修改 ` build/make/target/product/base_system.mk` 文件

在文件末尾添加如下代码：

```makefile
#ifeq ($(strip $(REDSTONE_FOTA_SUPPORT)), yes)
PRODUCT_PACKAGES += \
	Rsota
#endif
```

### 3. 在 `packages/apps/` 目录下添加红石 Rsota 应用

### 4. 修改 ` system/sepolicy/prebuilts/api/30.0/public/platform_app.te` 文件

在文件中添加如下代码：

```java
#redstone
allow platform_app system_app_data_file:dir r_dir_perms;
allow platform_app system_app_data_file:file r_file_perms;
#redstone
```

最终文件内容如下所示：

```
###
### Apps signed with the platform key.
###

#redstone
allow platform_app system_app_data_file:dir r_dir_perms;
allow platform_app system_app_data_file:file r_file_perms;
#redstone
type platform_app, domain;
```

> 注意：`te` 文件最后一行不能是注释，否则编译报错。

### 5. 修改 `system/sepolicy/prebuilts/api/30.0/public/system_app.te` 文件

在文件中添加如下代码：

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

### 6. 修改 `system/sepolicy/prebuilts/api/30.0/public/uncrypt.te` 文件

在文件中添加如下代码：

```
#redstone
allow uncrypt system_app_data_file:dir {read getattr };
allow uncrypt system_app_data_file:file {read getattr };
#redstone
```

### 7. 将 `system/sepolicy/prebuilts/api/30.0/public/` 目录下的 `platform_app.te`、`system_app.te`、`uncrypt.te` 拷贝到 `system/sepolicy/public` 目录下，覆盖对应的文件。

### 8.  修改 `vendor/wb_custom/wb_config.mk` 文件

在文件中添加如下代码：

```makefile
#redstone FOTA
REDSTONE_FOTA_SUPPORT=yes
REDSTONE_FOTA_APK_ICON=no
REDSTONE_FOTA_APK_KEY=none
REDSTONE_FOTA_APK_CHANNELID=none
#redstone FOTA
```

### 9. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/res/xml/my_device_info.xml` 文件

在如下代码：

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
<!--redstone ota-->
<Preference android:key="redstone_updates"
            android:order="8"
            android:title="System Update"
            android:summary="" >
    <intent android:action="android.intent.action.MAIN"
            android:targetPackage="com.abfota.systemUpdate"
            android:targetClass="com.redstone.ota.ui.activity.RsMainActivity" />
</Preference>
<!--redstone ota-->
```

### 10. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/deviceinfo/aboutphone/MyDeviceInfoFragment.java` 文件

10.1 导入如下类：

```java
//strat by redstone
import com.android.settings.deviceinfo.RsAdditionalSystemUpdatePreferenceController;
//end by redstone
```

10.2 在如下代码：

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

### 11. 在 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/deviceinfo/` 目录下添加 `RsAdditionalSystemUpdatePreferenceController.java` 文件

文件内容如下所示：

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

