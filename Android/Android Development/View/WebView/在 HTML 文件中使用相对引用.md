如果需要在 `HTMl` 文件中使用相对引用，需要在 `<head>` 标签中添加 `<base>` 元素，指定 `HTML` 文件的当前位置，例如：

```kotlin
val extendDirectory : String = Environment.getExternalStorageDirectory().absolutePath
val baseURL = "file://$extendDirectory/Note/"
val picturePath = "file://$extendDirectory/Note/images/08.png"
val htmlData = StringBuilder()
htmlData.append("<!DOCTYPE html\n")
    .append("<html>\n")
    .append("    <head>\n")
    .append("        <title>MyWeb</title>\n")
    .append("        <base href=\"$baseURL\">\n")
    .append("    </head>\n")
    .append("    <body>\n")
    .append("        <p>这是来自设备的图片：</p>\n")
    .append("        <img src=\"./images/08.png\" style=\"width:50%\"/>\n")
    .append("    </body>\n")
    .append("</html>")
mWebView.loadDataWithBaseURL(null, htmlData.toString(), "text/html", "utf-8", null)
```

