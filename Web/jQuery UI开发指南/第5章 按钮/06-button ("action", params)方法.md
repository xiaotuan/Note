### 5.3.2　 `button ("action", params)` 方法

`button ("action", params)` 方法能操作按钮，比如禁用按钮或者更改按钮文字。第一个参数 `"action"` 是一个字符串，指定是什么操作（比如， `"disable"` 表示禁用按钮）。表5-2描述该方法可用的操作。

<center class="my_markdown"><b class="my_markdown">表5-2　 `button ("action", params)` 方法的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `button("disable")` | 禁用按钮 |
| `button("enable")` | 启用按钮 |
| `button("refresh")` | 更新按钮布局。当用程序操作了按钮，按钮的显示状态未必和内部状态一致，这时该方法就很有用了 |
| `button("option",`   `param)` | 获得指定 `param` 选项的值。该选项是在 `button`   `(options)` 方法中使用的某个选项 |
| `button("option",`   `param,`   `value)` | 更改 `param` 选项的值。该选项是在 `button`   `(options)` 方法中使用的某个选项 |
| `button("destroy")` | 移除按钮管理。按钮变成没有CSS类和事件管理的简单HTML |

