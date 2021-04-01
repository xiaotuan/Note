### 2.3.1　 `tabs (options)` 方法

`tabs(options)` 方法声明把一个HTML元素（及其内容）当作选项卡来管理。 `options` 参数是一个对象，用来指定选项卡的外观及行为。 `options` 参数有不同类型的值，它们要么是直接用于管理选项卡，要么就是管理和选项卡有关的事件。

#### 1．选项卡的外观和行为

表2-1描述了修改选项卡的外观和行为的选项。

<center class="my_markdown"><b class="my_markdown">表2-1　管理选项卡的外观和行为的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.collapsible` | 当设置为 `true` 时，允许取消选中选项卡。当设置为 `false` （默认值）时，单击选中的选项卡不会取消选中（它仍然被选中） |
| `options.disabled` | 使用一个数组来指定禁用的选项卡的索引（因此不能选中）。比如，用[0,1]来禁用前两个选项卡 |
| `options.selected` | 指定首次选中的选项卡索引。默认为0，表示页面中的第一个选项卡 |
| `options.event` | 让用户选中新选项卡的事件的名称（默认是" `click` "）。例如，如果此选项设置为" `mouseover` "，则当鼠标光标移至选项卡时，就会选中该选项卡 |
| `options.fx` | 指定伴随选择选项卡时的特效，比如渐进地显示选项卡及其内容（指定 `options.fx = {{opacity:`   `"toggle"}}` ） |
| `options.ajaxOptions` | 指定Ajax的选项（通过Ajax来更新选项卡的内容）。比如， `options.ajaxOptions.data` 可以指定发送给服务器的参数 |

#### 2．管理与选项卡相关的事件

有些选项可用于管理选项卡，如选择、添加和删除选项卡。这些选项（表2-2列出的）接收 `event` 参数，随后的参数是发生事件的 `tab` 对象。这个 `tab` 对象由以下属性组成：

+ `index` ，发生事件的选项卡的索引（0表示第一个选项卡）：
+ `panel` ，对应选项卡内容的 `<div>` 元素。

<center class="my_markdown"><b class="my_markdown">表2-2　管理选项卡的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.select` | `select (event, tab)` 方法在选中选项卡时会被调用（要么手动选中，要么调用 `tabs ("select")` 方法） |
| `options.show` | `show (event, tab)` 方法在选项卡的内容变得可见时会被调用（手动选中、首次显示选中的选项卡时或者调用 `tabs ("select")` 方法） |
| `options.add` | `add (event, tab)` 方法在添加选项卡时会被调用（调用 `tabs ("add")` 方法） |
| `options.remove` | `remove (event, tab)` 方法在删除选项卡时会被调用（调用 `tabs ("remove")` 方法） |
| `options.enable` | `enable (event, tab)` 方法在激活选项卡时会被调用（调用 `tabs ("enable")` 方法） |
| `options.disable` | `disable (event, tab)` 方法在禁用选项卡时会被调用（调用 `tabs ("disable")` 方法） |
| `options.load` | `load (event, tab)` 方法在使用Ajax加载或查看选项卡的内容时会被调用（调用 `tab ("load")` 方法） |

