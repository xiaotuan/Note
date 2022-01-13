[toc]

### 1. 获取 DownloadManager 对象

**Kotlin**

```kotlin
mDownloadManager = getSystemService(Context.DOWNLOAD_SERVICE) as DownloadManager;
```

**Java**

```java
mDownloadManager = (DownloadManager) getSystemService(Context.DOWNLOAD_SERVICE);
```

### 2. 构建下载请求对象

**Kotlin**

```kotlin
val request = DownloadManager.Request(Uri.parse("https://dl.google.com/android/repository/platform-tools_r31.0.3-windows.zip"))
request.setTitle("platform-tools.zip")
request.setDescription("Downloading platform-tools.zip ...")
request.setAllowedNetworkTypes(DownloadManager.Request.NETWORK_MOBILE)
```

**Java**

```java
DownloadManager.Request request = new DownloadManager.Request(Uri.parse("https://dl.google.com/android/repository/platform-tools_r31.0.3-windows.zip"));
request.setTitle("platform-tools.zip");
request.setDescription("Downloading platform-tools.zip ...");
request.setAllowedNetworkTypes(DownloadManager.Request.NETWORK_MOBILE);
```

### 3. 开始下载

**Kotlin**

```kotlin
mDownloadId = mDownloadManager?.enqueue(request)
```

**Java**

```java
mDownloadId = mDownloadManager.enqueue(request);
```

### 4. 监听下载完成广播

#### 4.1 定义广播接收器

**Kotlin**

```kotlin
private val mReceiver = object : BroadcastReceiver() {
    override fun onReceive(context: Context?, intent: Intent?) {
        intent?.let {
            it.extras?.let { extras ->
                            val doneDownloadId = extras.getLong(DownloadManager.EXTRA_DOWNLOAD_ID)
                            mDownloadStatuTv.text = "${mDownloadStatuTv.text}\nDownload finished (${doneDownloadId})"
                            if (mDownloadId == doneDownloadId) {
                                Log.v(TAG, "Our download has completed.")
                            }
                           }
        }
    }
}
```

**Java**

```java
private BroadcastReceiver mReceiver = new BroadcastReceiver() {
    @Override
    public void onReceive(Context context, Intent intent) {
        Bundle extras = intent.getExtras();
        long doneDownloadId = extras.getLong(DownloadManager.EXTRA_DOWNLOAD_ID);
        mDownloadStatuTv.setText(mDownloadStatuTv.getText() + "\nDownload finished (" + doneDownloadId + ")");
        if (mDownloadId == doneDownloadId) {
            Log.v(TAG, "Our download has completed.");
        }
    }
};
```

#### 4.2 注册广播接收器

**Kotlin**

```kotlin
val filter = IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE)
registerReceiver(mReceiver, filter)
```

**Java**

```java
IntentFilter filter = new IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE);
registerReceiver(mReceiver, filter);
```

### 5. 取消下载

**Kotlin**

```kotlin
mDownloadManager.remove(mDownloadId)
```

**Java**

```java
mDownloadManager.remove(mDownloadId)
```

### 6. 相关 API 使用说明

+ 通过向 `DownloadManager` 的 `getUriForDownloadedFile()` 方法传递下载 ID，可以获取下载文件的 Uri。
+ 通过 `DownloadManager.Request` 的 `setDestinationInExternalFilesDir()`、`setDestinationInExternalPublicDir()` 和 `setDestinationUri()` 修改文件的保存路径。
+ 可以使用 `DownloadManager.Query` 对象和 `DownloadManager` 的 `query()` 方法查询下载的信息。可以按下载 ID（一个或多个）搜索，或者可以按下载状态搜索。

### 7. 完整示例代码

**Kotlin**

```kotlin
import android.app.DownloadManager
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var mDownloadStatuTv: TextView
    private var mDownloadManager: DownloadManager? = null
    private var mDownloadId = -1L;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mDownloadManager = getSystemService(Context.DOWNLOAD_SERVICE) as DownloadManager;

        mDownloadStatuTv = findViewById(R.id.tv)

        val filter = IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE)
        registerReceiver(mReceiver, filter)
    }

    override fun onDestroy() {
        unregisterReceiver(mReceiver)
        mDownloadManager = null
        super.onDestroy()
    }

    public fun doClick(view: View) {
        val request = DownloadManager.Request(Uri.parse("https://dl.google.com/android/repository/platform-tools_r31.0.3-windows.zip"))
        request.setTitle("platform-tools.zip")
        request.setDescription("Downloading platform-tools.zip ...")
        request.setAllowedNetworkTypes(DownloadManager.Request.NETWORK_MOBILE)

        mDownloadManager?.let {
            mDownloadId = it.enqueue(request)
            mDownloadStatuTv.text = "Download started ... ($mDownloadId)"
        }
    }

    private val mReceiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            intent?.let {
                it.extras?.let { extras ->
                    val doneDownloadId = extras.getLong(DownloadManager.EXTRA_DOWNLOAD_ID)
                    mDownloadStatuTv.text = "${mDownloadStatuTv.text}\nDownload finished (${doneDownloadId})"
                    if (mDownloadId == doneDownloadId) {
                        Log.v(TAG, "Our download has completed.")
                    }
                }
            }
        }
    }

    companion object {
        const val TAG = "qty"
    }
}
```

**Java**

```java
import androidx.appcompat.app.AppCompatActivity;
import android.app.DownloadManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;


public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private DownloadManager mDownloadManager;
    private TextView mDownloadStatuTv;
    private long mDownloadId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mDownloadStatuTv = findViewById(R.id.tv);

        IntentFilter filter = new IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE);
        registerReceiver(mReceiver, filter);
    }

    @Override
    protected void onResume() {
        super.onResume();
        mDownloadManager = (DownloadManager) getSystemService(Context.DOWNLOAD_SERVICE);
    }

    @Override
    protected void onPause() {
        super.onPause();
        unregisterReceiver(mReceiver);
        mDownloadManager = null;
    }

    public void doClick(View view) {
        DownloadManager.Request request = new DownloadManager.Request(Uri.parse("https://dl.google.com/android/repository/platform-tools_r31.0.3-windows.zip"));
        request.setTitle("platform-tools.zip");
        request.setDescription("Downloading platform-tools.zip ...");
        request.setAllowedNetworkTypes(DownloadManager.Request.NETWORK_MOBILE);

        mDownloadId = mDownloadManager.enqueue(request);

        mDownloadStatuTv.setText("Download started ... (" + mDownloadId + ")");
    }

    private BroadcastReceiver mReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            Bundle extras = intent.getExtras();
            long doneDownloadId = extras.getLong(DownloadManager.EXTRA_DOWNLOAD_ID);
            mDownloadStatuTv.setText(mDownloadStatuTv.getText() + "\nDownload finished (" + doneDownloadId + ")");
            if (mDownloadId == doneDownloadId) {
                Log.v(TAG, "Our download has completed.");
            }
        }
    };
}
```

