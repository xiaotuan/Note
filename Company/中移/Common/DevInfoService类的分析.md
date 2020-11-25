DevInfoService 类位于 frameworks/base/services/java/com/android/server/DevInfoService.java 下。它的主要功能是向外部提供设备信息和修改设备信息的方法，而设备信息的来源于 content://stbconfig/authentication/ 内容提供器，/system/etc/deviceinfo.txt 文件。并将设备信息写入 /swdb/devinfo/deviceinfo.txt （非长虹）或 /params/keypara.ini （长虹）文件中。

DevInfoService 类在构造方法中通过 ro.stb.manu 属性来判断设备是否是长虹设备，并以此来选择是加载 /params/keypara.ini 文件，还是 /swdb/devinfo/deviceinfo.txt 文件。

```java
public DevInfoService(Context context) {
    this.mContext = context;
    mStbManu = SystemProperties.get("ro.stb.manu");
    mDevInfoFilePath = "ch".equals(mStbManu)?mChDevInfoFile:mZgDevInfoFile; 
    mDevInfoFile = new File(mDevInfoFilePath);
    try {
        if (!mDevInfoFile.exists()) {
            mDevInfoFile.getParentFile().mkdir();
            mDevInfoFile.createNewFile();
        }
        mDevInfos = new Properties();
        mDevInfos.load(new FileInputStream(mDevInfoFile));
    } catch (Exception e) {
        e.printStackTrace();
    }

    try{

        File file = new File("/data/swupgradeparameters.txt");
        if(file.exists())
        {
            if("ch".equals(mStbManu)){
                setPlatfromMode();
            }
            //				file.delete();
        }
        loadDefaultDevinfo();
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

上面的方法首先创建 deviceinfo.txt 文件，并将该文件加载到属性流中。然后根据 /data/swupgradeparameters.txt 文件是否存在和设备是否是长虹设备来调用 setPlatfromMode() 方法。下面我们来看下 setPlatfromMode() 方法的内容：

```java
private void setPlatfromMode() {
    String value = null;
    value = SystemProperties.get("persist.sys.ch.areacode");
    int valueToint = Integer.parseInt(value); 
    int[] arr = new int[]{531,533,634,530,539,538,537,534,635,546,543,632,532,631,535,536,633};
    int index=0;
    for( int i=0;i<arr.length;i++)
    {
        if(valueToint == arr[i]){
            index = i;
            Secure.putString(mContext.getContentResolver(),"initialization_wizard","1");
            Log.e(TAG, "   value ="+value +" index = "+i);
        }
    }
    if(index >= 0 && index <= 11){
        Secure.putString(mContext.getContentResolver(),"platform_mode","huawei");
    }else if (index >= 12 && index <=16){
        Secure.putString(mContext.getContentResolver(),"platform_mode","zte");
    }
}
```

setPlatfromMode() 方法通过判断区域代码是否是 {531,533,634,530,539,538,537,534,635,546,543,632,532,631,535,536,633} 中的其中一个来设置 initialization_wizard 和 platform_mode 属性的值。

在 update() 方法中可以看到里面通过 sys.service.swprotect 属性的值来决定外部是否可以更新 deviceinfo.txt 文件的内容。

```java
/** Make sure the caller has permission to write this data.
     ** @throws SecurityException if the caller is forbidden to write. 
     */
@Override
public int update(String name, String value, int attribute) throws RemoteException, SecurityException {
    int ret = -1;
    FileOutputStream fos = null;
    String swprotect = null;
    int uid = Binder.getCallingUid();

    swprotect = SystemProperties.get("sys.service.swprotect","false");

    if(swprotect.equals("true") && (uid > Process.FIRST_APPLICATION_UID-1)){
        throw new SecurityException(
            String.format("Permission denial: writing to secure settings requires %1$s",
                          android.Manifest.permission.WRITE_SECURE_SETTINGS));
    }

    if(VDBG)
        Log.d(TAG, "update... name=" + name +",value="+value);

    ......
    return ret;
}
```

