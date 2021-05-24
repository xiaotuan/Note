[toc]

#### TestHandlersDriverActivity.kt

```kotlin
package com.androidbook.handlers

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import android.widget.TextView

open class TestHandlersDriverActivity : AppCompatActivity() {

    private var th: DeferWorkHandler? = null
    private var statusBackHandler: Handler? = null
    private var workerThread: Thread? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main)
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        super.onCreateOptionsMenu(menu)
        menuInflater.inflate(R.menu.main_menu, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        appendMenuItemText(item)
        when (item.itemId) {
            R.id.menu_clear -> emptyText()
            R.id.menu_test_thread -> testThread()
            R.id.menu_test_defered_handler -> testDeferedHandler()
        }
        return true
    }

    @SuppressLint("WrongViewCast")
    private fun getTextView(): TextView {
        return findViewById(R.id.text1)
    }

    @SuppressLint("SetTextI18n")
    open fun appendText(abc: String) {
        val tv = getTextView()
        tv.text = "${tv.text}\n$abc"
    }

    @SuppressLint("SetTextI18n")
    private fun appendMenuItemText(menuItem: MenuItem) {
        val tv = getTextView()
        tv.text = "${tv.text}\n${menuItem.title}"
    }

    private fun emptyText() {
        val tv = getTextView()
        tv.text = ""
    }

    private fun testDeferedHandler() {
        if (th == null) {
            th = DeferWorkHandler(this, Looper.getMainLooper())
            appendText("Creating a new handler")
        }
        appendText("Starting to do deferred work by sending messages")
        th?.doDeferredWork()
    }

    private fun testThread() {
        if (statusBackHandler == null) {
            statusBackHandler = ReportStatusHandler(this, Looper.getMainLooper())
        }
        if (workerThread != null && workerThread?.state != Thread.State.TERMINATED) {
            Log.d(TAG, "thread is new or alive, but not terminated")
        } else {
            Log.d(TAG, "thread is likely dead. starting now")
            // you have to create a new thread.
            // no way to resurrect a dead thread.
            workerThread = Thread(WorkerThreadRunnable(statusBackHandler!!))
            workerThread?.start()
        }
    }

    companion object {
        const val TAG = "DriverActivity"
    }
}
```

#### DeferWorkHandler.kt

```kotlin
package com.androidbook.handlers

import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.os.Message
import android.util.Log

open class DeferWorkHandler(
    private val parentActivity: TestHandlersDriverActivity,
    loop: Looper,
    private var count: Int = 0,
) : Handler(loop) {

    override fun handleMessage(msg: Message) {
        val pm = "message called:$count:${msg.data.getString("message")}"

        Log.d(TAG, pm)
        printMessage(pm)

        if (count > 5) return

        count++
        sendTestMessage(1)
    }

    private fun sendTestMessage(interval: Long) {
        val m = obtainMessage()
        prepareMessage(m)
        sendMessageDelayed(m, interval * 1000)
    }

    open fun doDeferredWork() {
        count = 0
        sendTestMessage(1)
    }

    private fun prepareMessage(m: Message) {
        val b = Bundle()
        b.putString("message", "Hello world")
        m.data = b
    }

    private fun printMessage(xyz: String) {
        parentActivity.appendText(xyz)
    }

    companion object {
        const val TAG = "TestHandler1"
    }
}
```

#### ReportStatusHandler.kt

```kotlin
package com.androidbook.handlers

import android.os.Handler
import android.os.Looper
import android.os.Message
import android.util.Log

class ReportStatusHandler(
    private val parentActivity: TestHandlersDriverActivity,
    loop: Looper,
) : Handler(loop) {

    override fun handleMessage(msg: Message) {
        val pm = Utils.getStringFromABundle(msg.data)

        Log.d(TAG, pm ?: "null")
        printMessage(pm ?: "null")
    }

    private fun printMessage(xyz: String) {
        parentActivity.appendText(xyz)
    }

    companion object {
        const val TAG = "TestHandler2"
    }
}
```

#### WorkerThreadRunnable.kt

```kotlin
package com.androidbook.handlers

import android.os.Handler
import android.util.Log

class WorkerThreadRunnable(private val mainThreadHandler: Handler) : Runnable {

    override fun run() {
        Log.d(TAG, "start execution")
        informStart()
        for (i in 1..10) {
            Utils.sleepForInSecs(1)
            informMiddle(i)
        }
        informFinish()
    }

    private fun informMiddle(count: Int) {
        val m = mainThreadHandler.obtainMessage()
        m.data = Utils.getStringAsABundle("done:$count")
        mainThreadHandler.sendMessage(m)
    }

    private fun informStart() {
        val m = mainThreadHandler.obtainMessage()
        m.data = Utils.getStringAsABundle("starting run")
        mainThreadHandler.sendMessage(m)
    }

    private fun informFinish() {
        val m = mainThreadHandler.obtainMessage()
        m.data = Utils.getStringAsABundle("Finishing run")
        mainThreadHandler.sendMessage(m)
    }

    companion object {
        const val TAG = "TestRunnable"
    }
}
```

#### Utils.kt

```kotlin
package com.androidbook.handlers

import android.os.Bundle
import android.util.Log
import java.lang.RuntimeException

class Utils {

    companion object {

        fun getThreadId(): Long {
            val t = Thread.currentThread()
            return t.id
        }

        fun getThreadSignature(): String {
            val t = Thread.currentThread()
            var gname: String? = t.threadGroup?.name
            return "${t.name}:(id)${t.id}:(priority)${t.priority}:(group)${gname ?: "null"}"
        }

        fun logThreadSignature() {
            Log.d("ThreadUtils", getThreadSignature())
        }

        fun sleepForInSecs(secs: Int) {
            try {
                Thread.sleep(secs * 1000L)
            } catch (x: InterruptedException) {
                throw RuntimeException("interrupted", x)
            }
        }

        fun getStringAsABundle(message: String): Bundle {
            val b = Bundle()
            b.putString("message", message)
            return b
        }

        fun getStringFromABundle(b: Bundle): String? {
            return b.getString("message")
        }

    }
}
```

#### main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    >
    <TextView
        android:id="@+id/text1"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Click Menu to see Test Options"
        />
</LinearLayout>
```

#### main_menu.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- This group uses the default category. -->
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

