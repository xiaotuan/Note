第一种方式：
1.修改\android-mst786_RT380_BMW\device\mstar\common\app\Android.mk
添加以下代码：

```make
include $(CLEAR_VARS)
LOCAL_MODULE := EasyConnected.RT01.4.4.0-d012be6-170802.apk
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := APPS
#LOCAL_MODULE_PATH := $(TARGET_OUT_DATA_APPS)
LOCAL_CERTIFICATE := platform
LOCAL_SRC_FILES := $(LOCAL_MODULE)
include $(BUILD_PREBUILT)
```

2.修改\android-mst786_RT380_BMW\device\mstar\mstarcedric3\full_mstarcedric3.mk
添加EasyConnected.RT01.4.4.0-d012be6-170802.apk \
完整代码如下 ：

```make
PRODUCT_PACKAGES += \
	uartdebug \
	busybox \
	LocalMM \
	Update \
	com.mstar.android.media \
	libcalibrationjni \
	libgetvbidata_jni \
	RtkDaemon \
	Camcorder \
	usbDongle.apk \
	librtkdaemonjni \
	rt_mcu \
	EasyConnected.RT01.4.4.0-d012be6-170802.apk \
	finalcam.apk \
	fuxinPDF_29.apk \
	kuaituv4.5.3.apk 
```

第二种方式：
修改\android-mst786_RT380_BMW\device\mstar\mstarcedric3\full_mstarcedric3.mk
添加如下代码：

```make
PRODUCT_COPY_FILES += \
	  device/mstar/common/app/EasyConnected.RT01.4.4.0-d012be6-170802.apk:system/app/EasyConnected.RT01.4.4.0-d012be6-170802.apk

PRODUCT_COPY_FILES += \
    device/mstar/mstarcedric3/CarEasyConnect/xbin/adb-ec:system/xbin/adb-ec \
    device/mstar/mstarcedric3/CarEasyConnect/xbin/usb_modeswitch-ec:system/xbin/usb_modeswitch-ec \
    device/mstar/mstarcedric3/CarEasyConnect/lib/libairplay-jni.so:system/lib/libairplay-jni.so \
    device/mstar/mstarcedric3/CarEasyConnect/lib/libcshell.so:system/lib/libcshell.so \
    device/mstar/mstarcedric3/CarEasyConnect/lib/libecgl2jni.so:system/lib/libecgl2jni.so \
    device/mstar/mstarcedric3/CarEasyConnect/lib/libecgl2jni_41.so:system/lib/libecgl2jni_41.so \
    device/mstar/mstarcedric3/CarEasyConnect/lib/libecgl2jni_vfpv3.so:system/lib/libecgl2jni_vfpv3.so \
    device/mstar/mstarcedric3/CarEasyConnect/lib/libgst_render.so:system/lib/libgst_render.so \
	  device/mstar/mstarcedric3/CarEasyConnect/lib/libmDNSEmbedded.so:system/lib/libmDNSEmbedded.so \
	  device/mstar/mstarcedric3/CarEasyConnect/lib/libmediaserver.so:system/lib/libmediaserver.so \
    device/mstar/mstarcedric3/CarEasyConnect/lib/libusbconfig.so:system/lib/libusbconfig.so
```

第三种升级：
直接把apk文件放入\android-mst786_RT380_BMW\out\target\product\mstarcedric3\system\app目录下,这种方法执行make clear会被清除