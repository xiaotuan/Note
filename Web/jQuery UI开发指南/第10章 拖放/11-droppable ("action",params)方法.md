### 10.4.2　 `droppable ("action",params)` 方法

`droppable ("action", params)` 方法会对保管元素执行一个操作，如禁止放置。具体的操作被指定为一个字符串，在第一个参数中指定（比如，使用 `"disable"` 来禁止放置）。表10-15中列出了这个方法可用的一些操作。

<center class="my_markdown"><b class="my_markdown">表10-15　 `droppable ("action", params)` 方法可用的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `droppable ("disable")` | 禁用放置操作。元素不再是保管元素 |
| `droppable ("enable")` | 重新激活放置操作。元素恢复为保管元素 |
| `droppable ("option",`   `param)` | 获取指定的 `param` 选项的值。该选项对应 `droppable`   `(options)` 方法中使用的某个选项 |
| `droppable ("option",`   `param,value)` | 更改指定的 `param` 选项的值。该选项对应 `droppable`   `(options)` 方法中使用的某个选项 |
| `droppable ("destroy")` | 移除放置管理。元素不再是保管元素 |

