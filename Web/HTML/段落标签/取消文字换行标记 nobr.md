如果浏览器中单行文字的宽度过长，浏览器会自动将该文字换行显示，如果希望强制浏览器不换行显示，可以使用相应的标记。

### 1. 语法

```html
<nobr>不换行显示的文字</nobr>
```

### 2. 示例代码

```html
<html>
    <head>
    	<title>文字不换行显示</title>
    </head>
    <body>
        <!--当浏览器宽度不够时，文本内容会自动换行显示-->
        World Wide Web（万维网WWW）是一种建立在Internrt上的、全球性的、交互的、多平台的、分布式的信息资源网络。它采用HTML语言描述超文本（Hypertext）文件。这里所说的超文本指的是包含有链接关系的文件，并且包含了多媒体对象的文件。<p>
        <!--下面这段文字不会自动换显示，当浏览器宽度不够时，会出现滚动条-->
        <p><nobr>World Wide Web（万维网WWW）是一种建立在Internrt上的、全球性的、交互的、多平台的、分布式的信息资源网络。它采用HTML语言描述超文本（Hypertext）文件。这里所说的超文本指的是包含有链接关系的文件，并且包含了多媒体对象的文件。</nobr></p>
    </body>
</html>
```

