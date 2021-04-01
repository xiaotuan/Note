### 4.4　在对话框中使用 `bind ()` 处理事件

除了可以在 `dialog (options)` 方法的选项中使用事件外，还可以使用 `bind ()` 方法来管理这些事件。

有了这些事件，就可以利用 `bind (eventName, callback)` 提供的回调方法，完成一些处理工作。

表4-9描述了使用 `bind ()` 方法来管理对话框的事件。

<center class="my_markdown"><b class="my_markdown">表4-9　使用 `bind ()` 方法来管理对话框的jQuery UI事件</b></center>

| 事件 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `dialogfocus` | 等同于 `options.focus` |
| `dialogopen` | 等同于 `options.open` |
| `dialogbeforeclose` | 等同于 `options.beforeclose` |
| `dialogclose` | 等同于 `options.close` |
| `dialogdrag` | 等同于 `options.drag` |
| `dialogdragstart` | 等同于 `options.dragstart` |
| `dialogdragstop` | 等同于 `options.dragstop` |
| `dialogresize` | 等同于 `options.resize` |
| `dialogresizestart` | 等同于 `options.resizestart` |
| `dialogresizestop` | 等同于 `options.resizestop` |

