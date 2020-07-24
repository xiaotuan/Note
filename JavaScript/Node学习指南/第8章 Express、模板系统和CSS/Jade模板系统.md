> 提示：Jade 官网：<http://jade-lang.com/>

在 `Jade` 模板系统中，`HTML` 元素用不带尖括号的名字表示，嵌套关系用缩进代表。所以对于一些代码：

```html
<html>
    <head>
        <title>This is the title</title>
    </head>
    <body>
        <p>Say hi World</p>
    </body>
</html>
```

在 `Jade` 中等价为以下写法：

```jade
html
  head
    title This is it
  body
    p Say Hi to the world
```

title 和 p 标签的内容都跟在标签名之后。没有结束标签符号，也是由缩进表示。以下例子使用了 class 和 id 属性以及多层嵌套：

```jade
html
  head
    title This is it
  body
    div.content
      div#title
        p nested data
```

该模板生成的 `HTML` 代码为：

```html
<html>
  <head>
    <title>This is it</title>
  </head>
  <body>
    <div class="content">
      <div id="title">
        <p>nested data</p>
      </div>
    </div>
  </body>
</html>
```

如果某个标签的内容过长，比如一个段落，可以使用竖线（|）来拼接内容：

```jade
p
  | some text
  | more text
  | and even more
```

对应的 `HTML` 为：

```html
<p>some text more text and even more</p>
```

另一种做法是使用句号（.），代表该标签区域内只包含文字，可以省略竖线：

```jade
p.
  some text
  more text
  and even more
```

还可以引用 `HTML` 代码作为内容，在生成的代码中也会被当做 `HTML` 代码处理：

```jade
body.
  <h1>A header</h1>
  <p>A paragraph</p>
```

form 元素通常有很多属性，在 `Jade` 中用括号表示，并可以设置属性的值（如果有）。属性和属性之间只需要空格分离，不过我每行只列出一个属性以增加可读性：

```jade
html
  head
    title This is it
  body
    form(method="POST"
         action="/widgets"
         enctype="application/x-www-form-urlencoded")
      input(type="text"
            name="widgetname"
            id="widgetname"
            size="25")
      input(type="text"
            name="widgetprice"
            id="widgetprice"
            size="25")
      input(type="submit"
            name="submit"
            id="submit"
            value="Submit")
```

生成 `HTML` 代码：

```html
<html>
  <head>
    <title>This is it</title>
  </head>
  <body>
    <form method="POST" action="/widgets" enctype="application/x-www-form-urlencoded">
      <input type="text" name="widgetname" id="widgetname" size="25" />
      <input type="text" name="widgetprice" id="widgetprice" size="25" />
      <input type="submit" name="submit" id="submit" value="Submit" />
    </form>
  </body>
</html>
```

**Jade 中简单的布局模板**

```jade
doctype html
html(lang="en")
  head
    title #{title}
    meta(charset="utf-8")
  body
    block content
```

在 `Jade` 中，使用 `#{}`) 将数据传递给模板。

在每个 content 模板的开始加入以下代码来使用新的布局模板：

```jade
extends layout
```

你不必使用 content 作为 block 的名字，还可以使用多个 block，并且如果你想进一步分解布局，还可以引用其他模板文件。我修改了 `layout.jade` 文件，包含一个 headerd，而不是直接在 layout 文件中使用 head：

```jade
doctype html
html(lang="en")
  include header
  body
    block content
```

`header.jade` 文件内容如下：

```jade
head
  title #{title}
  meta(charset="utf-8")
```

在 `layout.jade` 和 `header.jade` 文件中有两件事情需要注意下。

第一， include 相对路径。如果把 views 分解为以下目录结构：

```
/views
   |_/widgets
        |_layout.jade
        |_/standard
             |_header.jade
```

在 layout 文件中引用 header 模板时使用：

```
include standard/header
```

文件类型并不一定要是 `Jade`，也可以是 `HTML`。当引用的文件不为 `Jade` 文件类型时，需要加上文件扩展名：

```
include standard/header.html
```

第二，在 `header.jade` 文件中不要使用缩进。父文件中已经带有缩进了，引用的模板文件中不需要重复缩进。事实上，如果引用文件中带有缩进，生成代码时会报错。