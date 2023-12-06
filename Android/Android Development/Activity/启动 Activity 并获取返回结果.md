[toc]

### 1. Activity 类

在 `Activity` 类中可以通过调用 `startActivityForResult()` 方法来启动另一个 `Activity`，并获取 `Activity` 返回的数据。具体步骤如下：

1. 定义一个请求码

   ```java
   private int OPEN_DOCUMENT_REQUEST_CODE = 0x33;
   ```

2. 调用 `startActivityForResult()` 方法启动另外一个 `Activity`

   ```java
   Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
   intent.setType("application/pdf");
   intent.addCategory(Intent.CATEGORY_OPENABLE);
   startActivityForResult(intent, OPEN_DOCUMENT_REQUEST_CODE);
   ```

3. 在子 `Activity` 中的合适位置调用如下方法返回数据给父 `Activity`：

   ```kotlin
   setResult(resultCode: Int)
   setResult(resultCode: Int, data: Intent)
   ```

   一般来说，参数 `resultCode` 可以是以下任意一个预定义的常量。

   + Activity.RESULT_OK
   + Activity.RESULT_CANCELED

4. 在 `Activity` 中覆写 `onActivityResult()` 方法，在该方法中获取 `Activity` 返回的数据。

   ```java
   @Override
   protected void onActivityResult(int requestCode, int resultCode, Intent data) {
       super.onActivityResult(requestCode, resultCode, data);
       if (requestCode == OPEN_DOCUMENT_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
           if (data.getData() != null) {
               getContentResolver().takePersistableUriPermission(data.getData(), Intent.FLAG_GRANT_READ_URI_PERMISSION);
               Log.d(TAG, "onActivityResult=>File uri: " + data.getData());
           }
       }
   }
   ```

#### 1.1 完整代码

##### 1.1.1 Kotlin 的实现代码

   ```kotlin
   package com.android.androidkotlintest
   
   import android.app.Activity
   import android.content.Intent
   import android.os.Bundle
   import android.util.Log
   import android.view.View
   import android.view.View.OnClickListener
   import android.widget.Button
   
   private const val TAG = "MainActivity"
   private const val OPEN_DOCUMENT_REQUEST_CODE = 0x33
   
   class MainActivity : Activity(), OnClickListener {
   
       private lateinit var mOpenBtn: Button
   
       override fun onCreate(savedInstanceState: Bundle?) {
           super.onCreate(savedInstanceState)
           setContentView(R.layout.activity_main)
   
           mOpenBtn = findViewById(R.id.open)
           mOpenBtn.setOnClickListener(this)
       }
   
       override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
           super.onActivityResult(requestCode, resultCode, data)
           if (requestCode == OPEN_DOCUMENT_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
               data?.data?.also { documentUri ->
                   contentResolver.takePersistableUriPermission(
                       documentUri,
                       Intent.FLAG_GRANT_READ_URI_PERMISSION
                   )
                   Log.d(TAG, "onActivityResult=>documentUri: $documentUri")
               }
           }
       }
   
       override fun onClick(v: View?) {
           val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
               type = "application/pdf"
               addCategory(Intent.CATEGORY_OPENABLE)
           }
           startActivityForResult(intent, OPEN_DOCUMENT_REQUEST_CODE)
       }
   }
   ```

##### 1.1.2 Java 的实现代码

   ```java
   package com.qty.androidtest;
   
   import android.app.Activity;
   import android.content.Intent;
   import android.os.Bundle;
   import android.util.Log;
   import android.view.View;
   import android.widget.Button;
   
   public class MainActivity extends Activity implements View.OnClickListener {
   
       private static final String TAG = "MainActivity";
       private int OPEN_DOCUMENT_REQUEST_CODE = 0x33;
       private Button mOpenBtn;
   
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
   
           mOpenBtn = findViewById(R.id.open);
           mOpenBtn.setOnClickListener(this);
       }
   
       @Override
       protected void onActivityResult(int requestCode, int resultCode, Intent data) {
           super.onActivityResult(requestCode, resultCode, data);
           if (requestCode == OPEN_DOCUMENT_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
               if (data.getData() != null) {
                   getContentResolver().takePersistableUriPermission(data.getData(), Intent.FLAG_GRANT_READ_URI_PERMISSION);
                   Log.d(TAG, "onActivityResult=>File uri: " + data.getData());
               }
           }
       }
   
       @Override
       public void onClick(View v) {
           Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
           intent.setType("application/pdf");
           intent.addCategory(Intent.CATEGORY_OPENABLE);
           startActivityForResult(intent, OPEN_DOCUMENT_REQUEST_CODE);
       }
   }
   ```

### 2. ComponentActivity 类

在 `ComponentActivity` 中 `onActivityResult()` 已经被标记为弃用方法，推荐使用 `registerForActivityResult()` 方法启动另一个 `Activity` 并获取 `Activity` 返回的数据。具体步骤如下：

1. 在 `build.gradle` 文件中添加依赖（ `Kotlin` 工程默认添加）

   ```
   implementation 'androidx.appcompat:appcompat:1.4.1'
   ```

2. 确保 `Activity` 继承自 `AppCompatActivity` 类

   ```kotlin
   class MainActivity : AppCompatActivity() {
    	...   
   }
   ```

3. 定义 `ActivityResultLauncher<Intent>` 变量

   ```kotlin
   private lateinit var mActivityLauncher: ActivityResultLauncher<Intent>
   ```

4. 在 `onCreate()` 方法中初始化 `ActivityResultLauncher<Intent>` 变量

   ```kotlin
   mActivityLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
       if (result.resultCode == Activity.RESULT_OK) {
           result.data?.data?.also { documentUri ->
               contentResolver.takePersistableUriPermission(
                   documentUri,
                   Intent.FLAG_GRANT_READ_URI_PERMISSION
               )
               Log.d(TAG, "onActivityResult=>documentUri: $documentUri")
           }
       }
   }
   ```

5. 调用 `ActivityResultLauncher<Intent>` 变量的 `launch()` 方法启动另一个 `Activity`

   ```kotlin
   val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
       type = "application/pdf"
       addCategory(Intent.CATEGORY_OPENABLE)
   }
   mActivityLauncher.launch(intent)
   ```

> 注意：`ActivityResultLauncher<Intent>` 变量必须在 `onCreate` 方法中初始化，否则运行将会报错。

#### 2.1 完整代码

```kotlin
package com.android.androidkotlintest

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import android.view.View.OnClickListener
import android.widget.Button
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity

private const val TAG = "MainActivity"

class MainActivity : AppCompatActivity(), OnClickListener {

    private lateinit var mOpenBtn: Button
    private lateinit var mActivityLauncher: ActivityResultLauncher<Intent>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mOpenBtn = findViewById(R.id.open)
        mOpenBtn.setOnClickListener(this)

        mActivityLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            if (result.resultCode == Activity.RESULT_OK) {
                result.data?.data?.also { documentUri ->
                    contentResolver.takePersistableUriPermission(
                        documentUri,
                        Intent.FLAG_GRANT_READ_URI_PERMISSION
                    )
                    Log.d(TAG, "onActivityResult=>documentUri: $documentUri")
                }
            }
        }
    }

    override fun onClick(v: View?) {
        val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
            type = "application/pdf"
            addCategory(Intent.CATEGORY_OPENABLE)
        }
        mActivityLauncher.launch(intent)
    }
}
```

