可以通过 `WebView` 的如下三个方法加载本地 html 文件：

```java
public void loadUrl(String url);
public void loadData(String data, String mimeType, String encoding);
public void loadDataWithBaseURL(String baseUrl, String data,
            String mimeType, String encoding, String failUrl);
```

+ `loadUrl(String url)`

  url: 本地 html 文件的 URL

+ `loadData(String data, String mimeType, String encoding)`

  data：HTML 文件的内容；

  mimeType：HTML 文件的 mimeType，值为："text/html"

  encoding：data 的字符编码，一般为 "utf-8"。

+ `loadDataWithBaseURL(String baseUrl, String data, String mimeType, String encoding, String failUrl)`

  baseUrl：HTML 文件使用到的资源的根目录 URL

  data：HTML 文件的内容；

  mimeType：HTML 文件的 mimeType，值为："text/html"

  encoding：data 的字符编码，一般为 "utf-8"。

  failUrl：加载 data 失败后要显示的失败页面 URL。

例如：

**First.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <p>Antoni Gaudi's incredible buildings bring millions ...</p>
    </body>
</html>
```

**MainActivity.java**

```java
package com.qty.loadlocalhtml;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.webkit.WebView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();

    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mWebView = findViewById(R.id.webview);
        try {
            InputStream is = getAssets().open("First.html");
            BufferedReader br = new BufferedReader(new InputStreamReader(is));
            StringBuilder sb = new StringBuilder();
            String line = null;
            while ((line = br.readLine()) != null) {
                sb.append(line).append("\n");
            }
            br.close();
            is.close();
            Log.d(TAG, "html content: \n" + sb.toString());
            mWebView.loadData(sb.toString(), "text/html", "utf-8");
        } catch (IOException e) {
            Log.e(TAG, "onCreate=>error: ", e);
        }
    }
}
```

下面是调用 `loadDataWithBaseURL(String baseUrl, String data, String mimeType, String encoding, String failUrl)` 的示例代码：

**First.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <p>Antoni Gaudi's incredible buildings bring millions ...</p>
        <img src="01.jpg" />
    </body>
</html>
```

**MainActivity.java**

```java
package com.qty.loadlocalhtml;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.webkit.WebView;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();

    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mWebView = findViewById(R.id.webview);
        try {
            InputStream is = getAssets().open("First.html");
            BufferedReader br = new BufferedReader(new InputStreamReader(is));
            StringBuilder sb = new StringBuilder();
            String line = null;
            while ((line = br.readLine()) != null) {
                sb.append(line).append("\n");
            }
            br.close();
            is.close();
            Log.d(TAG, "html content: \n" + sb.toString());
            String basePath = "/storage/self/primary/images/";
            File file = new File(basePath);
            Log.d(TAG, "base path is exist: " + file.exists());
            if (!file.exists() || !file.isDirectory()) {
                file.mkdirs();
            }
            mWebView.loadDataWithBaseURL(file.toURI().toString(), sb.toString(), "text/html", "utf-8", null);
        } catch (IOException e) {
            Log.e(TAG, "onCreate=>error: ", e);
        }
    }
}
```

