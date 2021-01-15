在网页中嵌入 `jQuery` 程序库有两种理想的解决方案：

+ 使用 [Google 托管的内容分发网络](https://developers.google.com/speed/libraries) （ Content Delivery Network, CDN）来包含某个版本的 jQuery（本章采用这种方式）。
+ 从 [jQuery.com](https://jquery.com/download/) 上下载你自己的 jQuery 版本，将其安装在你自己的服务器或者本地文件系统上。

显示 jQuery 版本号对话框：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Example04</title>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>
        <script>
            alert('jQuery ' + jQuery.fn.jquery);
        </script>
    </body>
</html>
```

