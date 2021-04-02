### 11.3.2　 `selectable ("action",params)` 方法

`selectable ("action",params)` 方法可以对可选择元素执行某些操作，例如允许选择操作。具体的操作被指定为一个字符串，在第一个参数中指定（比如，使用 `"disable"` 来禁止操作）。表11-3中列出了这些可用的操作。

<center class="my_markdown"><b class="my_markdown">表11-3　 `selectable("action",params)` 方法可用的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `selectable ("disable")` | 禁止选择操作 |
| `selectable ("enable")` | 重新激活选择操作 |
| `selectable ("option",`   `param)` | 获取指定的 `param` 选项的值。该选项对应 `selectable`   `(options)` 方法中使用的某个选项 |
| `selectable ("option",`   `param,value)` | 更改指定的 `param` 选项的值。该选项对应 `selectable`   `(options)` 方法中使用的某个选项 |
| `selectable ("destroy")` | 移除选择管理 |

