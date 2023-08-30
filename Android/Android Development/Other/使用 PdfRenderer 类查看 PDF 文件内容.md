1. 通过 `PDF` 文件 `Uri` 创建 `PdfRenderer` 对象

   ```kotlin
   mPdfRenderer = PdfRenderer(fileDescriptor)
   ```

2. 通过 `PdfRenderer` 对象的 `openPage()` 方法获取 `PDF` 指定页数的数据。

   ```kotlin
   mCurrentPage = mPdfRenderer?.openPage(mCurrentPageNumber)
   ```

3. 通过 `PdfReaderer.Page` 对象创建该页的 `Bitmap` 对象

   ```kotlin
   val bitmap = createBitmap(page.width, page.height, Bitmap.Config.ARGB_8888)
   page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
   ```

4. 将得到的 `Bitmap` 对象设置到 `ImageView` 中显示出来。

   ```kotlin
   mPdfPageView.setImageBitmap(bitmap)
   ```

5. 完整代码如下：

   ```kotlin
   package com.android.androidkotlintest
   
   import android.app.Activity
   import android.content.Intent
   import android.graphics.Bitmap
   import android.graphics.pdf.PdfRenderer
   import android.net.Uri
   import android.os.Bundle
   import android.util.Log
   import android.view.View
   import android.view.View.OnClickListener
   import android.widget.Button
   import android.widget.ImageView
   import androidx.activity.result.ActivityResultLauncher
   import androidx.activity.result.contract.ActivityResultContracts
   import androidx.appcompat.app.AppCompatActivity
   import androidx.core.graphics.createBitmap
   import java.io.IOException
   
   private const val TAG = "MainActivity"
   private const val INITIAL_PAGE_INDEX = 0
   private const val CURRENT_PAGE_INDEX_KEY =
       "com.example.android.actionopendocument.state.CURRENT_PAGE_INDEX_KEY"
   
   class MainActivity : AppCompatActivity(), OnClickListener {
   
       private lateinit var mNoDocumentContainer: View
       private lateinit var mPdfViewContainer: View
       private lateinit var mPdfPageView: ImageView
       private lateinit var mPreviousButton: Button
       private lateinit var mNextButton: Button
       private lateinit var mOpenBtn: Button
       private lateinit var mActivityLauncher: ActivityResultLauncher<Intent>
   
       private var mPdfRenderer: PdfRenderer? = null
       private var mCurrentPage: PdfRenderer.Page? = null
   
       private var mCurrentPageNumber: Int = INITIAL_PAGE_INDEX
   
       override fun onCreate(savedInstanceState: Bundle?) {
           super.onCreate(savedInstanceState)
           setContentView(R.layout.activity_main)
   
           mNoDocumentContainer = findViewById(R.id.no_document_view)
           mPdfViewContainer = findViewById(R.id.pdf_contain)
           mPdfPageView = findViewById(R.id.pdf_view)
           mPreviousButton = findViewById(R.id.previous)
           mNextButton = findViewById(R.id.next)
           mOpenBtn = findViewById(R.id.open)
   
           mPreviousButton.setOnClickListener(this)
           mNextButton.setOnClickListener(this)
           mOpenBtn.setOnClickListener(this)
   
           mCurrentPageNumber = savedInstanceState?.getInt(CURRENT_PAGE_INDEX_KEY, INITIAL_PAGE_INDEX) ?: INITIAL_PAGE_INDEX
   
           mActivityLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
               if (result.resultCode == Activity.RESULT_OK) {
                   result.data?.data?.also { documentUri ->
                       contentResolver.takePersistableUriPermission(
                           documentUri,
                           Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                       )
                       Log.d(TAG, "onCreate=>documentUri: $documentUri")
                       try {
                           openRenderer(documentUri)
                           showPage(mCurrentPageNumber)
                           mNoDocumentContainer.visibility = View.GONE
                           mPdfViewContainer.visibility = View.VISIBLE
                       } catch (ex: IOException) {
                           Log.e(TAG, "onCreate=>error: $ex")
                       }
                   }
               }
           }
       }
   
       override fun onStop() {
           super.onStop()
           try {
               closeRenderer()
           } catch (ex: IOException) {
               Log.e(TAG, "onStop=>error: $ex")
           }
       }
   
       override fun onSaveInstanceState(outState: Bundle) {
           outState.putInt(CURRENT_PAGE_INDEX_KEY, mCurrentPage?.index ?: INITIAL_PAGE_INDEX)
           super.onSaveInstanceState(outState)
       }
   
       override fun onClick(v: View?) {
           when (v?.id) {
               R.id.previous -> {
                   mCurrentPage?.let {
                       showPage(it.index - 1)
                   }
               }
               R.id.next -> {
                   mCurrentPage?.let {
                       showPage(it.index + 1)
                   }
               }
               R.id.open -> {
                   val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
                       type = "application/pdf"
                       addCategory(Intent.CATEGORY_OPENABLE)
                   }
                   mActivityLauncher.launch(intent)
               }
           }
       }
   
       private fun openRenderer(uri: Uri) {
           val fileDescriptor =  contentResolver.openFileDescriptor(uri, "r") ?: return
           mPdfRenderer = PdfRenderer(fileDescriptor)
           mCurrentPage = mPdfRenderer?.openPage(mCurrentPageNumber)
       }
   
       private fun showPage(index: Int) {
           mPdfRenderer?.let { renderer ->
               if (index < 0 || index >= renderer.pageCount) return
   
               mCurrentPage?.close()
               mCurrentPage = renderer.openPage(index)
   
               mCurrentPage?.let { page ->
                   val bitmap = createBitmap(page.width, page.height, Bitmap.Config.ARGB_8888)
   
                   page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
                   mPdfPageView.setImageBitmap(bitmap)
   
                   val pageCount = renderer.pageCount
                   mPreviousButton.isEnabled = (0 != index)
                   mNextButton.isEnabled = (index + 1 < pageCount)
               }
           }
       }
   
       private fun closeRenderer() {
           mCurrentPage?.close()
           mPdfRenderer?.close()
       }
   }
   ```

   