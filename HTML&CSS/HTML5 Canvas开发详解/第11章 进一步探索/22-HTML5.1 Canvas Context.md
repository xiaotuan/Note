### 11.5.1　HTML5.1 Canvas Context

在HTML5.1中，Canvas的环境对象除了toDataURL()和getContext()之外将包含一些新方法。

#### 1．supportsContext()

这个方法允许开发者在浏览器中检测哪些Canvas的环境可以被支持。在本书中，大多数时间使用的是2D环境对象，本章介绍了“experimental-wbgl”或叫做“moz-3d”。在将来，新的Canvas环境都将在这个网站进行注册（<a class="my_markdown" href="['http://wiki.whatwg.org/wiki/CanvasContexts']">http://wiki.whatwg.org/wiki/CanvasContexts</a>）。

#### 2．toDataURLHD(), toBlob(), toBlobHD()

本书前面介绍过，toDataURL()允许开发者将Canvas上显示的内容导出为一个base64编码的字符串，该字符串也可以转换为图像。这个图像的解析度被限定为96dpi。在HTML5.1中，这个能力被进行了集中扩展。

+ toDataURLHD()；

根据本地的解析度返回画布的数据，不再限定为96dpi。

+ toBlob()；

将画布数据导出为一个96dpi的图像blob对象，取代原来的base64编码的字符串。

+ toBlobHD()；

根据本地解析度，将画布数据导出成为一个图像类型的blob对象。

