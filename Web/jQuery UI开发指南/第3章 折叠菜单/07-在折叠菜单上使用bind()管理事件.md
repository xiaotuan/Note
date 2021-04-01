### 3.4　在折叠菜单上使用 `bind()` 管理事件

除了在 `accordion (options)` 方法的选项中使用事件方法外，jQuery UI还支持使用 `bind ()` 方法来管理这些事件。jQuery UI为折叠菜单创建了不同的事件，如表3-5所示。

<center class="my_markdown"><b class="my_markdown">表3-5　管理 `accordion` 菜单的jQuery UI事件</b></center>

| 事件 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `accordionchange` | 同 `options.change` （见表3-3） |
| `accordionchangestart` | 同 `options.changestart` （见表3-3） |

有了这些事件，就可以利用 `bind (eventName, callback)` 提供的回调方法，执行处理一些事情。

