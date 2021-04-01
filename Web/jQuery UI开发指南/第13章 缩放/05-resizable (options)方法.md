### 13.3.1　 `resizable (options)` 方法

`resizable (options)` 方法将一个HTML元素声明为可缩放的。 `options` 参数为一个对象，指定了缩放时的相关行为。

#### 1．管理可缩放元素

我们先从管理缩放过程的选项看起（见表13-1），接着是指定哪些元素可被缩放（见表13-2），如何缩放（见表13-3），如何对缩放做限制（见表13-4）。

<center class="my_markdown"><b class="my_markdown">表13-1　管理可缩放元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.disabled` | 当设置为 `true` 时，禁用缩放机制。直到使用 `resizable`   `("enable")` 方法重新激活，用户才能再使用鼠标缩放元素 |
| `options.autoHide` | 隐藏缩放小图标，只有在鼠标滑过其上时显示 |
| `options.delay` | 指定一个延迟时间，只有在鼠标持续拖动超过延迟时间后，才开始缩放元素。默认值为0 |
| `options.distance` | 指定一个距离，只有在鼠标持续拖动超过这个距离后，才开始被缩放元素。默认值为1个像素 |
| `options.grid` | 用一个数组[x,y]来指定元素缩放过程中，每一次收缩或扩张的距离，在水平方向上为x像素的整数倍，垂直方向上为y像素的整数倍 |

<center class="my_markdown"><b class="my_markdown">表13-2　指定哪些元素可被缩放的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.alsoResize` | 其值可以为选择器、jQuery类对象或DOM元素。当原有的可缩放元素被缩放时，由本选项指定的元素会同时被缩放，而此元素可位于页面上任何位置。默认值为 `false` （即不会有其他元素同时被缩放） |
| `options.cancel` | 其值为一个选择器，指定不可被缩放的元素 |

<center class="my_markdown"><b class="my_markdown">表13-3　指定如何进行缩放的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.aspectRatio` | 设置是否维持元素宽高比。当设置为 `true` 时，元素会维持原始的宽高比；否则，需要指定一个具体的宽高比数值。例如，0.5表示元素会始终保持1:2的宽高比，即高度始终为宽度的2倍。默认值为 `false` （即不维持宽高比） |
| `options.handles` | 用字符串值来指定元素的某侧边或某个角可用以缩放。可用的值有分别代表四条边的 `n` （上）、  `e` （右）、  `s` （下）和 `w` （左），以及代表四个角的 `ne` （右上）、  `se` （右下）、  `nw` （左上）和 `sw` （左下）。默认值为“ `e，s，se` ”，即右边、底边，以及右下角是可以用来缩放元素的 |

<center class="my_markdown"><b class="my_markdown">表13-4　指定如何对缩放做限制的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.containment` | 限制缩放适用于哪个元素范围内。此元素可以通过选择器（选择结果若为多个元素，则取第一个）、DOM元素或字符串 `"parent"` （即父元素）来指定。默认值为 `false` （无限制） |
| `options.maxHeight` | 元素允许被放大到的最大高度。默认值为 `null` （无限制） |
| `options.maxWidth` | 元素允许被放大到的最大宽度。默认值为 `null` （无限制） |
| `options.minHeight` | 元素允许被缩小到的最小高度。默认值为10 |
| `options.minWidth` | 元素允许被缩小到的最小宽度。默认值为10 |

#### 2．管理缩放特效

使用表13-5中列出的选项可以管理缩放中的视觉特效，无论是制造一个效果还是复制一个缩放过的元素。

<center class="my_markdown"><b class="my_markdown">表13-5　管理缩放特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.animate` | 当设置为 `true` 时，在缩放过程中鼠标按键松开时会启用一个特效。默认值为 `false` （无特效） |
| `options.animateDuration` | 缩放特效的持续时间（以毫秒为单位）。此选项仅当 `options.animate` 设置为true时有效 |
| `options.ghost` | 当设置为 `true` 时，元素自身并不会在缩放操作中显示相应的缩放变化，而是由一个相对透明的“影子元素”来反映变化。此“影子元素”会在鼠标按键松开时被删除。 | 默认值为 `false` （元素自身随着缩放操作显示变化） |
| `options.helper` | 自定义CSS类，为被缩放的元素制定样式。如果使用此选项，则会创建一个新的 `<div>` 元素，将其作为被缩放的对象（拥有一个名为 `ui-resizable-helper` 的CSS类）。此元素会在鼠标按键松开时被删除。默认值为 `false` （不创建新的 `<div>` 元素） |

#### 3．管理元素缩放事件

与可缩放元素相关的事件管理着缩放操作的起止全程。和这些事件相关的方法（于表13-6中列出）都有两个参数：与鼠标事件相关的 `event` ，以及值为 `{originalElement, element, helper,`   `position, size, originalSize, OriginalPosition}` 的 `ui` <a class="my_markdown" href="['#anchor131']"><sup class="my_markdown">①</sup></a>。 `ui` 中的这些属性值将于表13-7中说明。

<center class="my_markdown"><b class="my_markdown">表13-6　管理事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.start` | `Start (event, ui)` 方法会在鼠标开始缩放元素时被调用 |
| `options.stop` | `Stop (event, ui)` 方法会在鼠标按键松开时被调用。此时缩放已完成 |
| `options.resize` | `Resize (event, ui)` 方法会在缩放开始后鼠标持续移动的过程中被调用 |

<center class="my_markdown"><b class="my_markdown">表13-7　 `ui` 对象 `{originalElement, element, helper, position,`   `size, originalSize, OriginalPosition}` 的属性说明</b></center>

| 属性 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `originalElement` | 记录原DOM元素，大多数情况下和 `element` 指向同一个元素 |
| `element` | 某些类型的DOM元素需要在外层使用 `<div>` 元素封装（例如 `<textarea>` 自身就有缩放功能，需要屏蔽），此时 `element` 指向的是外层的封装元素 |
| `helper` | 被缩放的元素（被鼠标点中的“原元素”或是在 `options.`   `helper` 中指定由jQuery UI创建的元素）所对应的jQuery类对象 |
| `position` | 表示元素当前位置的 `{top, left}` 坐标值 |
| `size` | 表示元素当前宽高的 `{width, height}` 尺寸值 |
| `originalSize` | 表示元素初始宽高的 `{width, height}` 尺寸值 |
| `originalPosition` | 表示元素初始位置的 `{top, left}` 坐标值 |

