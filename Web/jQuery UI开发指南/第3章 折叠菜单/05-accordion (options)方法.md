### 3.3.1　 `accordion (options)` 方法

`accordion (options)` 方法指定使用折叠菜单来管理HTML元素（及其内容）。 `options` 参数是一个对象，用来指定菜单的外观及行为。这些选项与菜单的行为、菜单内容的高度或者菜单的事件有关。

#### 1．管理折叠菜单的选项

表3-1描述了管理折叠菜单行为的选项。

<center class="my_markdown"><b class="my_markdown">表3-1　管理菜单行为的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.collapsible` | 当设置为 `true` 时，允许用户通过单击来关闭菜单。当设置为 `false` 时（默认），在打开的菜单上单击不会关闭该菜单 |
| `options.active` | 指定第一次访问页面时被打开菜单的索引。默认是0（第一个菜单）。若要指定在启动时不打开菜单，使用 `false` |
| `options.event` | 让用户选择新菜单的事件的名称（默认是 `"click"` ）。比如，如果指定为 `"mouseover"` ，则用户移动鼠标到菜单上就能选中该菜单 |
| `options. Animated` | 指定选择菜单时伴随的视觉特效。默认是 `"slide"` 。<a class="my_markdown" href="['#anchor31']"><sup class="my_markdown">①</sup></a>要用其他值，可以修改特效参数 `easing` 的值，也就是特效进行的方式（同时会保留幻灯片特效）。可以使用的值有 `"easeInQuad"` 、  `"easeInCubic"` 、  `"easeInQuart"` 、  `"easeInQuint"` 、  `"easeInSine"` 、  `"easeInExpo"` 、  `"easeInCirc"` 、  `"easeInElastic"` 、  `"easeInBack"` 及 `"easeInBounce"` 。设置为 `false` ，则显示菜单内容是没有过渡特效的 |

#### 2．管理菜单内容的高度

默认情况下，菜单会自动调整高度，以适应内容的高度。也可以手动设定高度。表3-2列出了管理菜单内容高度的选项。

<center class="my_markdown"><b class="my_markdown">表3-2　管理菜单高度的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.autoHeight` | 当设置为 `true` 时（默认），最高内容的高度会被应用到所有其他的菜单内容上。当设置为 `false` 时，每个菜单的高度等于其内容的实际高度，所以每个菜单都可能会有不同的高度 |
| `options.fillSpace` | 当设置为 `true` 时，所有的菜单内容拥有和全局 `<div>` 元素的父元素一样的高度和宽度。默认为 `false` |

#### 3．管理与菜单相关的事件

也有管理选择菜单的方法。这些方法接收 `event` 事件参数，随后是描述与该事件相关的 `menus` 对象（打开的菜单及关闭的菜单）。这个 `menus` 对象包含了以下属性。

+ `oldHeader` ，正在关闭的菜单的jQuery类对象。
+ `oldContent` ，正在关闭的菜单内容的jQuery类对象。
+ `newHeader` ，正在打开的菜单的jQuery类对象。
+ `newConetnt` ，正在打开的菜单内容的jQuery类对象。

表3-3描述了管理菜单事件的选项。

<center class="my_markdown"><b class="my_markdown">表3-3　管理菜单事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.change` | 当选择菜单时（要么手动调用，要么调用 `accordion`   `("activate")` 方法），在动画发生后（选择的菜单已经打开且先前打开的菜单已经关闭）会调用 `change`   `(event, menus)` 方法 |
| `options.changestart` | 当选择菜单时（要么手动调用，要么调用 `accordion`   `("activate")` 方法），在动画发生前（应该打开的菜单尚未打开，应该关闭的菜单也尚未关闭）会调用 `changestart`   `(event, menus)` 方法 |

