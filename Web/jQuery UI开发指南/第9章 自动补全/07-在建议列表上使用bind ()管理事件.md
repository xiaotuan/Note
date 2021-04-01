### 9.4　在建议列表上使用 `bind ()` 管理事件

除了 `autocomplete (options)` 方法中的 `options` 参数提供的事件方法，jQuery UI还允许我们使用 `bind ()` 方法来管理这些事件（详见表9-4）。

<center class="my_markdown"><b class="my_markdown">表9-4　jQuery UI创建的事件</b></center>

| 事件 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `autocompleteopen` | 等同于 `options.open` |
| `autocompleteclose` | 等同于 `options.close` |
| `autocompletesearch` | 等同于 `options.search` |
| `autocompletefocus` | 等同于 `options.focus` |
| `autocompleteselect` | 等同于 `options.select` |
| `autocompletechange` | 等同于 `options.change` |

