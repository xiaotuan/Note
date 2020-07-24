**表8-1 错误报告等级**

| 编号 | 常量 | 报告 |
| :-: |:- |:- |
| 1 | E_ERROR | 致命的运行时错误（它会阻止脚本的执行）|
| 2 | E_WARNING | 运行时警告（非致命的错误） |
| 4 | E_PARSE | 解析错误 |
| 8 | E_NOTICE | 注意（事情可能是或者可能不是一个问题） |
| 256 | E_USER_ERROR | 用户生成的错误消息，由 trigger_error() 函数生成 |
| 512 | E_USER_WARNING | 用户生成的警告，由 trigger_error() 函数生成 |
| 1024 | E_USER_NOTICE | 用户生成的注意，由 trigger_error() 函数生成 |
| 2048 | E_STRICT | 关于兼容性和互操作性的建议 |
| 8192 | E_DEPR_ECATED | 警告无法在未来 PHP 版本中使用的代码 |
| 30719 | E_ALL | 所有的错误、警告和建议 |

可以使用 error_reporting() 函数基于各个脚本来调整这种行为。

```php
error_reporting(0);	// Show no errors.
```

设置为 0 会完全关闭错误报告。`error_repoting(E_ALL)` 将会向 PHP 报告发生的每个错误。 可以添加一些编号来自定义错误报告的级别，或者可以把位运算符 [|(或)、~(非)、&(与)] 和常量一起使用。

```php
error_reporting(E_ALL & !E_NOTICE);
```

**提示**

+ 上表中 E_ALL 的数值会根据 PHP 的版本发生变化。
+ 由于你通常希望为 Web 站点中的每个页面调整 display_errors 和 error_reeporting，你可能想把这几行代码放在单独的 PHP 文件中，然后可以由任何 PHP 脚本包含它。
+ `trigger_error()` 函数是一种通过编程在 PHP 脚本中生成一个错误的方法。它的第一个参数是错误信息，第二个可选参数是数值类型的错误类型。默认的类型是 E_USER。

```php
if (/* some condition */) {
    trigger_error('Something Bad Happened!');
}
```

