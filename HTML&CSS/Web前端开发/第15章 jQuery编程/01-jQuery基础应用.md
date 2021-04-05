[toc]

### 1. 调用方法

**案例：示例 15-01：引入 jQuery 库**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="引用jQuery库" />
        <title>引用jQuery库</title>
        <link rel="stylesheet" href="style.css" />
        <script src="jquery/jquery.js"></script>
    </head>

    <body>
        <div id="bodyContent" class="body-content">
        </div>
    </body>
</html>
```

jQuery 官方网站（<http://jquery.com>）始终都包含该库最新的稳定版本，通过官网即可下载。

### 2. 基本语法

在 jQuery 程序中，使用最多的莫过于 "$" 美元符号。 \$ 就是 jQuery 的一个简写格式，无论是页面元素的选择，还是功能函数的前缀都必须使用该符号，以下为一个简单的 jQuery 函数示例：

```html
<script>
    $(document).ready(function() {
        alert("欢迎使用 jQuery");
    });
</script>
```

`$(document).ready(function(){})` 可以简写成 `$(function(){})`，为了增加代码可读性以及良好的编码习惯，在 jQuery 程序中依然建议采用统一书写格式。

在编写某个元素事件时，jQuery 程序可以使用链接式的方式编写元素的所有事件，通过下面的例子可以了解这一特点：

```html
<script>
    $(function() {
        $(".divtitle").click(function() {
            $(this).addClass("divColor");
        });
    });
</script>
```

### 3. 选择器

#### 3.1 基本选择器

基本选择器由元素 id、class、元素名、多个选择符组成。

<center><b>表 15-1 基本选择器语法</b></center>

| 选择器               | 描述                                   | 返回值   |
| -------------------- | -------------------------------------- | -------- |
| \#id                 | 根据提供的 id 属性值匹配一个元素       | 单个元素 |
| Element              | 根据提供的元素名匹配所有的元素         | 元素集合 |
| .class               | 根据提供的类名称匹配所有的元素         | 元素集合 |
| *                    | 匹配所有元素                           | 元素集合 |
| selector1, selectorN | 将每个选择器匹配到的元素合并后一起返回 | 元素集合 |

**案例：示例 15-02：基本选择器**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="基本选择器" />
        <title>基本选择器</title>
        <link rel="stylesheet" href="style.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //使用id匹配元素
                //显示id属性值为div的页面元素
                $("#div").css("display", "block");
                //使用元素名匹配元素
                //显示div元素下元素名为span的页面元素
                $("div span").css("display", "block");
                //使用类名匹配元素
                //显示类名为classdiv的页面元素
                $(".classdiv .one").css("display", "block");
                //匹配所有元素
                //显示页面中的所有元素
                $("*").css("display", " block");
                //合并匹配元素
                //显示id属性值为div和元素名为span的页面元素
                $("#div,span").css("display", " block");
            })
        </script>
    </head>

    <body>
        <div class="classdiv">
            <div id="div">id属性值</div>
            <div class="one">one类名</div>
            <span>span</span>
        </div>
    </body>
</html>
```

#### 3.2 层次选择器

层次选择器通过 DOM 元素间的层次关系获取元素，其主要的层次关系包含后代、父子、相邻、兄弟关系，通过其中某类关系可方便快捷第定位元素。

需要注意的是 ancestor descendant 与 parent>child 选择的元素集合是不同的，前者的层次关系时祖先与后代，而后者是父子关系；另外 prev+next 可以使用 .next() 函数代替，prev~siblings 可以使用 nextAll() 函数代替。

<center><b>表 15-2 层次选择器语法</b></center>

| 选择器              | 描述                                 | 返回值   |
| ------------------- | ------------------------------------ | -------- |
| ancestor descendant | 根据祖先元素匹配所有的后代元素       | 元素集合 |
| parent>child        | 根据父元素匹配所有的子元素           | 元素集合 |
| prev+next           | 匹配所有紧接在 prev 元素后的相邻元素 | 元素集合 |
| prev~siblings       | 匹配 prev 元素之后的所有兄弟元素     | 元素集合 |

**案例：示例 15-02：基本选择器**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="层次选择器" />
        <title>层次选择器</title>
        <link rel="stylesheet" href="style.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            //匹配后代元素
            $(function () {
                //显示div元素中所有的span元素
                $("div span").css("display", "block");
                $("#divMid").css("display", "block");
            })
            //匹配子元素
            $(function () {
                //显示div元素下的子span元素
                $("div>span").css("display", "block");
                $("#divMid").css("display", "block");
            })
            //匹配后面元素
            $(function () {
                //显示id属性值为divMid元素后的下一个div元素
                $("#divMid").next().css("display", "block");
                $("#divMid + div").css("display", "block");
            })
            //匹配所有后面元素
            $(function () {
                //显示id属性值为divMid元素后的所有div元素
                $("#divMid ~ div").css("display", "block");
                $("#divMid").nextAll().css("display", "block");
            })
            //匹配所有相邻元素
            $(function () {
                //显示id属性值为divMid的元素的所有相邻div元素
                $("#divMid").siblings("div").css("display", "block");
            })
        </script>
    </head>

    <body>
        <div class="classA">left</div>
        <div class="classA" id="divMid">
            <span class="classP" id="span1">
                <span class="classC" id="span2"></span>
            </span>
        </div>
        <div class="classA">right_1</div>
        <div class="classA">right_2</div>
    </body>
</html>
```

#### 3.3 过滤选择器

##### 3.3.1 简单过滤选择器

过滤选择器根据某类过滤规则进行元素的匹配，书写时都以冒号（:）开头，而简单过滤器便是过滤器当中使用最为广泛的一种。

<center><b>表 15-3 简单过滤选择器语法</b></center>

| 选择器            | 描述                                          | 返回值   |
| ----------------- | --------------------------------------------- | -------- |
| first() 或 :first | 获取第一个元素                                | 单个元素 |
| last() 或 :last   | 获取最后一个元素                              | 单个元素 |
| :not(selector)    | 获取除给定选择器外的所有元素                  | 元素集合 |
| :even             | 获取所有索引值为偶数的元素，索引号从 0 开始   | 元素集合 |
| :odd              | 获取所有索引值为奇数的元素，索引号从 0 开始   | 元素集合 |
| :eq(index)        | 获取指定索引值的元素，索引号从 0 开始         | 元素集合 |
| :gt(index)        | 获取所有大于给定索引值的元素，索引号从 0 开始 | 元素集合 |
| :lt(index)        | 获取所有小于给定索引值的元素，索引号从 0 开始 | 元素集合 |
| :header           | 获取所有标题类型的元素，如 h1、h2......       | 元素集合 |
| :animated         | 获取正在执行动画效果的元素                    | 元素集合 |

**案例：示例 15-04：简单过滤选择器**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="简单过滤选择器" />
        <title>简单过滤选择器</title>
        <link rel="stylesheet" href="style.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            //增加第一个元素的类别
            $(function () {
                $("#li:first").addClass("GetFocus");
            })
            //增加最后一个元素的类别
            $(function () {
                $("#li:last").addClass("GetFocus");
            })
            //增加去除所有与给定选择器匹配的元素类别
            $(function () {
                $("#li:not(.NotClass)").addClass("GetFocus");
            })
            //增加所有索引值为偶数的元素类别
            $(function () {
                $("#li:even").addClass("GetFocus");
            })
            //增加所有索引值为奇数的元素类别
            $(function () {
                $("#li:odd").addClass("GetFocus");
            })
            //增加一个给定索引值的元素类别
            $(function () {
                $("#li:eq(1)").addClass("GetFocus");
            })
            //增加所有大于给定索引值的元素类别
            $(function () {
                $("#li:get(1)").addClass("GetFocus");
            })
            //增加所有小于给定索引值的元素类别
            $(function () {
                $("#li:lt(4)").addClass("GetFocus");
            })
            //增加标题类元素类别
            $(function () {
                $("div h1").css("width", "240");
                $(":header").addClass("GetFocus");
            })
            //增加动画效果元素类别
            $(function () {
                animateIt();
                $("#spnMove:animated").addClass("GetFocus");
            })
            //动画效果
            function animateIt() {
                $("#spnMove").slideToggle("slow", animateIt);
            }
        </script>
    </head>

    <body>
        <div>
            <h1>基本过滤选择器</h1>
            <ul>
                <li class="DefClass"></li>
                <li class="DefClass"></li>
                <li class="NotClass"></li>
                <li class="DefClass"></li>
            </ul>
            <span id="spnMove">Span Move</span>
        </div>
    </body>
</html>
```

##### 3.3.2 内容过滤选择器

内容过滤选择器根据元素中的文字内容或所包含的子元素特征获取元素，其文字内容可以模糊匹配或绝对匹配进行元素定位。

<center><b>表 15-4 内容过滤选择语法</b></center>

| 选择器          | 描述                                 | 返回值   |
| --------------- | ------------------------------------ | -------- |
| :contains(text) | 获取包含给定文本的元素               | 元素集合 |
| :empty          | 获取所有不包含子元素或者文本的空元素 | 元素集合 |
| :has(selector)  | 获取含有选择器所匹配的元素           | 元素集合 |
| :parent         | 获取含有子元素或者文本的元素         | 元素集合 |

在 `:contains(text)` 内容过滤选择器中，如果是查找字母，要注意区分其大小写。

##### 3.3.3 可见性过滤选择器

可见性过滤选择器根据元素是否可见的特征获取元素。

<center><b>表 15-5 可见性过渡选择器语法</b></center>

| 选择器   | 描述                                           | 返回值   |
| -------- | ---------------------------------------------- | -------- |
| :hidden  | 获取所有不可见元素，或者 type 为 hidden 的元素 | 元素集合 |
| :visible | 获取所有的可见元素                             | 元素集合 |

`:hidden` 选择器所选择的不仅包括样式为 `display:none` 的所有元素，而且还包括属性 type 值为 hidden 和样式为 visibility:hidden 的所有元素。

##### 3.3.4 属性过虑选择器

属性过滤选择器根据元素的某个属性获取元素，如 id 属性值或匹配属性值的内容，并用中括号包裹。

<center><b>表 15-6 属性过滤选择器语法</b></center>

| 选择器                                 | 描述                                 | 返回值   |
| -------------------------------------- | ------------------------------------ | -------- |
| [attribute]                            | 获取包含给定属性的元素               | 元素集合 |
| [attribute=value]                      | 获取给定的属性等于某个特定值的元素   | 元素集合 |
| [attribute!=value]                     | 获取给定的属性不等于某个特定值的元素 | 元素集合 |
| [attribute^=value]                     | 获取给定的属性是以某些值开始的元素   | 元素集合 |
| [attribute$=value]                     | 获取给定的属性是以某些值结尾的元素   | 元素集合 |
| [attribute*=value]                     | 获取给定的属性包含某些值的元素       | 元素集合 |
| \[selector\]\[selector2\]\[selectorN\] | 获取满足多个条件的复合属性的元素     | 元素集合 |

**案例：示例 15-05：属性过滤选择器**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="引用jQuery库" />
        <title>属性过滤选择器</title>
        <link rel="stylesheet" href="style.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            //显示所有含有id属性值的元素
            $(function () {
                $("div[id]").show(3000);
            })
            //显示所有属性title值为“A”的元素
            $(function () {
                $("div[title='A']").show(3000);
            })
            //显示所有属性title的值不是“A”的元素
            $(function () {
                $("div[title!='A']").show(3000);
            })
            //显示所有属性title的值以“A”开始的元素
            $(function () {
                $("div[title^='A']").show(3000);
            })
            //显示所有属性title的值以“C”结束的元素
            $(function () {
                $("div[title$='C']").show(3000);
            })
            //显示所有属性title的值中含有“B”的元素
            $(function () {
                $("div[title*='B']").show(3000);
            })
            //显示所有属性title的值中含有“B”且属性id的值为“divAB”的元素
            $(function () {
                $("div[id='divAB'][title*='B']").show(3000);
            })
        </script>
    </head>

    <body>
        <div id="divID">ID</div>
        <div title="A">title A</div>
        <div id="divAB" title="AB">M</div>
        <div title="ABC"></div>
    </body>
</html>
```

##### 3.3.5 子元素过滤选择器

在页面开发过程中，常常遇到突出指定某行的需求。为了实现这样的需求，jQuery 中可通过子元素过滤选择器十分轻松地获取所有父元素中的某个元素。

<center><b>表 15-7 子元素过滤选择器语法</b></center>

| 选择器                           | 描述                                          | 返回值   |
| -------------------------------- | --------------------------------------------- | -------- |
| :nth-child(eq\|even\|odd\|index) | 获取每个父元素下的特定位置元素，索引从 1 开始 | 元素集合 |
| :first-child                     | 获取每个父元素下的第一个子元素                | 元素集合 |
| :last-child                      | 获取每个父元素下的最后一个子元素              | 元素集合 |
| :only-child                      | 获取每个父元素下的仅有一个子元素              | 元素集合 |

##### 3.3.6 表单对象属性过滤选择器

表单对象属性过滤选择器通过表单中的某个对象属性特征获取该元素。

<center><b>表 15-8 表单对象属性过滤选择器语法</b></center>

| 选择器    | 描述                             | 返回值   |
| --------- | -------------------------------- | -------- |
| :enabled  | 获取表单中所有属性为可用的元素   | 元素集合 |
| :disabled | 获取表单中所有属性为不可用的元素 | 元素集合 |
| :checked  | 获取表单中所有被选中的元素       | 元素集合 |
| :selected | 获取表单中所有被选中项的元素     | 元素集合 |

**案例：示例 15-06：表单对象属性过滤选择器**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="表单对象属性过滤选择器" />
        <title>表单对象属性过滤选择器</title>
        <link rel="stylesheet" href="style.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            //增加表单中所有属性为可用的元素类别
            $(function () {
                $("#div").show(3000);
                $("#form1 input:enabled").addClass("GetFocus");
            })
            //增加表单中所有属性为不可用的元素类别
            $(function () {
                $("#div").show(3000);
                $("#form1 input:disabled").addClass("GetFocus");
            })
            //增加表单中所有被选中的元素类别
            $(function () {
                $("#divB").show(3000);
                $("#form1 input:checked").addClass("GetFocus");
            })
            //显示表单中所有被选中option的元素内容
            $(function () {
                $("#divC").show(3000);
                $("#span2").html("被选项是：" + $("select option:selected").text());
            })
        </script>
    </head>

    <body>
        <form id="form1">
            <div id="div">
                <input type="text" value="可用文本框" class="clsIpt" />
                <input type="text" disabled="disabled" value="不可用文本框" class="clsIpt" />
            </div>
            <div id="divB">
                <input type="checkbox" value="1" checked="checked" />选中
                <input type="checkbox" value="0" class="clsIpt" />未选中
            </div>
            <div id="divC">
                <select multiple="multiple">
                    <option value="0">Item 0</option>
                    <option value="1" selected="selected">Item 1</option>
                    <option value="2">Item 2</option>
                    <option value="3" selected="selected">Item 3</option>
                </select>
                <span id="span2"></span>
            </div>
        </form>
    </body>
</html>
```

#### 3.4 表单选择器

<center><b>表 15-9 表单选择器语法</b></center>

| 选择器    | 描述                             | 返回值   |
| --------- | -------------------------------- | -------- |
| :input    | 获取所有 input、textarea、select | 元素集合 |
| :text     | 获取所有单行文本框               | 元素集合 |
| :password | 获取所有密码框                   | 元素集合 |
| :radio    | 获取所有单选按钮                 | 元素集合 |
| :checkbox | 获取所有复选框                   | 元素集合 |
| :submit   | 获取所有提交按钮                 | 元素集合 |
| :image    | 获取所有图像域                   | 元素集合 |
| :reset    | 获取所有重置按钮                 | 元素集合 |
| :button   | 获取所有按钮                     | 元素集合 |
| :file     | 获取所有文件域                   | 元素集合 |

**案例： 示例 15-07：表单选择器**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="表单选择器" />
        <title>表单选择器</title>
        <link rel="stylesheet" href="style.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            //显示Input类型元素的总数量
            $(function () {
                $("#form1 div").html("表单共找出Input类型元素：" + $("#form1 :input").length);
                $("#form1 div").addClass("div");
            })
            //显示所有文本框对象
            $(function () {
                $("#form1 :text").show(3000);
            })
            //显示所有密码框对象
            $(function () {
                $("#form1 :password").show(3000);
            })
            //显示所有单选按钮对象
            $(function () {
                $("#form1 :radio").show(3000);
                $("#form1 #span1").show(3000);
            })
            //显示所有复选框对象
            $(function () {
                $("#form1 :checkbox").show(3000);
                $("#form1 #span2").show(3000);
            })
            //显示所有提交按钮对象
            $(function () {
                $("#form1 :submit").show(3000);
            })
            //显示所有图片域对象
            $(function () {
                $("#form1 :image").show(3000);
            })
            //显示所有重置按钮对象
            $(function () {
                $("#form1 :reset").show(3000);
            })
            //显示所有按钮对象
            $(function () {
                $("#form1 :button").show(3000);
            })
            //显示所有文件域对象
            $(function () {
                $("#form1 :file").show(3000);
            })
        </script>
    </head>

    <body>
        <form id="form1">
            <textarea>多行文本框</textarea>
            <select>
                <option value="0">Item 0</option>
            </select>
            <input type="text" value="单行文本框" class="clsIpt" />
            <input type="password" value="password" class="clsIpt" />
            <input type="radio" /><span id="span1">radio</span>
            <input type="checkbox" /><span id="span2">checkbox</span>
            <input type="submit" value="submit" class="btn" />
            <input type="image" title="image" src="Images/logo.png" class="img" />
            <input type="reset" value="reset" class="btn" />
            <input type="button" value="button" class="btn" />
            <input type="file" title="file" class="txt" />
            <div id="divshow"></div>
        </form>
    </body>
</html>
```

### 4. 事件

严格来说事件在触发后被分为两个阶段，一个是捕获，另一个则是冒泡；但是大多数浏览器并不支持捕获阶段，jQuery 也不支持，因此在事件触发之后，往往执行冒泡过程，所谓的冒泡就是事件执行中的顺序。

**案例：示例 15-08：执行冒泡过程**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="执行冒泡过程" />
        <title>执行冒泡过程</title>
        <link rel="stylesheet" href="style.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //记录执行次数
                var intI = 0;
                //单击事件
                $("body,div,#btnshow").click(function () {
                    intI++;
                    $(".clshow").show().html("你好，").append("执行次数：" + intI);
                })
            })
        </script>
    </head>

    <body>
        <div>
            <input id="btnshow" type="button" value="点击" />
        </div>
        <div class="clshow"></div>
    </body>
</html>
```

在实际应用中，并不希望事件的冒泡现象发生，即单击按钮就执行单一的单击事件，并不触发其他外围的事件。在 jQuery 中可通过 stopPropagation() 方法来实现，该方法可以阻止冒泡过程的发生，具体代码如下所示：

```js
$(function(){
    // 记录执行次数
    var intI = 0;
    // 单击事件
    $("body,div,#btnshow").click(function() {
        intI++;
        $(".clshow").show().html("你好，").append("执行次数：" + intI);
        // 阻止冒泡过程
        event.stopPropagation();
    })
})
```

在编写代码过程中除了使用 stopPropagation() 方法来阻止事件冒泡过程外，还可通过语句 return false 阻止事件的冒泡过程。

#### 4.1 页面载入事件

写法一：

```js
$(document).ready(function() {
    // 代码部分
})
```

写法二：

```js
$(function() {
    // 代码部分
})
```

写法三：

```js
jQuery(document).ready(function() {
    // 代码部分
})
```

写法四：

```js
jQuery(function() {
    // 代码部分
})
```

#### 4.2 绑定事件

在进行事件绑定时，前面曾使用了 .click(function() {}) 绑定按钮的单击事件，除了这种写法之外，在 jQuery 中还可以使用 bind() 方法进行事件的绑定，bind() 功能是为每个选择元素的事件绑定处理函数，其语法结构如下所示：

```js
bind(type, [data], fn);
```

其中参数 type 为一个或多个类型的字符串，如 "click" 或 "change”， 也可以自定义类型，可以被参数 type 调用的类型包括：blur、focus、load、resize、scroll、unload、click、dblclick、mousedown、mouseup、mousemove、mouseover、mouseout、mouseenter、mouseleave、change、select、submit、keydown、keypress、keyup、error。

参数 data 是作为 event.data 属性值传递给事件对象的额外数据对象。

参数 fn 是绑定到每个选择元素的事件中的处理函数。

如果要在一个元素中绑定多个事件，可以将事件用空格隔开，具体代码如下所示：

```js
$(function() {
    $("#btn").bind("click mouseout", function() {
        $(this).attr("disabled", "disabled");
    })
})
```

在 jQuery 绑定事件时，还可通过传入一个映射，对所选对象绑定多个事件处理函数，具体代码如下所示：

```js
$(function() {
    $("#btn").bind({click:function() {
        alert("单击事件");
    },
    change:function() {
        alert("change 事件");
    }})
})
```

在 bind() 方法中，第二个参数 data 为可选项，表示作为 event.data 属性值传递到事件对象的额外数据对象，实际上，该参数很少使用。

```js
$(function() {
    var message = "执行的是 click 事件";
    $("#btn").bind("click", {msg:message}, function(event) {
        alert(event.data.msg);
    });
    message = "执行的是 change 事件";
    $("#btn").bind("change", {msg:message}, function(event) {
        alert(event.data.msg);
    });
})
```

#### 4.3 切换事件

在 jQuery 中，有两个方法用于事件的切换，一个是 hover()，另一个是 toggle()。所谓的切换事件，或是有两个以上的事件绑定于一个元素，在元素的行为动作间进行切换。

调用 jQuery 中的 hover() 方法可以使元素在鼠标悬停与鼠标溢出的事件中进行切换，该方法实际运用中，也可通过 jQuery 中的事件 mouseenter 与 mouseleave 进行替换，下面两种实现代码是等价的。

```js
// hover() 方法
$("a").hover(function() {
    // 执行代码一
}, function() {
    // 执行代码二
})
// mouseenter 与 mouseleave 方法
$("a").mouseenter(function() {
    // 执行代码一
})
$("a").mouseleave(function() {
    // 执行代码二
})
```

hover() 功能是当鼠标移动到所选的元素上面时，执行指定的第一个函数；当鼠标移出时执行指定的第二个函数。

但需要注意的是 jQuery 1.9 版本以后 hover 不再支持为 mouseenter 与 mouseleave 的缩写代名词。

在 toggle() 方法中，可以依次调用 N 个指定的函数，直到最后一个函数，然后重复对这些函数轮播调用。toggle() 方法的功能是每次单击后依次调用函数，说明一下，该方法在调用函数时并非随机或指定调用，而是通过函数设置的前后顺序进行调用，其语法结构如下所示：

```js
toggle(fn, fn1, fn2, [fn3, fn4, ...])
```

需要注意的是，在 jQuery 1.9 以后的版本删除了该函数。

#### 4.4 移除事件

在 jQuery 中，可通过 unbind() 方法移除绑定的所有事件或指定某一个事件，其语法结构如下所示：

```js
unbind([type],[fn])
```

其中参数 type 为移除的事件类型，fn 为需要移除的事件处理函数；如果该方法没有参数，则移除所有绑定事件；如果带有参数 type，则移除该参数指定的事件类型；如果带有参数 fn，则只移除绑定时指定的函数 fn。

```js
$(function() {
    // 按钮一绑定事件
    $("input:eq(0)").bind("click", function() {
        alert("按钮一的单击事件");
    });
    // 按钮二绑定事件
    $("input:eq(1)").bind("click", onclic());
    // 按钮三绑定事件
    $("input:eq(2)").bind("click", function() {
        // 移除全部单击事件
        $("input").unbind();
    });
})
function onclick() {
    alert("按钮二的单击事件");
}
```

unbind() 方法不仅可以移除某类型的全部事件，还可以移除某个指定的自定义事件。

#### 4.5 其他事件

下面主要介绍最为实用的两种处理事件的方法：one() 和 trigger()。

one() 方法的功能是为所选的元素绑定一个仅触发一次的处理函数，其语法结构如下所示：

```js
one(type, [data], fn)
```

其中参数 type 为事件类型，即需要触发什么类型的事件；data 为可选参数，表示作为 event.data 属性值传递给事件对象的额外数据对象；fn 为绑定事件时所要触发的函数。

有时希望页面在 DOM 加载完毕后，自动执行一些操作，在 jQuery 中调用 trigger() 方法可以很轻易地实现这个需求，triggle() 方法的功能是在所选择的元素上触发指定类型的事件，其语法结构如下所示：

```js
trigger(type, [data])
```

其中参数 type 为触发事件的类型，参数 data 为可选项，表示在触发事件时，传递给函数的附加参数。

```js
$(function() {
    // 获取文本框
    var otxt = $("input");
    // 自动选中文本框
    otxt.triggler("select");
    $("#divtip").html("文本被选中");
})
```

trigger() 方法可以实现触发性事件，即不必用户做任何动作，自动执行该方法中的事件。如果不希望页面自动执行，可使用 triggerHandler() 方法，使用方法与 trigger() 方法基本相同，只是该方法不会自动执行器包含的事件。

### 5. 常用效果

#### 5.1 隐藏/显示

在 JavaScript 中，一般通过改变元素的显示方式从而实现其隐藏/显示，如下代码所示：

```js
// 隐藏 id 属性值为 p 的元素
document.getElementById("p").style.display="none";
// 显示 id 属性值为 p 的元素
document.getElementById("p").style.display="block";
```

jQuery 中的 show() 与 hide() 方法不仅可以实现静态模式的显示与隐藏，还可以完成有动画特效的显示与隐藏，只需在方法的括号中加入相应的参数即可，其语法结构如下所示：

```js
// 动画效果的显示功能
show(speed[, callback])
// 动画效果的隐藏功能
hide(speed[, callback])
```

方法中的参数 speed 表示只需动画时的速度，该速度有三个默认字符值 "show"、"normal"、"fast"，其对应的速度分别是 "0.6秒"、"0.4秒"、"0.2秒"；如果不使用默认的字符值，也可以直接输入数字，如 "3000"，表示该动画执行的速度为 3000 毫秒。

#### 5.2 淡入/淡出

fadeIn() 与 fadeOut() 方法结构如下所示：

```js
fadeIn(speed[, callback])
fadeOut(speed[, callback])
```

**案例：示例 15-09：fadeIn() 与 fadeOut 方法**

```html
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="fadeIn()与fadeOut()方法" />
        <title>fadeIn()与fadeOut()方法</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                var tip = $(".divtip");
                //fadeIn事件
                $("#button1").click(function () {
                    tip.html("");
                    //在3000毫秒中淡入图片，并执行一个回调函数
                    $("img").fadeIn(3000, function () {
                        tip.html("淡入成功");
                    })
                })
                //fadeOut事件
                $("#button2").click(function () {
                    tip.html("");
                    //在3000毫秒中淡入图片，并执行一个回调函数
                    $("img").fadeOut(3000, function () {
                        tip.html("淡出成功");
                    })
                })
            })
        </script>
    </head>

    <body>
        <div>
            <div class="divtitle">
                <input type="button" value="fadeIn" id="button1" />
                <input type="button" value="fadeOut" id="button2" />
            </div>
            <div class=divcontent>
                <div class="divtip"></div>
                <img src="images/15-01/img01.jpg" alt="" />
            </div>
        </div>
    </body>
</html>
```

如果要将透明度指定一个值，则需要使用 fadeTo() 方法，其语法结构如下所示：

```js
fadeTo(speed, opacity[, callback])
```

#### 5.3 滑动

要实现元素的滑动效果，需要调用 jQuery 中的两个方法，一个是 slideDown()，另一个是 slideUp()，其语法结构如下所示：

```js
slideDown(speed[, callback])
slideUp(speed[, callback])
```

**案例：示例 15-10：slideDown() 与 slideUp() 方法**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="slideDown()与slideUp()方法" />
        <title>slideDown()与slideUp()方法</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //var btnshow=false;
                var title = $(".divtitle");
                var tip = $("#divtip");
                title.click(function () {
                    $("img").slideToggle(3000);
                });
            })
        </script>
    </head>

    <body>
        <div>
            <div class="divtitle">点击显示效果</div>
            <div class=divcontent>
                <img src="images/15-01/img01.jpg" alt="" />
                <div class="divtip"></div>
            </div>
        </div>
    </body>
</html>
```

slideUp() 与 slideDown() 方法的动画效果仅是减少或增加元素的高度，如果元素有 margin 或 padding 值，这些属性也会与动画的效果一起发生变化。

在 jQuery 中，通过 slideToggle() 方法，无需定义变量，可以根据当前元素的显示状态自动进行切换，其语法如下所示：

```js
slideToggle(speed[, callback])
```

#### 5.4 动画

在 jQuery 中，也允许用户自定义动画效果，通过使用 animate() 方法，可以制作出更复杂、更好的动画效果，其语法格式如下所示：

```js
animate(params[, duration][, easing][, callback])
```

其中，参数 params 表示用于制作动画效果的属性值样式和值的集合。可选项 [duration] 表示三种默认的速度字符 "slow"、"normal"、"fast" 或自定义的数字。可选项 [easing] 为动画插件使用，用于控制动画的表现效果，通常为 "linear" 和 "swing" 字符值。可选项 [callback] 为动画完成后，执行的回调函数。

**案例：示例 15-11：简单的动画**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="简单的动画" />
        <title>简单的动画</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //单击事件
                $(".divframe").click(function () {
                    $(this).animate({
                        width: "20%",
                        height: "70px"
                    }, 3000, function () {
                        $(this).css({ "border": "solid 1px #999" }).html("div变大了");
                    })
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            点击变大
        </div>
    </body>
</html>
```

**案例：示例 15-12：移动位置的动画**

需要注意的是，animate() 方法的第一个参数 params 在表示动画属性时，需要采用 "驼峰命名法"，即如果是 "font-size"，必须写成 "fontSize" 才有效。

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="移动位置的动画" />
        <title>移动位置的动画</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="text/css">
            .divframe {
                border: solid 1px #999;
                text-align: center;
            }

            .divframe .divlist {
                position: relative;
                border: solid 1px #f00;
                width: 70px;
                margin: auto;
            }
        </style>
        <script>
            $(function () {
                //左移单击事件
                $("#button1").click(function () {
                    $(".divlist").animate({
                        left: "-=50px"
                    }, 3000);
                })
                //右移单击事件
                $("#button2").click(function () {
                    $(".divlist").animate({
                        left: "+=50px"
                    }, 3000);
                })
            })
        </script>
    </head>

    <body>
        <div class="divtitle">
            <input type="button" id="button1" value="左移" />
            <input type="button" id="button2" value="右移" />
        </div>
        <div class="divframe">
            <div class="divlist">移动内容</div>
        </div>
    </body>
</html>
```

要使页面中的元素以动画效果移动，必须首先将该元素的 "position" 属性值设置为 "relative" 或 "absolute"，否则，无法移动该元素的位置。

**案例：示例 15-13：队列中的动画**

队列中的动画是指在元素中执行一个以上的多个动画效果，即有多个 animate() 方法在元素中执行。因此，根据这些方法的执行顺序，形成了动画 "队列"，产生队列后，动画的效果便按照队列的顺序依次执行。

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="队列中的动画" />
        <title>队列中的动画</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="text/css">
            .divframe {
                width: 50px;
                height: 50px;
                border: 1px solid #999;
            }
        </style>
        <script>
            $(function () {
                //单击事件
                $(".divframe").click(function () {
                    $(this).animate({ height: "100px" }, "slow")
                        .animate({ width: "100px" }, "slow")
                        .animate({ height: "50px" }, "slow")
                        .animate({ width: "50px" }, "slow")
                })
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            改变大小
        </div>
    </body>
</html>
```

> 提示：可在指定的某队列中插入其他方法，如队列延时方法 delay()。

**案例：示例 15-14：动画停止和延时**

在执行动画时，可通过 stop() 方法停止或 delay() 方法延时某个动画的执行。stop() 方法的语法结构如下所示：

```js
// stop() 方法语法格式
stop([clearQueue],[gotoEnd])
```

delay() 方法的具体语法格式如下所示：

```js
// delay() 方法语法格式
delay(duration, [queueName])
```

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="动画停止和延时" />
        <title>动画停止和延时</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script>
            $(function () {
                //开始单击事件
                $("#button1").click(function () {
                    $(".divframe img").slideToggle(3000);
                })
                //停止单击事件
                $("#button2").click(function () {
                    $(".divframe img").stop();
                });
                //延时单击事件
                $("#button3").click(function () {
                    $(".divframe img").delay(2000).slideToggle(3000);
                });
                $("body").append(reHtml);
            })
            function reHtml() {
                var str = "<b>返回字符串</b>";
                return str;
            }

        </script>
    </head>

    <body>
        <div class="divtitle">
            <input type="button" id="button1" value="开始" />
            <input type="button" id="button2" value="停止" />
            <input type="button" id="button3" value="延时" />
        </div>
        <div class="divframe">
            <img src="images/15-01/img01.jpg" />
        </div>
    </body>
</html>
```

### 6. 案例：使用 jQuery 实现图片轮转

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="使用jQuery实现图片轮转" />
        <title>使用jQuery实现图片轮转</title>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <style type="text/css">
            ol,
            ul {
                list-style: none
            }

            .divframe {
                width: 1000px;
                height: 400px;
                margin: auto;
                position: relative;
            }

            .scroll_list ul {
                margin: 0px;
                padding: 0px;
            }

            .scroll {
                margin: 0 auto;
                width: 938px;
                float: left;
            }

            .scroll_list {
                width: 10000em;
                position: absolute;
            }

            .box {
                height: 400px;
                float: left;
                width: 1000px;
                overflow: hidden;
                position: relative;
                margin-top: 10px;
            }

            .box li {
                display: block;
                float: left;
                width: 1000px;
                height: 400px;
            }

            .box li a img {
                max-width: 1000px;
                max-height: 400px;
            }

            .box li:hover {
                color: #999;
            }

            a.prev,
            a.next {
                background: url(images/15-01/input_bg1.png) no-repeat 0 0;
                display: block;
                width: 42px;
                height: 67px;
                float: left;
                cursor: pointer;
                z-index: 50;
            }

            a.prev {
                position: absolute;
                left: 10px;
                top: 170px;
            }

            a.next {
                background-image: url(images/15-01/input_bg2.png);
                position: absolute;
                left: 950px;
                top: 170px;
            }
        </style>
        <script>
            $(function () {
                //自动轮转
                setInterval("$(\".next\").click()", 3000);
                var page = 1;
                //向右滚动 
                $(".next").click(function () { //点击事件 
                    var v_wrap = $(this).parents(".scroll"); // 根据当前点击的元素获取到父元素 
                    var v_show = v_wrap.find(".scroll_list"); //找到图片展示的区域 
                    var v_cont = v_wrap.find(".box"); //找到图片展示区域的外围区域 
                    var v_width = v_cont.width();
                    var len = v_show.find("li").length; //图片个数 
                    var page_count = Math.ceil(len); //只要不是整数，就往大的方向取最小的整数 
                    if (!v_show.is(":animated")) {
                        if (page == page_count) {
                            v_show.animate({ left: '0px' }, "slow");
                            page = 1;
                        } else {
                            v_show.animate({ left: '-=' + v_width }, "slow");
                            page++;
                        }
                    }
                });
                //向左滚动 
                $(".prev").click(function () { //点击事件 
                    var v_wrap = $(this).parents(".scroll"); // 根据当前点击的元素获取到父元素 
                    var v_show = v_wrap.find(".scroll_list"); //找到图片展示的区域 
                    var v_cont = v_wrap.find(".box"); //找到图片展示区域的外围区域 
                    var v_width = v_cont.width();
                    var len = v_show.find("li").length; //图片个数 
                    //只要不是整数，就往大的方向取最小的整数 
                    var page_count = Math.ceil(len);
                    if (!v_show.is(":animated")) {
                        if (page == 1) {
                            v_show.animate({ left: '-=' + v_width * (page_count - 1) }, "slow");
                            page = page_count;
                        } else {
                            v_show.animate({ left: '+=' + v_width }, "slow");
                            page--;
                        }
                    }
                });
            })
        </script>
    </head>

    <body>
        <div class="divframe">
            <div class="scroll">
                <!-- "prev page" link -->
                <a class="prev"></a>
                <div class="box">
                    <div class="scroll_list">
                        <ul>
                            <li><a href="#"><img class="img1" src="images/15-01/img02.jpg" width="1000px"
                                        height="400px"></a></li>
                            <li><a href="#"><img class="img1" src="images/15-01/img03.jpg" width="1000px"
                                        height="400px"></a></li>
                            <li><a href="#"><img class="img1" src="images/15-01/img04.jpg" width="1000px"
                                        height="400px"></a></li>
                        </ul>
                    </div>
                </div>
                <!-- "next page" link -->
                <a class="next"></a>
            </div>
        </div>
    </body>
</html>
```



