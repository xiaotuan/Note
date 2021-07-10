[toc]

### 1. 展讯平台

#### 1.1 Android R

修改 `frameworks/av/media/mtp/MtpServer.cpp` 文件，将 `doGetDeviceInfo()` 函数的如下代码：

```cpp
mData.putString(mDeviceInfoManufacturer); // Manufacturer
mData.putString(mDeviceInfoModel); // Model
mData.putString(mDeviceInfoDeviceVersion); // Device Version
mData.putString(mDeviceInfoSerialNumber); // Serial Number
```

修改成：

```cpp
mData.putString(mDeviceInfoManufacturer); // Manufacturer
mData.putString("Magnum Pro"); // Model
mData.putString(mDeviceInfoDeviceVersion); // Device Version
mData.putString(mDeviceInfoSerialNumber); // Serial Number
```



