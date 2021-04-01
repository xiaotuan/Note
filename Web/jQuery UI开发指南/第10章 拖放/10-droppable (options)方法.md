### 10.4.1　 `droppable (options)` 方法

`droppable (options)` 方法声明一个HTML元素可以用作保管其他元素的元素。 `options` 参数是一个对象，用于指定相关元素的行为。

保管其他元素的元素是指由调用了 `droppable (options)` 方法的选择器所选取的一系列元素。其中的 `options` 主要定义了哪些元素可以被放置到保管元素上，以及放置元素时的行为。

#### 1．管理保管元素的行为

表10-10描述了 `droppable (options)` 方法的选项。

<center class="my_markdown"><b class="my_markdown">表10-10　管理保管元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.disabled` | 当设置为 `true` 时，不允许元素拖放时经过和放置于保管元素上，直到使用 `droppable ("enable")` 方法重新激活为止 |
| `options.tolerance` | 指定可移动元素需要以怎样的程度来覆盖保管元素，其放置行为才能被接受。可选值有 `"fit"` （完全覆盖）、  `"intersect"` （至少覆盖一半）、  `"touch"` （接触一点即可）以及 `"pointer"` （鼠标指针完全进入保管元素范围内）。默认值为 `"intersect"` |
| `options.addClasses` | 当设置为 `true` 时（默认值），CSS类 `ui-droppable` 会被加入到保管元素列表<a class="my_markdown" href="['#anchor103']"><sup class="my_markdown">③</sup></a> |

#### 2．指定被放置的元素

默认的情况下，所有可移动元素都可以放置到保管元素上。利用表10-11列出的选项，可以准确描述哪些可移动元素是可被接纳的。

<center class="my_markdown"><b class="my_markdown">表10-11　指定可以被保管的元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.accept` | 指定哪些元素是被接纳元素。其值为一个选择器或一个被页面中所有可移动元素所调用的回调函数（以 `accept (element)` 的形式，其中 `element` 即为相应的可拖动元素）。如果元素可被接纳则函数应返回 `true` 。默认的选择器是 `"*"` ，表明所有的元素都可以接纳 |
| `options.scope` | 值为一个字符串，限定只有 `options.scope` 值（在 `draggable`   `(options)` 中定义）为同一字符串的可移动元素才能够被放置。此元素需同时定义在 `options.accept` 中 |

#### 3．管理保管元素外观

你可以给保管元素添加CSS类，并根据一定的条件来改变其外观。表10-12列出了可用的选项。

<center class="my_markdown"><b class="my_markdown">表10-12　管理保管元素外观的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.hoverClass` | 指定代表一个或多个CSS类的字符串。当被接纳元素（在 `options.accept` 中指定）移动至保管元素上方时，将这些CSS类赋予保管元素 |
| `options.activeClass` | 指定代表一个或多个CSS类的字符串。当任意一个被接纳元素（在 `options.accept` 中指定）被拖动时（并不需要进入保管元素范围内），将这些CSS类赋予保管元素 |

#### 4．管理保管元素事件

与保管元素相关的事件用于管理被接纳元素的开始移动、停止移动与放置。与这些事件相关的每一个方法都有两个参数： `event` 对应的是鼠标事件（表10-13中列出），而 `ui` 是一个值为 `{draggable,`   `helper, position,`   `offset}` 的对象（表10-14中描述）。<a class="my_markdown" href="['#anchor104']"><sup class="my_markdown">④</sup></a>

<center class="my_markdown"><b class="my_markdown">表10-13　管理事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.activate` | `activate (event,ui)` 方法会在被接纳元素开始移动时（元素被单击且鼠标开始挪动时）被调用 |
| `options.deactivate` | `deactivate (event,ui)` 方法会在被接纳元素停止移动时（鼠标按键松开时）被调用 |
| `options.over` | `over (event,ui)` 方法会在被接纳元素移动到保管元素之上时（如 `options.tolerance` 中定义的）被调用 |
| `options.out` | `out (event,ui)` 方法会在被接纳元素移出到保管元素范围之外（如 `options.tolerance` 中定义的）被调用 |
| `options.drop` | `drop (event,ui)` 方法会在被接纳元素放置到保管元素上时（鼠标按键松开时）被调用 |

<center class="my_markdown"><b class="my_markdown">表10-14　 `ui` 对象 `{draggable, helper, potision, offset}` 的属性说明</b></center>

| 属性 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `ui.draggable` | 用鼠标点中想要拖动的元素（如果在 `draggable (options)` 方法中使用 `options.helper` 指定了副本元素的话，则此处对应的并非实际拖动时的元素）所对应的jQuery类对象 |
| `ui.helper` | 实际移动的元素对应的jQuery类对象（如果在 `draggable`   `(options)` 方法中使用 `options.helper` 指定了副本元素的话，则此处对应的也不是一开始被点中的元素） |
| `ui.position` | `helper` 的位置坐标 `{top, left}` |
| `ui.offset` | 被拖动的元素相对于页面左上角的绝对坐标值 `{top,left}` |

