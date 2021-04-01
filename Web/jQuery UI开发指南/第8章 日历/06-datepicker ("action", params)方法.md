### 8.3.2　 `datepicker ("action", params)` 方法

`datepicker ("action", params)` 方法能操作日历，比如选择新的日期。第一个参数 `"action"` 是一个字符串，指定是什么操作（比如， `"show"` 表示显示日历）。表8-9列出了可用的操作。

<center class="my_markdown"><b class="my_markdown">表8-9　 `datepicker ("action", params)` 方法的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `datepicker ("show")` | 显示日历 |
| `datepicker ("hide")` | 隐藏日历 |
| `datepicker ("getDate")` | 返回选择的日期的Date对象。如果没有指定日期格式（ `options.dateFormat` ），即使已经引入了一个国家的JavaScript语言文件，日期也以mm/ dd/yy形式表示。如果想使用 `datepicker`   `("getDate")` 获得不是英文格式的日期，请确保始终指定了 `options.dateFormat` 选项 |
| `datepicker ("setDate",`   `date)` | 初始化日历的预设日期。 `date` 参数是上面已经提到过的表示形式（Date对象、当前日期之前或之后的天数或者是字符串）。如果没有指定日期格式（ `options.`   `dateFormat` ），即使已经引入了一个国家的JavaScript语言文件，日期也以mm/ dd/yy形式表示。如果想使用 `datepicker`   `("setDate"` )设置不是英文格式的日期，请确保始终指定了 `options.dateFormat` 选项 |
| `Datepicker ("option",`   `param)` | 获取指定的 `param` 选项的值。该选项对应 `datepicker`   `(options)` 方法中使用的某个选项 |
| `datepicker ("option",`   `param, value)` | 更改指定的 `param` 选项的值。该选项对应 `datepicker`   `(options)` 方法中使用的某个选项 |
| `datepicker ("destroy")` | 移除日历管理。日历变成没有CSS类和事件管理的简单HTML |

