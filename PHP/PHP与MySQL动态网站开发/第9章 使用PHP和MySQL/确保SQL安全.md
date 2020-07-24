关于 PHP 的数据库安全可归结为三大类问题：

1. 保护 MySQL 访问信息；
2. 不要呈现关于数据库的过多信息；
3. 在运行查询时要小心谨慎，对于那些涉及用户提交数据的查询尤其需要这样。

可以通过确保 Web 目录外面的 MySQL 连接脚本的安全来达到第一个目标。通过不允许用户查看 PHP 的出错消息或者你的查询来达到第二个目标。

对于第三个目标，可以并且应该采用许多步骤来达到，它们都基于永远不要信任用户提供的数据这个前提。第一，验证提交了某个值，或者验证它是否具有正确的类型（数字、字符串等）。第二，使用正则表达式确保提交的数据与你所期待的匹配。第三，可以强制转换某些值的类型以保证它们是数字。第四，通过 `mysqli_real_escape_string()` 函数处理用户提交的数据。这个函数通过转义那些可能有问题的字符来清理数据，其用法如下：

```php
$safe = mysqli_real_escape_string($dbc, _data_);
```

**提示**

+ 如果看到下面的错误信息，则意味着 `mysqli_real_escape_string()` 函数不能访问数据库。

```
Notic: Undefined variable: dbc in C:\xampp\htdocs\register.php on line 18
Warning: mysqli_real_escape_string() expects parameter 1 to be mysqli, null given in C:\xampp\htdocs\register.php online 18
```

+ 如果在服务器上启用 Magic Quotes，那么在使用 `mysqli_real_escape_string()` 函数之前，需要删除 Magic Quotes 添加的任何斜杠。代码如下：

```php
$fn = mysqli_real_escaape_string($dbc, trim(stripslashes($_POST['first_name'])));
```
