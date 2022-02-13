[toc]

> 警告
>
> 由于 Handler 有可能导致内存泄漏，所以现在推荐在定义 Handler 类时，使用静态类。

### 1. 一个 Handler 示例代码

#### 1.1 Kotlin

```kotlin
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.os.Message
import android.util.Log
import java.lang.ref.WeakReference

class DefaultWorkHandler(
    looper: Looper,
    activity: MainActivity
): Handler(looper) {

    private var activityRef: WeakReference<MainActivity> = WeakReference(activity)

    private var count = 0

    override fun handleMessage(msg: Message) {
        val pm = "message called: $count : ${msg.data["message"]}"
        Log.d(TAG, pm)
        printMessage(pm)
        if (count > 5) return
        count++
        sendTestMessage(1)
    }

    public fun sendTestMessage(interval: Long) {
        val m = obtainMessage()
        prepareMessage(m)
        sendMessageDelayed(m, interval * 1000)
    }
    
    public fun doDeferredWork() {
        count = 0
        sendTestMessage(1)
    }

    public fun prepareMessage(m: Message) {
        val b = Bundle()
        b.putString("message", "hello World")
        m.data = b
    }

    // This method just prints a message
    // in a text box in the parent activity.
    // You can see this method in Listing 13-9
    private fun printMessage(xyz: String) {
        activityRef.get()?.appendText(xyz)
    }

    companion object {
        const val TAG = "DefaultWorkHandler"
    }

}
```

#### 1.2 Java

```java
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;

import androidx.annotation.NonNull;

import java.lang.ref.WeakReference;

public class DefaultWorkHandler extends Handler {

    private static final String TAG = "DefaultWorkHandler";

    // Keep track of how many times we sent the message
    private int count = 0;

    // A parent driver activity we can use
    // to inform of status.
    private WeakReference<MainActivity> mActivity;

    // During construction we take in the parent
    // driver activity.
    public DefaultWorkHandler(MainActivity activity) {
        mActivity = new WeakReference<>(activity);
    }

    @Override
    public void handleMessage(@NonNull Message msg) {
        String pm = "message called: " + count + ":" + msg.getData().getString("message");
        Log.d(TAG, pm);
        printMessage(pm);
        if (count > 5) return;
        count++;
        sendTestMessage(1);
    }

    public void sendTestMessage(long interval) {
        Message m = obtainMessage();
        prepareMessage(m);
        sendMessageDelayed(m, interval * 1000);
    }

    public void doDeferredWork() {
        count = 0;
        sendTestMessage(1);
    }

    public void prepareMessage(Message m) {
        Bundle b = new Bundle();
        b.putString("message", "Hello World");
        m.setData(b);
    }

    // This method just prints a message
    // in a text box in the parent activity.
    // You can see this method in Listing 13-9
    private void printMessage(String xyz) {
        MainActivity activity = mActivity.get();
        if (activity != null) {
            activity.appendText(xyz);
        }
    }
}
```

