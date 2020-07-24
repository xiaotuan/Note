1. 创建 AIDL 文件，例如：IConnectServiceInterface.aidl。
2. 创建回调的 AIDL 文件，例如：IConnectServiceCallback.aidl。

```java
package com.wise.gate;

interface IConnectSerivceCallback {

    void onInitCompleted(boolean success);

}
```

3. 在 IConnectServiceInterface.aidl 文件中添加设置回调的方法。

```java
package com.wise.gate;

import com.wise.gate.IConnectSerivceCallback;

interface IConnectServiceInterface {

    void init();
    void registerCallback(IConnectSerivceCallback cb);
    void unregisterCallback(IConnectSerivceCallback cb);

}
```

4. 在 Service 中实现 IConnectServiceInterface.aidl 接口。

```java
package com.wise.gate.server;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteCallbackList;
import android.os.RemoteException;

import com.wise.gate.IConnectSerivceCallback;
import com.wise.gate.IConnectServiceInterface;

public class ConnectService extends Service {

    private RemoteCallbackList<IConnectSerivceCallback> mCallbacks;

    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        mCallbacks = new RemoteCallbackList<>();
    }


    private IConnectServiceInterface.Stub mBinder = new IConnectServiceInterface.Stub() {

        @Override
        public void init() throws RemoteException {

        }

        @Override
        public void registerCallback(IConnectSerivceCallback cb) {
            if (cb != null) {
                mCallbacks.register(cb);
            } else {
                Log.w(ConnectService.this, "registerCallback=>callback is null.");
            }
        }

        @Override
        public void unregisterCallback(IConnectSerivceCallback cb) {
            if (cb != null) {
                mCallbacks.unregister(cb);
            } else {
                Log.w(ConnectService.this, "unregisterCallback=>callback is null.");
            }
        }
    };

}
```

6. 在需要接收回调的类中实现 IConnectServiceCallback.aidl 接口，并将其注册到服务中。

```java
public class WiseGate extends AppCompatActivity {

    private IConnectServiceInterface mService;

    private boolean isInited;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(this, R.layout.activity_wise_gate);
		mService.registerCallback(mServiceCallback);
    }


    @Override
    protected void onDestroy() {
        super.onDestroy();
    }

    private IConnectSerivceCallback.Stub mServiceCallback = new IConnectSerivceCallback.Stub() {

        @Override
        public void onInitCompleted(boolean success) throws RemoteException {

        }

    };

}
```

7. 在服务中调用回调接口。

```java
public void notifyInitCompleted(boolean success) {
        synchronized (mLock) {
            mCallbacks.beginBroadcast();
            for (int i = 0; i < mCallbacks.getRegisteredCallbackCount(); i++) {
                try {
                    mCallbacks.getBroadcastItem(i).onInitCompleted(success);
                } catch (Exception ignore) {}
            }
            mCallbacks.finishBroadcast();
        }
    }
```

