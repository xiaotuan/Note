### 6.3.2　 `progressbar ("action", params)` 方法

`progressbar ("action", params)` 方法能操作进度条，比如更改填充的百分比。第一个参数 `"action"` 是一个字符串，指定是什么操作（比如， `"value"` 表示改变填充的百分比）。表6-2描述了该方法的选项。

<center class="my_markdown"><b class="my_markdown">表6-2　 `progressbar("action", params)` 方法的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `progressbar("value")` | 获取 `options.value` 的当前值，即进度条的填充百分比 |
| `progressbar("value",`   `value)` | 指定一个新的进度条填充百分比值 |
| `progressbar("option",`   `param)` | 获得指定 `param` 选项的值。该选项是 `progressbar`   `(options)` 方法中使用的某个选项 |
| `progressbar("option",`   `param,`   `value)` | 更改 `param` 选项的值。该选项是 `progressbar`   `(options)` 方法中使用的某个选项 |
| `progressbar("destroy")` | 移除进度条管理。进度条变成没有CSS类和事件管理的简单HTML |

