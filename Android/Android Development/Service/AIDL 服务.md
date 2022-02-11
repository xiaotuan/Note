[toc]

### 1. 构建 AIDL 服务

要构建远程服务，执行以下步骤：

（1）编写一个 AIDL 文件来向客户端定义接口。AIDL 文件使用 Java 语法并拥有扩展名 `.aidl`。AIDL 文件内部使用的包名称与 Android 项目所使用的包相同。

（2）将 AIDL 文件添加到项目 aidl 目录下，Android Studio 将调用 AIDL 编译器从 AIDL 文件生成 Java 接口（AIDL 编译器在构建过程中调用）。

（3）实现一个服务并从 onBind() 方法返回所生成的接口。

（4）将服务配置添加到 AndroidManifest.xml 文件中。

#### 1.1 定义 AIDL 接口

##### 1.1.1 Kotlin

```kotlin
// This file is IStockQuoteService.aidl
package com.androidbook.services.stockquoteservice;

interface IStockQuoteService {
    double getQuote(String ticker);
}
```

##### 1.1.2 Java

```java
// This file is IStockQuoteService.aidl
package com.androidbook.services.stockquoteservice;

interface IStockQuoteService {
    double getQuote(String ticker);
}
```

> 注意：
>
> AIDL 文件放置的目录结构必须与 AIDL 文件的包名一致。

#### 1.2 实现 AIDL 接口

##### 1.2.1 Kotlin

```kotlin
package com.androidbook.services.stockquoteservice

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.util.Log

class StockQuoteService: Service() {

    override fun onBind(intent: Intent?): IBinder? {
        Log.d(TAG, "onBind() called")
        return StockQuoteServiceImpl()
    }

    override fun onCreate() {
        super.onCreate()
        Log.v(TAG, "onCreate() called")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "onDestroy() called")
    }

    class StockQuoteServiceImpl: IStockQuoteService.Stub() {

        override fun getQuote(ticker: String?): Double {
            Log.v(TAG, "getQuote() called for $ticker")
            return 20.0
        }

    }

    companion object {
        const val TAG = "StockQuoteService"
    }
}
```

##### 1.2.2 Java

```java
package com.androidbook.services.stockquoteservice;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteException;
import android.util.Log;

import androidx.annotation.Nullable;

public class StockQuoteService extends Service {

    private static final String TAG = "StockQuoteService";

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        Log.d(TAG, "onBind() called");
        return new StockQuoteServiceImpl();
    }

    @Override
    public void onCreate() {
        super.onCreate();
        Log.d(TAG, "onCreate() called");
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "onDestroy() called");
    }

    class StockQuoteServiceImpl extends IStockQuoteService.Stub {

        @Override
        public double getQuote(String ticker) throws RemoteException {
            Log.v(TAG, "getQuote() called for " + ticker);
            return 20.0;
        }

    }
}
```

### 2. 从客户端应用程序调用服务

从客户端应用程序调用服务步骤如下：

（1） 创建一个新的 Android 项目，将其命名为 StockQuoeClient。使用不同的包名称，比如 com.androidbook.stockquoteclient。

（2）在此项目中的 aidl 目录下创建一个新 Java 包，将其命名为 com.androidbook.services.stockquoteservice。

（3）将 IStockQuoteService.aidl 文件从 StockQuoteService 项目复制到新创建的包。

#### 2.1 Kotlin

```kotlin
package com.androidbook.services.stockquoteservice

import android.app.Activity
import android.content.ComponentName
import android.content.Intent
import android.content.ServiceConnection
import android.os.Bundle
import android.os.IBinder
import android.os.RemoteException
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.Toast
import android.widget.ToggleButton

class MainActivity: Activity() {

    private var stockService: IStockQuoteService? = null
    private lateinit var bindBtn: ToggleButton
    private lateinit var  callBtn: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main);

        bindBtn = findViewById(R.id.bindBtn)
        callBtn = findViewById(R.id.callBtn)
    }

    override fun onDestroy() {
        Log.d(TAG, "onDestroy() called")
        if (callBtn.isEnabled()) {
            unbindService(serConn)
        }
        super.onDestroy()
    }

    public fun doClick(view: View) {
        when (view.id) {
            R.id.bindBtn -> {
                if ((view as ToggleButton).isChecked) {
                    bindService(Intent(IStockQuoteService::class.java.name), serConn, BIND_AUTO_CREATE)
                } else {
                    unbindService(serConn)
                    callBtn.isEnabled = false
                }
            }
            R.id.callBtn -> {
                callService()
            }
        }
    }

    private fun callService() {
        try {
            val quote = stockService.getQuote("ANDROID");
            Toast.makeText(this, "Value from service is $quote", Toast.LENGTH_SHORT).show()
        } catch (e: RemoteException) {
            Log.e(TAG, "callService=>error: ", e);
        }
    }

    private val serConn = object: ServiceConnection {
        override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
            Log.v(TAG, "onServiceConnected() called")
            stockService = IStockQuoteService.Stub.asInterface(service)
            bindBtn.isChecked = true
            callBtn.isEnabled = true
        }

        override fun onServiceDisconnected(name: ComponentName?) {
            Log.v(TAG, "onServiceDisconnected() called")
            bindBtn.isChecked = false
            callBtn.isEnabled = false
            stockService = null
        }
    }

    companion object {
        const val TAG = "MainActivity"
    }
}
```

#### 2.2 Java

```java
package com.androidbook.services.stockquoteservice;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import android.widget.ToggleButton;

import androidx.annotation.Nullable;

public class MainActivity extends Activity {

    private static final String TAG = "StockQuoteClient";

    private IStockQuoteService stockService = null;
    private ToggleButton bindBtn;
    private Button callBtn;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        bindBtn = findViewById(R.id.bindBtn);
        callBtn = findViewById(R.id.callBtn);
    }

    @Override
    protected void onDestroy() {
        Log.v(TAG, "onDestroy() called");
        if (callBtn.isEnabled()) {
            unbindService(serConn);
        }
        super.onDestroy();
    }

    public void doClick(View view) {
        switch(view.getId()) {
            case R.id.bindBtn:
                if (((ToggleButton) view).isChecked()) {
                    bindService(new Intent(IStockQuoteService.class.getName()),
                            serConn, Context.BIND_AUTO_CREATE);
                } else {
                    unbindService(serConn);
                    callBtn.setEnabled(false);
                }
                break;

            case R.id.callBtn:
                callService();
                break;
        }
    }

    private void callService() {
        try {
            double val = stockService.getQuote("ANDROID");
            Toast.makeText(this, "Value from service is " + val,
                    Toast.LENGTH_SHORT).show();
        } catch (RemoteException e) {
            Log.e(TAG, "callService=>error: ", e);
        }
    }

    private ServiceConnection serConn = new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            Log.v(TAG, "onServiceConnected() called");
            stockService = IStockQuoteService.Stub.asInterface(service);
            bindBtn.setChecked(true);
            callBtn.setEnabled(true);
        }

        @Override
        public void onServiceDisconnected(ComponentName name) {
            Log.v(TAG, "onServiceDisconnected() called");
            bindBtn.setChecked(false);
            callBtn.setEnabled(false);
            stockService = null;
        }
    };
}
```

> 注意
>
> `onServiceDisconnected()` 回调方法在服务解绑时并不会被调用，只有在服务崩溃时才会调用它。