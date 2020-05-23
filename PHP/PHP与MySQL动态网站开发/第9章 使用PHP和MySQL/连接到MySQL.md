连接 MySQL 的代码格式如下：

```php
$dbc = mysqli_connect(hostname, username, password, db_name);
```

例如：

```php
// Set the database access information as constants:
DEFINE ('DB_USER', 'username');
DEFINE ('DB_PASSWORD', 'password');
DEFINE ('DB_HOST', 'localhost');
DEFINE ('DB_NAME', 'sitename');

// Make the connection:
$dbc = @mysqli_connect (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) OR die ('Could not connect to MySQL: ' . mysqli_connect_error() );

// Set the encoding...
mysqli_set_charset($dbc, 'utf8');
```

在调用函数前面放置一个错误控制运算符（@），可以防止在 Web 浏览器中显示 PHP 错误。

> 建议把包含敏感的 MySQL访问信息的文件放在 web目录的上一级目录中，或者把它放在 Web 目录的外面。这样，就不能从 Web 浏览器访问该文件。

如果发生一个连接问题，可以调用 `mysqli_connect_error()`，它返回连接错误消息，它不带参数：

```php
mysqli_connect_error();
```

**提示**

+ 如果使用的 PHP 版本不支持 `mysqli_set_charset()` 函数，就需要执行 `SET NAMES *encoding*` 来代替：

```sql
mysqli_query($dbc, 'SET NAMES utf8');;
```

+ 如果接收到一个错误，声称 `mysqli_connect()` 是一个未定义的函数，这意味着没有包含对 `Improved MySQL Extension` 的支持来编译 PHP。
+ 在运行脚本时，如果看到 `Can't connect ...` 错误消息，它很可能意味着 MySQL 没有运行。
+ 如果在建立 MySQL 连接时不需要选择数据库，可以从 `mysqli_connect()` 函数中省略该参数：

```php
$dbc = mysqli_connect(hostname, username, password);
```

然后，在合适时，可以使用以下代码选择数据库：


```php
mysqli_select_db($dbc, db_name);
```
