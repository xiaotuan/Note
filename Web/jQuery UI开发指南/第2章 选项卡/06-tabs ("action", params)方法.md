### 2.3.2　 `tabs ("action", params)` 方法

和前面的 `tabs (options)` 方法不同，这个新形式的方法能在创建选项卡后修改选项卡的行为。

`tabs ("action", params)` 方法允许通过JavaScript程序操作选项卡，比如选择、禁用、添加或者删除选项卡。第一个参数是一个字符串，指定是什么操作（例如， `"add"` 表示添加选项卡），随后的是和这个操作有关的参数（例如，选项卡的索引）。

调用这些方法有时会引起一个和操作同名的事件发生（ `add` 事件由 `"add"` 这个操作触发）。这些在 `options` 中处理的事件已经讨论过了，表2-3列出了可以执行的 操作。

<center class="my_markdown"><b class="my_markdown">表2-3　 `tabs ("action",params)` 方法的操作</b></center>

| 方法 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `tabs ("add", "#id",`   `title, index)` | 在 `index` 指定的位置（从0开始）添加选项卡。该添加的选项卡后面的选项卡的索引号增1。 `"#id"`  是和这个选项卡内容相关的 `<div>` 元素的 `id` （ `<div>` 由jQuery UI创建时，它的内容应稍后再添加）； `title` 参数是选项卡的标题；如果未指定 `index` 参数，选项卡会被添加在列表的末尾 |
| `tabs ("remove", index)` | 移除指定的选项卡及其内容 |
| `tabs ("disable", index)` | 禁用指定的选项卡 |
| `tabs ("enable", index)` | 激活指定的选项卡 |
| `tabs ("select", index)` | 选中指定的选项卡，该选项卡的内容变得可见 |
| `tabs ("url", index, url)` | 将选项卡的内容和由 `url` 参数指定的URL联系起来。这会调用 `tabs ("load", index)` 方法，通过Ajax方式来获取选项卡的内容 |
| `tabs ("load", index)` | 根据 `tabs ("url", index, url)` 中的 `url` 参数指定的URL，通过Ajax方式获取选项卡的内容 |
| `tabs ("rotate",`   `duration, repeat)` | 按指定的时间周期 `duration` （以毫秒为单位），定期选中每个选项卡。如果 `repeat` 为 `true` ，则重复周期，否则只执行一遍（默认） |
| `tabs ("destroy")` | 移除选项卡管理。选项卡再次成了没有CSS类和事件管理的简单HTML |
| `tabs ("length")` | 返回由选择器选取的结果集中的第一个元素中的选项卡个数 |

