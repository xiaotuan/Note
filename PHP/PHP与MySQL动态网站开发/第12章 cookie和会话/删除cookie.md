如果发送一个包含名称但没有值的 cookie，其效果就相当于删除现有的同名 cookie。

```php
setcookie('first_name', 'Tyler');
```

要删除 first_name cookie，可以编写如下代码：

```php
setcookie('first_name');
```

一种附加的预防措施，还可以把到期日期设置成过去的某个日期：

```php
setcookie('first_name', '', time() - 3600);
```

