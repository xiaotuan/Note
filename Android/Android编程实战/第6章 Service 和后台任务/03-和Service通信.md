[toc]

### 1. 使用 Intent 进行异步消息传递

有多种方法可以实现这种机制，但是如果想保持 IntentService 的异步行为，最好的方法还是发送广播，该方法和在 IntentService 中启动一个操作一样简单。

```java
private void uploadPhoto(Bitmap photo) {
    // TODO: 网络调用
    sendBroadcast(new Intent(BROADCAST_UPLOAD_COMPLETED));
}
```

这种解决方案的缺点是通知的结果受限于 Intent。此外，该方法也不适合在 IntentService 和 Activity 之间进行大规模快速更新操作，比如更新进度条，因为这会阻塞系统。

### 2. 本地绑定的 Service

下面使用本地 Binder 来修改之前的例子。

```java
package com.aptl.services;

import android.app.Notification;
import android.app.Service;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Binder;
import android.os.IBinder;

/**
 * @author Erik Hellman
 */
public class MyLocalService extends Service {
    private static final int NOTIFICATION_ID = 1001;
    private LocalBinder mLocalBinder = new LocalBinder();
    private Callback mCallback;

    public IBinder onBind(Intent intent) {
        return mLocalBinder;
    }

    public void performLongRunningOperation(MyComplexDataObject dataObject) {
        new MyAsyncTask().execute(dataObject);
    }

    public void setCallback(Callback callback) {
        mCallback = callback;
    }

    public class LocalBinder extends Binder {
        public MyLocalService getService() {
            return MyLocalService.this;
        }
    }

    public interface Callback {
        void onOperationProgress(int progress);
        void onOperationCompleted(MyComplexResult complexResult);
    }

    private final class MyAsyncTask extends AsyncTask<MyComplexDataObject, Integer, MyComplexResult> {

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            startForeground(NOTIFICATION_ID, buildNotification());
        }

        @Override
        protected void onProgressUpdate(Integer... values) {
            if(mCallback != null && values.length > 0) {
                for (Integer value : values) {
                    mCallback.onOperationProgress(value);
                }
            }
        }

        @Override
        protected MyComplexResult doInBackground(MyComplexDataObject... myComplexDataObjects) {
            MyComplexResult complexResult = new MyComplexResult();
            // Actual operation left out for brevity...
            return complexResult;
        }

        @Override
        protected void onPostExecute(MyComplexResult myComplexResult) {
            if(mCallback != null ) {
                mCallback.onOperationCompleted(myComplexResult);
            }
            stopForeground(true);
        }

        @Override
        protected void onCancelled(MyComplexResult complexResult) {
            super.onCancelled(complexResult);
            stopForeground(true);
        }
    }

    private Notification buildNotification() {
        Notification notification = null;
        // Create a notification for the service..
        return notification;
    }
}
```

下面的代码显示了更新后的 Activity。值得注意的变化是 Activity 实现了 MyLocalService.Callback 接口。当在 onServiceConnected() 方法中获取到对 Service 的引用后，调用 setCallback(this) has 方法，以便 Activity 能在操作执行期间受到回调通知。还有一点非常重要，当用户离开 Activity 或者调用 onPause() 时，不要忘记移除回调监听（也就是调用 setCallback(null) 方法），否则可能会导致内存泄漏。

```java
package com.aptl.services;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.view.View;

public class MainActivity extends Activity
        implements ServiceConnection, MyLocalService.Callback {
    private MyLocalService mService;

    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
    }

    @Override
    protected void onResume() {
        super.onResume();
        Intent bindIntent = new Intent(this, MyLocalService.class);
        bindService(bindIntent, this, BIND_AUTO_CREATE);
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (mService != null) {
            mService.setCallback(null); // Important to avoid memory leaks
            unbindService(this);
        }
    }

    public void onTriggerLongRunningOperation(View view) {
        if(mService != null) {
            mService.performLongRunningOperation(new MyComplexDataObject());
        }
    }

    @Override
    public void onOperationProgress(int progress) {
        // TODO Update user interface with progress..
    }

    @Override
    public void onOperationCompleted(MyComplexResult complexResult) {
        // TODO Show result to user...
    }

    @Override
    public void onServiceConnected(ComponentName componentName,
                                   IBinder iBinder) {
        mService = ((MyLocalService.LocalBinder) iBinder).getService();
        mService.setCallback(this);

        // Once we have a reference to the service, we can update the UI and
        // enable buttons that should otherwise be disabled.
        findViewById(R.id.trigger_operation_button).setEnabled(true);
    }

    @Override
    public void onServiceDisconnected(ComponentName componentName) {
        // Disable the button as we are loosing the reference to the service.
        findViewById(R.id.trigger_operation_button).setEnabled(false);
        mService = null;
    }
}
```

