[toc]

### 1.  允许 WebView 对文件的操作

```kotlin
val webView = findViewById(R.id.webview)
webView.settings.apply {
    allowUniversalAccessFromFileURLs = true
    allowFileAccess = true
    allowFileAccessFromFileURLs = true
    allowContentAccess = true
}
```

### 2. 设置图片路径

图片路径必须以 `file:///` 开头：

```kotlin
val picturePath = "file://${Environment.getExternalStorageDirectory().absolutePath}${File.separator}08.png"
val htmlData = StringBuilder()
htmlData.append("<!DOCTYPE html\n")
    .append("<html>\n")
    .append("    <head>\n")
    .append("        <title>MyWeb</title>\n")
    .append("    </head>\n")
    .append("    <body>\n")
    .append("        <p>这是来自设备的图片：</p>\n")
    .append("        <img src=\"${picturePath}\" style=\"width:100%\"/>\n")
    .append("    </body>\n")
    .append("</html>")
QLog.d(this, "showNote=>html: ${htmlData.toString()}")
mWebView.loadDataWithBaseURL(null, htmlData.toString(), "text/html", "utf-8", null)
```

