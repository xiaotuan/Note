### 4.3.1　 `dialog (options)` 方法

`dialog (options)` 方法声明使用对话框机制来管理HTML元素（及其内容）。 `options` 参数是一个对象，用来指定对话框窗口的外观及行为。该参数选项可以管理对话框窗口的外观、位置、大小以及视觉特效行为。

表4-1描述了管理对话框外观的选项。

<center class="my_markdown"><b class="my_markdown">表4-1　管理对话框外观的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.title` | 给对话框窗口指定标题 |
| `options.buttons` | 在对话框中添加按钮。这是一些对象，每个对象的属性是按钮上的文字，值是用户单击按钮时调用的回调函数 |

表4-2描述了管理对话框位置的选项。

<center class="my_markdown"><b class="my_markdown">表4-2　管理对话框在页面中位置的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.position` | 对话框窗口的位置是由坐标 `[left, top]` 指定的，或者是像下面这样的字符串： | + `"left top"` 、 `"top right"` 、 `"bottom left"` 或者 `"right bottom"` （页面的4个角） | + `"top"` 或者 `"bottom"` （顶部或者底部, 按宽度居中） | + `"left"` 或者 `"right"` （左边或者右边，按高度居中） | + `"center"` （按宽度和高度居中）对话框窗口默认按宽度和高度居中（ `"center"` ） |

表4-3描述了管理对话框大小的选项。

<center class="my_markdown"><b class="my_markdown">表4-3　管理对话框大小的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.height` | 对话框的初始高度（以像素为单位）。默认值是 `"auto"` （自动调整大小以便显示所有的内容） |
| `options.width` | 对话框的初始宽度（以像素为单位）。默认是300 |
| `options.maxHeight` | 对话框可以调整到的最大高度（以像素为单位） |
| `options.maxWidth` | 对话框可以调整到的最大宽度（以像素为单位） |
| `options.minHeight` | 对话框可以调整到的最小高度（以像素为单位）。默认值是150 |
| `options.minWidth` | 对话框可以调整到的最小宽度（以像素为单位）。默认值是150 |

#### 1．管理对话框的视觉特效

可以使用jQuery UI，通过 `options.show` 和 `options.hide` 选项来指定对话框显示和消失时的特效（在表4-4中描述）。

<center class="my_markdown"><b class="my_markdown">表4-4　管理视觉特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.show` | 对话框显示时伴随的视觉特效（表4-5列出了这些特效）。当设置为 `false` （默认）时，对话框显示时没有特效 |
| `options.hide` | 对话框消失时伴随的视觉特效（下表列出）。当设置为 `false` （默认），对话框消失时没有特效 |

<center class="my_markdown"><b class="my_markdown">表4-5　jQuery UI提供的特效</b></center>

| 特效名称 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `"blind"` | 元素从顶部显示或消失 |
| `"bounce"` | 元素断断续续地显示或消失，垂直运动 |
| `"clip"` | 元素从中心垂直地显示或消失 |
| `"drop"` | 元素从左边显示或消失，有透明度变化 |
| `"fold"` | 元素从左上角显示或消失 |
| `"highlight"` | 元素显示或消失，伴随透明度和背景色的变化 |
| `"puff"` | 元素从中心开始缩放。显示时“收缩”，消失时“生长” |
| `"pulsate"` | 元素以闪烁形式显示或消失 |
| `"scale"` | 元素从中心开始缩放。消失时“收缩”，显示时“生长” |
| `"slide"` | 元素从它的右侧显示或消失 |

#### 2．管理对话框的行为

表4-6描述了管理对话框在打开、移动、叠加及调整大小时的行为的选项。

<center class="my_markdown"><b class="my_markdown">表4-6　管理对话框的行为的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.autoOpen` | 如果为 `true` （默认），调用 `dialog (options)` 方法时就会打开对话框 | 如果为 `false` ，对话框已经创建，但仅通过调用 `dialog`   `("open")` 才会变成可见 |
| `options.draggable` | 如果为 `true` （默认），在页面上可以移动对话框 |
| `options.resizable` | 如果为 `true` （默认），在页面上可以调整对话框的大小 |
| `options.modal` | 如果为 `true` ，对话框是模态的（无法访问页面上其他在对话框之外的元素） | 默认值为 `false` （对话框不是模态的） |
| `options.stack` | 如果为 `true` （默认），对话框能被叠加（单击窗口或对话框将它带到“前景”上来） | 如果为 `false` ，对话框按打开顺序叠加在一起，但用户不能改变堆叠的顺序 |

#### 3．管理对话框的事件

对话框的事件方法（表4-7中描述）允许在对话框的不同阶段完成一些处理工作。它们相当于是在这些不同阶段时调用的回调函数。回调函数中的 `this` 值是与对话框内容相关联的 `<div>` 元素。

<center class="my_markdown"><b class="my_markdown">表4-7　管理对话框事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.focus` | 当对话框被激活时（首次显示及每次在它上面单击）会调用 `focus`   `(event)` 方法 |
| `options.open` | 当对话框被显示时（首次显示或之后调用 `dialog`   `("open")` 方法）会调用 `open (event)` 方法 |
| `options.beforeclose` | 当对话框将要关闭时（当单击关闭按钮或调用 `dialog`   `("close")` 方法），会调用 `beforeclose (event)` 方法。如果该函数返回 `false` ，对话框将不会关闭。关闭的对话框可以用 `dialog ("open")` 重新打开 |
| `options.close` | 当对话框关闭时（当单击关闭按钮或调用 `dialog`   `("close")` 方法），会调用 `close (event)` 方法。关闭的对话框可以用 `dialog ("open")` 重新打开 |
| `options.drag` | 在移动页面上的对话框时，每次移动鼠标都会调用 `drag (event)` 方法 |
| `options.dragStart` | 在开始移动页面上的对话框时，会调用 `dragStart`   `(event)` 方法 |
| `options.dragStop` | 在结束移动页面上的对话框时（松开鼠标按钮）会调用 `dragStop (event)` 方法 |
| `options.resize` | 在调整页面上的对话框的大小时，每次移动鼠标都会调用 `resize (event)` 方法 |
| `options.resizeStart` | 在开始调整页面上的对话框大小时会调用 `resizeStart`   `(event)` 方法 |
| `options.resizeStop` | 在结束调整页面上的对话框大小时（松开鼠标按钮）会调用 `resizeStop (event)` 方法 |

