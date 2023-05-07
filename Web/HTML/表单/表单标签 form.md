[toc]

在 HTML 中，`<form></form>` 标记对用来创建一个表单，即定义表单的开始和结束位置，在标记对之间的一切都属于表单的内容。

### 1. 处理动作 —— action

语法：

```html
<form action="表单的处理程序">
    ......
</form>
```

表单的处理程序定义的是表单要提交的地址，也就是表单中收集到的资料将要传递的程序地址。这一地址可以是绝对地址，也可以是相对地址，还可以是一些其他的地址形式，如 E-mail 地址等。

示例代码：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>设定表单的处理程序</title>
    </head>
    <body>
        <!-- 这是一个没有控件的表单 -->
        <form action="mail:mingri@qq.com">
            
        </form>
    </body>
</html>
```

### 2. 表单名称—— name

名称属性 `name` 用于给表单命名。这一属性不是表单的必须属性，但是为了防止表单信息在提交到后台处理程序时出现混乱，一般要设置一个与表单功能符合的名称。

语法：

```html
<form name="表单名称">
    ......
</form>
```

> 注意：表单名称找那个不能包含特殊符号和空格。

示例代码：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>插入密码域</title>
</head>
<body>
<h1>用户调查</h1>
<form action="mail;mingri@qq.com" method="get" name="register">
    姓名：<input type="text" name="usernamr" size="20" />
    <br /><br />
    密码：<input  type="password" name="password" size="20" maxlength="8" />
    <br /><br />
    确认密码：<input type="password" name="qupassword" size="20" maxlength="8" />
</form>
</body>
</html>
```

### 3. 传送方法—— method

表单的 `method` 属性用来定义处理程序从表单中获得信息的方式，可取值为 `get` 或 `post`，它决定了表单中已收集的数据是用什么方法发送到服务器的。　

+ `method=get` ：使用这个设置时，表单数据会被视为 CGI 或 ASP 的参数发送，也就是来访者输入的数据会附加在 URL 之后，由用户端直接发送至服务器，所以速度上会比 `post` 快，但缺点是数据长度不能够太长。在没有指定 `method` 的情形下，一般都会视 `get` 为默认值。　

+ `method=post` ：使用这种设置时，表单数据是与 URL 分开发送的，用户端的计算机会通知服务器来读取数据，所以通常没有数据长度上的限制，缺点是速度上会比 `get` 慢。

**语法：**

```html
<form method="传送方式">
    ......
</form>
```

传送方式的值只有两种选择，即 `get` 或 `post`。

**示例代码：**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>插入密码域</title>
</head>
<body>
<h1>用户调查</h1>
<form action="mail;mingri@qq.com" method="get" name="register">
    姓名：<input type="text" name="usernamr" size="20" />
    <br /><br />
    密码：<input  type="password" name="password" size="20" maxlength="8" />
    <br /><br />
    确认密码：<input type="password" name="qupassword" size="20" maxlength="8" />
</form>
</body>
</html>
```

### 4. 编码方式—— enctype

表单中的 `enctype` 参数用于设置表单信息提交的编码方式。

**语法：**

```html
<form enctype="编码方式">
    ......
</form>
```

`enctype` 属性为表单定义了 MIME 编码方式，编码方式的取值如下所示：

| enctype 取值                      | 取值的含义                            |
| --------------------------------- | ------------------------------------- |
| text/plain                        | 以纯文本的形式传送                    |
| application/x-www-form-urlencoded | 默认的编码形式                        |
| multipart/form-data               | MIME 编码，上传文件的表单必须选择该项 |

**示例代码：**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>设定表单的编码方式</title>
    </head>
    <body>
        <!-- 这是一个没有控件的表单 -->
        <form action="mail:mingri@qq.com" name="register" method="post" enctype="text/plain">
            
        </form>
    </body>
</html>
```

### 5. 目标显示方式—— target

`target` 属性用来指定目标窗口的打开方式。表单的目标窗口往往用来显示表单的返回信息，例如是否成功提交了表单的内容、是否出错等。

**语法：**

```html
<form target="目标窗口的打开方式">
    ......
</form>
```

目标窗口的打开方式包含4个取值：`_blank`、`_parent`、`_self` 和 `_top`。其中，`_blank` 是指将返回信息显示在新打开的窗口中；`_parent` 是指将返回信息显示在父级的浏览器窗口中；`_self` 则表示将返回信息显示在当前浏览器窗口中；`_top` 表示将返回信息显示在顶级浏览器窗口中。

**示例代码：**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>设定木条窗口的打开方式</title>
    </head>
    <body>
        <form action="mail:mingri@qq.com" name="register" method="post" enctype="text/plain" target="_self">
            
        </form>
    </body>
</html>
```



