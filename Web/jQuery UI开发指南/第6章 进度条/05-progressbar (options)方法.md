### 6.3.1　 `progressbar (options)` 方法

`progressbar (options)` 方法声明使用进度条机制来管理HTML元素。 `options` 参数是一个对象，用来指定按钮的外观及行为。有允许管理进度条或者是进度条事件发生的可用选项（表6-1中描述）。

<center class="my_markdown"><b class="my_markdown">表6-1　管理进度条及事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.value` | 进度条填充的百分比（从0到100） |
| `options.change` | `change (event)` 方法在进度条填充的百分比改变时（通过改变 `options.value` 选项）会被调用 |

