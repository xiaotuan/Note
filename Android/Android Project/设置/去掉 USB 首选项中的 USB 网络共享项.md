[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android U

修改 `u_sys/vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/android/settings/connecteddevice/usb/UsbDetailsFunctionsController.java` 文件中的如下代码：

```diff
@@ -49,7 +49,7 @@ public class UsbDetailsFunctionsController extends UsbDetailsController
 
     static {
         FUNCTIONS_MAP.put(UsbManager.FUNCTION_MTP, R.string.usb_use_file_transfers);
-        FUNCTIONS_MAP.put(UsbManager.FUNCTION_RNDIS, R.string.usb_use_tethering);
+        // FUNCTIONS_MAP.put(UsbManager.FUNCTION_RNDIS, R.string.usb_use_tethering);
         FUNCTIONS_MAP.put(UsbManager.FUNCTION_MIDI, R.string.usb_use_MIDI);
         FUNCTIONS_MAP.put(UsbManager.FUNCTION_PTP, R.string.usb_use_photo_transfers);
         FUNCTIONS_MAP.put(UsbManager.FUNCTION_UVC, R.string.usb_use_uvc_webcam);
```

