[toc]

#### TestHandlerDriverActivity.java

```java
package com.androidbook.handlers;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.TextView;

public class TestHandlersDriverActivity extends AppCompatActivity {

    private static final String TAG = "DriverActivity";

    private DeferWorkHandler th = null;
    private Handler statusBackHandler = null;
    private Thread workerThread = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.main_menu, menu);
        return true;
    }

    @SuppressLint("NonConstantResourceId")
    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        appendMenuItemText(item);
        switch (item.getItemId()) {
            case R.id.menu_clear:
                emptyText();
                break;

            case R.id.menu_test_thread:
                testThread();
                break;

            case R.id.menu_test_defered_handler:
                testDeferedHandler();
                break;
        }
        return true;
    }

    private TextView getTextView() {
        return findViewById(R.id.text1);
    }

    public void appendText(String abc) {
        TextView tv = getTextView();
        tv.setText(String.format("%s\n%s", tv.getText(), abc));
    }

    private void appendMenuItemText(MenuItem menuItem) {
        String title = menuItem.getTitle().toString();
        TextView tv = getTextView();
        tv.setText(String.format("%s\n%s", tv.getText(), title));
    }

    private void emptyText() {
        TextView tv = getTextView();
        tv.setText("");
    }

    private void testDeferedHandler() {
        if (th == null) {
            th = new DeferWorkHandler(this);
            appendText("Starting to do deferred work by sending messages");
        }
        appendText("Starting to do deferred work by sending messages");
        th.doDeferredWork();
    }

    private void testThread() {
        if (statusBackHandler == null) {
            statusBackHandler = new ReportStatusHandler(this);
        }
        if (workerThread != null && workerThread.getState() != Thread.State.TERMINATED) {
            Log.d(TAG, "thread is new or alive, but not terminated");
        } else {
            Log.d(TAG, "thread is likely dead. starting now");
            // you have to create a new thread.
            // no way to resurrect a dead thread.
            workerThread = new Thread(new WorkerThreadRunnable(statusBackHandler));
            workerThread.start();
        }
    }
}
```

#### DeferWorkHandler.java

```java
package com.androidbook.handlers;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;

import androidx.annotation.NonNull;

public class DeferWorkHandler extends Handler {

    public static final String TAG = "TestHandler1";

    private int count = 0;
    private final TestHandlersDriverActivity parentActivity;

    public DeferWorkHandler(TestHandlersDriverActivity inParentActivity) {
        parentActivity = inParentActivity;
    }

    @Override
    public void handleMessage(@NonNull Message msg) {
        String pm = "message called:" + count + ":" +
                msg.getData().getString("message");

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

    private void printMessage(String xyz) {
        parentActivity.appendText(xyz);
    }
}
```

#### ReportStatusHandler.java

```java
package com.androidbook.handlers;

import android.os.Handler;
import android.os.Message;
import android.util.Log;

import androidx.annotation.NonNull;

public class ReportStatusHandler extends Handler {

    private static final String TAG = "TestHandler2";

    private final TestHandlersDriverActivity parentActivity;

    public ReportStatusHandler(TestHandlersDriverActivity inParentActivity) {
        parentActivity = inParentActivity;
    }

    @Override
    public void handleMessage(@NonNull Message msg) {
        String pm = Utils.getStringFromABundle(msg.getData());

        Log.d(TAG, pm);
        printMessage(pm);
    }

    private void printMessage(String xyz) {
        parentActivity.appendText(xyz);
    }

}
```

#### WorkerThreadRunnable.java

```java
package com.androidbook.handlers;

import android.os.Handler;
import android.os.Message;
import android.util.Log;

public class WorkerThreadRunnable implements Runnable {

    private static final String TAG = "TestRunnable";

    private final Handler mainThreadHandler;

    public WorkerThreadRunnable(Handler h) {
        mainThreadHandler = h;
    }

    @Override
    public void run() {
        Log.d(TAG, "start execution");
        informStart();
        for (int i = 1; i <= 10; i++) {
            Utils.sleepForInSecs(1);
            informMiddle(i);
        }
        informFinish();
    }

    private void informMiddle(int count) {
        Message m = mainThreadHandler.obtainMessage();
        m.setData(Utils.getStringAsABundle("done:" + count));
        mainThreadHandler.sendMessage(m);
    }

    private void informStart() {
        Message m = mainThreadHandler.obtainMessage();
        m.setData(Utils.getStringAsABundle("starting run"));
        mainThreadHandler.sendMessage(m);
    }

    private void informFinish() {
        Message m = mainThreadHandler.obtainMessage();
        m.setData(Utils.getStringAsABundle("Finishing run"));
        mainThreadHandler.sendMessage(m);
    }

}
```

#### Utils.java

```java
package com.androidbook.handlers;

import android.os.Bundle;
import android.util.Log;

public class Utils {

    public static long getThreadId() {
        Thread t = Thread.currentThread();
        return t.getId();
    }

    public static String getThradSignature() {
        Thread t = Thread.currentThread();
        long l = t.getId();
        String name = t.getName();
        long p = t.getPriority();
        String gname = "null";
        if (t.getThreadGroup() != null) {
            gname = t.getName();
        }
        return (name + ":(id)" + l + ":(priority)" + p +
                ":(group)" + gname);
    }

    public static void logThreadSignature() {
        Log.d("ThreadUtils", getThradSignature());
    }

    public static void sleepForInSecs(int secs) {
        try {
            Thread.sleep(secs * 1000);
        } catch (InterruptedException e) {
            throw new RuntimeException("interrupted", e);
        }
    }

    public static Bundle getStringAsABundle(String message) {
        Bundle b = new Bundle();
        b.putString("message", message);
        return b;
    }

    public static String getStringFromABundle(Bundle b) {
        return b.getString("message");
    }

}
```

#### main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/text1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Click Menu to see Test Options" />

</LinearLayout>
```

#### main_menu.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">

    <!--    This group uses the default category.   -->
    <group android:id="@+id/menuGroup_Main">

        <item
            android:id="@+id/MenuId_OpenGL15_Current"
            android:title="Current" />

        <item
            android:id="@+id/menu_clear"
            android:title="clear" />

        <item
            android:id="@+id/menu_test_thread"
            android:title="Test Worker Thread" />

        <item
            android:id="@+id/menu_test_defered_handler"
            android:title="Test Defered Handler" />

    </group>

</menu>
```

#### AndroidManifest.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.androidbook.handlers">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.TestHandlers">
        <activity android:name=".TestHandlersDriverActivity"
            android:label="Test Handler Driver">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

