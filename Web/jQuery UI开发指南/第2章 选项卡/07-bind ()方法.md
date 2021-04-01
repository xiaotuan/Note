### 2.4　 `bind ()` 方法

除了在 `tabs (options)` 方法的选项中使用事件方法外，jQuery UI还支持使用 `bind ()` 方法来管理这些事件。jQuery UI为选项卡创建了不同的事件，在表2-4列出。

<center class="my_markdown"><b class="my_markdown">表2-4　管理选项卡的jQuery UI事件</b></center>

| 事件 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `tabsselect` | 选中了选项卡（手动选中或者使用 `tabs ("select")` 方法） |
| `tabsshow` | 选项卡内容变得可见了（手动选中、首次显示选中的选项卡时或者调用  `tabs ("select")` 方法） |
| `tabsadd` | 添加了选项卡（调用 `tabs ("add")` 方法） |
| `tabsremove` | 移除了选项卡（调用 `tabs ("remove")` 方法） |
| `tabsenable` | 激活了选项卡（调用 `tabs ("enable")` 方法） |
| `tabsdisable` | 禁用了选项卡（调用 `tabs ("disable")` 方法） |
| `tabsload` | 选项卡的内容已通过Ajax加载完成了（调用 `tabs ("load")` 方法） |

有了这些事件，就可以利用 `bind (eventName, callback)` 提供的回调方法，完成一些处理工作。

