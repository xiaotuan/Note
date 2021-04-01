### 7.3.1　 `slider (options)` 方法

`slider (options)` 方法声明使用滑块机制来管理HTML元素。 `options` 参数是一个对象，用来指定滑块的外观及行为。

有些选项允许在滑块轴上显示多个游标并且指定游标在滑块轴上面是否能够互相通过。

#### 1．管理滑块的外观和行为

表7-1描述了管理滑块外观和行为的选项。

<center class="my_markdown"><b class="my_markdown">表7-1　管理滑块外观和行为的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.disabled` | 当设置为 `true` 时，禁用滑块。直到滑块恢复到可用状态（用 `slider("enable")` ），游标才能移动或在滑块轴上单击 |
| `options.animate` | 如果为 `true` ，用户在滑块轴上直接单击时创建一个动画特效。默认设置为 `false` ，此时用户在滑块轴上单击时是直接把游标放置到单击位置的，没有动画特效 |
| `options.orientation` | 指定滑块是水平方向的还是垂直方向的。默认值是 `"horizontal"` （水平的）。使用 `"vertical"` 时将垂直放置滑块 |

#### 2．管理滑块游标的值

表7-2描述了管理滑块上游标值的可用选项。

<center class="my_markdown"><b class="my_markdown">表7-2　管理滑块游标值的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.min` | 指定游标在滑块轴起始位置（第一个刻度）时的值。默认是0 |
| `options.max` | 指定游标在滑块轴末尾位置（最后一个刻度）时的值。默认是100 |
| `options.value` | 指定游标在 `[options.min, options.max]` 区间上的值 |
| `options.values` | 当使用多个游标时，用数组指定它们的游标值。 `values` 的个数就是使用的游标数 |
| `options.range` | 当设置为 `true` 时，指定应该使用两个游标（ `options.`   `values` 数组的长度应该是2，每个值指定了游标的初始值）如果是 `"min"` 或者 `"max"` ，只能使用一个游标（如果不是，这个选项是无效的）。不管是哪种情况，如果设置为 `true` ，滑块轴上的两个游标之间的空间会被着色；如果设置为 `"min"` ，则游标和滑块轴起始位置之间的空间会被着色；如果设置为 `"max"` ，则游标和滑块轴末尾位置之间的空间会被着色 |
| `options.step` | 指定滑块轴上每次移动游标的增量位移。默认是1 |

#### 3．管理滑块上的事件

表7-3列出的事件要么是在单击游标或单击滑块轴时发生，要么是调用 `slider ("value", value)` 或者调用 `slider ("values", index, value)` 方法时发生。

<center class="my_markdown"><b class="my_markdown">表7-3　管理滑块上事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.start` | `start (event)` 方法在开始移动游标时会被调用 |
| `options.stop` | `stop (event)` 方法在结束移动游标时会被调用 |
| `options.change` | `change (event)` 方法在结束移动游标时会被调用（和 `options.stop` 一样） |
| `options.slide` | `slide (event)` 方法在拖动游标时会被调用。直接在滑块轴上单击时不会调用该方法<a class="my_markdown" href="['#anchor71']"><sup class="my_markdown">①</sup></a> |

