[toc]

Android 官方文档指出："默认情况下，应用的所有组件都运行在同一个进程和线程中（主线程）。" 更具体的说，Android 组件（Activity、BroadcastReceiver、Service 以及 Application）的所有回调（基本上时所有的 onX 方法）都运行在主线程里。因此，Service 的 onStartCommand 方法和 Activity 的 onResume 也运行在同一个线程里。

所有对主线程的操作都是通过直接使用 Handler 对象或者间接使用部分 Android API （比如， runOnUiThread 方法）往队列里发送消息完成的。可以通过 Context.getMainLooper() 来查询应用程序主线程的 Looper 对象。

只有那些必须在主线程执行的方法才能放在主线程中。其他一切操作都应放在另一个单独的线程中执行。实际情况下，那些不会耗时的操作也可以放在主线程中。如果能够确保在另一个单独的线程中执行文件、数据库或者网络操作，通常主线程会是安全的。另外，对于某些应用或者游戏，开发人员可能会不定期执行一些与 UI 无关的计算，这些操作也应该放在一个单独的线程中执行。然而，也要确保同一时间不会运行太多线程，原因是 CPU 切换线程也会造成性能损失。

### 1. Thread 类

Thread 类是 Android 中所有线程的基类，Java SE 中也含它。如果要在线程中执行代码，既可以创建一个具体的类（即继承自 Thread 的新类），也可以把实现 Runnable 接口的类对象传给 Thread 的构造函数。本书的例子使用了后者。

```java
import android.app.Activity;
import android.os.SystemClock;
import android.view.View;
import android.widget.ProgressBar;

public class MyThread implements Thread {

    private Object[] mInput;
    private Activity mActivity;
    private int mProgress = 0;

    public MyThread(Activity activity, Object ... input) {
        mActivity = activity;
        mInput = input;
    }

    @Override
    public void run() {
        mProgress = 0;
        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                mActivity.findViewById(R.id.progressBar).setVisibility(View.VISIBLE);
                ((ProgressBar) mActivity.findViewById(R.id.progressBar)).setProgress(0);
            }
        };
        mActivity.runOnUiThread(runnable);

        // 循环并处理输入
        for (Object input : mInput) {
            // 上传到服务器（用睡眠模拟）
            SystemClock.sleep(50);

            runnable = new Runnable() {
                @Override
                public void run() {
                    ((ProgressBar) mActivity.findViewById(R.id.progressBar)).setMax(++mProgress);
                    ((ProgressBar) mActivity.findViewById(R.id.progressBar)).setProgress(mInput.length);
                }
            };
            mActivity.runOnUiThread(runnable);
        }

        runnable = new Runnable() {
            @Override
            public void run() {
                mActivity.findViewById(R.id.progressBar).setVisibility(View.INVISIBLE);
            }
        };
        mActivity.runOnUiThread(runnable);
    }
}
```

因为只能对 Thread 实例调用一次 start 方法，所以每次执行操作都需要创建一个新的 Thread 对象。不断创建新的线程是非常昂贵的，本例还有改进的空间

### 2. AsyncTask 

AsyncTask 允许开发者定义一个运行在单独线程中的任务，还能在任务的不同阶段提供回调函数。这些回调函数被设计成无需使用 runOnUiThread 方法即可更新 UI。

```java
import android.app.Activity;
import android.os.AsyncTask;
import android.os.SystemClock;
import android.view.View;
import android.widget.ProgressBar;

public class MyAsyncTask extends AsyncTask<String, Integer, Integer> {

    private Activity mActivity;

    public MyAsyncTask(Activity activity) {
        mActivity = activity;
    }

    @Override
    protected void onPreExecute() {
        super.onPreExecute();
        // 下面的代码会运行在主线程中
        mActivity.findViewById(R.id.progressBar).setVisibility(View.VISIBLE);
        ((ProgressBar) mActivity.findViewById(R.id.progressBar)).setProgress(0);
    }

    @Override
    protected Integer doInBackground(String... inputs) {
        // 下面的代码不会运行在主线程中
        int progress = 0;

        for (String input : inputs) {
            // 把输入上传到服务器（用睡眠代替）
            SystemClock.sleep(50);
            publishProgress(++progress, inputs.length);
        }

        return progress;
    }

    @Override
    protected void onProgressUpdate(Integer... values) {
        super.onProgressUpdate(values);
        // 下面的代码会运行在主线程中
        ((ProgressBar) mActivity.findViewById(R.id.progressBar)).setMax(values[1]);
        ((ProgressBar) mActivity.findViewById(R.id.progressBar)).setProgress(values[0]);
    }

    @Override
    protected void onPostExecute(Integer integer) {
        super.onPostExecute(integer);
        // 下面的代码会运行在主线程中
        mActivity.findViewById(R.id.progressBar).setVisibility(View.INVISIBLE);
    }
}
```

使用 AsyncTask 唯一的问题是该类的实例只能使用一次，这意味着每次执行操作都要新建一个 MyAsyncTask 对象。虽然是个轻量级的类（实际的线程是由 ExecutorService 管理的），但它不适合那些频繁的操作。它适合文件下载，以及不会频繁发生或通过用户交互等类似情况的操作。

### 3. Handler 类

Handler 类允许开发者准确地控制操作的执行时间，还可以重复多次使用它。执行操作的线程会一直运行，直到被显示地终止。Looper 类会处理幕后的事情，但开发者很少需要直接和它打交道，相反可以通过包装类 HandlerThread 创建它。

```java
import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.Message;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class SampleActivity extends Activity implements Handler.Callback {

    private Handler mHandler;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        // 使用 Looper 开启一个新线程
        HandlerThread handlerThread = new HandlerThread("BackgroundThread");
        handlerThread.start();
        // 创建 Handler 对象
        mHandler = new Handler(handlerThread.getLooper(), this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 关闭 Looper 线程
        mHandler.getLooper().quit();
    }

    @Override
    public boolean handleMessage(@NonNull Message message) {
        // 处理消息...

        // 回收消息对象
        message.recycle();
        return true;
    }
}
```

我们可以使用多种方法给 Handler 发送消息，下面列出最常见的三种：

```java
public void sendMessageDemo(Object data) {
    // 创建一个带有 data 参数的 Message，然后立刻把它发送到 handler 执行
    Message.obtain(mHandler, SYNC_DATA, data).sendToTarget();

    // 立刻给 handler 发送一个简单的空消息
    mHandler.sendEmptyMessage(SYNC_DATA);

    // 给 handler 发送一个简单的空消息，该消息会在 30 秒后执行
    mHandler.sendEmptyMessageDelayed(SYNC_DATA, THIRTY_SECONDS_IN_MILLISECONDS);

    // 给 handler 发送带有 arguments 和 obj 参数的消息，并在两分钟后执行
    int recipient = getRecipientId();
    int priority = 5;
    Message msg = mHandler.obtainMessage(SYNC_DATA, recipient, priority, data);
    mHandler.sendEmptyMessageDelayed(msg, TWO_MINUTES_IN_MILLISECONDS);
}
```

多个 Handler 对象可以共用一个回调函数，就像代理方法一样，处理应用程序消息会很有用。甚至可以在 Activity 和 Service 之间共享回调函数。

```java
// 用于 what 成员变量的常量值
public static final int SYNC_DATA = 10;
public static final int PING_SERVER = 20;

@Override
public boolean handleMessage(@NonNull Message message) {
    switch (message.what) {
        case SYNC_DATA:
            // 执行耗时的网络输入/输出操作
            syncDataWithServer(message.obj);
            break;
            
        case PING_SERVER:
            // ping 服务器，应该定期执行
            pingServer();
            break;
    }
    
    // 回收消息对象以便节省内存
    message.recycle();
    return true;
}
```

#### 3.1 间隔地执行操作

```java
package com.example.android.basictransition;

import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.Message;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class SampleActivity extends Activity implements Handler.Callback {

    private static final String PING_URL = "http://www.server.com/ping";
    private static final int SIXTY_SECONDS_IN_MILLISECONDS = 60 * 1000;
    public static final int SYNC_DATA = 10;
    public static final int PING_SERVER = 20;
    private Handler mHandler;
    private boolean mPingServer = false;
    private int mFailedPings = 0;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        // 使用 Looper 开启一个新线程
        HandlerThread handlerThread = new HandlerThread("BackgroundThread");
        handlerThread.start();
        // 创建 Handler 对象
        mHandler = new Handler(handlerThread.getLooper(), this);
    }

    @Override
    protected void onResume() {
        super.onResume();
        mPingServer = true;
        mHandler.sendEmptyMessage(PING_SERVER);
    }

    @Override
    protected void onPause() {
        super.onPause();
        mPingServer = false;
        mHandler.removeMessages(PING_SERVER);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 关闭 Looper 线程
        mHandler.getLooper().quit();
    }

    @Override
    public boolean handleMessage(@NonNull Message message) {
        switch (message.what) {
            case SYNC_DATA:
                // 执行耗时的网络输入/输出操作
                syncDataWithServer(message.obj);
                break;

            case PING_SERVER:
                // ping 服务器，应该定期执行
                pingServer();
                break;
        }

        // 回收消息对象以便节省内存
        message.recycle();
        return true;
    }

    private void pingServer() {
        HttpURLConnection urlConnection = null;
        try {
            URL pingUrl = new URL(PING_URL);
            urlConnection = (HttpURLConnection) pingUrl.openConnection();
            urlConnection.setRequestMethod("GET");
            urlConnection.connect();
            if (urlConnection.getResponseCode() == 200) {
                mFailedPings = 0;
            }
            // 这儿也需要处理网络失败的情况。。。
        } catch (IOException e) {
            // 还需要处理网络错误...
        } finally {
            if (urlConnection != null) urlConnection.disconnect();
        }

        if (mPingServer) {
            mHandler.sendEmptyMessageDelayed(PING_SERVER, SIXTY_SECONDS_IN_MILLISECONDS);
        }
    }

    private void syncDataWithServer(Object obj) {

    }
}
```

#### 3.2 在 Handler 中使用 MainLooper

因为在构造函数中传递 Looper 对象可以为 Handler 分配线程，所以我们可以创建一个处理主线程消息的 Handler。

```java
@Override
public boolean handleMessage(Message message) {
    switch (message.what) {
        case SYNC_DATA:
            syncDataWithServer(message.obj);
            break;
            
        case SET_PROGRESS:
            ProgressBar progressBar = (ProgressBar)findViewById(R.id.progressBar);
            progressBar.setProgress(message.arg1);
            progressBar.setMax(message.arg2);
            break;
    }
    
    message.recycle();
    return true;
}
```

前面的 handleMessage 例子可以接收两种类型的消息，SYNC_DATA 和 SET_PROGRESS。第一个需要运行在一个单独的线程中，而第二个由于要更新 UI 需要运行在主线程中。

```java
@Override
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.main);
    mMainHandler = new Handler(getMainLooper(), this);
    HandlerThread handlerThread = new HnalderThread("BackgroundThread");
    handlerThread.start();
    mHandler = new Handler(handlerThread.getLooper(), this);
}
```

### 4. 选择合适的线程

API 中和线程相关的类还有 ExecutorService 和 Loader。ExecutorService 适合处理并行运行的多个任务，这非常适合编写多客户端的服务器应用。 AsyncTask 内部同样使用 ExecutorService 处理多线程。