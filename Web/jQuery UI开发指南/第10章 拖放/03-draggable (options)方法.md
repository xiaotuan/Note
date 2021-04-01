### 10.1.1　 `draggable (options)` 方法

`draggable (options)` 方法声明了一个在HTML页面中可以被移动的HTML元素。 `options` 参数是一个对象，指定了相关元素的行为。

#### 1．指定可移动元素

使用表10-1中的参数选项来指定可移动的元素。默认情况下， `draggable (options)` 方法会应用到列表的所有元素上。以下这些选项可以禁止所有或是部分元素，甚至是刚刚创建的新元素的移动。

<center class="my_markdown"><b class="my_markdown">表10-1　管理可移动元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.disabled` | 当设置为 `true` 时，禁止移动元素，直到使用 `draggable`   `("enable")` 方法重新激活为止 |
| `options.cancel` | 指定一个选择器，将其选取的元素设置为不能移动。此方法使你能限定起始处能拖动的列表元素（即 `draggable`   `(options)` 方法作用的对象） |
| `options.helper` | 创建和移动所选元素的副本。如果指定 `"clone"` 值，则可以给元素复制一个副本，且被移动的将是复制后的副本，原元素留在原位置。但若使用 `"original"` 值（也是默认值），则被移动的将是原元素。如果指定了一个回调函数，那么会由它来创建并返回将要被移动的新元素。然而无论新元素是在哪种情形下（使用 `"clone"` 还是使用回调函数）创建的，它都会在移动结束后被删除 |
| `options.appendTo` | 使用 `options.helper` 创建的新元素，将由本选项指定其在移动阶段隶属于哪个元素。可用的值有选择器（如果选择结果是列表，则只会考虑列表的第一个元素）、单个DOM元素或字符串值 `"parent"` （即父元素）。默认值为 `"parent"` |

#### 2．管理元素的移动

表10-2描述了用于管理元素实际移动的选项。

<center class="my_markdown"><b class="my_markdown">表10-2　管理元素移动的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.addClasses` | 设置为 `true` 时（默认情况）表示分别为可移动的元素及正在移动的元素添加名为 `ui-draggable` 和 `ui-draggable-dragging` 的CSS类 |
| `options.cursor` | 指定元素移动时的CSS属性 `cursor` 。它表示鼠标指针的形状。可用的值有： | + `"auto"` （默认） | + `"crosshair"` （十字形） | + `"default"` （箭头形） | + `"pointer"` （手形） | + `"move"` （十字交叉箭头形） | + `"e-resize"` （表示向右方（east）拉伸的符号，常见有左右方向箭头形） | + `"ne-resize"` （表示向右上方（north east）拉伸的符号，常见有左下右上方向箭头形） | + `"nw-resize"` （表示向左上方（north west）拉伸的符号，常见有左上-右下方向箭头形） | + `"n-resize"` （表示向上方（north）拉伸的符号，常见有上下方向箭头形） | + `"se-resize"` （表示向右下方（south east）拉伸的符号，常见有左上右下方向箭头形） | + `"sw-resize"` （表示向左下方（south west）拉伸的符号，常见有左下右上方向箭头形） | + `"s-resize"` （表示向下方（south）拉伸的符号，常见有上下方向箭头形） | + `"w-resize"` （表示向左方（west）拉伸的符号，常见有左右方向箭头形） | + `"text"` （表示文本编辑的符号，常见有大写字母I形） | + `"wait"` （表示系统繁忙的符号，常见有沙漏形） | + `"help"` （表示帮助的符号，常见有问号形） |
| `options.delay` | 指定一个延迟时间，以毫秒为单位，只有在鼠标持续拖动超过延迟时间后，元素才开始移动。默认值为0 |
| `options.distance` | 指定一个距离，以像素为单位，只有在鼠标持续拖动超过这个距离后，元素才会开始移动。默认值为1（也就是说，1个像素已经足够认定拖动元素的意图了） |
| `options.opacity` | 元素移动时的透明度（介于0和1之间）。默认值为1（不透明） |
| `options.scope` | 一个字符串，限定被移动的元素只能放置在 `options.`   `scope` 值（通过 `droppable`   `(options)` 方法定义）为同一字符串的项上 |
| `options.connectToSortable` | 指定一个元素可排序的列表。拖放之后，元素将成为该列表的一部分<a class="my_markdown" href="['#anchor101']"><sup class="my_markdown">①</sup></a> |

#### 3．管理放置元素时的特效

一旦元素被移动，它就会停留在最终被放置的地方（默认行为）。使用表10-3中列出的选项可以为元素在被放置时指定一个新的行为（例如，立即返回到其原始位置）。

<center class="my_markdown"><b class="my_markdown">表10-3　管理放置元素时的特效选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.revert` | 设置元素是否在被放置时返回其原始位置。设置为 `true` 时，元素将返回原始位置。设置为 `false` 时，将停留在被放置处。设置为 `"valid"` 时，如果元素被正确放置在能够接纳它的元素上，元素会返回。而设置为 `"invalid"` 时，则刚好相反，当其被放置在不能接纳它的元素上时才会返回 |
| `options.revertDuration` | 设置元素被放置后返回原始位置（见上一选项 `options.revert` ）的过程持续时间（单位为毫秒）。默认情况下，持续时间为500 ms |

#### 4．管理移动限制

默认情况下，元素可以随着鼠标在页面上被随意拖动。要改变这一默认行为，我们可以使用表10-4中列出的选项。

<center class="my_markdown"><b class="my_markdown">表10-4　管理移动限制的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.grid` | 用一个数组[x,y]来指定元素拖动过程中每一次移动的距离，在水平方向上为x像素的整数倍，垂直方向上为y像素的整数倍 |
| `options.axis` | 指定移动轴方向（ `"x"` 即只能沿水平轴方向移动，  `"y"` 即只能沿垂直轴方向移动）。默认值为 `false` （即没有指定轴方向，可以往任意方向移动） |
| `options.containment` | 指定一个容器元素，拖动将限定在此元素范围内。此元素可以通过选择器（选择结果若为集合，则只会考虑集合的第一项）、DOM元素或者字符串 `"parent"` （即父元素）或 `"window"` （即HTML页面）来指定。 | 还可以通过数组[x1，y1，x2，y2]的形式，将一个由对角顶点(x1，y1)和(x2，y2)形成的矩形区域指定为移动限定区域 |
| `options.snap` | 调整某元素在另一元素之上移动时的显示情况。如果要将某元素移向另一元素，则位移过程（以像素为单位）中两个元素并不能很完美地上下摆放。 | 本选项的值为一个选择器，用来指定哪些元素由jQuery UI来管理调整（即当被拖动的元素越过选择器所选择的元素时，其位置会被调整）。设置为 `true` 则等效于值为 `".ui-`   `draggable"` 的选择器——被移动的元素会在经过所有同类元素时被自动调整。默认值为 `false` （不做调整）<a class="my_markdown" href="['#anchor102']"><sup class="my_markdown">②</sup></a> |
| `options.snapMode` | 设置被移动的元素和 `options.snap` 中指定的元素间应当如何做调整。值设为 `"inner"` 时表示与内部元素做调整，相应地 `"outer"` 表示外部元素，而 `"both"` 则指定与内外元素都要做调整。默认值为 `"both"` |
| `options.snapTolerance` | 位置偏移时触发调整行为所需的最大像素距离。默认值为20个像素，意味着一旦被移动的元素离 `options.snap` 中指定的元素只有20个像素距离时，即会按照 `options.snapMode` 的设置做出相应的调整显示 |

#### 5．管理窗口滚动

要将元素拖动到某个在当前区域看不见的位置并非不可能。要做到这一点，只需配置一下，允许页面在拖动元素时能够滚动即可。表10-5列出了用于管理窗口滚动的一些选项。

<center class="my_markdown"><b class="my_markdown">表10-5　管理窗口滚动的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.scroll` | 当设置为 `true` 时（默认值），如果元素拖动超出窗口的可视区域，则窗口会自动滚动 |
| `options.scrollSensitivity` | 设置鼠标移出窗口多少像素时触发窗口的滚动显示。默认值为20个像素。此选项仅当 `options.scroll` 值为 `true` 时有效 |
| `options.scrollSpeed` | 设置滚动显示的速度。默认值为20 |

#### 6．管理可移动元素的事件

与可移动元素相关的事件管理着移动的起止和过程。和这些事件相关的方法都有两个参数：鼠标事件 `event` ，以及值为 `{helper, position, offset}` 的 `ui` 。 `ui` 中的3个属性值将于表10-6中说明，而事件选项则在表10-7中列出。

<center class="my_markdown"><b class="my_markdown">表10-6　 `ui` 对象 `{helper, position, offset}` 的属性说明</b></center>

| 属性 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `ui.helper` | 被拖动的元素（被鼠标点中的元素或是在 `options.helper` 中指定的元素）所对应的jQuery类对象 |
| `ui.position` | 如果被拖动的元素是由 `options.helper` 指定的，则返回值为相对页面左上角的绝对坐标值 `{top, left}` 如果被拖动的是被点中的元素，则返回值为相对元素自身起始位置的偏移量，即从(0,0)开始计算 |
| `ui.offset` | 其返回值始终为被移动的元素相对于页面左上角的绝对坐标值 `{top, left}` |

<center class="my_markdown"><b class="my_markdown">表10-7　管理可移动元素的事件</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.start` | `start(event,ui)` 方法会在移动开始时（元素被单击且鼠标开始挪动的瞬间）被调用 |
| `options.drag` | `drag(event,ui)` 方法会在移动开始后持续的过程中被调用 |
| `options.stop` | `stop(event,ui)` 方法会在拖动完成后（鼠标按键松开的瞬间）被调用 |

