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

