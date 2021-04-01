### 12.3.1　 `sortable(options)` 方法

`sortable(options)` 方法声明了一个含有可调序元素的HTML元素。 `options` 参数为一个对象，指定了与调序相关的行为。这些选项中有很多都和我们在第10章中学过的 `draggable (options)` 方法中的选项类似。

#### 1．指定和管理可移动元素

使用表12-1中列出的选项可以指定哪些元素可以被拖动，用以调序。在默认情况下， `sortable`   `(options)` 方法所应用的元素的所有后代元素都是可以被移动的。而使用下面的选项，可以禁止全部或部分，甚至是刚刚创建的元素的移动。表12-2描述了管理指定的可移动元素的选项。

<center class="my_markdown"><b class="my_markdown">表12-1　指定可移动元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.disabled` | 当设置为 `true` 时，禁止移动元素，直到使用 `sortable`   `("enable")` 方法重新激活为止 |
| `options.cancel` | 指定一个选择器，将其选取的元素设置为不能移动。用户不能再通过单击这其中任意元素来调序。此方法使你能在 `sortable`   `(options)` 方法作用的对象中剔除部分元素 |
| `options.helper` | 移动的不光可以是鼠标指向的“原元素”，我们还可以指定其他元素。 如果指定 `"clone"` 值，则可以给元素复制一个副本，且被移动的将是复制后的副本，原元素留在原位置。但若使用 `"original"` 值（也是默认值），则被移动的将是原元素。如果你指定了一个回调函数，那么会由它来创建并返回将要被移动的新元素。然而无论新元素是在哪种情形下（使用 `"clone"` 还是使用回调函数）创建的，它都会在移动结束后被删除 |
| `options.appendTo` | 使用 `options.helper` 创建的新元素，将由本选项指定其在移动阶段隶属于哪个元素。可用的值有选择器（如果选择结果是列表，则只会考虑列表的第一个元素）、单个DOM元素或字符串值 `"parent"` （即父元素）。默认值为 `"parent"` |

<center class="my_markdown"><b class="my_markdown">表12-2　管理可移动元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.cursor` | 指定元素移动时的CSS属性 `cursor` 。它表示鼠标指针的形状。可用的值有： | + `"auto"` （同 `default` ） | + `"crosshair"` （十字形） | + `"default"` （箭头形） | + `"pointer"` （手形） | + `"move"` （十字交叉箭头形） | + `"e-resize"` （表示向右方拉伸的符号，常见有左右方向箭头形） | + `"ne-resize"` （表示向右上方拉伸的符号，常见有左下右上方向箭头形） | + `"nw-resize"` （表示向左上方拉伸的符号，常见有左上右下方向箭头形） | + `"n-resize"` （表示向上方拉伸的符号，常见有上下方向箭头形） | + `"se-resize"` （表示向右下方拉伸的符号，常见有左上右下方向箭头形） | + `"sw-resize"` （表示向左下方拉伸的符号，常见有左下右上方向箭头形） | + `"s-resize"` （表示向下方拉伸的符号，常见有上下方向箭头形） | + `"w-resize"` （表示向左方拉伸的符号，常见有左右方向箭头形） | + `"text"` （表示文本编辑的符号，常见有大写字母I形） | + `"wait"` （表示系统繁忙的符号，常见有沙漏形） | + `"help"` （表示帮助的符号，常见有问号形） |
| `options.delay` | 指定一个延迟时间，以毫秒为单位，只有在鼠标持续拖动超过延迟时间后，才开始移动元素。默认值为0 |
| `options.distance` | 指定一个距离，以像素为单位，只有在鼠标持续拖动超过这个距离后，才开始移动元素。默认值为1个像素（也就是说，1个像素已经足够认定拖动元素的意图了） |
| `options.opacity` | 元素移动时的透明度设置（介于0和1之间）。默认值为1（不透明） |

#### 2．指定和管理可调序元素

使用表12-3中列出的选项可以指定可被调序的元素。默认情况下，调用了 `sortable (options)` 方法的元素的所有直接子元素都是可相互调序的，但不能和其他列表中的元素调序。表12- 4中列出的选项可以改变这一行为。

<center class="my_markdown"><b class="my_markdown">表12-3　指定可调序元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.items` | 指定可调序元素的选择器。在默认情况下，此选择器为 `">*"` ，代表调用了 `sortable (options)` 方法的元素的所有直接子元素 |
| `options.connectWith` | 指定可供插入元素的保管元素的选择器。当前的可调序元素可以放置到选择器选取的保管元素中，但反过来却不一定可行（除非那些保管元素也使用了 `options.`   `connectWith` ，允许“礼尚往来”）。默认值为 `false` （即可调序元素不能放置到其他保管元素中） |
| `options.dropOnEmpty` | 如果设置为 `ture` ，则允许将元素放置到空列表中。要使用此选项，需要先将对应的空列表包括在 `options.`   `connectWith` 中 |

<center class="my_markdown"><b class="my_markdown">表12-4　管理可调序元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.tolerance` | 指定可拖动元素需要以怎样的程度来覆盖保管元素，其放置行为才能被接受。可选值有 `"intersect"` （至少覆盖一半）以及 `"pointer"` （鼠标指针完全进入保管元素范围内）。默认值为 `"intersect"` |

#### 3．管理占位空白

当你移动一个元素时，它会在列表中留下一个占位空白（尺寸和自身一致）。jQuery UI把一个类名为 `ui-sortable-placeholder` 的元素（即占位元素）放在空白处。此元素默认是不可见的（CSS属性 `visibility` 设置为 `hidden` ），但可以使用表12-5中的选项定制其外观。

<center class="my_markdown"><b class="my_markdown">表12-5　定制占位元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.forcePlaceholderSize` | 当设置为 `true` 时，会在元素移动时给占位元素赋予一个尺寸。此选项只有在占位元素初始化后才能生效，默认值为 `false` |
| `options.placeholder` | 给占位元素添加的CSS类。只有 `options.`   `forcePlaceholderSize` 设置为 `true` 时才能生效 |

#### 4．管理放置元素时的特效

一旦元素被移动，它就会不停顿地直达最终位置（默认操作）。我们也可以在元素被插入到新位置（鼠标按键松开的地方）时制造一个视觉特效。这个选项列在表12-6中。

<center class="my_markdown"><b class="my_markdown">表12-6　管理视觉特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.revert` | 当设置为 `true` 时，在元素插入到新位置时会产生一点特效。也可以指定一个放置时的持续时间（以毫秒为单位）。默认值为 `false` （放置时没有特效） |

#### 5．管理移动限制

使用表12-7中列出的选项可以对移动中的元素添加一些限制。默认情况下，元素可以随着鼠标在页面上被随意拖动。

<center class="my_markdown"><b class="my_markdown">表12-7　管理移动限制的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.grid` | 用一个数组[x,y]来指定元素拖动过程中每一次移动的距离，在水平方向上为x像素的整数倍，垂直方向上为y像素的整数倍 |
| `options.axis` | 指定移动轴方向（ `"x"` 即只能沿水平轴方向移动， `"y"` 即只能沿垂直轴方向移动）。默认值为 `false` （即没有指定轴方向，可以往任意方向移动） |
| `options.containment` | 指定一个容器元素，拖动将限定在此元素范围内。此元素可以通过选择器（选择结果若为列表，则只会考虑列表的第一项）、DOM元素或者字符串 `"parent"` （即父元素）或 `"window"` （即整个HTML页面）来指定。还可以通过数组[x1, y1, x2, y2]的形式，将一个由对角顶点(x1, y1)和(x2, y2)形成的矩形区域指定为移动限定区域 |

#### 6．管理窗口滚动

你可以把元素拖动到某个在当前区域看不见的位置。要做到这一点，我们可以在浏览器窗口内滚动当前页面。表12-8列出了这些选项。

<center class="my_markdown"><b class="my_markdown">表12-8　管理窗口滚动的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.scroll` | 当设置为 `true` 时（默认值），如果元素拖动超出窗口的可视区域，则窗口会自动滚动 |
| `options.scrollSensitivity` | 设置鼠标移出窗口多少像素时触发窗口的滚动显示。默认值为20个像素。此选项仅当 `options.`   `scroll` 值为 `true` 时有效 |
| `options.scrollSpeed` | 设置滚动显示的速度。默认值为20 |

#### 7．管理可调序元素的事件

与可移动元素相关的事件管理着调序的起止和过程。和这些事件相关的方法都有两个参数：鼠标事件 `event` ，以及值为 `{item,helper, position, originalPosition, placeholder,sender,offset}` 的 `ui` <a class="my_markdown" href="['#anchor121']"><sup class="my_markdown">①</sup></a>。事件方法于表12-9中说明，而 `ui` 中的属性值则在表12-10中列出。

<center class="my_markdown"><b class="my_markdown">表12-9　管理可调序元素事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.start` | `start (event,ui)` 方法会在移动开始时（元素被单击且鼠标开始挪动的瞬间）被调用 |
| `options.stop` | `stop (event,ui)` 方法会在拖动完成后（鼠标按键松开的瞬间）被调用 |
| `options.beforeStop` | `beforeStop (event,ui)` 方法会在 `options.stop` 之前被调用，而此时占位元素还仍然在列表中 |
| `options.sort` | `sort (event,ui)` 方法会在移动开始后持续的过程中被调用（类似 `drag (event,ui)` 方法） |
| `options.change` | `change (event,ui)` 方法会在一个元素和一个被拖动的元素调换位置之后被调用。此时仍然可以继续调序操作 |
| `options.update` | `update (event,ui)` 方法会在拖动完成（ `options.`   `beforeStop` 之后）时被调用。其中被拖动元素已经与另一个元素调换了位置 |

<center class="my_markdown"><b class="my_markdown">表12-10　 `ui` 对象 `{item, helper, position, originalPosition,` 
  `placeholder, sender, offset}` 的属性说明</b></center>

| 属性 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `item` | 被单击的元素（但不一定是正在移动的元素。请参阅表12-1中的 `options.helper` 选项）对应的jQuery类对象 |
| `helper` | 实际在移动的元素（被鼠标点中的“原元素”或是在options.helper中指定的元素）对应的jQuery类对象 |
| `position` | 如果被拖动的元素是由 `options.helper` 指定的，则返回值为相对页面左上角的绝对坐标值 `{top, left}` 。如果被拖动的是原元素，则返回值为相对元素自身起始位置的偏移量，即从(0, 0)开始计算 |
| `originalPosition` | 记录开始移动前的 `position` 值 |
| `placeholder` | 占位元素（为放置元素预留空白位置的透明元素）对应的jQuery类对象 |
| `sender` | 被拖动的元素所在的保管元素对应的jQuery类对象。在有些方法中可能为 `null` （例如，在 `options.start` 中可能为null，而稍后在 `options.activate` 中才会定义）（此属性只在使用了 `options.connectWith` 选项的联动列表间调换元素时有效）对应的jQuery类对象 |
| `offset` | 其返回值始终为被移动的元素相对于页面左上角的绝对坐标值 `{top, left}` |

其他事件则是在不同的列表间调换元素时触发的。前面的表格里曾经提过，要在不同的列表间调换元素，需要使用 `connectWith` 选项。此选项是一个选择器，指定了可供插入元素的列表元素。在列表间触发的事件可以帮助我们判断是外部列表的元素被引入到了当前列表中，还是当前列表的元素被放置到了外部列表中。表12-11列出了管理列表间调换元素的事件的选项。

<center class="my_markdown"><b class="my_markdown">表12-11　管理多个列表间调换元素的事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.receive` | `receive (event, ui)` 方法会在外部列表的元素被引入到当前列表中时被调用 |
| `options.remove` | `remove (event, ui)` 方法会在当前列表的元素被放置到外部列表中时被调用 |
| `options.activate` | `activate (event, ui)` 方法会在元素移动开始时（无论是从当前列表还是外部列表）被调用。这一事件常用于提示你某个外部列表正在进行调序操作 |
| `options.deactivate` | `deactivate (event, ui)` 方法会在元素移动结束时（无论是从当前列表还是外部列表）被调用。这一事件常用于通知你某个外部列表完成了一次调序操作 |

