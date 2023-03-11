[toc]

### 1. 文字标签 font

设置不同的文字效果的属性位于文字格式标记 `<font>` 中。

#### 1.1 语法

```html
<font>文字内容</font>
```

### 2. 设置文字字体 —— face

#### 2.1 语法

```html
<font face="字体1,字体2, ... ">应用了该字体的文字</font>
```

在该语法中，`face` 属性的值可以是 1 个或者多个。默认情况下，使用第1种字体进行显示；如果第 1 种字体不存在，则使用第2种字体进行代替，以此类推。如果设置的几种字体在浏览器中都不存在，则会以默认字体显示。

#### 2.2 示例代码

```html
<html>
    <head>
    	<title>不同字体的显示效果</title>
    </head>
    <body>
        <font face="华文彩云">登山则情满于山</font><br /><br />
        <font face="隶书">观海则意溢于海</font>
    </body>
</html>
```

### 3. 设置字号 —— size

`HTML` 语言提供了 `<font>` 标记 `size`属性来设置普通文字的字号。

#### 3.1 语法

```html
<font size="文字字号"></font>
```

文字的字号可以设置 1 ~ 7，也可以是 +1 ~ +7 或者是 -1 ~ -7。这些字号并没有一个固定的大小值，而是相对于默认文字大小来设定的，默认文字的大小与 3 号字相同，而数值越大，文字也越大。

#### 3.2 示例代码

```html
<html>
    <head>
    	<title>设置不同的文字大小</title>
    </head>
    <body>
        <font size="1">1 号字体的效果</font><br/>
        <font size="2">2 号字体的效果</font><br/>
        <font size="3">3 号字体的效果</font><br/>
        <font size="4">4 号字体的效果</font><br/>
        <font size="5">5 号字体的效果</font><br/>
        <font size="6">6 号字体的效果</font><br/>
        <font size="7">7 号字体的效果</font><br/>
        <font size="+2">默认字号+2，也就是5 号字体的效果</font><br/>
        <font size="-1">默认字号-1，即2 号字体的效果</font><br/>
    </body>
</html>
```

### 4. 设置文字颜色 —— color

#### 4.1 语法

```html
<font color="颜色代码"></font>
```

#### 4.2 示例代码

```html
<html>
    <head>
    	<title>设置不同的文字颜色</title>
    </head>
    <body>
        <font face="隶书" size="+4" color="#0066FF">明日科技</font><br/>
        <font face="宋体"size="+5" color="#FFCC66">编程词典</font><br/>
        <font face="华文楷体"size="+3" color="#99FF00">数字化出版的领导者</font><br/>
    </body>
</html>
```

