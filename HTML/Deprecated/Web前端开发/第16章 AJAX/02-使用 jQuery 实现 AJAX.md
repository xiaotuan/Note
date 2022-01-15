[toc]

### 1. 基本方法

#### 1.1 load() 方法

##### 1.1.1 载入 HTML 文档

load() 方法能载入远程 HTML 代码并插入 DOM 中。其结构如下所示：

```js
load(url[, data][, complete])
```

<center><b>表 16-1 load() 方法参数解释</b></center>

| 参数名称 | 参数选择 | 参数类型 | 参数说明                      |
| -------- | -------- | -------- | ----------------------------- |
| url      | 必须     | String   | 请求 HTML 的 URL 地址         |
| data     | 可选     | Object   | 发送至服务器的 key/value 数据 |
| complete | 可选     | function | 请求完成时的回调函数名称      |

**案例：示例 16-03：载入 HTML 文档**

**16-03-01.html**

```html
<!DOCTYPE html>
<html>
    <head>
    <meta charset="utf-8" />
    <title>AJAX要载入的页面</title>
    </head>
    <body>
        <div>
            <ul>
                <li class="title">这是一个AJAX载入文档的示例-标题</li>
                <li>内容是一个列表</li>
                <li>读取到此列表</li>
                <li>成功使用AJAX方式调用数据</li>
            </ul>
        </div>
    </body>
</html>
```

**16-03.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="AJAX" />
        <meta content="使用AJAX操作载入HTML文档" />
        <title>使用AJAX操作载入HTML文档</title>
        <script type="text/javascript" src="jquery/jquery-1.11.3.js"></script>
        <script type="text/javascript">
            $(function () {
                $("#showAjax").click(function () {
                    $("#ajaxContent").load("16-03-01.html");
                });
            })
        </script>
    </head>

    <body>
        <div><input type="button" id="showAjax" value="AJAX载入页面" /></div>
        <div id="ajaxContent">点击"AJAX载入页面"按钮，此处的内容将被替换为文件16-03-01.html中的内容</div>
    </body>
</html>
```

##### 1.1.2 筛选载入的 HTML 文档

通过 load() 方法的 URL 参数来达到从 HTML 文档里筛选内容的目的。在 16-03.html 中，起作用的 jQuery 代码如下所示：

```js
$(function() {
    $("#showAjax").click(function() {
        $("#ajaxContent").load("16-03-01.html .title");
    })
})
```

##### 1.1.3 传递方式

load() 方法的传递方法根据 data 来自动指定。如果没有参数传递，则采用 GET 方法传递；如果指定了 data 数据，则传递方式自动转换为 POST 方式。

##### 1.1.4 回调参数

对于必须在加载完成后才能继续的操作，load() 方法提供了回调函数。

可选的 complete 参数规定当 load() 方法完成后所要允许的回调函数。回调函数可以设置不同的参数；responseTXT，包含调用成功时的结果内容；statusTXT，包含调用的状态；xhr，包含 XMLHttpRequest 对象。

#### 1.2 $.get() 方法

$.get() 使用 GET 方法进行异步请求。其语法结构具体如下所示：

```js
$.get(url[, data][, callback][, type])
```

<center><b>表 16-2 $.get() 方法参数解释</b></center>

| 参数名称 | 参数选择 | 参数类型 | 参数说明                                                     |
| -------- | -------- | -------- | ------------------------------------------------------------ |
| url      | 必须     | String   | 请求 HTML 的 URL 地址                                        |
| data     | 可选     | Object   | 发送至服务器的 key/value 数据，作为 QueryString 附加到请求 URL 中 |
| callback | 可选     | function | 载入成功时回调函数（只有当 Respose 的返回状态是 success 才调用该方法）自动将请求结果和状态传递给该方法 |
| type     | 可选     | String   | 服务器端返回的内容格式，包括 xml、html、script、json、text 和 _default |

数据格式。服务器返回的数据格式可以有很多种，但都可以完成同样的任务，下面是集中返回数据格式的对比应用。

a. HTML 片段

服务器端返回的数据格式是 HTML 片段时，不需要处理就可以将 HTML 数据插入到页面中。

b. XML 文档

服务器端返回的数据格式是 XML 文档时，需要对返回的数据进行处理。jQuery 对 DOM 有强大的处理能力，处理 XML 文档与处理 HTML 文档一样，也可以使用常规的 attr()、find()、filter() 及其他方法。

c. JSON 文件

服务器端返回的数据格式是 JSON 文件时，需要对返回的数据处理后才可以将数据添加到页面。

d. text

服务器端返回纯文本字符串，不需要处理就可以直接使用。

**案例：示例 16-04：使用 $.get() 方法进行数据验证，返回不同的数据格式**

**16-04.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="AJAX" />
        <meta content="使用Get方法进行数据验证" />
        <title>使用Get方法进行数据验证</title>
        <style type="text/css">
            body {
                margin: 0;
                padding: 0;
                font-size: 12px;
            }

            .center {
                margin: 0 auto;
                text-align: center;
                width: 100%;
            }

            .submitButton {
                margin-top: 20px;
            }

            .submitButton input {
                margin: 0 5px;
            }

            .submitInput {
                margin: 20px 0px;
            }

            .submitInput input {
                width: 150px;
                height: 20px;
                border: 1px solid #ccc;
            }

            .submitInput div {
                height: 30px;
            }
        </style>
        <script type="text/javascript" src="jquery/jquery-1.11.3.js"></script>
        <script type="text/javascript">
            $(function () {

                //返回HTML数据处理
                $('#checkHtml').click(function () {
                    var username = $('#username').val();
                    var password = $('#password').val();
                    $.get('index.php',
                        {
                            username: username,
                            password: password,
                            type: 'html'
                        },
                        function (data) {
                            $("#showContent").html('HTML数据：' + data);
                        })
                });

                //返回XML数据处理
                $('#checkXml').click(function () {
                    var username = $('#username').val();
                    var password = $('#password').val();
                    $.get('index.php',
                        {
                            username: username,
                            password: password,
                            type: 'xml'
                        },
                        function (data) {
                            var info = $(data).find('result').text();
                            var str = '';
                            if (info == '验证成功') {
                                str += 'XML数据：<span style="color:green;">' + info + '</span>';
                            } else {
                                str += 'XML数据：<span style="color:red;">' + info + '</span>';
                            }
                            $("#showContent").html(str);
                        })
                });

                //返回JSON数据处理
                $('#checkJson').click(function () {
                    var username = $('#username').val();
                    var password = $('#password').val();
                    $.get('index.php',
                        {
                            username: username,
                            password: password,
                            type: 'json'
                        },
                        function (data) {
                            var dataJSON = JSON.parse(data);//将JSON字符串格式化为对象
                            var str = '';
                            if (dataJSON.result == '1') {
                                str += 'JSON数据：<span style="color:green;">' + dataJSON.info + '</span>';
                            } else {
                                str += 'JSON数据：<span style="color:red;">' + dataJSON.info + '</span>';
                            }
                            $("#showContent").html(str);
                        })
                });

                //返回TEXT数据
                $('#checkText').click(function () {
                    var username = $('#username').val();
                    var password = $('#password').val();
                    $.get('index.php',
                        {
                            username: username,
                            password: password,
                            type: 'text'
                        },
                        function (data) {
                            var str = '';
                            if (data == '验证成功') {
                                str += 'TEXT数据：<span style="color:green;">验证成功</span>';
                            }
                            if (data == '验证失败') {
                                str += 'TEXT数据：<span style="color:red;">验证失败</span>';
                            }
                            $("#showContent").html(str);
                        })
                });

            })
        </script>
    </head>

    <body>
        <div class="center">
            <div class="submitButton"><input type="button" id="checkHtml" value="返回HTML数据" /><input type="button"
                    id="checkXml" value="返回XML数据" /><input type="button" id="checkJson" value="返回JSON数据" /><input
                    type="button" id="checkText" value="返回TEXT数据" /></div>
            <div class="submitInput">
                <form id="check">
                    <div>用户名：<input type="text" maxlength="20" id="username" /></div>
                    <div>密<span style="display:inline-block;width:12px;"></span>码：<input type="password" maxlength="10"
                            id="password" /></div>
                </form>
            </div>
            <div id="showContent">返回数据显示在这里，用户名为admin，密码为admin返回“验证成功”，否则返回验证失败</div>
        </div>
    </body>
</html>
```

**index.php**

```php
<?php
if (isset($_GET['username']) && isset($_GET['password']) && isset($_GET['type'])) {
    $username = $_GET['username'];
    $password = $_GET['password'];
    $info = '';
    if ($username == 'admin' && $password == 'admin') {
        $info.='验证成功';
    } else {
        $info .= '验证失败';
    }
    switch ($_GET['type']) {
        case 'html':
            if ($info == '验证成功') {
                $result = '<span style="color:green;">' . $info . '</span>';
            } else if ($info == '验证失败') {
                $result = '<span style="color:red;">' . $info . '</span>';
            }
            break;
        case 'xml':
            header('Content-Type: text/xml');
            $result = '';
            $result.='<?xml version="1.0" encoding="utf-8" ?>';
            $result.='<result>';
            if ($info == '验证成功') {
                $result.=$info;
            } else if ($info == '验证失败') {
                $result.=$info;
            }
            $result.='</result>';
            break;
        case 'json':
            if ($info == '验证成功') {
                $array = array('info' => $info, 'result' => '1');
            } else if ($info == '验证失败') {
                $array = array('info' => $info, 'result' => '0');
            }
            $result = json_encode($array);
            break;
        case 'text':
            $result = $info;
            break;
    }
    echo $result;
}
?>
```

#### 1.3 $.post() 方法

\$.post() 与 \$.get() 方法的区别：

+ GET 请求会将参数跟在 URL 后进行传递，POST 请求则是作为 HTTP 消息的实体内容发送给 Web 服务器。在 AJAX 请求中，这种区别对于用户不可见。
+ GET 方式对传输的数据大小限制（通常不能大于 2KB），而使用 POST 方式传递的数据量要比 GET 大（理论上不受限制）。
+ GET 方式请求的数据会被浏览器缓存起来，其他用户可以从浏览器的历史记录中读取到这些数据。在个别情况下，GET 方式会带来严重的安全问题，使用 POST 方式传递数据可以避免这一现实。
+ GET 方式和 POST 方式传递的数据在服务器端获取的方式有所不同。使用 PHP 获取 GET 方式提交的数据可以使用 \$\_GET[] 获取，获取 POST 方式提交的数据可以使用 \$\_POST[] 获取，使用 GET 方式和 POST 方式提交的数据，都可以使用 \$\_REQUEST[] 获取。

**案例：示例 16-05：使用 $.post() 方法验证用户名、密码**

**16-05.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="AJAX" />
        <meta content="使用POST方法进行数据验证" />
        <title>使用POST方法进行数据验证</title>
        <style type="text/css">
            body {
                margin: 0;
                padding: 0;
                font-size: 12px;
            }

            .center {
                margin: 0 auto;
                text-align: center;
                width: 100%;
            }

            .submitButton {
                margin-top: 20px;
            }

            .submitButton input {
                margin: 0 5px;
            }

            .submitInput {
                margin: 20px 0px;
            }

            .submitInput input {
                width: 150px;
                height: 20px;
                border: 1px solid #ccc;
            }

            .submitInput div {
                height: 30px;
            }
        </style>
        <script type="text/javascript" src="jquery/jquery-1.11.3.js"></script>
        <script type="text/javascript">
            $(function () {

                //返回HTML数据处理
                $('#checkHtml').click(function () {
                    var username = $('#username').val();
                    var password = $('#password').val();
                    $.post('index.php',
                        {
                            username: username,
                            password: password,
                            type: 'html'
                        },
                        function (data) {
                            $("#showContent").html(data);
                        })
                });
            })
        </script>
    </head>

    <body>
        <div class="center">
            <div class="submitButton"><input type="button" id="checkHtml" value="提交数据" /></div>
            <div class="submitInput">
                <form id="check">
                    <div>用户名：<input type="text" maxlength="20" id="username" /></div>
                    <div>密<span style="display:inline-block;width:12px;"></span>码：<input type="password" maxlength="10"
                            id="password" /></div>
                </form>
            </div>
            <div id="showContent">返回数据显示在这里，用户名为admin，密码为admin返回“验证成功”，否则返回验证失败</div>
        </div>
    </body>
</html>
```

**index.php**

```php
<?php
if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $info = '';
    if ($username == 'admin' && $password == 'admin') {
        $info.='验证成功';
    } else {
        $info .= '验证失败';
    }
    if ($info == '验证成功') {
    $result = '<span style="color:green;">' . $info . '</span>';
    } else if ($info == '验证失败') {
        $result = '<span style="color:red;">' . $info . '</span>';
    }
    echo $result;
}
?>
```

#### 1.4 $.getScript() 方法

在页面加载时就加载全部 JavaScript 文件是不必要的，理想状态是在需要某个 JavaScript 文件时再进行加载。jQuery 提供了 $.getScript() 方法实现这一功能，可以直接加载 JS 文件，与加载 HTML 片段一样简单方便，且不需要对 JavaScript 文件进行处理，JavaScript 文件会自动执行。

```js
$("#button").click(function() {
    $.getScript('***.js');
})
```

#### 1.5 $.getJSON() 方法

\$.getJSON() 方法用于加载 JSON 文件，与 \$.getScript() 方法用法相同。

#### 1.6 $.ajax() 方法

\$.ajax() 方法不仅能实现与 load()、\$.get()、\$.post() 方法基本相同的功能，还可以设定 beforeSend（提交前回调函数）、error（请求失败后处理）、success（请求成功后处理）以及 complete（请求完成后处理）回调函数。

$.ajax() 方法是 jQuery 最底层的 AJAX 实现，也就是说 jQuery 的其他 AJAX 方法都是基于此方法实现的。使用的语法结构如下所示：

```js
$.ajax(options)
```

<center><b>表 16-3 $.ajax() 方法参数解释</b></center>

| 参数名称          | 参数类型 | 参数说明                                                     |
| ----------------- | -------- | ------------------------------------------------------------ |
| async             | boolean  | 默认值为 true。默认设置下，所有请求均为异步请求。如果需要发送同步请求，请将此选项设置为 false。注意，同步请求将锁住浏览器，用户其他操作必须等待请求完成才可以执行 |
| beforeSend(XHR)   | function | 发送请求前可以修改 XMLHttpRequest 对象的函数，如添加自定义 HTTP 头。如果返回 false，可以取消本次 AJAX 请求。XMLHttpRequest 对象是唯一的参数 |
| cache             | boolean  | 默认值为 true，dataType 为 script 和 jsonp 时默认为 false。设置为 false 将不缓存此页面。 |
| complete(XHR, TS) | function | 请求完成后回调函数（请求成功或失败之后均调用）。参数：XMLHttpRequest 对象和一个描述请求类型的字符串。 |
| contentType       | string   | 默认值为 "application/x-www-form-urlencoded"。发送信息至服务器时的内容编码类型。默认值适合大多数情况。如果你明确传递了一个 content-type 给 $.ajax()，那么它必定会发送给服务器（即使没有数据要发送） |
| context           | object   | 这个对象用于设置 AJAX 相关回调函数的上下文。也就是说，让回调函数内 this 指向这个对象（如果不设定这个参数，那么 this 就指向调用本次 AJAX 请求时传递的 options 参数）。比如指定一个 DOM 元素作为 content 参数，这样就设置了 success 回调函数的上下文为这个 DOM 元素 |
| data              | string   | 发送到服务器的数据。将自动转换为请求字符串格式。GET 请求中将附加在 URL 后。禁止自动转换可以查看 processData 选项。对象必须是 key/value 格式。如果为数组，jQuery 将自动为不同值对应同一个名称。如 {foo:["bar1", "bar2"]} 转换为 '$foo=bar1&foo=bar2' |
| dataFilter        | function | 给 AJAX 返回的原始数据进行预处理的函数。提供 data 和 type 两个参数：data 是 AJAX 返回的原始数据，type 是调用 jQuery.ajax 时提供的 dataType 参数。函数返回的值将由 jQuery 进一步处理 |
| dataType          | string   | 预期服务器返回的数据类型。如果不指定，jQuery 将自动根据 HTTP 包 MIME 信息来智能判断，比如 XMLMIME 类型就被识别为 XML。可用类型如下：<br />xml：返回 XML 文档，可用 jQuery 处理<br />html：返回纯文本 HTML 信息；包含的 script 标签会在插入 DOM 时执行。<br />Script：返回纯文本 JavaScript 代码，不会自动缓存结果。除非设置了 "cache" 参数。注意：在远程请求时（不在同一个域下），所有 POST 请求都将转为 GET 请求（因为将使用 DOM 的 script 标签来加载）<br />json：返回 JSON 数据。<br />Jsonp：JSONP 格式。使用 JSONP 形式调用函数时，如 "myurl?callback=?" jQuery 将自动替换?为正确的函数名，以执行回调函数。<br />Text：返回纯文本字符串 |
| error             | function | 请求失败时调用此函数。<br />有以下三个参数：XMLHttpRequest 对象、错误信息、（可选）捕获的异常对象。<br />如果发生了错误，错误信息（第二个参数）除了得到 null 之外，还可能是 timeout、error、notmodified 和 parsererror |
| global            | boolean  | 是否触发全局 AJAX 事件。默认值：true。设置为 false 将不会触发全局 AJAX 事件，如 ajaxStart 或 ajaxStop 可用于控制不同的 AJAX 事件 |
| ifModified        | boolean  | 仅在服务器数据改变时获取新数据。默认值：false。使用 HTTP 包 Last-Modified 头信息判断 |
| jsonp             | string   | 在一个 jsonp 请求中重写回调函数的名字。这个值用来替代在 "callback=?" 这种 GET 或 POST 请求中 URL 参数时的 "callback" 部分，比如 {jsonp:'onJsonPLoad'} 会导致将 "onJsonPLoad=?" 传给服务器 |
| jsonpCallback     | string   | 为 jsonp 请求指定一个回调函数名。这个值将用来取代 jQuery 自动生成的随机函数名。这主要用来让 jQuery 生成独特的函数名，这样管理请求更容易，也能方便地提供回调函数和错误处理。也可以在让浏览器缓存 GET 请求时，指定这个回调函数名 |
| password          | string   | 用于响应 HTTP 访问认证请求的密码                             |
| processData       | boolean  | 默认值为 true。默认情况下，通过 data 选项传递进来的数据，如果是一个对象（技术上讲只要不是字符串），都会处理转化成一个查询字符串，以配合默认内容类型 "application/x-www-form-urlencoded"。如果要发送 DOM 树信息或其他不希望转换的信息，请设置为 false |
| scriptCharset     | string   | 只有当请求时 dataType 为 "jsonp" 或 "script"，并且 type 是 "GET" 才会用于强制修改 charset。通常只在本地和远程的内容编码不同时使用 |
| success           | function | 请求成功后的回调函数。参数：由服务器返回并根据 dataType 参数进行处理后的数据；描述状态的字符串 |
| traditional       | boolean  | 如果你想要用传统的方式来序列化数据，那么就设置为 true        |
| timeout           | number   | 设置请求超时时间（毫秒）。此设置将覆盖全局设置               |
| type              | string   | 默认值：GET。请求方式 POST 或 GET。注意：其他 HTTP 请求方式，如 PUT 和 DELETE 也可以使用，但仅有部分浏览器支持 |
| url               | string   | 默认值：当前页地址。发送请求的地址                           |
| username          | string   | 用于响应 HTTP 访问认证请求的用户名                           |
| xhr               | function | 需要返回一个 XMLHttpRequest 对象。默认在 IE 下是 ActiveXObject，而其他情况下是 XMLHttpRequest。用于重写或者一个增强的 XMLHttpRequest 对象 |

使用 \$.ajax() 替代 \$.getScript() 方法，具体代码如下所示：

```js
$.ajax({
    type: "GET",
    url:"***.js",
    datatype:"script"
})
```

使用 \$.ajax() 替代 \$.getJSON() 方法，具体代码如下所示：

```js
$.ajax({
    type:"GET",
    url:"***.json",
    datatype:"json",
    success:function(data) {
        ......
    }
})
```

### 2. jQuery 中全局事件

<center><b>表 16-4 jQuery 中 AJAX 全局事件方法</b></center>

| 方法名称       | 参数类型                           | 参数说明                                                     |
| -------------- | ---------------------------------- | ------------------------------------------------------------ |
| ajaxStart()    | function                           | 规定当 AJAX 请求开始时运行的函数                             |
| ajaxStop()     | function                           | 规定当 AJAX 请求结束时运行的函数                             |
| ajaxComplete() | function(event, xhr, options)      | 规定当 AJAX 请求完成时运行的函数<br />额外的参数：<br />event：包含 event 对象<br />xhr：包含 XMLHttpRequest 对象<br />options：包含 AJAX 请求中使用的选项 |
| ajaxError()    | function(event, xhr, options, exc) | 规定当请求失败时运行的函数。<br />额外的参数：<br />event：包含 event 对象<br />xhr：包含 XMLHttpRequest 对象<br />options：包含 AJAX 请求中使用的选项<br />exc：包含 JavaScript exception |
| ajaxSend()     | function(event, xhr, options)      | 规定请求即将发送时运行的函数。<br />额外的参数：<br />event：包含 event 对象<br />xhr：包含 XMLHttpRequest 对象<br />options：包含 AJAX 请求中使用的选项 |
| ajaxSuccess()  | function(event, xhr, options)      | 规定当请求成功时运行的函数。<br />额外的参数：<br />event：包含 event 对象<br />xhr：包含 XMLHttpRequest 对象<br />options：包含 AJAX 请求中使用的选项 |


