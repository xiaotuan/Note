[toc]

### 1. Service 的创建和销毁

在 onCreate() 方法中，开发者初始化新的 Handler 对象，获取系统服务，注册 BroadcastReceiver 以及执行 Service 操作需要的其他初始化工作。需要注意的是 onCreate() 方法也运行在主线程中。

所有的清理工作都应在 onDestroy() 方法中完成。特别地，需要停止所有已经启动的 HandlerThread 对象，并且注销之前注册的 BroadcastReceiver。同样的，onDestroy() 方法也运行在主线程中。

### 2. 启动 Service

Service 可通过两种方式启动：通过 Context.startService() 方法接收一个 Intent，或者客户端通过 Context.bindService() 方法来绑定它。

调用 Context.startService() 时，参数中的 Intent 必须匹配 Service 定义的 intent-filter。使用 Context.startService() 启动 Service 时， Service 的 onStartCommand() 方法会被调用，并受到发送给 Service 的 Intent。该方法返回一个整型常量，用来告诉系统如何处理 Service 的重启操作。开发者需要记住三种返回值：START_STICKY，START_NOT_STICKY 以及 START_REDELIVER_INTENT。

返回 START_STICKY 代表当系统出于某些原因关闭 Service 时，Service 会被重新启动。然而，当系统重新启动 Service 时，onStartCommand() 参数中的 Intent 会被置为 null。

返回 START_NOT_STICKY 意味着 Service 不会在系统关闭它后重新启动。

返回 START_REDELIVER_INTENT 与 START_STICKY 一样，不过当系统重启 Service 时，onStartCommand() 会收到 Service 被销毁之前接收到的最后一个 Intent。

```sequence
Title: Service异步交互序列图
	participant MyActivity
	participant MyService
	participant mHandler
	
	MyActivity->>MyService:startService()
	MyService->>mHandler:mHandler.sendEmptyMessage()
	mHandler->>MyActivity:sendBroadcast()
	mHandler->>MyService:stopSelf()
```

<center><b>Service 异步交互序列图</b></center>

### 3. 绑定 Service

第二种启动 Service 的方法是使用 Context.bindService()。被绑定的 Service 会一直运行，直到所有绑定的客户端都断开后才会停止。

```sequence
Title: Service异步交互序列图
	participant MyActivity
	participant MyService
	participant MyAsyncTask
	
	MyActivity->>MyService:bindService()
	MyService->>MyActivity:onServiceConnected()
	MyActivity->>MyService:addCallback(this)
	MyActivity->>MyService:performLongRunningOperation()
	MyService->>MyAsyncTask:new MyAsyncTask().execute(...)
	MyAsyncTask->>MyActivity:onOperationCompleted()
	MyAsyncTask->>MyService:stopSelf()
```
<center><b>本地binder序列图</b></center>

下面的代码演示了如何实现一个本地的 Binder：

```java
public class MyLocalService extends Service {
    
    private LocalBinder mLocalBinder = new LocalBinder();
    
    public IBinder onBind(Intent intent) {
        return mLocalBinder;
    }
    
    public void doLongRunningOperation() {
        // TODO: 为耗时操作启动新线程
    }
    
    public class LocalBinder extends Binder {
        public MyLocalService getService() {
            return MyLocalService.this;
        }
    }
}
```

如果要在 Activity 中使用上面的 Service，通常需要在 onResume() 和 onPause() 方法中实现绑定和解绑操作，如下代码所示：

```java
public class MyActivity extends Activity implements ServiceConnection {
    
    private MyLocalService mService;
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
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
            unbindService(this);
        }
    }
    
    @Override
    public void onServiceConnected(ComponentName componentName, IBinder iBinder) {
        mService = ((MyLocalService.LocalBinder) iBinder).getService();
    }
    
    @Override
    public void onServiceDisconnected(ComponentName componentName) {
        mService = null;
    }
}
```

### 4. 保持活跃

如果需要在应用不处于活动状态的情况下仍然保持 Service 在前台运行，则可以调用 Service.startForeground()。

```java
@Override
public int onStartCommand(Intent intent, int flags, int startId) {
    if (intent != null) {
        String action = intent.getAction();
        if (ACTION_SHARE_PHOTO.equals(action)) {
            // 构建要显示的通知
            Notification.Builder builder = new Notification.Builder(this);
            builder.setSmallIcon(R.drawable.notification_icon);
            builder.setContentTitle(getString(R.string.notification_title));
            builder.setContentText(getString(R.string.notification_text));
            Notification notification = builder.build();
            // 在前台运行 Service
            startForeground(NOTIFICATION_ID, notification);
            
            // 执行后台操作
            String photoText = intent.getStringExtra(EXTRA_PHOTO_TEXT);
            Bitmap photoBitmap = intent.getParcelableExtra(EXTRA_PHOTO_BITMAP);
            uploadPhotoWithText(photoBitmap, photoText);
        }
    }
    return START_NOT_STICKY;
}
```

可以通过调用 stopForeground(true) 方法停止前台运行。

### 5. 停止 Service

