[toc]

### 1. MTK

#### 1.1 MT8781

##### 1.1.1 Android T

1. 修改 `sys/frameworks/av/media/mtp/MtpServer.cpp` 文件中 `MtpResponseCode MtpServer::doGetDeviceInfo()` 方法的如下代码：

   ```diff
   @@ -533,8 +533,14 @@ MtpResponseCode MtpServer::doGetDeviceInfo() {
        mData.putAUInt16(captureFormats); // Capture Formats
        mData.putAUInt16(playbackFormats);  // Playback Formats
    
   +    // Modify MTP device model and manufacturer property by qty {{&&
   +    /*
        mData.putString(mDeviceInfoManufacturer); // Manufacturer
        mData.putString(mDeviceInfoModel); // Model
   +    */
   +    mData.putString(mDeviceInfoManufacturer); // Manufacturer
   +    mData.putString("A90"); // Model
   +    // &&}}
        mData.putString(mDeviceInfoDeviceVersion); // Device Version
        mData.putString(mDeviceInfoSerialNumber); // Serial Number
    
   ```

2. 修改 `sys/frameworks/base/media/java/android/mtp/MtpDatabase.java` 文件中 `getDeviceProperty(()` 方法的如下代码：

   ```diff
   @@ -687,7 +687,10 @@ public class MtpDatabase implements AutoCloseable {
                case MtpConstants.DEVICE_PROPERTY_SYNCHRONIZATION_PARTNER:
                case MtpConstants.DEVICE_PROPERTY_DEVICE_FRIENDLY_NAME:
                    // writable string properties kept in shared preferences
   -                value = Build.MODEL;
   +                               // Modify the MTP name by qty at 2023-02-25 {{&&
   +                // value = mDeviceProperties.getString(Integer.toString(property), "");
   +                               value = "A90";
   +                               // &&}}
                    length = value.length();
                    if (length > 255) {
                        length = 255;
   ```

   