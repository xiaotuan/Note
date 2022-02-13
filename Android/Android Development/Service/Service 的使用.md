[toc]

> 注意：
>
> `Service` 是运行在主线程上的，因此进行耗时操作时应该为其创建独立线程。

### 1. 定义继承 Service 的类

**kotlin**

```kotlin
import android.app.*
import android.content.Intent
import android.os.Build
import android.os.IBinder
import android.util.Log

class BackgroundService : Service() {

    private lateinit var mNotificationManager: NotificationManager
    private val mThreads = ThreadGroup("ServiceWorker")

    override fun onBind(intent: Intent): IBinder? {
        Log.v(TAG, "in onBind()")
        return null
    }

    override fun onCreate() {
        super.onCreate()
        Log.v(TAG, "in onCreate()")
        mNotificationManager = getSystemService(NOTIFICATION_SERVICE) as NotificationManager
        displayNotificationMessage("Background Service is running")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        super.onStartCommand(intent, flags, startId)
        val counter = intent?.extras?.getInt("counter")
        Log.v(TAG, "in onStartCommand(), counter = $counter, startId = $startId")
        counter?.apply {
            Thread(mThreads, ServiceWorker(this), "BackgroundService").start()
        }
        return START_STICKY
    }

    override fun onDestroy() {
        Log.v(TAG, "in onDestroy(). Interrupting threads and cancelling notifications")
        mThreads.interrupt()
        mNotificationManager.cancelAll()
        super.onDestroy()
    }

    private fun displayNotificationMessage(message: String) {
        val contentIntent = PendingIntent.getActivity(this, 0,
            Intent(this, MainActivity::class.java), 0)
        val channelId = "ChannelId" // 通知渠道
        val builder = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(channelId,
                "通知的渠道名称",
                NotificationManager.IMPORTANCE_DEFAULT)
            mNotificationManager.createNotificationChannel(channel)
            Notification.Builder(applicationContext, channelId)
                .setContentTitle("通知标题")
                .setContentText("通知内容")
                .setSmallIcon(R.mipmap.ic_launcher)
                .setContentIntent(contentIntent)
        } else {
            Notification.Builder(applicationContext)
                .setContentTitle("通知标题")
                .setContentText("通知内容")
                .setSmallIcon(R.mipmap.ic_launcher)
                .setContentIntent(contentIntent)
        }
        mNotificationManager.notify(12, builder.build())
    }

    class ServiceWorker(
        var counter: Int = -1,
    ): Runnable {

        override fun run() {
            val TAG2 = "ServiceWorker: " + Thread.currentThread().id
            // do background processing here... we'll just sleep...
            try {
                Log.v(TAG2, "sleeping for 10 seconds. counter = $counter")
                Thread.sleep(10000)
                Log.v(TAG2, "... waking up")
            } catch (e: InterruptedException) {
                Log.v(TAG2, "... sleep interrupted")
            }
        }

    }

    companion object {
        const val TAG = "BackgroundService"
    }
}
```

**Java**

```java
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.os.IBinder;
import android.util.Log;

public class BackgroundService extends Service {

    private static final String TAG = "BackgroundService";

    private NotificationManager mNotificationManager;
    private ThreadGroup mThreads = new ThreadGroup("ServiceWorker");

    @Override
    public IBinder onBind(Intent intent) {
        Log.v(TAG, "in onBind()");
        return null;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        Log.v(TAG, "in onCreate()");
        mNotificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        displayNotificationMessage("Background Service is running");
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        super.onStartCommand(intent, flags, startId);
        int counter = intent.getExtras().getInt("counter");
        Log.v(TAG, "in onStartCommand(), counter = " + counter +
                ", startId = " + startId);

        new Thread(mThreads, new ServiceWorker(counter), "BackgroundService").start();

        return START_STICKY;
    }

    @Override
    public void onDestroy() {
        Log.v(TAG, "in onDestroy(). Interrupting threads and cancelling notifications");
        mThreads.interrupt();
        mNotificationManager.cancelAll();
        super.onDestroy();
    }

    private void displayNotificationMessage(String message) {
        PendingIntent contentIntent = PendingIntent.getActivity(this, 0, new Intent(this, MainActivity.class), 0);

        Context context = getApplicationContext();
        String channelId = "ChannelId"; // 通知渠道
        Notification.Builder builder = new Notification.Builder(context)
                .setContentTitle("通知标题")
                .setContentText("通知内容")
                .setSmallIcon(R.mipmap.ic_launcher)
                .setContentIntent(contentIntent);;
        // 2. 获取系统的通知管理器(必须设置channelId)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(
                    channelId,
                    "通知的渠道名称",
                    NotificationManager.IMPORTANCE_DEFAULT);
            builder.setChannelId(channelId);
            mNotificationManager.createNotificationChannel(channel);
        }
        // 3. 发送通知(Notification与NotificationManager的channelId必须对应)
        mNotificationManager.notify(12, builder.build());
    }

    class ServiceWorker implements Runnable {
        private int counter = -1;

        public ServiceWorker(int counter) {
            this.counter = counter;
        }

        @Override
        public void run() {
            final String TAG2 = "ServiceWorker:" + Thread.currentThread().getId();
            // do background processing here... we'll just sleep...
            try {
                Log.v(TAG2, "sleeping for 10 seconds. counter = " + counter);
                Thread.sleep(10000);
                Log.v(TAG2, "... waking up");
            } catch (InterruptedException e) {
                Log.v(TAG2, "... sleep interrupted");
            }
        }
    }
}
```

### 2. 启动服务

#### 2.1 Kotlin

```kotlin
startService(Intent(this@MainActivity, BackgroundService::class.java))
```

#### 2.2 Java

```java
startService(new Intent(MainActivity.this, BackgroundService.class));
```

### 3. 停止服务

#### 3.1 在服务中停止服务

##### 3.1.1 Kotlin

```kotlin
stopSelf()
或
stopSelfResult(startId)	// 停止指定服务实例
```

##### 3.1.2 Java

```java
stopSelf();
或
stopSelfResult(startId);	// 停止指定服务实例
```

#### 3.2 在服务外停止服务

##### 3.2.1 Kotlin

```kotlin
context.stopService(Intent(this@MainActivity, BackgroundService::class.java))
```

##### 3.2.2 Java

```java
context.stopService(new Intent(MainActivity.this, BackgroundService.class);
```

### 4. 提示

`onStartCommand()` 方法的返回值可以是如下值：

+ `Service.START_NOT_STICKY`：如果没有挂起的 Intent，不应重新启动服务。
+ `Service.START_STICKY`：即使没有挂起的 Intent，Android 也应该重新启动服务。当服务重新启动时，使用一个空 Intent 调用 onCreate 和 onStartCommand。
+ `Service.START_REDELIVER_INTENT`：如果服务在启动时被杀死，那么它将被重新启动并且将最后的 Intent 再次通过 onStartCommand 方法，除非是调用了 stopSelf()。
