[toc]

### 1. 节点操作

#### 1.1 查找操作

具体代码如下所示：

```js
var html_node = $("ul li:eq(1)");
alert(html_node.text());
```

#### 1.2 创建节点

函数 `$()` 用于动态创建页面元素，其语法结构如下所示：

```js
$(html)
```

其中参数 html 表示用于动态创建 DOM 元素的 HTML 标记字符串，即如果要在页面中动态创建一个 div 元素，并设置其内容与属性，具体代码如下所示：

```js
var div = "<div class='newclass'>创建的新的 div 块</div>";
$("body").append(div);
```

#### 1.3 插入节点

##### 1.3.1 内部插入节点

<center><b>表 15-10 内部插入节点方法</b></center>

| 方法语法                       | 描述                                           | 参数说明                               |
| ------------------------------ | ---------------------------------------------- | -------------------------------------- |
| append(content)                | 向所选择的元素内部插入内容                     | content：追加到目标中的内容            |
| append(function(index, html))  | 向所选择的元素内部插入 function 函数返回的内容 | 通过函数返回追加到目标的内容           |
| appendTo(content)              | 把所选择的元素追加到另一个指定的元素集合中     | content：被追加的内容                  |
| prepend(content)               | 向每个所选择的元素内部前置内容                 | content：插入目标元素内容前面的内容    |
| prepend(function(index, html)) | 向所选择的元素内部前置 function 函数返回的内容 | 通过函数返回插入目标元素内部前面的内容 |
| prependTo(content)             | 将所选择的元素前置到另一个指定的元素集合中     | content：用于选择元素的 jQuery 表达式  |

prepend(function(index, html)) 的功能是将一个 function 函数作为 append 方法的参数，该函数的功能必须返回一个字符串，作为 append 方法插入的内容，其中 index 参数为对象在这个集合中的索引值，html 参数为该对象原有的 html 值。

```js
$(function() {
    $("div").append(reHtml);
});

function reHtml() {
    var str = "<b>返回字符串</b>";
    return str;
}
```

appendTo(content) 方法用于将一个元素插入另一个指定的元素中，及如果要将 span 标记插入 div 标记中，具体代码如下所示：

```js
$("span").appendTo($("div"));
```

也就是把 appendTo() 方法前半部分的内容插入其后半部分的内容中。

##### 1.3.2 外部插入节点

<center><b>表 15-11 外部插入节点方法</b></center>

| 方法语法              | 描述                                               | 参数说明                           |
| --------------------- | -------------------------------------------------- | ---------------------------------- |
| after(content)        | 向所选择的元素外部后面插入内容                     | 插入目标元素外部后面的内容         |
| after(function)       | 向所选择的元素外部后面插入 function 函数返回的内容 | 通过函数返回插入目标外部后面的内容 |
| before(content)       | 向所选择的元素外部前面插入内容                     | 插入目标元素外部前面的内容         |
| before(function)      | 想所选择的元素外部前面插入 function 函数返回的内容 | 通过函数返回插入目标外部前面的内容 |
| insertAfter(content)  | 将所选择的元素插入到另一个指定的元素外部后面       | 插入目标元素外部后面的内容         |
| insertBefore(content) | 将所选择的元素插入到另一个指定的元素外部前面       | 插入目标元素外部前面的内容         |

#### 1.4 删除节点

jQuery 提供了两种可以删除元素的方法，即 remove() 和 empty()。严格的说，empty() 方法并非真正意义上的删除，使用该方法，仅仅可以清空全部的节点或节点所包含的所有后代元素，并非删除节点与元素。remove() 方法的语法结构如下所示：

```js
remove([expr])
```

其中参数 expr 为可选项，如果接受参数，则该参数为筛选元素的 jQuery 表达式，通过该表达式获取指定的元素进行删除。

Empty() 方法的语法结构如下所示：

```js
empty()
```

其功能为清空所选择的页面元素及其所有后代元素。

**案例：示例 15-16：删除节点**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="删除节点" />
        <title>删除节点</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //单击事件
                $("#btn").click(function () {
                    $("ul li").remove("li[title=1]");
                    $("ul li:eq(2)").remove();
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <ul>
                <li title="1">这是第一条新闻</li>
                <li title="2">这是第二条新闻</li>
                <li title="3">这是第三条新闻</li>
                <li title="4">这是第四条新闻</li>
            </ul>
        </div>
        <input type="button" value="执行删除操作" id="btn" />
    </body>
</html>
```

#### 1.5 复制节点

在 jQuery 中可通过 clone() 方法来实现节点的复制，其语法结构如下所示：

```js
clone()
```

该方法只是复制元素本身，被赋值后的新元素不具有任何元素行为。如果需要在复制时将该元素的全部行为也进行复制，可以使用 clone(true) 来实现。

**案例：示例 15-17：复制节点**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="复制节点" />
        <title>复制节点</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="text/css">
            .divframe {
                width: 100px;
                height: 450px;
                border: 1px solid #999;
                float: left;
                margin-left: 10px;
            }
        </style>
        <script>
            $(function () {
                //单击事件
                $(".divframe").click(function () {
                    $(this).clone(true).appendTo("body");
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            div块
        </div>
    </body>
</html>
```

#### 1.6 替换节点

在 jQuery 中，如果要替换元素中的节点，可以使用 replaceWith() 和 replaceAll() 这两种方法，replaceWith() 方法的语法结构如下所示：

```js
replaceWith(content)
```

replaceAll() 方法的语法结构如下所示：

```js
replaceAll(selector)
```

**案例：示例 15-18：替换节点**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="替换节点" />
        <title>替换节点</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="text/css">
            .divframe {
                width: 100px;
                height: 450px;
                border: 1px solid #999;
                float: left;
                margin-left: 10px;
            }
        </style>
        <script>
            $(function () {
                //单击事件
                $("#btn").click(function () {
                    $("#span1").replaceWith("<span>李四</span>");
                    $("<span>计科2班</span>").replaceAll("#span2");
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <p>姓名：<span id="span1">张三</span></p>
            <p>班级：<span id="span2">计科1班</span></p>
            <input type="button" value="点击替换" id="btn" />
        </div>
    </body>
</html>
```

replaceWith() 与 replaceAll() 方法都可以实现元素节点的替换，二者最大的区别在于替换字符的顺序，前者是用括号中的字符替换所选择的元素，后者是用字符串替换括号中所选择的元素。同时，一旦完成替换，被替换元素中的全部事件都将消失。

#### 1.7 包裹节点

<center><b>表 15-12 包裹节点</b></center>

| 方法语法        | 描述                                                         | 参数说明                                          |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------- |
| wraphtml()      | 把所有选择的元素用其他字符串代码包裹起来                     | html 参数为字符串代码，用于生成元素并包裹所选元素 |
| wrap(elem)      | 把所有选择的元素用其他 DOM 元素包裹起来                      | elem 参数用于包裹所选元素的 DOM 元素              |
| wrap(fn)        | 把所有选择的元素用 function 函数返回的代码包裹起来           | Fn 参数为包裹结构的一个函数                       |
| unwrap()        | 移除所选元素的父元素或包裹标记                               | 无                                                |
| wrapAll(html)   | 把所有选择的元素用单个元素包裹起来                           | html 参数为字符串代码，用于生成元素并包裹所选元素 |
| wrapAll(elem)   | 把所有选择的元素用单个 DOM 元素包裹起来                      | elem 参数用于包裹所选元素的 DOM 元素              |
| wrapInner(html) | 把所有选择的元素的子内容（包括文本节点）用字符串代码包裹起来 | html 参数为字符串代码，用于生成元素并包裹所选元素 |
| wrapInner(elem) | 把所有选择的元素的子内容（包括文本节点）用 DOM 元素包裹起来  | elem 参数用于包裹所选元素的 DOM 元素              |
| wrapInner(fn)   | 把所有选择的元素的子内容（包括文本节点）用函数返回的代码包裹起来 | fn 参数为包裹结构的一个函数                       |

wrap(html) 与 wrapInner(html) 方法较为常用，前者包裹外部元素，后者包裹元素内容的文本字符。

**案例：示例 15-19：包裹节点**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="包裹节点" />
        <title>包裹节点</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="text/css">
            .divframe {
                width: 100px;
                height: 450px;
                border: 1px solid #999;
                float: left;
                margin-left: 10px;
            }
        </style>
        <script>
            $(function () {
                //单击事件
                $("#btn").click(function () {
                    //所有段落标记字体加粗
                    $("p").wrap("<b></b>");
                    //所有段落中的span标记斜体
                    $("span").wrapInner("<i></i>");
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <p>姓名：<span id="span1">张三</span></p>
            <p>班级：<span id="span2">计科1班</span></p>
            <input type="button" value="点击包裹" id="btn" />
        </div>
    </body>
</html>
```

#### 1.8 遍历节点

在 JavaScript 中，需要先获取元素的总长度，然后用 for 语句循环处理。而在 jQuery 中可以直接使用 each() 方法轻松实现元素的遍历，其语法结构如下所示：

```js
each(callback)
```

其中参数 callback 是一个 function 函数，该函数还可以接受一个形参 index，此形参为遍历元素的序列（从 0 开始）。

**案例： 示例 15-20：遍历节点**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="遍历节点" />
        <title>遍历节点</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //单击事件
                $("#btn").click(function () {
                    $("li").each(function (i) {
                        //为新闻添加序号
                        var content = $(this).text();
                        $(this).html(i + 1 + "、" + content);
                    })
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <ul>
                <li>这是第一条新闻</li>
                <li>这是第二条新闻</li>
                <li>这是第三条新闻</li>
                <li>这是第四条新闻</li>
            </ul>
        </div>
        <input type="button" value="为新闻添加序号" id="btn" />
    </body>
</html>
```

### 2. 属性操作

#### 2.1 获取元素属性

可通过 attr() 方法获取元素的属性，其语法结构如下所示：

```js
attr(name)
```

**案例：示例 15-21：获取元素属性**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="获取元素属性" />
        <title>获取元素属性</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //单击事件
                $("#btn").click(function () {
                    var con = $("img");
                    alert("title=" + con.attr("title") + "，src=" + con.attr("src"));
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <img title="这是一张图片" src="images/15-01/img01.jpg" alt="" />
        </div>
        <input type="button" value="获取元素属性" id="btn" />
    </body>
</html>
```

#### 2.2 设置元素的属性

attr() 方法不仅可以用来获取元素的属性值，还可以用来设置元素的属性，其设置元素属性的语法格式如下所示：

```js
attr(key, value)
```

如果要设置多个属性，也可以通过 attr() 方法实现，其语法结构如下所示：

```js
attr({key0:value0, key1:value1})
```

**案例：示例 15-22：设置元素属性**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="设置元素属性" />
        <title>设置元素属性</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //单击事件
                $("#btn").click(function () {
                    var con = $("img");
                    con.attr({ title: "更换后的图片", src: "images/15-01/img02.jpg" });
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <img title="这是一张图片" src="images/15-01/img01.jpg" alt="" />
        </div>
        <input type="button" value="更换元素内容" id="btn" />
    </body>
</html>
```

另外，attr() 方法还可以绑定一个 function() 函数，通过该函数返回的值作为元素的属性值，其语法结构如下所示：

```js
attr(key, function(index))
```

其中，参数 index 为当前元素的索引号，整个函数返回一个字符串作为元素的属性值。

#### 2.3 删除元素属性

使用 removeAttr() 方法可以将元素的属性删除，其语法结构如下所示：

```js
removeAttr(name)
```

可通过如下代码删除元素 `<img>` 中的 src 属性值。

```js
$("img").removeAttr("src");
```

### 4. 样式操作

#### 4.1 直接设置元素样式

在 jQuery 中可以通过 css() 方法直接为某个指定的元素设置样式值，其语法结构如下所示：

```js
css(name, value)
```

例如：

```js
$("p").css("font-weight", "bold");
```

#### 4.2 增加 CSS 类别

通过 addClass() 方法可以增加元素类别的名称，其语法结构如下所示：

```js
addClass(class)
```

也可以增加多个类别的名称，只需要用空格将其隔开即可，其语法结构如下所示：

```js
addClass(class0 class1 ...)
```

例如：

```js
$("p").addClass("fontWeight fontSize");
```

#### 4.3 类别切换

通过 toggleClass() 方法可以切换不同的元素类别，其语法结构如下所示：

```js
toggleClass(class)
```

**案例：示例 15-23：类别切换**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="类别切换" />
        <title>类别切换</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="" text/css>
            .divframe {
        width:100px;
        height:100px;
        border:1px solid #999;
    }
    .divred {
        border:1px solid #f00;
    }
    </style>
        <script>
            $(function () {
                //单击事件
                $(".divframe").click(function () {
                    $(this).toggleClass("divred");
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            点击变换边框颜色
        </div>
    </body>
</html>
```

#### 4.4 删除类别

removeClass() 方法则用于删除类别，其语法结构如下所示：

```js
removeClass([class])
```

其中，参数 class 为类别名称，该名称的可选项，当选择该名称时，则删除名称是 class 的类别，有多个类别时用空格隔开。如果不选择该名称，则删除元素中的所有类别。比如要删除 p 元素标记的 cls 类别，具体代码如下所示：

```js
$("p").removeClass("cls");
```

如果要删除 cls 和 cls1 的类别，具体代码如下所示：

```js
$("p").removeClass("cls cls1");
```

如果要删除 p 元素标记的所有类别，具体代码如下所示：

```js
$("p").removeClass();
```

### 5. 内容操作

在 jQuery 中，操作元素内容的方法包括 html() 和 text()，前者与 JavaScript 中的 innerHTML 属性相似，即获取和设置元素的 HTML 内容；而后者类似于 JavaScript 中的 innerText 属性，即获取或设置元素的文本内容。

<center><b>表 15-13 html() 与 text() 方法的区别</b></center>

| 方法语法    | 描述                     | 参数说明               |
| ----------- | ------------------------ | ---------------------- |
| html()      | 用于获取元素的 HTML 内容 | 无                     |
| html(value) | 用于设置元素的 HTML 内容 | 参数为元素的 HTML 内容 |
| text()      | 用于获取元素的文本内容   | 无                     |
| text(value) | 用于设置元素的文本内容   | 参数为元素的文本内容   |

html() 方法仅支持 XHTML 的文档，不能用于 XML 文档；而 text() 则既支持 HTML 文档，也支持 XML 文档。

在 jQuery 中，如果要获取元素的值，可以通过 val() 方法来实现，其语法结构如下所示：

```js
val(value)
```

如果不带参数 value，则是获取元素的值；反之则是将参数 value 的值赋给元素，该方法常用于表单中获取和设置元素对象的值，另外通过 val() 方法还可以获取 select 元素的多个选项值，其语法结构如下所示：

```js
val().join(",");
```

**案例：示例 15-24：内容操作**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="内容操作" />
        <title>内容操作</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //列表框值发生改变事件
                $("select").change(function () {
                    //获取列表框所选中的全部选项的值
                    var strSelect = $("select").val().join(",");
                    //显示选中的值
                    $("#p1").html(strSelect);
                });
                //文本框值发生改变事件
                $("input").change(function () {
                    //获取文本框的值
                    var strText = $("input").val();
                    //显示选中的值
                    $("#p2").html(strText);
                });
                //文本框focus事件
                $("input").focus(function () {
                    //清空文本框的值
                    $("input").val("");
                });
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <select multiple="multiple">
                <option value="1">Item 1</option>
                <option value="2">Item 2</option>
                <option value="3">Item 3</option>
                <option value="4">Item 4</option>
                <option value="5">Item 5</option>
                <option value="6">Item 6</option>
            </select>
            <p id="p1"></p>
        </div>
        <div>
            <input type="text" />
            <p id="p2"></p>
        </div>
    </body>
</html>
```

在 val(value) 方法中，如果有参数，其参数还可以是数组的形式，即 val(array)，其作用是设置元素被选中。例如 `$(":radio").val(["radio2", "radio3"])。

### 6. 案例：使用 jQuery 实现表格排序**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="使用jQuery实现表格排序" />
        <title>使用jQuery实现表格排序</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="" text/css>
            table, table td, table th {
    border: none;
    vertical-align: top;
    border-collapse: collapse;
    word-break: break-all;
    }
    .MainTable {
    width: 500px;
    line-height: 45px;
    margin: auto;
    text-align: left;
    }
    .MainTable tr {
    border-bottom:1px solid #E1E1E1;
    }
    .MainTable td {
    padding: 0 10px 0 0;
    }
    /*正序排列样式*/
    .sort_asc {
    background:url(images/15-01/sorticon.png) 55px 18px no-repeat;
    cursor:pointer;
    }
    /*倒序排列样式*/
    .sort_desc {
    background:url(images/15-01/sorticon.png) 55px -18px no-repeat;
    cursor:pointer;
    }
    .list_sort {
    width: 60px;
    text-align: center;
    }
    </style>
        <script>
            $(function () {
                $("#sortID").click(function () {
                    var NewContent;
                    //当前排序为正序排列
                    if ($(this).hasClass("sort_asc")) {
                        //重新排列列表内容
                        for (var i = 9; i > -1; i--) {
                            NewContent += "<tr>" + $("#pageContent tr").eq(i).html() + "</tr>";
                        }
                        //替换原有列表内容
                        $("#pageContent").html(NewContent);
                        //使排序状态变为倒序
                        $("#sortID").removeClass("sort_asc");
                        $("#sortID").addClass("sort_desc");
                    } else {
                        //重新排列列表内容
                        for (var i = 9; i > -1; i--) {
                            NewContent += "<tr>" + $("#pageContent tr").eq(i).html() + "</tr>";
                        }
                        //替换原有列表内容
                        $("#pageContent").html(NewContent);
                        //使排序状态变为正序
                        $("#sortID").removeClass("sort_desc");
                        $("#sortID").addClass("sort_asc");
                    }
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <table class="MainTable">
                <thead>
                    <tr>
                        <th class="sort_asc list_sort" id="sortID">序号</th>
                        <th>内容</th>
                    </tr>
                </thead>
                <tbody id="pageContent">
                    <tr>
                        <td class="list_sort">1</td>
                        <td>互联网网站访问量排行第1名：百度</td>
                    </tr>
                    <tr>
                        <td class="list_sort">2</td>
                        <td>互联网网站访问量排行第2名：新浪</td>
                    </tr>
                    <tr>
                        <td class="list_sort">3</td>
                        <td>互联网网站访问量排行第3名：网易</td>
                    </tr>
                    <tr>
                        <td class="list_sort">4</td>
                        <td>互联网网站访问量排行第4名：腾讯</td>
                    </tr>
                    <tr>
                        <td class="list_sort">5</td>
                        <td>互联网网站访问量排行第5名：搜狐</td>
                    </tr>
                    <tr>
                        <td class="list_sort">6</td>
                        <td>互联网网站访问量排行第6名：淘宝</td>
                    </tr>
                    <tr>
                        <td class="list_sort">7</td>
                        <td>互联网网站访问量排行第7名：搜狗</td>
                    </tr>
                    <tr>
                        <td class="list_sort">8</td>
                        <td>互联网网站访问量排行第8名：360安全中心</td>
                    </tr>
                    <tr>
                        <td class="list_sort">9</td>
                        <td>互联网网站访问量排行第9名：京东商城</td>
                    </tr>
                    <tr>
                        <td class="list_sort">10</td>
                        <td>互联网网站访问量排行第10名：优酷网</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>
</html>
```

