要想通过系统文件管理系统选择文件，可以通过 `Intent.ACTION_OPEN_DOCUMENT` 动作启动选择 `Activity`。具体步骤如下：

1. 定义一个请求码

   ```kotlin
   private const val OPEN_DOCUMENT_REQUEST_CODE = 0x33
   ```

2. 覆写 `Activity` 的 `onActivityResult` 方法

   ```kotlin
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
   ```

   > 注意：如果需要写入文件的话，在调用 `contentResolver.takePersistableUriPermission()` 方法时，应该传入 `Intent.FLAG_GRANT_WRITE_URI_PERMISSION` 参数：
   >
   > ```kotlin
   > contentResolver.takePersistableUriPermission(
   >     documentUri,
   >     Intent.FLAG_GRANT_WRITE_URI_PERMISSION
   > )
   > ```

3. 通过 `startActivityForResult()` 方法启动文件选择 `Activity`

   ```kotlin
   val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
       type = "application/pdf"
       addCategory(Intent.CATEGORY_OPENABLE)
   }
   startActivityForResult(intent, OPEN_DOCUMENT_REQUEST_CODE)
   ```

4. 完整代码如下：

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

   
