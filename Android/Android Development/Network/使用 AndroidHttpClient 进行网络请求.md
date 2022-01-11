`Android 2.2` 引入了 `HttpClient` 的一个新子类 `AndroidHttpClient`。此类背后的理念是通过提供默认值和适合 Android 应用程序的逻辑。连接管理器默认为 `ThreadSafeClientConnManager`。

`AndroidHttpClient` 的使用步骤如下：

+ 要创建 `AndroidHttpClient`，可以调用 `AndroidHttpClient` 类的静态 `newInstance()` 方法。
+ `newInstance()` 方法的参数为一个 HTTP 代理字符串。
+ 当在此客户端上调用 `execute()` 时，必须位于独立于主 UI 线程的线程中。从主 UI 线程发出 HTTP 调用是一种糟糕的做法，所以 `AndroidHttpClient` 不会允许这么做。
+ 完成对 `AndroidHttpClient` 实例的处理之后，必须对它调用 `close()`。
+ 有一些方便的静态方法可用于处理来自服务器的压缩响应，包括：
  + modifyRequestToAcceptGzipResponse(HttpRequest request)
  + getCompressedEntity(byte[] data, ContentResolver resolver)
  + getUngzippedContent(HttpEntity entity)

### 1. GET 请求

**Kotlin**

```kotlin
import android.net.http.AndroidHttpClient
import android.os.Bundle
import android.util.Log
import org.apache.http.client.methods.HttpGet
import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Exception
import java.lang.StringBuilder

Thread() {
    val ahc = AndroidHttpClient.newInstance(null)
    val httpGet = HttpGet("https://www.baidu.com")
    try {
        val resp = ahc.execute(httpGet)
        if (resp.statusLine.statusCode == 200) {
            val sb = StringBuilder()
            val reader = BufferedReader(InputStreamReader(resp.entity.content))
            var line: String? = reader.readLine()
            while (line != null) {
                sb.append(line)
                line = reader.readLine()
            }
            Log.d(TAG, "respone: " + sb.toString())
        }
    } catch(e: Exception) {
        Log.e(TAG, "error: ", e)
    }
}.start()
```

**Java**

```java
import android.net.http.AndroidHttpClient;
import android.os.Bundle;
import android.util.Log;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

new Thread(() -> {
    AndroidHttpClient ahc = AndroidHttpClient.newInstance(null);
    HttpGet get = new HttpGet("https://www.baidu.com");
    Log.d(TAG, "start execute.");
    try {
        HttpResponse resp = ahc.execute(get);
        Log.d(TAG, "code: " + resp.getStatusLine().getStatusCode());
        if (resp.getStatusLine().getStatusCode() == 200) {
            BufferedReader br = new BufferedReader(new InputStreamReader(resp.getEntity().getContent()));
            StringBuffer sb = new StringBuffer();
            String line = null;
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
            Log.d(TAG, "respone: " + sb.toString());
        } else {
            Log.d(TAG, "request fail.");
        }
    } catch (IOException e) {
        Log.d(TAG, "error: ", e);
    }
    ahc.close();
}).start();
```

### 2. POST 请求

POST 请求可用参照 [使用 HttpClient 进行 POST 请求.md](./使用 HttpClient 进行 POST 请求.md) 文章，使用 `HttpPost` 类构建 `AndroidHttpClient` 的请求参数即可。
