HTML 表单是使用 form 标签和多种用于获取输出的元素创建的。form 标签看起来如下：

```html
<form action="script.php" method="post">
</form>
```

PHP 脚本把接收到的信息存储在特殊的变量中，例如，假定你有一个表单，其中有一个输入，定义如下：

```html
<input type="text" name="city" />
```

无论用户用户在该元素中输入什么内容，都可以通过一个名为 `$_REQUEST['city']` 或者 `$_POST['city']` 的 PHP 变量访问它。使拼写和大小写完全匹配非常重要。

如果在安装 PHP 时启用 Magic Quotes，当 PHP 脚本打印出表单数据时，你将看到这些反斜杠。可以使用 `stripslashes()` 函数撤销它的作用：

```php
$var = stripslashes($var);
```
