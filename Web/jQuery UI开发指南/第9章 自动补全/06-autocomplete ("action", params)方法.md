### 9.3.2　 `autocomplete ("action", params)` 方法

使用 `autocomplete ("action",params)` 方法会对建议列表执行一个操作，如显示或隐藏。具体操作是一个字符串，在第一个参数中指定（比如，使用 `"close"` 来隐藏列表）。表9-3中列出了这些操作。

<center class="my_markdown"><b class="my_markdown">表9-3　 `autocomplete ("action", params)` 方法操作</b></center>

| 行为 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `autocomplete ("disable")` | 禁用自动补全机制。建议列表将不再显示 |
| `autocomplete ("enable")` | 重新激活自动补全机制。建议列表将再次显示 |
| `autocomplete ("search",`   `value)` | 在数据源（在 `options.source` 中指定）中搜索匹配字符串 `value` 。字符串 `value` 需要达到最少字符数（在 `options.minLength` 中指定），否则搜索不会执行。一旦匹配出一个建议列表，即会将相应项列出 |
| `autocomplete ("close")` | 隐藏建议列表 |
| `autocomplete("widget")` | 获取建议列表对应的 `<ul>` DOM元素。这是一个可以简便地访问列表的jQuery类对象，而不需要使用jQuery选择器 |
| `autocomplete("option",`   `param)` | 获取指定的 `Param` 选项的值。该选项对应 `autocomplete`   `(options)` 中使用的某个选项 |
| `autocomplete("option",`   `param, value)` | 改变 `param` 选项的值。该选项对应 `autocomplete`   `(options)` 中使用的某个选项 |
| `autocomplete ("destroy")` | 移除自动补全管理。建议列表被删除 |

