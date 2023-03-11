[toc]

`meta` 元素提供的信息是用户不可见的，它不显示在页面中，一般用来定义页面信息的名称、关键字、作者等。在 `HTML` 中，`meta` 标记不需要设置结束标记，在一个尖括号内就是一个 `meta` 内容，而在一个`HTML` 头页面中可以有多个 `meta` 元素。`meta` 元素的属性有两种：`name` 和 `http-equiv`，其中`name` 属性主要用于描述网页，以便于搜索引擎机器人查找和分类。

### 1. 设置页面关键字

设置页面关键字是为了向搜索引擎说明这一网页的关键字，从而帮助搜索引擎对该网页进行查找和分类，它可以提高被搜索到的几率，一般可设置多个关键字，之间用逗号隔开。但是由于很多搜索引擎在检索时会限制关键字的数量，因此在设置关键字时不要过多，应“一击即中”。

#### 1.1 语法

```html
<meta name="keyname" content="具体的关键字">
```

#### 1.2 示例代码

```html
<html>
    <head>
        <title>设置页面关键字</title>
        <meta name="keyword" content="html,元信息,关键字">
    </head>
    <body>
    </body>
</html>
```

### 2. 设置页面描述

设置页面描述也是为了便于搜索引擎的查找，它用来描述网页的主题等，与关键字一样，设置的页面描述也不会在网页中显示出来。

#### 2.1 语法

```html
<meta name="description" content="对页面的描述语言">
```

#### 2.2 示例代码

```html
<html>
    <head>
        <title>设置页面描述</title>
        <meta name="keyword" content="html,元信息,关键字">
        <meta name="description" content="关于HTML 使用的网站">
    </head>
    <body>
    </body>
</html>
```

### 3. 设置编辑工具

现在有很多编辑软件都可以制作网页，在源代码的头页面中可以设置网页编辑工具的名称。

#### 3.1 语法

```html
<meta name="generator" content="编辑软件的名称">
```

#### 3.2 示例代码

```html
<html>
    <head>
        <title>设置编辑工具</title>
        <meta name="keyword" content="html,元信息,关键字">
        <meta name="description" content="关于HTML 使用的网站">
        <meta name="generator" content="Adobe Dreamweaver CC">
    </head>
    <body>
    </body>
</html>
```

### 4. 设定作者信息

在页面的源代码中，可以显示页面制作者的姓名及个人信息。这可以在源代码中保留作者希望保留的信息。

#### 4.1 语法

```html
<meta name="author" content="作者的姓名">
```

#### 4.2 示例代码

```html
<html>
    <head>
        <title>设定作者信息</title>
        <meta name="keyword" content="html,元信息,关键字">
        <meta name="description" content="关于HTML 使用的网站">
        <meta name="generator" content=" Adobe Dreamweaver CS5.5">
        <meta name="author" content="李小米">
    </head>
    <body>
    </body>
</html>
```

### 5. 限制搜索方式

网页可以通过在 `<meta>` 标记中的设置来限制搜索引擎对页面的搜索方式。

#### 5.1 语法

```html
<meta name="robots" content="搜索方式">
```

<center><b>content 值与其对应的含义</b></center>

| Content 的值 | 描述                             | Content 的值 | 描述                                 |
| ------------ | -------------------------------- | ------------ | ------------------------------------ |
| All          | 表示能搜索当前网页及其链接的网页 | Noindex      | 表示不能搜索当前网页                 |
| Index        | 表示能搜索当前网页               | None         | 表示不能搜索当前网页及与其链接的网页 |
| Nofollow     | 表示不能搜索与当前网页链接的网页 |              |                                      |

#### 5.2 示例代码

```html
<html>
    <head>
        <title>限制搜索方式</title>
        <meta name="robots" content="index">
    </head>
    <body>
    </body>
</html>
```

### 6. 设置网页文字及语言

#### 6.1 语法

第一种方法：

```html
<meta http-equiv="Content-Type" content="text/html; charset=字符集类型">
```

第二种方法：

```html
<meta http-equiv="Content-Language" content="语言">
```

其中 `charset` 设置了网页的内码语系，也就是字符集的类型，`charset` 往往设置为 `gb2312`，即简体中文。英文是 `ISO-8859-1` 字符集，此外还有 `BIG5`、`utf-8`、`shift-Jis`、`Euc`、`Koi8` 等字符集。如果采用第二种方法，则简体中文的设置为：

```html
<meta http-equiv="Content-Language" content="zh_CN">
```

### 7. 设置网页的定时跳转

#### 7.1 语法

```html
<meta http-equiv="refresh" content="跳转时间;url=链接地址">
```

在该语法中，`refresh` 表示网页的刷新，而在 `content` 中设定刷新的时间和刷新后的地址，时间和链接地址之间用分号相隔。默认情况下，跳转时间是以秒为单位的。

#### 7.2 示例代码

```html
<html>
    <head>
        <title>设置网页的定时跳转</title>
        <meta http-equiv="refresh" content="3;url=http://www.mingribook.com">
    </head>
    <body>
    	您好，本页在3 秒之后将自动跳转到明日图书网
    </body>
</html>
```

### 8. 设定有效期限

在某些网站上会设置网页的到期时间，一旦过期则必须到服务器上重新调用。

#### 8.1 语法

```html
<meta http-equiv="expires" content="到期的时间">
```

到期的时间必须是 GMT 时间格式，即星期，日月年时分秒，这些时间都使用英文和数字进行设定。

#### 8.2 示例代码

```html
<html>
    <head>
        <title>设置有效期限</title>
        <meta http-equiv="expires" content="Web, 14 september 2011 16:20:00 GMT ">
    </head>
    <body>
    </body>
</html>
```

### 9. 禁止从缓存中调用

#### 9.1 语法

```html
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="pragma" content=" no-cache ">
```

`cache-control` 和 `pragma` 都可以用来设定缓存的属性，而在 `content` 中则是真正禁止调用缓存的语句。

#### 9.2 示例代码

```html
<html>
    <head>
        <title>禁止从缓存中调用</title>
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="pragma" content=" no-cache ">
    </head>
    <body>
    </body>
</html>
```

### 10. 删除过期的 cookie

#### 10.1 语法

```html
<meta http-equiv="set-cookie" content="到期的时间">
```

到期的时间同样是 GMT 时间格式。

#### 10.2 示例代码

```html
<html>
    <head>
        <title>删除过期的cookie</title>
        <meta http-equiv="set-cookie" content=" Web, 14 september 2011 16:20:00 GMT">
    </head>
    <body>
    </body>
</html>
```

### 11. 强制打开新窗口

强制网页在当前窗口中以独立的页面显示，可以防止自己的网页被别人当作一个 frame 页调用。

#### 11.1 语法

```html
<meta http-equiv="windows-target" content="_top">
```

`windows-target` 表示新网页的打开方式，而 `content` 中设置 `_top` 则代表打开的是一个独立页面。

#### 11.2 示例代码

```html
<html>
    <head>
        <title>强制打开新窗口</title>
        <meta http-equiv="windows-target" content="_top">
    </head>
    <body>
    </body>
</html>
```

### 12. 设置网页的过渡效果

#### 12.1 语法

```html
<meta http-equiv="过渡事件" content="revealtrans(duration=过渡效果持续时间,transition=过渡方式)">
```

进入页面的 `http-equiv` 值为 `page-enter` ，离开页面的 `http-equiv` 值为 `page-exist`。过渡效果的持续时间默认情况下以秒为单位，过渡方式的编号及含义如下表所示。

| 编号 | 含义           | 编号 | 含义                 |
| ---- | -------------- | ---- | -------------------- |
| 0    | 盒状收缩       | 12   | 随意溶解             |
| 1    | 盒状放射       | 13   | 从左右两端向中间展开 |
| 2    | 圆形收缩       | 14   | 从中间向左右两端展开 |
| 3    | 圆形反射       | 15   | 从上下两端向中间展开 |
| 4    | 由下往上       | 16   | 从中间向上下两端展开 |
| 5    | 由上往下       | 17   | 从右上角向左下角展开 |
| 6    | 从左至右       | 18   | 从右下角向左上角展开 |
| 7    | 从右至左       | 19   | 从左上角向右下角展开 |
| 8    | 垂直百叶窗     | 20   | 从左下角向右上角展开 |
| 9    | 水平百叶窗     | 21   | 水平线状展开         |
| 10   | 水平格状百叶窗 | 22   | 垂直线状展开         |
| 11   | 垂直格状百叶窗 | 23   | 随机产生一种过渡方式 |

#### 12.2 示例代码

```html
<html>
    <head>
    	<title>页面的过渡效果</title>
    </head>
    <body bgcolor="#FFCC00">
        <center><h2>页面的过渡效果</h2>
            <img src="images/1.jpg" width="498" height="349" /><br/><br/><br/>
            <a href="2-enter.html">进入网页</a><br/><br/><br/>
            <a href="2-exit.html">离开网页</a>
    	</center>
    </body>
</html>
```

```html
<html>
    <head>
        <title>页面的进入效果</title>
        <meta http-equiv="page-enter" content="revealtrans(duration=3,transition=21)"/>
    </head>
    <body bgcolor="#FFCC99">
        <center><h2>显示页面的进入效果</h2>
            <img src="images/2.jpg" width="498" height="462" /><br /><br />
            <a href="2-gd.html">返回</a>
        </center>
    </body>
</html>
```

### 13. 设定建立网站的日期

#### 13.1 语法

```html
<meta name="build" content="网站建立的日期">
```

#### 13.2 示例代码

```html
<html>
    <head>
        <title>设定网站建立日期</title>
        <meta name="build" content="2008.08.08">
    </head>
    <body>
    </body>
</html>
```

### 14. 设定网页版权信息

#### 14.1 语法

```html
<meta name="copyright" content="网页版权信息">
```

#### 14.2 示例代码

```html
<html>
    <head>
        <title>设定网页版权</title>
        <meta name="copyright" content="明日科技">
    </head>
    <body>
    </body>
</html>
```

### 15. 设定联系人的邮箱

#### 15.1 语法

```html
<meta name="reply-to" content="邮箱地址">
```

#### 15.2 示例代码

```html
<html>
    <head>
        <title>设定网站联系人邮箱</title>
        <meta name="reply-to" content="mingrisoft@mingrisoft.com">
    </head>
    <body>
    </body>
</html>
```

