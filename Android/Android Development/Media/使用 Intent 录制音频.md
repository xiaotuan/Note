[toc]

> 注意
>
> 可能设备中并无提供 `android.provider.MediaStore.RECORD_SOUND` 动作的应用，直接调用会导致报错。

### 1. 通过 Intent 启动录音应用

#### 1.1 Kotlin

```kotlin
import android.content.Intent
import android.util.Log
import android.widget.Toast

try {
    val intt = Intent("android.provider.MediaStore.RECORD_SOUND")
    startActivityForResult(intt, 0)
} catch (e : Exception) {
    Log.e(TAG, "No found provider record sound app. error: ", e);
    Toast.makeText(this, "No found provider record sound app", Toast.LENGTH_SHORT).show();
}
```

#### 1.2 Java

```java
import android.content.Intent;
import android.util.Log;
import android.widget.Toast;

try {
    Intent intt = new Intent("android.provider.MediaStore.RECORD_SOUND");
    startActivityForResult(intt, 0);
} catch (Exception e) {
    Log.e(TAG, "No found provider record sound app. error: ", e);
    Toast.makeText(this, "No found provider record sound app", Toast.LENGTH_SHORT).show();
}
```

### 2. 获取录音文件

通过 Activity 的 onActivityResult() 回调方法获取录音文件。

#### 2.1 Kotlin

```kotlin
import android.util.Log
import android.net.Uri

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    when (requestCode) {
        0 -> {
            if (resultCode == RESULT_OK) {
                val recordedAudioPath = data?.data as Uri;
                Log.v(TAG, "Uri is $recordedAudioPath");
            }
        }
    }
}
```

#### 2.2 Java

```java
import android.content.Intent;
import android.util.Log;
import android.net.Uri;

@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    switch (requestCode) {
        case  0:
            if (resultCode == RESULT_OK) {
                Uri recordedAudioPath = data.getData();
                Log.v(TAG, "Uri is " + recordedAudioPath.toString());
            }
    }
}
```

