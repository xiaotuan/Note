### 3.3.2　 `accordion ("action", params)` 方法

`accordion ("action", params)` 方法允许操作菜单，比如选中或取消选中菜单。第一个参数是一个字符串，指定是什么操作（例如， `"activate"` 表示选中新菜单），随后的是和该操作有关的参数（例如，菜单的索引）。表3-4列出了该方法的一些操作。

<center class="my_markdown"><b class="my_markdown">表3-4　 `accordion ("action",params)` 方法的操作</b></center>

| 方法 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `accordion ("activate", index)` | 选中指定的菜单 |
| `accordion ("disable")` | 禁用所有菜单。任何单击都是无效的 |
| `accordion ("enable")` | 重新激活所有菜单。单击又有效了 |
| `accordion ("destroy")` | 移除菜单管理。菜单再次成了没有CSS类和事件管理的简单HTML |

