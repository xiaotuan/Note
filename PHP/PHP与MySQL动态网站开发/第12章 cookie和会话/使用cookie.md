通过 `setcookie()` 函数发送 cookie：

```php
setcookie(name, value);
setcookie('name', 'Nicole');
```

在给 cookie 命名时，不要使用空格或标点符号，但是，要特别注意使用正确的大小写字母。

> 提示：
> + cookiee 被限制为总共包含大约 4 KB 的数据，每个 Web 浏览器可以记住来自任何一个站点的有限数据的 cookie。对于目前的大多数 Web 浏览器，这个限制是 50 个 cookie。
> + 因为不同的浏览器将以不同的方式处理 cookie，PHP 中有几个函数可以在不同的浏览器中生成不同的结果， setcookie() 函数是其中之一。一定要在不同平台上的多个浏览器中测试你的 Web 站点，以确保一致性。

