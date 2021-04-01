### 12.3.2　 `sortable("action",params)` 方法

`sortable("action",params)` 方法会对可调换元素执行一个操作，如允许它们移动。具体的操作被指定为一个字符串，在第一个参数中指定（比如，使用 `"disable"` 来禁止操作）。表12-12中列出了这个方法可用的一些操作。

<center class="my_markdown"><b class="my_markdown">表12-12　 `sortable ("action", params)` 方法可用的操作</b></center>

| 操作 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `sortable ("disable")` | 禁止调换元素 |
| `sortable ("enable")` | 重新激活元素调换操作 |
| `sortable ("refresh")` | 必要的情况下刷新列表元素 |
| `sortable ("serialize")` | 返回对应整个列表的序列化字符串。可以用在Ajax的请求参数中 |
| `sortable ("toArray")` | 以数组的形式返回列表元素的 `id` ，若没有 `id` 则返回空字符串 |
| `sortable ("option",`   `param)` | 获取指定的 `param` 选项的值。该选项对应 `sortable`   `(options)` 方法中使用的某个选项 |
| `sortable ("option",`   `param, value)` | 更改指定的 `param` 选项的值。该选项对应 `sortable`   `(options)` 方法中使用的某个选项 |
| `sortable ("destroy")` | 移除元素调换管理 |

