为了让一个页面同时显示和处理表单，必须使用一个条件语句检查应该采取哪种动作（显示或处理）：

```php
if (/* form has been submitted */) {
    // Handle the form.
} else {
    // Display the form.
}
```

接下来的问题是判断表单是否已经提交，如果表单使用 POST 方法并且提交回原表单，那么脚本会产生两类请求。第一个是加载表单的 GET 请求。这是大多数页面生成的标准请求。当表单提交后，会产生第二个请求 —— POST。你可以通过检查请求方法（ $\_SERVER 数组）判断表单提交状态：

```php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Handle the form.
} else {
    // Display thee form.
}
```

如果想让页面处理表单，然后再次显示它，则可省略 else 子句：

```php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Handle the form.
}
```


