要想使 `WebView` 可以执行 `Javascript` 脚本，需要将 `WebView` 的 `WebSettings`  属性的 `javaScriptEnabled` 属性设置为 `true`：

```kotlin
mWebView.settings.apply {
    allowUniversalAccessFromFileURLs = true
    allowFileAccess = true
    allowFileAccessFromFileURLs = true
    allowContentAccess = true
    javaScriptEnabled = true
}
```

在 `Android` 工程的 `assets` 目录中添加要使用的 `Javascript` 和 `CSS` 文件，`assets` 文件夹中的文件 `URL` 格式如下：

```
file:///android_asset/文件在assets目录中的相对路径
```

比如在 `assets` 目录下有一个 `js` 目录用于存放 `prism.js` 的 `Javascript` 文件，则该文件的 `URL` 为：

```
file:///android_asset/js/prism.js
```

因此可以像下面的代码那样使用本地 `Javascript` 和 `CSS` 文件：

```kotlin
private fun showNote() {
    val extendDirectory : String = Environment.getExternalStorageDirectory().absolutePath
    QLog.d(this, "showNote=>extendDirectory: " + extendDirectory)
    QLog.d(this, "showNote=>picture exist: ${File("$extendDirectory/Note/images/08.png").exists()}")
    val baseURL = "file://$extendDirectory/Note/"
    val picturePath = "file://$extendDirectory/Note/images/08.png"
    val prismJsPath = "file:///android_asset/js/prism.js"
    val prismCssPath = "file:///android_asset/css/prism_default.css"
    QLog.d(this, "showNote=>js: ${File("$extendDirectory/QNote/prism.js").exists()}, css: ${File("$extendDirectory/QNote/prism_default.css").exists()}")
    val htmlData = StringBuilder()
    htmlData.append("""<!DOCTYPE html>
<html>
<head>
    <title>Prism Test</title>
    <link href="$prismCssPath" rel="stylesheet" />
    <style type="text/css">
        ::-webkit-scrollbar {display: none;}
    </style>
</head>
<body>
    <div>
    <pre><code class="language-java" style="white-space: pre-wrap;width=100%;">package com.qty.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloServlet extends HttpServlet {

@Override
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    // 获得 username 请求参数
    String userName = req.getParameter("username");

    if (userName == null) {
        // 仅仅为了演示 resp.sendError() 的用法。
        resp.sendError(resp.SC_FORBIDDEN);
        return;
    }

    // 设置 HTTP 响应的正文的 MIME 类型及字符编码
    resp.setContentType("text/html;charset=GBK");

    /* 输出 HTML 文档 */
    PrintWriter out = resp.getWriter();
    out.println("<html><head><title>HelloServlet</title></head>");
    out.println("<body>");
    out.println("你好：" + userName);
    out.println("</body></html>");

    System.out.println("before close(): " + resp.isCommitted()); // false
    out.close();	// 关闭 PrintWriter
    System.out.println("after close(): " + resp.isCommitted()); // true
}

}</code></pre>
    <script src="$prismJsPath"></script>
</body>
</html>""")
    mWebView.loadDataWithBaseURL(null, htmlData.toString(), "text/html", "utf-8", null);
}
```

