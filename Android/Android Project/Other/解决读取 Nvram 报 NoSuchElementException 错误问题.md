[toc]

### 1. MTK

#### 1.1 MT8765

##### 1.1.1 Android R

读取 Nvram 代码如下：

```java
import com.android.internal.util.HexDump;
import vendor.mediatek.hardware.nvram.V1_0.INvram;

private static final String PRODUCT_INFO_FILENAME = "PRODUCT_INFO";
private static final int VERSION_LENGTH = 12;
private static final int VERSION_INDEX = 1023 - VERSION_LENGTH;

private static byte[] readNvramData(int position, int length) {
    Log.d(TAG, "readNvramData=>position: " + position + ", length: " + length);
    byte[] data = new byte[length];
    try {
        INvram service = INvram.getService(true);
        if (service != null) {
            String originStr = service.readFileByName(PRODUCT_INFO_FILENAME, position + length);
            Log.d(TAG, "readNvramData=>readFileByName: " + originStr + ", length: " + originStr.length());
            if (originStr.length() >= (position + length)) {
                byte[] hexStringToByteArray = HexDump.hexStringToByteArray(originStr.substring(0, originStr.length() - 1));
                for (int i = position, j = 0; i < (position + length); i++, j++) {
                    data[j] = hexStringToByteArray[i];
                }
            } else {
                Log.e(TAG, "readNvramData=>The format of NVRAM is not correct");
            }
        } else {
            Log.e(TAG, "readNvramData=>Service is null.");
        }
    } catch (Exception e) {
        Log.d(TAG, "readNvramData=>error: ", e);
    }
    return data;
}

private static int writeNvramData(byte[] data, int position) {
    Log.d(TAG, "writeNvramData=>position: " + position + ", data: " + Arrays.toString(data));
    int result = -1;
    try {
        INvram service = INvram.getService(true);
        if (service != null) {
            String originStr = service.readFileByName(PRODUCT_INFO_FILENAME, position + data.length);
            Log.d(TAG, "writeNvramData=>originStr: " + originStr + ", length: " + originStr.length());
            if (originStr.length() >= (position + data.length)) {
                byte[] originData = HexDump.hexStringToByteArray(originStr.substring(0, originStr.length() - 1));
                for (int i = position, j = 0; i < (position + data.length); i++, j++) {
                    originData[i] = data[j];
                }
                ArrayList<Byte> arrayList = new ArrayList<>(position + data.length);
                for (int i = 0; i < originData.length; i++) {
                    arrayList.add(originData[i]);
                }
                result = service.writeFileByNamevec(PRODUCT_INFO_FILENAME, arrayList.size(), arrayList);
            } else {
                Log.e(TAG, "writeNvramData=>The format of NVRAM is not correct");
            }
        } else {
            Log.e(TAG, "writeNvramData=>Service is null.");
        }
    } catch (Exception e) {
        Log.e(TAG, "writeNvramData=>error: ", e);
    }
    return result;
}
```

在 Android.bp 文件中引入如下库：

```
vendor.mediatek.hardware.nvram-V1.0-java
```

运行程序后报如下错误：

```
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator: readNvramData=>error:
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator: java.util.NoSuchElementException
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at android.os.HwBinder.getService(Native Method)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at vendor.mediatek.hardware.nvram.V1_0.INvram.getService(INvram.java:113)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at vendor.mediatek.hardware.nvram.V1_0.INvram.getService(INvram.java:120)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator.readNvramData(KeyguardViewMediator.java:2886)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator.getVersionFromNv(KeyguardViewMediator.java:2840)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator.needShowPasswordDialog(KeyguardViewMediator.java:2756)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator.access$3000(KeyguardViewMediator.java:174)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator$3.keyguardGone(KeyguardViewMediator.java:738)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.statusbar.phone.StatusBarKeyguardViewManager.hide(StatusBarKeyguardViewManager.java:682)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator.handleStartKeyguardExitAnimation(KeyguardViewMediator.java:2225)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator.access$5600(KeyguardViewMediator.java:174)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.systemui.keyguard.KeyguardViewMediator$6.handleMessage(KeyguardViewMediator.java:1882)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at android.os.Handler.dispatchMessage(Handler.java:106)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at android.os.Looper.loop(Looper.java:223)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at android.app.ActivityThread.main(ActivityThread.java:7723)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at java.lang.reflect.Method.invoke(Native Method)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:612)
08-11 00:25:11.791  1485  1485 D KeyguardViewMediator:  at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:997)
```

经查是 SELinux 权限导致的，SELinux 权限报错如下：

```
08-10 13:04:56.397   372   372 E SELinux : avc:  denied  { find } for interface=vendor.mediatek.hardware.nvram::INvram sid=u:r:platform_app:s0:c512,c768 pid=4573 scontext=u:r:platform_app:s0:c512,c768 tcontext=u:object_r:nvram_agent_binder_hwservice:s0 tclass=hwservice_manager permissive=0
08-11 00:25:11.788  1485  1485 W ndroid.systemui: type=1400 audit(0.0:293): avc: denied { call } for scontext=u:r:platform_app:s0:c512,c768 tcontext=u:r:nvram_agent_binder:s0 tclass=binder permissive=0 app=com.android.systemui
```

通过如下命令：

```shell
$ audit2allow -i log > audio.txt
```

分析出应用缺少如下 SELinux 权限：

```
# Date: 2023/08/10
# Operation: Nvram
# Purpose: SystemUI need Read and Write Nvram
allow platform_app nvram_agent_binder_hwservice:hwservice_manager find;
allow platform_app nvram_agent_binder:binder call;
```

添加上述权限后，代码运行正常。