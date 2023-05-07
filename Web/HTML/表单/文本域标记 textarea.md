文本域标记与文字字段的区别在于可以添加多行文字，从而可以输入更多的文本。这类控件在一些留言本中最为常见。

**语法：**

```html
<textarea name="文本域名称" value="文本域默认值" rows="行数" cols="列数"></textarea>
```

<center><b>文本域标记属性</b></center>

| 文本域标记属性 | 描述         | 文本域标记属性 | 描述           |
| -------------- | ------------ | -------------- | -------------- |
| name           | 文本域的名称 | cols           | 文本域的列表   |
| rows           | 文本域的行数 | value          | 文本域的默认值 |

**示例代码：**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>添加文本域</title>
</head>
<body>
用户调查留言：<br /><br />
<form action="mailto:mingrisoft@mingrisoft.com" name="invest" method="post">
    用户名：<input name="username" type="text" size="20" id="username" /><br /><br />
    密码：<input name="passworg" type="password" size="20" /><br /><br />
    留言：<textarea name="liuyan"  rows="5" cols="40">
    </textarea><br /><br />
    <input type="submit" name="submit" value="提交" />
</form>
</body>
</html>
```

![14](./images/14.png)