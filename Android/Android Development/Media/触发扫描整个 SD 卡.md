可以通过如下代码触发系统扫描整个 SD 卡：

**Kotlin**

```kotlin
import android.os.Environment
import android.net.Uri
import android.content.Intent

sendBroadcast(Intent(Intent.ACTION_MEDIA_MOUNTED, Uri.parse("file://" + Environment.getExternalStorageDirectory().absolutePath)))
```

**Java**

```java
import android.os.Environment;
import android.net.Uri;
import android.content.Intent;

sendBroadcast(new Intent(Intent.ACTION_MEDIA_MOUNTED, Uri.parse("file://" + Environment.getExternalStorageDirectory().getAbsolutePath())));
```

