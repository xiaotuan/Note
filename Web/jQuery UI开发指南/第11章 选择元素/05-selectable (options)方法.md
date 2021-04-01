### 11.3.1　 `selectable (options)` 方法

`selectable (options)` 方法声明了一个包含可选择元素的HTML元素。 `options` 参数指定了选择时的行为。

#### 1．管理已选元素

`selectable (options)` 方法作用的元素的所有后代元素都是可选择的，同时也都继承了 `ui-selectee` 的CSS类名（无论是否已经被选中）。使用表11-1中列出的选项可以过滤这些后代元素以精确指定可选择元素的范围。

<center class="my_markdown"><b class="my_markdown">表11-1　指定可选元素的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.disabled` | 当设置为 `true` 时，禁用选择功能。直到使用 `selectable`   `("enable")` 方法重新激活这一功能，用户才能再选择元素 |
| `options.filter` | 一个选择器，指定哪些元素可以成为选区的一部分。这些元素会继承 `ui-selectee` 类，并成为可选择的元素。默认情况下，选择器为 `"*"` （即所有后代元素都是可选择的） |
| `options.cancel` | 一个选择器指定某些元素将不能成为选区的起点（但仍然可以成为选区的一部分） |
| `options.distance` | 指定一个距离值（以像素为单位），鼠标移动达到此距离后才能被认定为选择行为。此选项在有些情况下非常实用，例如避免简单的单击被解释为群体多选。默认值为0，此时只需对某个元素进行简单的单击即可选择或取消选择它 |

#### 2．管理已选元素事件

使用表11-2中列出的选项可以管理已选元素发生的事件，例如单个元素的选择或取消选择。后文中的第一个用例演示了这些事件在页面上发生的时间顺序。

<center class="my_markdown"><b class="my_markdown">表11-2　管理已选元素事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.start` | 当鼠标每次单击使用了 `seletable (options)` 方法的元素时，都会调用 `start (event)` 方法，然后再开始选择序列（即在之前选择的基础上添加新选或取消选择的元素） |
| `options.stop` | 当鼠标按键松开时会调用 `stop (event)` 方法。此时选择序列已经完成 |
| `options.selecting` | 当选择了一个新元素且鼠标按键还没有松开时（即此次选择序列还没有调用 `stop ()` 方法时）会调用 `selecting`   `(event, ui)` 方法。被选中的DOM元素会记录为 `ui.selecting` |
| `options.unselecting` | 当取消选择某个元素且鼠标按键还没有松开时（即此次选择序列还没有调用 `stop ()` 方法时）会调用 `unselecting`   `(event, ui)` 方法。被取消选择的DOM元素会记录为 `ui.unselecting` |
| `options.selected` | 当鼠标按键松开时，当前选择序列中每一个被选中的元素都会调用 `selected (event, ui)` 方法。而之前被选过的元素不会触发调用（即便它们还是保持了被选中的状态）。新增的被选中的DOM元素会记录为 `ui.selected` |
| `options.unselected` | 当鼠标按键松开时，当前选择序列中每一个被取消选择的元素都会调用 `unselected (event,ui)` 方法。之前已经取消选择的元素不会触发调用（即便它们仍然没被选中）。这些被取消选择的DOM元素会记录为 `ui.unselected` |

我们将术语“选择序列”定义为从 `options.start` 到 `options.stop` 过程中调用的所有方法。在这每一个方法中， `"this"` 变量指向的是调用 `selectable (options)` 方法的元素（即拥有 `ui-selectable`  CSS类的元素）。

