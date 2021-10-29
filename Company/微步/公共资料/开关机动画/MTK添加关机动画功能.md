[toc]

### 1. 修改 `device/mediateksample/m863u_bsp_64/device.mk`

在 `device.mk` 文件末尾添加如下代码：

```diff
@@ -175,5 +175,12 @@ $(call inherit-product, device/mediatek/mt6739/device.mk)
 
 $(call inherit-product-if-exists, vendor/mediatek/libs/$(MTK_TARGET_PROJECT)/device-vendor.mk)
 
-
+#add bootanimation
+PRODUCT_SYSTEM_DEFAULT_PROPERTIES += \
+  persist.sys.bootanimation=1 \
+  persist.sys.shutanimation=1
+
+PRODUCT_PACKAGES += \
+    mtkbootanimation \
+    libmtkbootanimation
```

### 2. 修改 `frameworks/av/services/audioflinger/Threads.cpp`

```diff
@@ -5609,6 +5609,14 @@ AudioFlinger::PlaybackThread::mixer_state AudioFlinger::MixerThread::prepareTrac
                 track->mHasVolumeController = false;
             }
 
+            char mvalue[PROPERTY_VALUE_MAX] = { 1 };
+            property_get("service.bootanim.exit", mvalue, "");
+            if (strcmp(mvalue,"0") == 0){
+                //ALOGE("bootanim volume setting");
+                vlf = 0.25f;
+                vrf = 0.25f;
+            }
+
             // XXX: these things DON'T need to be done each time
             mAudioMixer->setBufferProvider(trackId, track);
             mAudioMixer->enable(trackId);
```

### 3. 注释掉 `frameworks/base/cmds/bootanimation/Android.bp` 文件内容

### 4. 修改 `vendor/mediatek/proprietary/frameworks/base/res/res/values/config.xml`

```diff
@@ -150,4 +150,8 @@
     <integer name="bt_multidevice_performance">400</integer>
     <!-- For Mobile Data Service -->
     <integer name="config_mobile_test_sim_mtu">0</integer>
+
+    <integer name="shutdown_animation_play_time">6000</integer>
+    <bool name="reboot_animation_play_time_delay">true</bool>
+    
 </resources>
```

### 5. 修改 `vendor/mediatek/proprietary/frameworks/base/res/res/values/symbols.xml`

```diff
@@ -877,4 +877,8 @@
   <java-symbol type="integer" name="bt_multidevice_performance" />
   <!-- For Mobile Data Service -->
   <java-symbol type="integer" name="config_mobile_test_sim_mtu" />
+
+  <java-symbol type="integer" name="shutdown_animation_play_time" />
+  <java-symbol type="bool" name="reboot_animation_play_time_delay" />
+  
 </resources>
```

### 6. 修改 `vendor/mediatek/proprietary/frameworks/base/services/core/java/com/mediatek/server/MtkShutdownThread.java`

```diff
@@ -85,7 +85,7 @@ public class MtkShutdownThread extends ShutdownThread{
 
     ///added for Shutdown animation @{
     private static final String OPERATOR_SYSPROP = "persist.vendor.operator.optr";
-    private static final int MIN_SHUTDOWN_ANIMATION_PLAY_TIME = 5 * 1000;
+    private static int MIN_SHUTDOWN_ANIMATION_PLAY_TIME = 5 * 1000;
 
     // CU/CMCC operator require 3-5s
     private static long beginAnimationTime = 0;
@@ -234,7 +234,11 @@ public class MtkShutdownThread extends ShutdownThread{
         Log.i(TAG, "set service.shutanim.running to 1");
         SystemProperties.set("service.shutanim.running", "1");
         /*M: play animation*/
-        if ((mReboot == true && mReason != null && mReason.equals("recovery")) ||
+        if (((MtkShutdownThread)sInstance).mContext.getResources().getBoolean(
+                com.mediatek.internal.R.bool.reboot_animation_play_time_delay) || (mReboot == true)) {
+            //Log.i(TAG, "shutdownAnimationService delayForPlayAnimation");
+            delayForPlayAnimation();
+        } else if ((mReboot == true && mReason != null && mReason.equals("recovery")) ||
                 (mReboot == false)) {
             delayForPlayAnimation();
         }
@@ -275,6 +279,14 @@ public class MtkShutdownThread extends ShutdownThread{
         } catch (RemoteException e) {
             e.printStackTrace();
         }
+
+        if (context.getResources().getInteger(
+                com.mediatek.internal.R.integer.shutdown_animation_play_time) != 0) {
+            MIN_SHUTDOWN_ANIMATION_PLAY_TIME = context.getResources().getInteger(
+                com.mediatek.internal.R.integer.shutdown_animation_play_time);
+            //Log.i(TAG, "mtkShutdownThread bootanimCust MIN_SHUTDOWN_ANIMATION_PLAY_TIME = " + MIN_SHUTDOWN_ANIMATION_PLAY_TIME);
+        }
+
         beginAnimationTime = SystemClock.elapsedRealtime() + MIN_SHUTDOWN_ANIMATION_PLAY_TIME;
         //Disable key dispatch
         try {
@@ -352,6 +364,13 @@ public class MtkShutdownThread extends ShutdownThread{
         int screenTurnOffTime = 0;
         try {
             screenTurnOffTime = getScreenTurnOffTime();
+            if (context.getResources().getInteger(
+                    com.mediatek.internal.R.integer.shutdown_animation_play_time) != 0) {
+                screenTurnOffTime = context.getResources().getInteger(
+                    com.mediatek.internal.R.integer.shutdown_animation_play_time);
+                //Log.i(TAG, "screen turn off time shutdown_animation_play_time =" + context.getResources().getInteger(
+                //    com.mediatek.internal.R.integer.shutdown_animation_play_time));
+            }
             Log.i(TAG, "screen turn off time screenTurnOffTime =" + screenTurnOffTime);
         } catch (Exception e) {
             e.printStackTrace();
@@ -360,7 +379,15 @@ public class MtkShutdownThread extends ShutdownThread{
     }
 
     public static int isCustBootAnim() {
+        int mode = DEFAULT_MODE;
+        if(mShutOffAnimation == -1) {
+            mode = ANIMATION_MODE; //Enable Shutdown Animation
+            mShutOffAnimation = mode;
+            //Log.i(TAG,"mShutOffAnimation: " + mode);
+            return mode;
+        } else {
             return mShutOffAnimation;
+        }
     }
 }
```

### 7. 添加 `vendor/mediatek/proprietary/operator/frameworks/bootanimation/Android.mk` 文件

```makefile
# Copyright Statement:
#
# This software/firmware and related documentation ("MediaTek Software") are
# protected under relevant copyright laws. The information contained herein
# is confidential and proprietary to MediaTek Inc. and/or its licensors.
# Without the prior written permission of MediaTek inc. and/or its licensors,
# any reproduction, modification, use or disclosure of MediaTek Software,
# and information contained herein, in whole or in part, shall be strictly prohibited.

# MediaTek Inc. (C) 2012. All rights reserved.
#
# BY OPENING THIS FILE, RECEIVER HEREBY UNEQUIVOCALLY ACKNOWLEDGES AND AGREES
# THAT THE SOFTWARE/FIRMWARE AND ITS DOCUMENTATIONS ("MEDIATEK SOFTWARE")
# RECEIVED FROM MEDIATEK AND/OR ITS REPRESENTATIVES ARE PROVIDED TO RECEIVER ON
# AN "AS-IS" BASIS ONLY. MEDIATEK EXPRESSLY DISCLAIMS ANY AND ALL WARRANTIES,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT.
# NEITHER DOES MEDIATEK PROVIDE ANY WARRANTY WHATSOEVER WITH RESPECT TO THE
# SOFTWARE OF ANY THIRD PARTY WHICH MAY BE USED BY, INCORPORATED IN, OR
# SUPPLIED WITH THE MEDIATEK SOFTWARE, AND RECEIVER AGREES TO LOOK ONLY TO SUCH
# THIRD PARTY FOR ANY WARRANTY CLAIM RELATING THERETO. RECEIVER EXPRESSLY ACKNOWLEDGES
# THAT IT IS RECEIVER'S SOLE RESPONSIBILITY TO OBTAIN FROM ANY THIRD PARTY ALL PROPER LICENSES
# CONTAINED IN MEDIATEK SOFTWARE. MEDIATEK SHALL ALSO NOT BE RESPONSIBLE FOR ANY MEDIATEK
# SOFTWARE RELEASES MADE TO RECEIVER'S SPECIFICATION OR TO CONFORM TO A PARTICULAR
# STANDARD OR OPEN FORUM. RECEIVER'S SOLE AND EXCLUSIVE REMEDY AND MEDIATEK'S ENTIRE AND
# CUMULATIVE LIABILITY WITH RESPECT TO THE MEDIATEK SOFTWARE RELEASED HEREUNDER WILL BE,
# AT MEDIATEK'S OPTION, TO REVISE OR REPLACE THE MEDIATEK SOFTWARE AT ISSUE,
# OR REFUND ANY SOFTWARE LICENSE FEES OR SERVICE CHARGE PAID BY RECEIVER TO
# MEDIATEK FOR SUCH MEDIATEK SOFTWARE AT ISSUE.
#
# The following software/firmware and/or related documentation ("MediaTek Software")
# have been modified by MediaTek Inc. All revisions are subject to any receiver's
# applicable license agreements with MediaTek Inc.

ifneq ($(TARGET_BUILD_PDK),true)

LOCAL_PATH := $(call my-dir)
cxp_support := no

ifdef MSSI_MTK_CARRIEREXPRESS_PACK
    ifneq ($(strip $(MSSI_MTK_CARRIEREXPRESS_PACK)),no)
        cxp_support := yes
    endif
endif

ifeq ($(strip $(cxp_support)),yes)
    include $(LOCAL_PATH)/MtkBootanimation/Android.mk
    $(foreach OP_SPEC, $(MTK_REGIONAL_OP_PACK), \
        $(eval OPTR := $(word 1,$(subst _,$(space),$(OP_SPEC)))) \
        $(eval OPTR_DIR := $(TMP_PATH)/../$(OPTR)) \
        $(if $(wildcard $(OPTR_DIR)/Android.mk), \
            $(eval include $(OPTR_DIR)/Android.mk), \
            $(eval include $(call all-makefiles-under,$(OPTR_DIR))) \
        ))
else
    include $(call all-makefiles-under,$(call my-dir))
endif
endif
```

### 8. 添加 `vendor/mediatek/proprietary/operator/frameworks/bootanimation/MtkBootanimation/Android.mk`

```makefile
bootanimation_CommonCFlags = -DGL_GLEXT_PROTOTYPES -DEGL_EGLEXT_PROTOTYPES
bootanimation_CommonCFlags += -Wall -Werror -Wunused -Wunreachable-code -Wno-deprecated-declarations


# bootanimation executable
# =========================================================

LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_CFLAGS += ${bootanimation_CommonCFlags}

LOCAL_SHARED_LIBRARIES := \
    libOpenSLES \
    libandroidfw \
    libbase \
    libbinder \
    libmtkbootanimation \
    libcutils \
    liblog \
    libutils \

LOCAL_SRC_FILES:= \
    BootAnimationUtil.cpp \

#ifeq ($(PRODUCT_IOT),true)
#LOCAL_SRC_FILES += \
#    iot/iotbootanimation_main.cpp \
#    iot/BootAction.cpp

#LOCAL_SHARED_LIBRARIES += \
#    libandroidthings \
#    libbase \
#    libbinder

#LOCAL_STATIC_LIBRARIES += cpufeatures

#else

LOCAL_SRC_FILES += \
    bootanimation_main.cpp \
    audioplay.cpp \

#endif  # PRODUCT_IOT

LOCAL_MODULE:= mtkbootanimation

LOCAL_INIT_RC := mtkbootanim.rc

ifdef TARGET_32_BIT_SURFACEFLINGER
LOCAL_32_BIT_ONLY := true
endif

include $(BUILD_EXECUTABLE)
#ifeq (OP01,$(word 1,$(subst _, ,$(OPTR_SPEC_SEG_DEF))))
#    ifeq ($(strip $(MTK_BSP_PACKAGE)), yes)
#        include $(BUILD_EXECUTABLE)
#    endif
#else ifeq (OP02,$(word 1,$(subst _, ,$(OPTR_SPEC_SEG_DEF))))
#    ifeq ($(strip $(MTK_BSP_PACKAGE)), yes)
#        include $(BUILD_EXECUTABLE)
#    endif
#else ifeq (OP09,$(word 1,$(subst _, ,$(OPTR_SPEC_SEG_DEF))))
#    ifeq ($(strip $(MTK_BSP_PACKAGE)), yes)
#        include $(BUILD_EXECUTABLE)
#    endif
#endif

# libbootanimation
# ===========================================================

include $(CLEAR_VARS)
LOCAL_MODULE := libmtkbootanimation
LOCAL_CFLAGS += ${bootanimation_CommonCFlags}

LOCAL_SRC_FILES:= \
    BootAnimation.cpp


#ifdef MSSI_MTK_CARRIEREXPRESS_PACK
#    ifneq ($(strip $(MSSI_MTK_CARRIEREXPRESS_PACK)), no)
#        LOCAL_CFLAGS += -DMSSI_MTK_CARRIEREXPRESS_PACK
#        LOCAL_CPPFLAGS += -DMSSI_MTK_CARRIEREXPRESS_PACK
#    endif
#endif

LOCAL_CFLAGS += ${bootanimation_CommonCFlags}
LOCAL_C_INCLUDES += \
    external/tinyalsa/include \
    frameworks/wilhelm/include \
    vendor/mediatek/proprietary/hardware/terservice/include/

LOCAL_SHARED_LIBRARIES := \
    libcutils \
    liblog \
    libandroidfw \
    libutils \
    libbinder \
    libui \
    libhwui \
    libEGL \
    libETC1 \
    libGLESv2 \
    libmedia \
    libGLESv1_CM \
    libgui \
    libtinyalsa \
    libbase \
    libterservice


LOCAL_C_INCLUDES += $(TOP)/$(MTK_ROOT)/frameworks-ext/native/include
LOCAL_C_INCLUDES += external/skia/include
ifdef TARGET_32_BIT_SURFACEFLINGER
LOCAL_32_BIT_ONLY := true
endif

include $(BUILD_SHARED_LIBRARY)
#ifeq (OP01,$(word 1,$(subst _, ,$(OPTR_SPEC_SEG_DEF))))
#    ifeq ($(strip $(MTK_BSP_PACKAGE)), yes)
#        include $(BUILD_SHARED_LIBRARY)
#    endif
#else ifeq (OP02,$(word 1,$(subst _, ,$(OPTR_SPEC_SEG_DEF))))
#    ifeq ($(strip $(MTK_BSP_PACKAGE)), yes)
#        include $(BUILD_SHARED_LIBRARY)
#    endif
#else ifeq (OP09,$(word 1,$(subst _, ,$(OPTR_SPEC_SEG_DEF))))
#    ifeq ($(strip $(MTK_BSP_PACKAGE)), yes)
#        include $(BUILD_SHARED_LIBRARY)
#    endif
#endif
```

### 9. 修改 `vendor/mediatek/proprietary/operator/frameworks/bootanimation/MtkBootanimation/BootAnimation.cpp`

```diff
@@ -45,7 +45,7 @@
 #include <ui/PixelFormat.h>
 #include <ui/Rect.h>
 #include <ui/Region.h>
-#include <ui/DisplayInfo.h>
+#include <ui/DisplayConfig.h>
 
 #include <gui/ISurfaceComposer.h>
 #include <gui/Surface.h>
@@ -77,6 +77,9 @@
 
 #define PATH_COUNT 3
 
+#include <binder/IServiceManager.h>
+#include "ITerService.h"
+#define REGIONAL_BOOTANIM_GET_MNC   "persist.vendor.bootanim.mnc"
 
 #ifdef MSSI_MTK_CARRIEREXPRESS_PACK
 #define GLOBAL_DEVICE_BOOTANIM_OPTR_NAME "persist.vendor.operator.optr"
@@ -412,19 +415,34 @@ status_t BootAnimation::readyToRun() {
 
     mAssets.addDefaultAssets();
 
-    sp<IBinder> dtoken(SurfaceComposerClient::getBuiltInDisplay(
-            ISurfaceComposer::eDisplayIdMain));
-    DisplayInfo dinfo;
-    status_t status = SurfaceComposerClient::getDisplayInfo(dtoken, &dinfo);
+    // sp<IBinder> dtoken(SurfaceComposerClient::getBuiltInDisplay(
+    //         ISurfaceComposer::eDisplayIdMain));
+    // DisplayInfo dinfo;
+    // status_t status = SurfaceComposerClient::getDisplayInfo(dtoken, &dinfo);
+    // if (status)
+    //     return -1;
+    // /// M: The tablet rotation maybe 90/270 degrees, so set the lcm config for tablet
+    // //SurfaceComposerClient::setDisplayProjection(dtoken, DisplayState::eOrientationDefault, Rect(dinfo.w, dinfo.h), Rect(dinfo.w, dinfo.h));
+    // t.setDisplayProjection(dtoken, DisplayState::eOrientationDefault, Rect(dinfo.w, dinfo.h), Rect(dinfo.w, dinfo.h));
+    // t.apply();
+    // // create the native surface
+    // sp<SurfaceControl> control = session()->createSurface(String8("BootAnimation"),
+    //         dinfo.w, dinfo.h, PIXEL_FORMAT_RGB_565);
+
+    sp<IBinder> dtoken = SurfaceComposerClient::getInternalDisplayToken();
+    DisplayConfig displayConfig;
+    status_t status = SurfaceComposerClient::getActiveDisplayConfig(dtoken, &displayConfig);
     if (status)
         return -1;
+    ui::Size resolution = displayConfig.resolution;
     /// M: The tablet rotation maybe 90/270 degrees, so set the lcm config for tablet
     //SurfaceComposerClient::setDisplayProjection(dtoken, DisplayState::eOrientationDefault, Rect(dinfo.w, dinfo.h), Rect(dinfo.w, dinfo.h));
-    t.setDisplayProjection(dtoken, DisplayState::eOrientationDefault, Rect(dinfo.w, dinfo.h), Rect(dinfo.w, dinfo.h));
+    t.setDisplayProjection(dtoken, ui::ROTATION_0, Rect(resolution.getWidth(), resolution.getHeight()), 
+            Rect(resolution.getWidth(), resolution.getHeight()));
     t.apply();
     // create the native surface
     sp<SurfaceControl> control = session()->createSurface(String8("BootAnimation"),
-            dinfo.w, dinfo.h, PIXEL_FORMAT_RGB_565);
+            resolution.getWidth(), resolution.getHeight(), PIXEL_FORMAT_RGB_565);
 
 /*
     SurfaceComposerClient::openGlobalTransaction();
@@ -538,7 +556,8 @@ bool BootAnimation::threadLoop()
     // We have no bootanimation file, so we use the stock android logo
     // animation.
     sp<MediaPlayer> mediaplayer;
-    const char* resourcePath = NULL;
+    // const char* resourcePath = NULL;
+    const char* resourcePath = initAudioPath();
     status_t mediastatus = NO_ERROR;
     if (resourcePath != NULL) {
         bPlayMP3 = true;
@@ -1510,6 +1529,7 @@ const char* BootAnimation::initAudioPath() {
 void BootAnimation::initBootanimationZip() {
     ZipFileRO* zipFile = NULL;
     String8     ZipFileName;
+    char BootanimFileName[PROPERTY_VALUE_MAX];
 #ifdef MSSI_MTK_CARRIEREXPRESS_PACK
     char OPTR[PROPERTY_VALUE_MAX];
     // ter-service
```

