`HTML` 页面通过基底网址把当前 `HTML` 页面中所有的相对 `URL` 转换成绝对 `URL`。一般情况下，通过基底网址标记 `<base>` 设置 `HTML` 页面的绝对路径，那么在页面中的链接地址只需设置成相对地址即可，当浏览器浏览页面时，会通过 `<base>` 标记将相对地址附在基底网址的后面，从而转化成绝对地址。
例如，在HTML页面的头部定义基底网址如下。

```html
 <base href="http://www.mingribook.com/html">
```

在页面主体中设置的某一个相对地址如下。
```html
<a href="../html/book.html">
```

当使用浏览器浏览时，这个链接地址就变成如下的绝对地址。

```html
http://www.mingribook.com/html/book.html
```

### 1. 语法

```html
<base href="链接地址" target="新窗口的打开方式">
```

链接地址就是要设置的页面的基底地址，而新窗口的打开方式可以设置为不同的效果，其属性值及含义如下表所示：

| 属性值  | 打开方式                                   |
| ------- | ------------------------------------------ |
| _parent | 在上一级窗口打开，一般常用在分帧的框架页中 |
| _blank  | 在新窗口打开                               |
| _self   | 在同一窗口打开，可以省略                   |
| _top    | 在浏览器的整个窗口打开，忽略任何框架       |

### 2. 示例代码

```html
<html>
    <head>
        <base href="http://www.mingribook.com" target="_blank">
        <title>基底网址标记</title>
    </head>
    <body>
    	<a href="../1-2.htm">打开一个相对地址</a>
    </body>
</html>
```

