[toc]

### 1. 使用 ActivityResultLauncher 类

#### 1.1 传递数据

**Kotlin**

```kotlin
package com.qty.testkotlin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts

private const val TAG = "MainActivity"

class MainActivity : AppCompatActivity() {

    private lateinit var receiverData: TextView
    private lateinit var startActivity: Button
    private lateinit var activityResultLauncher: ActivityResultLauncher<Intent>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        activityResultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            result?.let {
                it.data?.let { intent ->
                    intent.getStringExtra("data")?.let { dataStr ->
                        receiverData.text = "接收到返回数据：$dataStr"
                    }
                }
            }
        }

        receiverData = findViewById(R.id.receive_data)
        startActivity = findViewById(R.id.start_activity);

        startActivity.setOnClickListener {
            val intent = Intent(this, SecondActivity::class.java)
            intent.putExtra("data", "Data is from MainActivity.")
            // 启动其他 Activity
            activityResultLauncher.launch(intent)
        }
    }

}
```

**Java**

```java
package com.qty.androidtestjava;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContract;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityOptionsCompat;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    private TextView mReceiveData;
    private Button mStartActivity;
    private ActivityResultLauncher<Intent> mActivityLauncher;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mActivityLauncher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(), result -> {
            if (result != null) {
                if (result.getData() != null) {
                    String dataStr = result.getData().getStringExtra("data");
                    mReceiveData.setText("接收到返回数据： " + dataStr);
                }
            }
        });

        mReceiveData = findViewById(R.id.receive_data);
        mStartActivity = findViewById(R.id.start_activity);

        mStartActivity.setOnClickListener(v -> {
            Intent intent = new Intent(this, SecondActivity.class);
            intent.putExtra("data", "This data is from MainActivity.");
            mActivityLauncher.launch(intent);
        });
    }

}
```

#### 1.2 接收数据

接收数据方法与使用 startActivityForResult() 方法一样。

### 2. 使用 startActivityForResult() 方法

要将 `extra` 数据信息添加给 `Intent`，需要调用 `Intent.putExtra(...)` 函数，例如：

**Kotlin**

```kotlin
Intent.putExtra(name: String, value: Boolean)
```

**Java**

```java
Intent.putExtra(String name, boolean value)
```

#### 1.1 传递数据

**Kotlin**

```kotlin
package com.qty.testkotlin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

private const val TAG = "MainActivity"
private const val REQUEST_CODE = 88

class MainActivity : AppCompatActivity() {

    private lateinit var receiverData: TextView
    private lateinit var startActivity: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        receiverData = findViewById(R.id.receive_data)
        startActivity = findViewById(R.id.start_activity);

        startActivity.setOnClickListener {
            val intent = Intent(this, SecondActivity::class.java)
            intent.putExtra("data", "Data is from MainActivity.")
            startActivityForResult(intent, REQUEST_CODE)
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_CODE) {
            if (resultCode == RESULT_OK) {
                data?.also {
                    it.getStringExtra("data")?.let {
                        receiverData.text = "接收到返回数据：$it"
                    }
                }
            }
        }
    }
}
```

**Java**

```java
package com.qty.androidtestjava;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    private static final int REQUEST_CODE = 88;

    private TextView mReceiveData;
    private Button mStartActivity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mReceiveData = findViewById(R.id.receive_data);
        mStartActivity = findViewById(R.id.start_activity);

        mStartActivity.setOnClickListener(v -> {
            Intent intent = new Intent(this, SecondActivity.class);
            intent.putExtra("data", "This data is from MainActivity.");
            startActivityForResult(intent, REQUEST_CODE);
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CODE) {
            if (resultCode == RESULT_OK) {
                if (data != null) {
                    String dataStr = data.getStringExtra("data");
                    if (dataStr != null) {
                        mReceiveData.setText("接收到返回数据： " + dataStr);
                    }
                }
            }
        }
    }
}
```

#### 2.2 接收数据

**Kotlin**

```kotlin
package com.qty.testkotlin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.MenuItem
import android.widget.Button
import android.widget.TextView

private const val TAG = "SecondActivity"

class SecondActivity : AppCompatActivity() {

    private lateinit var receiveData: TextView
    private lateinit var returnBtn: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        receiveData = findViewById(R.id.other_activity_data)
        returnBtn = findViewById(R.id.return_data)

        supportActionBar?.setDisplayShowHomeEnabled(true)

        returnBtn.setOnClickListener {
            val data = Intent()
            data.putExtra("data", "Data is from second activity.")
            setResult(RESULT_OK, data)
            finish()
        }

        intent?.let {
            it.getStringExtra("data")?.let {
                receiveData.text = "接收到传递过来的数据：$it"
            }
        }
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        if (item.itemId == android.R.id.home) {
            finish()
            return true
        }
        return super.onOptionsItemSelected(item)
    }
}
```

**Java**

```java
package com.qty.androidtestjava;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity {

    private static final String TAG = "SecondActivity";

    private TextView mReceiveDataTv;
    private Button mBackBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        }

        mReceiveDataTv = findViewById(R.id.other_activity_data);
        mBackBtn = findViewById(R.id.return_data);

        mBackBtn.setOnClickListener(v -> {
            Intent data = new Intent();
            data.putExtra("data", "This data is from SecondActivity.");
            setResult(RESULT_OK, data);
            finish();
        });

        if (getIntent() != null) {
            String dataStr = getIntent().getStringExtra("data");
            if (dataStr != null) {
                mReceiveDataTv.setText("接收到传递过来的数据：" + dataStr);
            }
        }
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        if (item.getItemId() == android.R.id.home) {
            finish();
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
```
