> 注意：Android 最新版本已经不再内置 httpclient 库，需要在 build.gradle 添加 httpclient 库的依赖：
>
> ```
> dependencies {
> 	......
>     implementation 'org.apache.httpcomponents:httpclient:4.5.13'
>     ......
> }
> ```
>
> 具体可以版本号请查阅 <https://mvnrepository.com/artifact/org.apache.httpcomponents/httpclient>。

实现代码如下所示：

**Java**

```java
package com.androidbook.services.httpget;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HttpGetDemo extends AppCompatActivity {

    private static final String TAG = HttpGetDemo.class.getSimpleName();

    /** Called when the activity is first created. */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onResume() {
        super.onResume();
        new Thread(new Runnable() {
            @Override
            public void run() {
                getRequest();
            }
        }).start();
    }

    private void getRequest() {
        BufferedReader in = null;
        try {
            HttpClient client = new DefaultHttpClient();
            HttpGet request = new HttpGet("http://www.baidu.com");
            HttpResponse response = client.execute(request);
            in = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));

            StringBuffer sb = new StringBuffer("");
            String line = "";
            String NL = System.getProperty("line.separator");
            while ((line = in.readLine()) != null) {
                sb.append(line + NL);
            }
            in.close();

            String page = sb.toString();
            Log.d(TAG, "getRequest=>page: \n" + page);
        } catch (Exception e) {
            //TODO Auto-generated catch block
           Log.e(TAG, "getRequest=>error", e);
        } finally {
            if (in != null) {
                try {
                    in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

**Kotlin**
```kotlin
package com.androidbook.services.httpget

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import org.apache.http.client.methods.HttpGet
import org.apache.http.impl.client.DefaultHttpClient
import java.io.BufferedReader
import java.io.InputStreamReader

@Suppress("DEPRECATION")
class HttpGetDemo : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onResume() {
        super.onResume()
        Thread {
            getRequest()
        }.start()
    }

    private fun getRequest() {
        val client = DefaultHttpClient()
        val request = HttpGet("http://www.baidu.com")
        val response = client.execute(request)
        val br = BufferedReader(InputStreamReader(response.entity.content))

        val sb = StringBuffer("")
        val nl = System.getProperty("line.separator")

        var line:String? = br.readLine()
        while (line != null) {
            sb.append(line + nl)
            line = br.readLine()
        }
        br.close()

        val page = sb.toString()
        Log.d(TAG, "getRequest=>page: \n$page")
    }

    companion object {
        const val TAG = "HttpGetDemo"
    }

}
```

> 提示：在编译该工程时，出现如下错误：
>
> ```
> More than one file was found with OS independent path 'META-INF/DEPENDENCIES'
> ```
>
> 解决方法如下:
>
> 在 build.gradle 文件中的 android 项中添加如下代码即可：
>
> ```
> android {
>     ......
> 
>     packagingOptions {
>         exclude 'META-INF/DEPENDENCIES'
>         exclude 'META-INF/NOTICE'
>         exclude 'META-INF/LICENSE'
>         exclude 'META-INF/LICENSE.txt'
>         exclude 'META-INF/NOTICE.txt'
>     }
> 
> 	......
> }
> ```



