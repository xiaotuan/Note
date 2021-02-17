[toc]

### 1. 什么是 jQuery 插件

#### 1.1 使用方法

+ 在页面中导入包含插件的 JS 文件，并确定它的引用在主 jQuery 库之后，具体代码如下所示：

    ```html
    <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
    <script language="javascript" type="text/javascript" src="jquery/jquery.pl.js"></script>
    ```

+ 在 JS 文件或页面 JS 代码中，使用插件定义的语法进行书写，即可完成该插件的调用。最新的插件都可以从 jQuery 的官网（<http://plugins.jquery.com>）中进行获取。

#### 1.2 常用插件

##### 1.2.1 验证插件 validate

该插件具有如下功能：

+ 自带验证规则：其中包含必填、数字、URL 等众多验证规则。
+ 验证信息提示：可以使用默认的提示信息，也可以自定义提示信息，覆盖默认内容。
+ 多种事件触发：不仅在表单提交时触发验证，而且在 keyup 或者 blur 事件中也能触发。
+ 允许自定义验证规则：除使用自带的验证规则外，还可以方便地自定义验证规则。

##### 1.2.2 表单插件 form

引入该插件后，通过调用 ajaxForm() 或 ajaxSubmit() 两个方法，可以很容易地实现 AJAX 方式提交数据，并通过方法中的 options 对象设置参数、获取服务器返回的数据。同时，该插件还包含如下一些重要方法：

formSerialize()：用于格式化表单中有用的数据，并将其自动调整成适合 AJAX 异步请求的 URL 地址格式。

clearForm()：清除表单中所有输入值的内容。

resetForm()：重置表单中所有的字段内容，即将表单中的所有字段内容都恢复到页面加载时的默认值。

##### 1.2.3 Cookie 插件 cookie

在 jQuery 中引用 cookie 插件后，可以很方便地定义某个 cookie 对象，并设置 cookie 值。

##### 1.2.4 搜索插件 AutoComplete

在 jQuery 中引入该插件后，用户在使用文本框搜索信息时可使用插件中的 autocomplete 方法绑定文本框。当在文本框中输入某个字符时，通过该方法中指定的数据 URL 可返回相匹配的数据，自动显示在文本框下，提示用户进行选择。

##### 1.2.5 图片灯箱插件 notesforlightbox

##### 1.2.6 右键菜单插件 contextmenu

##### 1.2.7 图片放大镜插件 jqzoom

jqzoom 是一款基于 jQuery 库的图片放大插件，在页面中实现放大的方法是：先准备两张一大一小的相同图片，在页面打开时，展示小图片，当鼠标在小图片的任意位置移动时，调用插件中的 jqzoom() 方法，绑定另外一张相同的大图片，在指定位置显示与小图片所选区域相同的大图片，从而实现逼真的放大效果。

### 2. jQuery UI

#### 2.1 交互性插件

##### 2.1.1 拖动插件

Draggable（拖动）插件能使请求的对象拖动，通过这个插件，可以使用 DOM 元素跟随鼠标进行移动，通过设置方法中的 option 选项，可实现各种各样的拖动需求，其语法结构如下所示：

```js
draggable(option)
```

<center><b>表 15-14 选项 options 可接受的常用参数</b></center>

| 参数           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| helper         | 表示拖动的对象，默认值为 original，即拖动自身；如果设置为 clone，那么以复制的形式进行拖动 |
| handle         | 表示触发拖动的对象，常用于一个 DOM 元素                      |
| dragPrevention | 设置不触发拖动的对象                                         |
| start          | 当拖动启动时触发的回调函数 function(e, ui) ，其中参数 e 表示 event 事件， e.target 表示被拖动的对象；参数 ui 表示与拖动相关的对象 |
| stop           | 停止拖动时触发的回调函数，参数说明与 start 相同              |
| drag           | 在拖动过程中触发的回调函数，参数说明与 start 相同            |
| zIndex         | 设置被拖动时，helper 对象的 z-index 值                       |
| axis           | 设置拖动时的坐标，可设为 x 或 y 值                           |
| containment    | 设置拖动时的区域，可以设为 document、parent 或其他指定的元素和对象 |
| grid           | 设置拖动时的步长，如 grid:[50,60]，表示 x 坐标每次移动 50px，y 坐标每次移动 60px |
| opacity        | 设置对象在拖动过程中的透明度，范围是 0.0 ~ 1.0               |
| revent         | 设置一个布尔值，如果为 true，则表示对象被拖动结束后，又会自动返回原地；如果为 false，则不会返回原地，默认值为 false |
| scroll         | 设置一个布尔值，如果为 true，则表示对象在拖动时，容器自动滚动，默认为 true |
| disable        | 临时性禁用拖动功能                                           |
| enable         | 重新开启对象的拖动功能                                       |
| destroy        | 彻底移除对象上的拖动功能                                     |

##### 2.1.2 放置

可以通过 droppable（放置）插件 "存放" 拖动的对象，即类似网上商城中购物车的效果，其语法结构如下所示：

```js
droppable(options)
```

<center><b>表 15-15 选项 options 可接受的常用参数</b></center>

| 参数        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| accept      | 可以为字符串或函数，如果是字符串，表示通过字符串获取的元素允许接收；如果是函数，表示只有执行函数后，返回 true 时，才允许接收 |
| activeClass | 被接收的对象在拖动时，接收容器的 CSS 样式                    |
| hoverClass  | 被接收的对象在进入接收容器时，容器的 CSS 样式                |
| active      | 被接收的对象在拖动时调用的函数 function(e, ui) 。其中函数 e 表示 event 事件，e.target 表示被拖动的对象，参数 ui 表示与拖动相关的对象。 |
| deactive    | 被接收的对象停止拖动时调用的函数，其中的参数说明与 active 一样 |
| over        | 被接收的对象拖动到接收容器上方时调用的函数，其中的参数说明与 active 一样 |
| out         | 被接收的对象拖出接收容器时调用的函数，其中的参数说明与 active 一样 |
| drop        | 被接收的对象拖动后完全进入接收容器时调用的函数，其中的参数说明与 active 一样 |

##### 2.1.3 排序插件

可以通过 sortable（排序）插件将有序列的标记按照用户的想法任意拖动位置，形成一个新的序列，从而实现拖动排序的功能，其语法格式如下所示：

```js
sortable(options)
```

其中，选项 options 所调用的参数与插件 draggable 中的 options 参数有很多相似之处。需要说明的是参数 item，该参数用于申请在页面中那些元素以拖动的方式进行排序。

#### 2.2 微型插件

##### 2.2.1 折叠面板插件

其语法格式如下所示：

```js
accordion(options)
```

<center><b>表 15-16 选项 options 可接受的参数</b></center>

| 参数       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| animated   | 设置折叠时的效果，默认值为 slide；也可以自定义动画。如果设置为 false，表示不要设置折叠时的动画效果。 |
| active     | 设置默认展开的主体效果，默认值为 1                           |
| autoHeight | 内容高度是否设置为自动增高，默认为 true                      |
| event      | 设置展开选项的事件，默认值为 click，也可以设置双击、鼠标滑过事件 |
| fillSpace  | 设置内容是否充满父元素的高度，默认值为 false，如果实在为 true，那么 autoHeight 参数设置的值无效 |
| icon       | 设置小图标，其设置的格式为{"header", "主题默认图标类别名", "headerSelected", "主题选中时图标类别名"} |

##### 2.2.2 日历

在 jQuery UI 中可以使用 datepicker （日历）插件来实现网页中的选择日期效果，其语法格式如下所示：

```js
$(".selector").datepicker(options)
```

<center><b>表 15-16 选项 options 可接受的常用参数</b></center>

| 参数            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| changeMonth     | 设置一个布尔值，如果为 true，则可以在标题处出现一个下拉选择框，可以选择月份，默认值为 false |
| changeYear      | 设置一个布尔值，如果为 true，则可以在标题处出现一个下拉选择框，可以选择年份，默认值为 false |
| showButtonPanel | 设置一个布尔值，如果为 true，则在日期的下面显示一个面板，其中有两个按钮；一个为 "今天"，另一个为 "关闭"，默认值为 false，表示不显示 |
| closeText       | 设置关闭按钮上的文字信息，这项设置的前提是 showButtonPanel 的值必须为 true，否则显示不了效果 |
| dateFormat      | 设置显示在文本框中的日期格式，可设置为 {dateFormat:'yy-mm-dd'}，表示日期的格式为年-月-日 |
| defaultDate     | 设置一个默认日期值，如 {defaultDate:+7} 表示弹出日期选择窗口后，默认的日期是当前日期再加上 7 天 |
| showAnim        | 设置显示弹出或隐藏日期选择窗口的方式。可以设置的方式有 "show" "slideDown" "fadeIn"，或者为 ""，表示没有弹出日期选择窗口的方式 |
| showWeek        | 设置一个布尔值，如果为 true，则可以显示每天对应的星期，默认值为 false |
| yearRange       | 设置年份的范围，如 {year:'2000:2015'}，表示年份下拉列表框的最小值为 2000 年，最大值为 2015 年，默认值为 c-10:c+10，当前年份的前后十年 |

##### 2.2.3 选项卡插件

在 jQuery UI 中，通过在页面中导入 tabs 插件，并调用插件中的 tabs() 方法直接针对列表生成对应菜单，可轻松地实现选项卡功能，其语法结构如下所示：

```js
tabs(options)
```

<center><b>表 15-18 选项 options 可接受的常用参数</b></center>

| 参数        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| collapsible | 是否可折叠选项卡的内容，设置一个布尔值，如果为 true，那么允许用户折叠选项卡的内容，即首次单击关闭，默认值为 false |
| disabled    | 设置不可用选项卡，如 {disabled:[1,2]}，表示选项卡中第1项、第2项不可用 |
| event       | 设置触发切换选项卡的事件，默认值为 click，也可以设置为 mousemove |
| fx          | 设置切换选项卡时的一些动画效果                               |
| selected    | 设置被选中选项卡的 Index，如 {selected:2}，表示第2项选项卡被选中 |

##### 2.2.4 对话框插件

其语法结构如下所示：

```js
$(".selector").dialog(options)
```

<center><b>表 15-19 选项 options 可接受的常用参数</b></center>

| 参数          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| autoOpen      | 设置一个布尔值，如果为 false，则不显示对话框，默认值为 true  |
| bgiframe      | 设置一个布尔值，如果为 true，则表示在 IE6 下，弹出的对话框可以遮盖住页面中类似于 \<select\> 标记的下拉列表框，默认值为 false |
| buttons       | 设置对话框中的按钮，如 {"button", {"OK":function(){$(this).dialog("close");}}}，表示设置了一个文本内容为 "OK" 的按钮，单击该按钮将关闭对话框 |
| closeOnEscape | 设置一个布尔值，如果为 false，则表示不适用 Esc 快捷键的方式关闭对话框，默认为 true |
| draggable     | 设置一个布尔值，表示是否可以拖动对话框，默认值为 true        |
| hide          | 设置对话框关闭时的动画效果，可以设置为 slide 等各种动画效果，默认值为 null |
| modal         | 设置对话框是否以模式的方式显示，模式指的是页面背景变灰、不允许操作、焦点锁定对话框的效果，默认值为 false |
| position      | 设置对话框弹出时在页面中的位置，可以设置为 top、center、bottom、left、right，默认值为 center |
| show          | 设置对话框显示时的动画效果，说明与 hide 参数一样             |
| title         | 设置对话框中主题部分的文字，默认为空                         |

### 3. jQuery Mobile

#### 3.1 使用

jQuery Mobile 的最新版本可在官网 （<http://jquerymobile.com>）下载获得。

在使用时，需要用到 jQuery Mobile 中的 CSS 样式文件以及 jQuery Mobile 的 JS 文件，引用的具体代码如下所示：

```html
<link rel="stylesheet" href="style/jquery.mobile.css" />
<script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
<script language="javascript" type="text/javascript" src="jquery/jquery.mobile.js"></script>
```

#### 3.2 页面

##### 3.2.1 jQuery Mobile 页面模板

**案例：示例 15-26：Page Header**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <title>Page Header</title>
        <link rel="stylesheet" href="style/jquery.mobile.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <!--<script src="custom-script-here.js"></script>-->
        <script language="javascript" type="text/javascript" src="jquery/jquery.mobile.js"></script>
    </head>

    <body>
        <div data-role="page">
            <div data-role="header">
                <h1>Page Header</h1>
            </div>
            <div data-role="content">
                <p>Hello jQuery Mobile</p>
            </div>
            <div data-role="footer">
                <h1>Page Footer</h1>
            </div>
        </div>
    </body>
</html>
```

对于 jQuery Mobile 来说，这是一个推荐的视图配置。

device-width 值表示希望让内容扩展到屏幕的整个宽度。initial-scale 设置了用来查看 Web 页面的初始缩放百分比或缩放因数。值为 1，则显示一个未缩放的文档。

data-role="page" 为一个 jQuery Mobile 页面定义了页面容器，只有在构建多页面设置时，才会用到该元素。

Data-role="header" 是页眉（header）或标题栏，该属性是可选的。

Data-role="content" 是内容主体的包装器，该属性也是可选的。

Data-role="footer" 包含页脚栏，该属性同样是可选的。

##### 3.2.2 多页面模板

使用多页面模板的结构如下所示：

```html
<!-- 第一个页面 -->
<div data-role="page" id="Home" data-title="Home">
    <div data-role="header">
        <h1>Page Header</h1>
    </div>
    <div data-role="content">
        <p>Hello jQuery Mobile</p>
        <a href="#contact" data-role="button">Contact US</a>
    </div>
</div>
<!-- 第二个页面 -->
<div data-role="page" id="contact" data-title="contact">
    <div data-role="header">
        <h1>Page Header</h1>
    </div>
    <div data-role="content">
        <p>Hello</p>
    </div>
</div>
```

当链接到一个内部页面时，必须通过页面的 id 来引用，即使用 href="#id"，当链接到一个包含多个页面的页面时，必须为其链接添加 rel="external"。

##### 3.2.3 单页面文档与多页面文档对比

在大多数情况下，建议使用单页面模型，然后在后台将常用的页面动态添加到 DOM 中。在希望动态载入的任何链接上添加 data-prefetch 属性即可实现该行为。

#### 3.3 过渡效果

jQuery Mobile 拥有一系列关于如何从一页过渡到下一页的效果，默认情况下，框架会为所有的过渡应用 "淡入淡出" 效果。通过为链接、按钮或表单添加 data-transition 属性，可以设置其他过渡效果。

<center><b>表 15-20 过渡效果常用选项</b></center>

| 参数      | 说明                       |
| --------- | -------------------------- |
| fade      | 默认，淡入淡出到下一页     |
| flip      | 从后向前翻转到下一页       |
| flow      | 抛出当前页面，引用下一页   |
| pop       | 像弹出窗口一样转到下一页   |
| slide     | 从右向左滑动到下一页       |
| slidefade | 从右向左滑动并淡入到下一页 |
| slideup   | 从下到上滑动到下一页       |
| slidedown | 从上到下滑动到下一页       |
| turn      | 转向下一页                 |
| none      | 无过渡效果                 |

#### 3.4 按钮

jQuery Mobile 中的按钮可通过三种方法进行创建：一是使用 \<button\> 元素，二是使用 \<input\> 元素，三是使用 data-role="button" 的 \<a\> 元素。

一般在实际应用中，使用 data-role="button" 的 \<a\> 元素来创建页面之间的链接，而 \<input\> 和 \<button\> 元素一般用于表单之中。

##### 3.4.1 行内按钮

默认情况下按钮会占据屏幕的全部宽度，如果需要按钮适应其内容，或者需要两个或多个按钮并排显示，可通过添加 data-inline="true" 属性来实现。

##### 3.4.2 组合按钮

jQuery Mobile 提供了对按钮进行组合的简单方法。将 data-role="controlgroup" 属性与 data-type="horizontal|vertical" 一同使用，以规定水平或垂直地组合按钮。默认情况下，组合按钮是崔志分组的，彼此间没有外边距和空白，并且只有第一个和最后一个按钮拥有圆角。

##### 3.4.3 回退按钮

在 jQuery Mobile 中，回退按钮在默认情况下是禁用的，如果想要在页面中添加回退按钮，可通过以下两种方法实现：一是在页面容器中添加 data-auto-back-btn="true" 属性，可以为某个特定页面添加回退按钮；二是在绑定 mobileinit 选项时，通过将 addBackBtn 选项设置为 true，可以在全局启用回退按钮。如果希望创建一个行为与回退按钮类似的按钮，则可以在 \<a\> 元素中添加 data-rel="back" 属性。

<center><b>表 15-21 按钮的 data-* 属性</b></center>

| 方法语法     | 值            | 参数说明           |
| ------------ | ------------- | ------------------ |
| data-corners | true \| false | 规定按钮是否有圆角 |
| data-mini    | true \| false | 规定是否为小型按钮 |
| data-shadow  | true \| false | 规定按钮是否有阴影 |

##### 3.4.4 按钮图标

在 jQuery Mobile 中几乎不需要任何处理就可以将图像设计为按钮，当使用 \<a\> 元素来包含图像时，无需任何修改。但是在使用 \<input\> 元素时，则需要添加 data-role="none" 属性来实现将图像设计为按钮，其实现代码如下所示：

```html
<input type="image" src="images/15-01/btn.jpg" data-role="none" />
```

还可以通过添加 data-icon 属性来设置要显示的图标，并将图标添加到任何按钮。

当然也可以通过 data-iconpos 属性来对图标进行定位，其参数值 top、right、bottom、left 分别对应显示位置的上、右、下、左显示位置。如果只需要显示图标，则将 data-iconpos 设置为 notext 即可。

#### 3.5 样式切换

jQuery Mobile 自带了一些主题，只需在组件上添加 data-theme 属性即可，它的值可以为 a、b、c、d 或 e。此外，jQuery Mobile 还提供了一个强大的 ThemerRoller 组件（<http://jquerymobile.com/themeroller>），可以自定义主题。

