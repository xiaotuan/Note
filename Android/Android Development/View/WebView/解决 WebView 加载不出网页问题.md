**1. 问题代码**

```java
import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.webkit.WebChromeClient;
import android.webkit.WebView;

public class MainActivity extends Activity {

    private static final String TAG = "MainActivity";

    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN | View.SYSTEM_UI_FLAG_LAYOUT_STABLE);
        getWindow().setStatusBarColor(getResources().getColor(android.R.color.transparent));
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mWebView = findViewById(R.id.acer_legal);
        mWebView.loadUrl("file:///android_res/raw/eula.htm");
    }
    
}
```

**2. 问题现象**

启动应用后，WebView 一片空白，没有内容，换成百度网站也一样，使用品牌手机测试能够显示内容。

**3. 原因分析**

将 `mWebView.loadUrl("file:///android_res/raw/eula.htm");` 移至 `onResume()` 方法执行后可以显示出来，可能是过早加载网页造成的。

**4. 解决办法**

将 `mWebView.loadUrl("file:///android_res/raw/eula.htm");` 移至 `onResume()` 方法执行。

```java
import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.webkit.WebChromeClient;
import android.webkit.WebView;

public class MainActivity extends Activity {

    private static final String TAG = "MainActivity";

    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN | View.SYSTEM_UI_FLAG_LAYOUT_STABLE);
        getWindow().setStatusBarColor(getResources().getColor(android.R.color.transparent));
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mWebView = findViewById(R.id.acer_legal);
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        mWebView.loadUrl("file:///android_res/raw/eula.htm");
    }
}
```

