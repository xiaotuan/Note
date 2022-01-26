[toc]

> 下面的代码来自 mokoid 工程，mokoid 工程下载方法如下：
>
> ```shell
> $ svn checkout http://mokoid.googlecode.com/svn/trunk/mokoid-read-only
> ```

在 Android 下有以下两种访问 HAL 的方法：

+ Android  的 app 直接通过 service 调用 `.so` 格式的 JNI：此方法比较简单高效，但是不正规。
+ **经过 Manager 调用 Service：** 此方法实现起来比较复杂，但更符合目前的 Android 框架。

### 1. 直接调用 service 方法的实现代码

#### 1.1 HAL 层的实现代码

**hardware/modules/led/led.c** 的实现代码如下：

```c
#define LOG_TAG "MokoidLedStub"
#include <hardware/hardware.h>
#include <fcntl.h>
#include <errno.h>
#include <cutils/log.h>
#include <cutils/atomic.h>
#include <mokoid/led.h>
/***********************************************************************/
int led_device_close(struct hw_device_t* device)
{
    struct led_control_device_t* ctx = (struct led_control_device_t*)device;
    if (ctx) {
        free(ctx);
    }
    return 0;
}

int led_on(struct led_control_device_t *dev, int32_t led)
{
    LOGI("LED Stub: set %d on.", led);
    return 0;
}

int led_off(struct led_control_device_t *dev, int32_t led)
{
    LOGI("LED Stub: set %d off.", led);
    return 0;
}

static int led_device_open(const struct hw_module_t* module, const char* name, 
        struct hw_device_t** device)
{
    struct led_control_device_t *dev;
    dev = (struct led_control_device_t *)malloc(sizeof(*dev));
    memset(dev, 0, sizeof(*dev));
    dev->common.tag = HARDWARE_DEVICE_TAG;
    dev->common.version = 0;
    dev->common.module = module;
    dev->common.close = led_device_close;
    dev->set_on = led_on;   // 实例化支持的操作
    dev->set_off = led_off;
    *device = &dev->common; // 将实例化的 led_control_device_t 地址返回给 JNI 层
success:
    return 0;
}

static struct hw_module_methods_t led_module_methods = {
    open: led_device_open
};

const struct led_module_t HAL_MODULE_INFO_SYM = {
    // 定义此对象相当于向系统注册了一个 ID 为 LED_HARDWARE_MODULE_ID 的 stub
    common: {
        tag: HARDWARE_MODULE_TAG,
        version_major: 1,
        version_minor: 0,
        id: LED_HARDWARE_MODULE_ID,
        name: "Sample LED Stub",
        author: "The Mokoid Open Source Project",
        methods: &led_module_methods,   // 实现了一个 open 的方法供 JNI 层调用
    }
    /* supporting APIs go here */
};
```

#### 1.2 JNI 层的实现代码

**frameworks/base/service/jni/com_mokoid_server_ledService.cpp**

```cpp
struct led_control_device_t *sLedDevice = NULL;
static jboolean mokoid_setOn(JNIEnv* env, jobject thiz, jint led) {
    LOGI("LedService JNI: mokoid_setOn() is invoked.");
    if (sLedDevice == NULL) {
        LOGI("LedService JNI: sLedDevice was not fetched correctly.");
        return -1;
    } else {
        return sLedDevice->set_on(sLedDevice, led); // 调用 HAL 层的注册方法
    }
}

static jboolean mokoid_setOff(JNIEnv* env, jobject thiz, jint led) {
    LOGI("LedService JNI: mokoid_setOff() is invoked.");
    if (sLedDevice == NULL) {
        LOGI("LedService JNI: sLedDevice was not fetched correctly.");
        return -1;
    } else {
        sLedDevice->set_on(sLedDevice, led);    // 调用 HAL 层的注册方法
    }
}

/** helper APIs——JNI 通过 LED_HARDSOFTWARE_MODULE_ID 找到对应的 stub */
static inline int led_control_open(const struct hw_module_t* module, struct led_control_device_t** device) {
    return module->methods->open(module, LED_HARDWARE_MODULE_ID, (struct hw_device_t**)device);
}

static jboolean mokoid_init(JNIEnv *env, jclass clazz) {
    led_module_t* module;
    if (hw_get_module(LED_HARDWARE_MODULE_ID, (const hw_module_t**)&module) == 0) {
        LOGI("LedService JNI: LED Stub found.");
        if (led_control_open(&module->common, &sLedDevice) == 0) {
            LOGI("LedService JNI: Got Stub operations.");
            return 0;
        }
    }
    LOGE("LedService JNI: Get Stub operations failed.");
    return -1;
}

// JNINativeMethod 是 JNI 层的注册方法
static const JNINativeMethod gMethods[] = {
    {"__init", "() Z", // Framework 层调用 __init 时触发
            (void*)mokoid_init},
    { "_set_on", "(I)Z", (void*)mokoid_setOn},
    { "_set_off", "(I)Z", (void*)mokoid_setOfff},
};

static int registerMethods(JNIEnv* env) {
    static const char* const kClassName = "com/mokoid/server/LedService";
    jclass clazz;
    /* 查找 class */
    clazz = env->FindClass(kClassName);
    if (clazz == NULL) {
        LOGE("Can't find class %s\n", kClassName);
        return -1;
    }
    /* 注册所有方法 */
    if (env->RegisterNatives(clazz, gMethods, sizeof(gMethods) / sizeof(gMethods[0])) != JNI_OK) {
        LOGE("Failed registering methods for %s\n", kClassName);
        return -1;
    }
    /* 填充剩余的 ID cache */
    return 0;
}

// Framework 层加载 JNI 库时调用
jint JNI_OnLoad(JavaVM* vm, void* reserved) {
    JNIEnv* env = NULL;
    jint result = -1;
    if (vm->GetEnv((void**) &env, JNI_VERSION_1_4) != JNI_OK) {
        LOGE("ERROR: GetEnv failed\n");
        goto bail;
    }
    assert(env != NULL);
    if (registerMethods(env) != 0) {
        LOGE("ERROR: PlatformLibrary native registration failed\n");
        goto bail;
    }
    /* 成功，返回有些的版本号 */
    result = JNI_VERSION_1_4;
bail:
    return result;
}
```

#### 1.3 Service 的实现

**frameworks/base/service/java/com/android/server/LedService.java**

```java
package com.mokoid.server;

import android.util.Config;
import android.util.Log;
import android.content.Context;
import android.os.Binder;
import android.os.Bundle;
import android.os.RemoteException;
import android.os.IBinder;
import mokoid.hardware.ILedService;

public final class LedService extends ILedService.Stub {

    static {
        System.load("/system/lib/libmokoid_runtime.so");    // 加载 JNI 动态库
    }

    public LedService() {
        Log.i("LedService", "Go to get LED Stub...");
        _init();
    }

    /*
     * Mokoid LED native methods.
     */
    public boolean setOn(int led) {
        Log.i("MokoidPlatform", "LED On");
        return _set_on(led);
    }

    public boolean setOff(int led) {
        Log.i("MokoidPlatform", "LED Off");
        return _set_off(led);
    }

    private static native boolean _init();  // 声明 JNI 库可以提供的方法
    private static native boolean _set_on(int led);
    private static native boolean _set_off(int led);
}
```

#### 1.4 APP 测试程序的实现代码

**apps/LedClient/src/com/mokoid/LedClient/LedClient.java**

```java
package com.mokoid.LedClient;

import com.mokoid.server.LedService;    // 导入 Framework 层的 LedService

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class LedClient extends Activity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // 调用库中的 API
        LedService ls = new LedService();   // 实例化 LedService
        ls.setOn(1);    // 通过 LedService 提供的方法控制底层硬件

        TextView tv = new TextView(this);
        tv.setText("LED 0 is on.");
        setContentView(tv);
    }
}
```

### 2. 通过 Manager 调用 service 的实现代码

#### 2.1 Manager 的实现代码

**frameworks/base/core/java/mokoid/hardware/LedManager.java**

```java
package mokoid.hardware;

import android.content.Context;
import android.os.Binder;
import android.os.Bundle;
import android.os.Parcelable;
import android.os.ParcelFileDescriptor;
import android.os.Process;
import android.os.RemoteException;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import mokoid.hardware.ILedService;

/**
 * 用来访问 Mokoid LedService 的类
 */
public class LedManager {

    private static final String TAG = "LedManager";
    private ILedService mLedService;

    public LedManager() {
        mLedService = ILedService.Stub.asInterface(ServiceManager.getService("led"));

        if (mLedService != null) {
            Log.i(TAG, "The LedManager object is ready.");
        }
    }

    public boolean LedOn(int n) {
        boolean result = false;
        try {
            result = mLedService.setOn(n);
        } catch (RemoteException e) {
            Log.e(TAG, "RemoteException in LedManager.LedOn: ",  e);
        }
        return result;
    }

    public boolean LedOff(int n) {
        boolean result = false;

        try {
            result = mLedService.setOff(n);
        } catch (RemoteException e) {
            Log.e(TAG, "RemoteException in LedManager.LedOff: ", e);
        }
        return result;
    }
}
```

**frameworks/base/core/java/mokoid/hardware/ILedService.java**

```java
package mokoid.hardware;

interface ILedService {
    boolean setOn(int led);
    boolean setOff(int led);
}
```

#### 2.2 SystemServer 的实现代码

**apps/LedTest/src/com/mokoid/LedTest/LedSystemServer.java**

```java
package com.mokoid.LedTest;

import com.mokoid.server.LedService;

import android.os.IBinder;
import android.os.ServiceManager;
import android.util.Log;
import android.app.Service;
import android.content.Context;
import android.content.Intent;

// 代表一个后台进程
public class LedSystemServer extends Service {
    
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onStart(Intent intent, int startId) {
        Log.i("LedSystemServer", "Start LedService...");
        LedService ls = new LedService();
        try {
            ServiceManager.addService("led", ls);
        } catch (RuntimeException e) {
            Log.e("LedSystemServer", "Start LedService failed.");
        }
    }
}
```

#### 2.3 APP 测试程序

**mokoid-read-only/apps/LedTest/src/com/mokoid/LedTest/LedTest.java**

```java
package com.mokoid.LedTest;

import mokoid.hardware.LedManager;
import com.mokoid.server.LedService;
import android.app.Activity;
import android.osBundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Button;
import android.content.Intent;
import android.view.View;

public class LedTest extends Activity implements View.OnClickListener {

    private LedManager mLedManager = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // 在一个独立的进程启动 LedService
        startService(new Intent("com.mokoid.systemserver"));
        // 测试
        Button btn = new Button(this);
        btn.setText("Click to turn LED 1 On");
        btn.setOnClickListener(this);
        setContentView(btn);
    }

    public void onClick(View v) {
        // 获取 LedManager
        if (mLedManager == null) {
            Log.i("LedTest", "Create a new LedManager object.");
            mLedManager = new LedManager();
        }
        if (mLedManager != null) {
            Log.i("LedTest", "Got LedManager object.");
        }
        mLedManager.LedOn(1);
        TextView tv = new TextView(this);
        tv.setText("LED 1 is On.");
        setContentView(tv);
    }
}
```

