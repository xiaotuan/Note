### 10.1.2　 `draggable ("action", params)` 方法

`draggable ("action",params)` 方法会对可移动元素执行一个操作，如禁止移动。具体的操作被指定为一个字符串，在第一个参数中指定（比如，使用 `"disable"` 来禁止拖放）。表10-8中列出了这个方法可用的一些操作。

<center class="my_markdown"><b class="my_markdown">表10-8　 `draggable("action", params)` 方法可用的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `draggable ("disable")` | 禁用拖动管理。在重新调用 `draggable`   `("enable")` 方法之前元素不能再被移动 |
| `draggable ("enable")` | 重新激活拖动管理。元素可以再次被拖动 |
| `draggable ("option",`   `param)` | 获取指定的 `param` 选项的值。该选项对应 `draggable`   `(options)` 方法中使用的某个选项 |
| `draggable ("option",`   `params, value)` | 更改指定的 `param` 选项的值。该选项对应 `draggable`   `(options)` 方法中使用的某个选项 |
| `draggable ("destroy")` | 移除拖动管理。元素将无法再被移动 |

