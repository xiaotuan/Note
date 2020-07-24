<center><font size="5"><b>查看 PDF 文件</b></font></center>

> 摘自：[android/storage-samples/ActionOpenDocument](https://github.com/android/storage-samples/tree/master/ActionOpenDocument)

```kotlin
import android.graphics.Bitmap
import android.graphics.Bitmap.createBitmap
import android.graphics.pdf.PdfRenderer

private lateinit var pdfRenderer: PdfRenderer
private lateinit var currentPage: PdfRenderer.Page
private var currentPageNumber: Int = 0
private lateinit var pdfPageView: ImageView

override fun onStart() {
    super.onStart()

    val documentUri = arguments?.getString(DOCUMENT_URI_ARGUMENT)?.toUri() ?: return
    try {
        openRenderer(activity, documentUri)
        showPage(currentPageNumber)
    } catch (ioException: IOException) {
        Log.d(TAG, "Exception opening document", ioException)
    }
}

override fun onStop() {
    super.onStop()

    try {
        closeRenderer()
    } catch (ioException: IOException) {
        Log.d(TAG, "Exception closing document", ioException)
    }
}

@Throws(IOException::class)
private fun openRenderer(context: Context?, documentUri: Uri) {
    if (context == null) return

    val fileDescriptor = context.contentResolver.openFileDescriptor(documentUri, "r") ?: return

    pdfRenderer = PdfRenderer(fileDescriptor)
    currentPage = pdfRenderer.openPage(currentPageNumber)
}

@Throws(IOException::class)
private fun closeRenderer() {
    currentPage.close()
    pdfRenderer.close()
}

private fun showPage(index: Int) {
    if (index < 0 || index >= pdfRenderer.pageCount) return

    currentPage.close()
    currentPage = pdfRenderer.openPage(index)

    val bitmap = createBitmap(currentPage.width, currentPage.height, Bitmap.Config.ARGB_8888)

    currentPage.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
    pdfPageView.setImageBitmap(bitmap)

    val pageCount = pdfRenderer.pageCount
    previousButton.isEnabled = (0 != index)
    nextButton.isEnabled = (index + 1 < pageCount)
    activity?.title = getString(R.string.app_name_with_index, index + 1, pageCount)
}
```