### 4.3.2　 `dialog ("action", params)` 方法

`dialog("action", params)` 方法能操作对话框，比如打开或关闭。第一个参数 `"action"` 是一个字符串，指定是什么操作（比如， `"open"` 表示打开对话框窗口）。

表4-8描述了使用该方法时可以执行的操作。

<center class="my_markdown"><b class="my_markdown">表4-8　 `dialog ("action", params)` 方法的操作</b></center>

| 方法 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `dialog ("open")` | 打开对话框 |
| `dialog ("close")` | 关闭对话框。然后对话框隐藏，可以用 `dialog`   `("open")` 重新打开 |
| `dialog ("destroy")` | 删除对话框管理。对话框恢复为没有CSS类和事件管理的简单HTML并在页面中隐藏了 |
| `dialog ("disable")` | 使对话框看起来像是被禁用，实际上却没有禁用。对话框的一些元素（标题栏、内容、边框）仍然可用 |
| `dialog ("enable")` | 恢复对话框元素的标准外观 |
| `dialog ("isOpen")` | 如果对话框列表中有一个是打开的，返回 `true` ，否则返回 `false` |
| `dialog ("moveToTop")` | 将相应的对话框定位在“前景”位置（在其他对话框之上） |
| `dialog ("option",`   `param)` | 获取指定的 `param` 选项的值。该选项对应在 `dialog`   `("options")` 方法中使用的某个选项 |
| `dialog ("option", param,`   `value)` | 更改 `param` 选项的值。该选项对应在 `dialog`   `("options")` 方法中使用的某个选项 |

