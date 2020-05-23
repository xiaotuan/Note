利用 PHP 脚本来更新数据库记录，需要使用 UPDATE 查询，并且可以利用 PHP 的 `mysqli_affected_rows()` 函数来验证查询的成功执行。`mysqli_affected_rows()` 函数会返回受 INSERT、UPDATE 或 DELETE 查询影响的行数。其用法如下：

```php
$num = mysqli_affected_rows($dbc);
```

**提示**

+ 如果使用命令 `TRUNCATE tablename` 从表中删除所有记录，则 mysqli_affected_rows() 会返回 0，即使查询成功执行并且删除了每一行。这只是一种古怪的行为。
+ 如果运行 UPDATE 查询，但是实质上没有更改任意列的值，则 `mysqli_affected_rows()` 会返回 0。