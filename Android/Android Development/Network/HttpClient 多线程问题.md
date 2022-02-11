[toc]

### 1. 定义统一的 HttpClient

在实际应用中，应该为整个应用程序创建一个 `HttpClient`，并将其用于所有 HTTP 通信。应该注意在通过同一个 `HttpClient` 同时发出多个请求时可能发生的多线程问题。可以使用 `ThreadSafeClientConnManager` 创建 `DefaultHttpClient` 来解决多线程问题。

**Kotlin**

```kotlin
import org.apache.http.HttpVersion
import org.apache.http.client.HttpClient
import org.apache.http.conn.params.ConnManagerParams
import org.apache.http.conn.scheme.PlainSocketFactory
import org.apache.http.conn.scheme.Scheme
import org.apache.http.conn.scheme.SchemeRegistry
import org.apache.http.conn.ssl.SSLSocketFactory
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.impl.conn.tsccm.ThreadSafeClientConnManager
import org.apache.http.params.BasicHttpParams
import org.apache.http.params.HttpConnectionParams
import org.apache.http.params.HttpProtocolParams
import org.apache.http.protocol.HTTP

class CustomHttpClient private constructor(){

    companion object {

        val mHttpClient: HttpClient by lazy(mode = LazyThreadSafetyMode.SYNCHRONIZED) {
            getHttpClient()
        }

        private fun getHttpClient(): HttpClient {
            val params = BasicHttpParams()
            HttpProtocolParams.setVersion(params, HttpVersion.HTTP_1_1)
            HttpProtocolParams.setContentCharset(params, HTTP.DEFAULT_CONTENT_CHARSET)
            HttpProtocolParams.setUseExpectContinue(params, true)
            HttpProtocolParams.setUserAgent(params, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

            ConnManagerParams.setTimeout(params, 1000)

            HttpConnectionParams.setConnectionTimeout(params, 5000)
            HttpConnectionParams.setSoTimeout(params, 10000)

            val schReg = SchemeRegistry()
            schReg.register(Scheme("http", PlainSocketFactory.getSocketFactory(), 80))
            schReg.register(Scheme("https", SSLSocketFactory.getSocketFactory(), 443))
            val conMgr = ThreadSafeClientConnManager(params, schReg)

            return DefaultHttpClient(conMgr, params)
        }
    }
}
```

**Java**

```java
import org.apache.http.HttpVersion;
import org.apache.http.client.HttpClient;
import org.apache.http.conn.ClientConnectionManager;
import org.apache.http.conn.params.ConnManagerParams;
import org.apache.http.conn.scheme.PlainSocketFactory;
import org.apache.http.conn.scheme.Scheme;
import org.apache.http.conn.scheme.SchemeRegistry;
import org.apache.http.conn.ssl.SSLSocketFactory;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.conn.tsccm.ThreadSafeClientConnManager;
import org.apache.http.params.BasicHttpParams;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.params.HttpParams;
import org.apache.http.params.HttpProtocolParams;
import org.apache.http.protocol.HTTP;

public class CustomHttpClient {

    private static HttpClient mHttpClient;

    /**
     * A private Constructor prevents instantiation
     */
    private CustomHttpClient() {
    }

    public static synchronized HttpClient getHttpClient() {
        if (mHttpClient == null) {
            HttpParams params = new BasicHttpParams();
            HttpProtocolParams.setVersion(params, HttpVersion.HTTP_1_1);
            HttpProtocolParams.setContentCharset(params, HTTP.DEFAULT_CONTENT_CHARSET);
            HttpProtocolParams.setUseExpectContinue(params, true);
            HttpProtocolParams.setUserAgent(params, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36");

            ConnManagerParams.setTimeout(params, 1000);

            HttpConnectionParams.setConnectionTimeout(params, 5000);
            HttpConnectionParams.setSoTimeout(params, 10000);

            SchemeRegistry schReg = new SchemeRegistry();
            schReg.register(new Scheme("http", PlainSocketFactory.getSocketFactory(), 80));
            schReg.register(new Scheme("https", SSLSocketFactory.getSocketFactory(), 443));

            ClientConnectionManager conMgr = new ThreadSafeClientConnManager(params, schReg);

            mHttpClient = new DefaultHttpClient(conMgr, params);
        }

        return mHttpClient;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        throw new CloneNotSupportedException();
    }
}
```

### 2. 使用统一的 HttpClient

#### 2.1 Kotlin

```kotlin
import android.app.Activity
import android.os.Bundle
import android.util.Log
import org.apache.http.client.HttpClient
import org.apache.http.client.methods.HttpGet
import org.apache.http.impl.client.BasicResponseHandler
import java.io.IOException

class HttpActivity: Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main)

        getHttpContent();
    }

    private fun getHttpContent() {
        Thread {
            try {
                val request = HttpGet("http://www.google.com/")
                val page = CustomHttpClient.mHttpClient.execute(request, BasicResponseHandler())
                Log.d(TAG, "getHttpContent=>page: $page")
            } catch (e: IOException) {
                // covers:
                //      ClientProtocolException
                //      ConnectTimeoutException
                //      ConnectionPoolTimeoutException
                //      SocketTimeoutException
                Log.e(TAG, "getHttpContent=>error: ", e)
            }
        }.start()
    }

    companion object {
        const val TAG = "HttpActivity"
    }
}
```

#### 2.2 Java

```java
import android.app.Activity;
import android.os.Bundle;
import android.util.Log;

import androidx.annotation.Nullable;

import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;

import java.io.IOException;

public class HttpActivity extends Activity {

    private static final String TAG = HttpActivity.class.getSimpleName();

    private HttpClient mHttpClient;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        mHttpClient = CustomHttpClient.getHttpClient();
        getHttpContent();
    }

    public void getHttpContent() {
        new Thread(() -> {
            try {
                HttpGet request = new HttpGet("http://www.google.com/");
                String page = mHttpClient.execute(request, new BasicResponseHandler());
                Log.d(TAG, "getHttpContent=>page: " + page);
            } catch (IOException e) {
                // covers:
                //      ClientProtocolException
                //      ConnectTimeoutException
                //      ConnectionPoolTimeoutException
                //      SocketTimeoutException
                Log.e(TAG, "getHttpContent=>error: ", e);
            }
        }).start();
    }
}
```

### 3. 为特定请求设置连接参数

#### 3.1 Kotlin

```kotlin
val request = HttpGet("http://www.google.com/")
val params = request.getParams()
HttpConnectionParams.setSoTimeout(params, 60000)	// 1 minute
request.setParams(params)
val page = httpClient.execute(request, BasicResponseHandler())
Log.d(TAG, "page: " + page)
```

#### 3.2 Java

```java
HttpGet request = new HttpGet("http://www.google.com/");
HttpParams params = request.getParams();
HttpConnectionParams.setSoTimeout(params, 60000);	// 1 minute
request.setParams(params);
String page = httpClient.execute(request, new BasicResponseHandler());
Log.d(TAG, "page: " + page);
```

