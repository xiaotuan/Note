### 13.3.2　 `resizable ("action", params)` 方法

`resizable ("action", params)` 方法会对可缩放元素执行一个操作，如允许或禁止缩放。具体的操作被指定为一个字符串，在第一个参数中指定（比如，使用 `"disable"` 来禁止缩放操作）。表13-8中列出了这些可用的操作。

<center class="my_markdown"><b class="my_markdown">表13-8　 `resizable("action",params)` 方法可用的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `resizable ("disable")` | 禁止缩放操作 |
| `resizable ("enable")` | 重新激活缩放操作 |
| `resizable ("option",`   `param)` | 获取指定的 `param` 选项的值。该选项对应 `resizable`   `(options)` 方法中使用的某个选项 |
| `resizable ("option",`   `param, value)` | 更改指定的 `param` 选项的值。该选项对应 `resizable`   `(options)` 方法中使用的某个选项 |
| `resizable ("destory")` | 移除缩放管理 |

