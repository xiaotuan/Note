在 HTML 的表单元素中，还有一个 `id` 标记。这个标记是较为特殊的标记，它主要用于标记一个唯一的元素。这个元素可以是文字字段、密码域、其他的表单元素，甚至也可以定义一幅图像、一个表格。但是在实际应用中，表单是使用 `id` 标记最多的一类元素。

**语法：**

```html
<id="元素的标识名"></id>
```

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

