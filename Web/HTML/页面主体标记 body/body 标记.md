[toc]

网页的主体部分以 `<body>` 标记标志它的开始，以 `</body>` 标志它的结束。在网页的主体标记中有很多的属性设置，如下表所示：

| 属性         | 描述                                           |
| ------------ | ---------------------------------------------- |
| text         | 设定页面文字的颜色                             |
| bgcolor      | 设定页面背景的颜色                             |
| background   | 设定页面的背景图像                             |
| bgproperties | 设定页面的背景图像为固定，不随页面的滚动而滚动 |
| link         | 设定页面默认的链接颜色                         |
| alink        | 设定鼠标正在单击时的链接颜色                   |
| vlink        | 设定访问过后的链接颜色                         |
| topmargin    | 设定页面的上边距                               |
| leftmargin   | 设定页面的左边距                               |

### 1. 设置文字颜色 —— text

`<body>` 元素的 `text` 属性可以改变整个页面默认文字的颜色。在没有对文字进行单独定义颜色的时候，这个属性将对页面中所有的文字产生作用。

#### 1.1 语法

```html
<body text="颜色代码">
```

#### 1.1 示例代码

```html
<html>
    <head>
    	<title>设置页面文字颜色</title>
    </head>
    <body text="#0000FF">
    	设定页面的文字颜色为蓝色
    </body>
</html>
```

### 2. 背景颜色属性 —— bgcolor

`<body>` 元素的 `bgcolor` 属性用来设定整个页面的背景颜色。

#### 2.1 语法

```html
<body bgcolor="颜色代码">
```

#### 2.2 示例代码

```html
<html>
    <head>
        <title>设置页面文字颜色</title>
    </head>
    <body bgcolor="#0000FF" text="#FFFFFF">
    	设定页面的背景为蓝色，文字的颜色为白色
    </body>
</html>
```

### 3. 背景图像属性 —— background

页面中可以使用 `jpg` 或 `gif` 图片来表现。这些图片可以作为页面的背景图，通过 `<body>` 语句中的 `background` 属性来实现。它与向网页中插入图片不同，它放在网页的最底层，文字和图片等都位于它的上面。文字、插入的图片等会覆盖背景图片。在默认的情况下，背景图片在水平方向和垂直方向上会不断重复出现，直到铺满整个网页。

#### 3.1 语法

```html
<body background="文件链接地址" bgproperties="背景图片固定属性">
```

#### 3.2 示例代码

```html
<html>
    <head>
    	<title>背景图片</title>
    </head>
    <body background="images/1.jpg">
    </body>
</html>
```

### 4. 设置链接文字属性 —— link

#### 4.1 语法

```html
<body link="颜色代码">
```

#### 4.4 示例代码

```html
<html>
    <head>
    <title>页面的链接文字</title>
    </head>
    <body text="#6699FF" link="#FF0000">
        <center>
            设置文字的链接效果
            <br /><br />
            <a href="http://www.mingribook.com">链接文字</a>
            <br /><br />
        </center>
    </body>
</html> 
```

### 5. 设置边距 —— margin

在网页的制作过程中，还可以定义页面的空白，也就是网页内容与浏览器边框之间的距离。其中包括上边框和左边框，设定合适的边距可以防止网页外观过于拥挤。

#### 5.1 语法

```html
<body topmargin=上边距的值leftmargin=左边距的值>
```

在默认情况下，边距的值是以像素为单位的。

#### 5.2 示例代码

```html
<html>
    <head>
    	<title>设置边距</title>
    </head>
    <body topmargin="60" leftmargin="50">
    	设置页面的上边距为60像素
    	<br/>
    	设置页面的左边距为50像素
    </body>
</html>
```

