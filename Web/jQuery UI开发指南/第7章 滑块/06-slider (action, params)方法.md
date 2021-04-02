### 7.3.2　 `slider ("action", params)` 方法

`slider ("action", params)` 方法（如表7-4所描述的）能操作滑块，比如，把游标移动到一个新的位置。第一个参数 `"action"` 是一个字符串，指定是什么操作（比如， `"value"` 表示指定游标新的值）。

<center class="my_markdown"><b class="my_markdown">表7-4　 `slider("action", params)` 方法的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `slider ("disable")` | 禁用滑块功能。在其上单击无效 |
| `slider ("enable")` | 激活滑块功能。在其上单击重新有效 |
| `slider ("value")` | 获取 `option.value` （游标）的当前值。在只有一个游标时使用该方法（如果游标不止一个，请用 `slider("values")` 方法） |
| `slider ("value",`   `value)` | 更改游标的值。在只有一个游标时使用该方法（否则请用 `slider("values", values)` 方法） |
| `slider ("values")` | 获得 `options.values` 的当前值（包括所有游标的值，是个数组） |
| `slider ("values",`   `values)` | 给所有游标赋予新的值，是个数组 |
| `slider ("option",`   `param)` | 获得指定 `param` 选项的值。该选项是 `slider(options)` 方法中使用的某个选项 |
| `slider ("option",`   `param, value)` | 更改指定param选项的值。该选项是 `slider(options)` 方法中使用的某个选项 |
| `slider ("destroy")` | 移除滑块管理。滑块变成没有CSS类和事件管理的简单HTML |

