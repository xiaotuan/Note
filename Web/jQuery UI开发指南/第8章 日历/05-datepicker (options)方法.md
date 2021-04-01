### 8.3.1　 `datepicker (options)` 方法

`datepicker (options)` 方法声明使用日历机制来管理 `<input>` 元素（或者是 `<div>` 元素，或者是 `<span>` 元素，这取决于想如何来显示日历）。 `options` 参数是一个对象，用来指定日历的外观及行为。也能够指定不同国家的日期显示格式。

#### 1．管理日历的外观和显示时的视觉特效

表8-1列出的选项可以用来设置日历的外观。

<center class="my_markdown"><b class="my_markdown">表8-1　管理日历外观的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.firstDay` | 整数，指定日历中的星期从星期几开始。值0表示星期天（默认值） |
| `options.numberOfMonths` | 日历中同时显示的月份个数。例如，值3指定日历连续显示三个月份。如果是一个数组，则是显示月份的行数和列数。例如，[3, 2]指定日历共显示六个月份，每一行显示三个月份。默认值是1（单个月份） |
| `options.showOtherMonths` | 如果月份的第一天不落在 `options.firstDay` 指定的日期上，则月份开始和结束的没有使用的单元格可以显示上个月份或下个月份中的日期。默认值是 `fasle` （当前月份中没有使用的单元格不会显示上个月份及下个月份中的日期） |
| `options.selectOtherMonths` | 当设置为 `true` 时，表示可以在当前月份中选择上个月份或下个月份中的日期。使用该选项时，需要设置 `options.showOther Months` 为 `true` |
| `options.changeMonth` | 当设置为 `true` 时，显示快速选择月份的下拉列表。下拉列表显示在日历的最上面，替代了月份和年份的显示。默认值为 `false` |
| `options.changeYear` | 当设置为 `true` 时，显示快速选择年份的下拉列表。下拉列表显示在日历的最上面，替代了月份和年份的显示。默认值为 `false` |

使用 `options.showAnim` 选项，jQuery UI也可以在日历窗口显示或者消失时应用特效。表8-2描述了该选项，表8-3列出了详细的特效。

<center class="my_markdown"><b class="my_markdown">表8-2　管理特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.showAnim` | 日历在显示或者消失时产生的视觉特效名称 默认是 `"fadeIn"` 特效。设置为 `false` 时不会产生特效 |
| `options.duration` | 日历显示或者消失时特效的持续时间，单位是毫秒 |

<center class="my_markdown"><b class="my_markdown">表8-3　jQuery和jQuery UI提供的特效</b></center>

| 特效 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `"fadein"` | 使元素在显示或消失时伴随透明度的变化 |
| `"blind"` | 使元素从顶部显示或消失 |
| `"bounce"` | 使元素从垂直方向以“弹跳”方式显示或消失 |
| `"clip"` | 使元素从中心垂直地显示或消失 |
| `"drop"` | 使元素从左边显示或消失，有透明度变化 |
| `"fold"` | 使元素从左上角显示或消失 |
| `"highlight"` | 使元素显示或消失时伴随透明度和背景色的变化 |
| `"puff"` | 使元素从中心开始缩放。显示时“收缩”，消失时“生长” |
| `"pulsate"` | 使元素以闪烁形式显示或消失 |
| `"scale"` | 使元素从中心开始缩放。消失时“收缩”，显示时“生长” |
| `"slide"` | 使元素从它的右侧显示或消失 |

#### 2．国际化选项

默认情况下，日历显示为英文。jQuery UI几乎能显示所有主要的语种（德语、法语、西班牙语等），只需要把对应该语言的JavaScript语言文件引入即可。这些文件位于目录jqueryui/ development-bundle/ui/i18n下面。

一旦HTML引入了语言文件，有些选项默认就包含了（像月份和年份的名称、日期格式等），但也可以使用表8-4列出的选项来更改他们。日期格式是由 `options.dateFormat` 选项指定的字符串，也可以用表8-5列出的代码来配置。

<center class="my_markdown"><b class="my_markdown">表8-4　国际化选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.dateFormat` | 指定日历返回的日期格式。对于英文的日期，默认值是mm/dd/yy（根据表8-5列出的约定） |
| `options.dayNames` | 以数组形式指定星期中的天的长格式名称（Sunday、 Monday、Tuesday等）。数组必须从Sunday开始。 |
| `options.dayNamesShort` | 以数组形式指定星期中的天的短格式名称（Sun、 Mon、Tue等）。数组必须从Sun（星期日）开始 |
| `options.dayName s Min` | 以数组形式指定星期中的天的最小格式名称（Su、 Mo、Tu等）。这是日历每一列的名称。数组必须从Su（星期日）开始 |
| `options.monthNames` | 以数组形式指定月份的长格式名称（January、 February等）。数组必须从January开始 |
| `options.monthNamesShort` | 以数组形式指定月份的短格式名称（Jan、Feb等）。数组必须从Jan（一月）开始 |

<center class="my_markdown"><b class="my_markdown">表8-5　日期格式代码</b></center>

| 代码 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `d` | 月份中的天，从1到31 |
| `dd` | 月份中的天，从01到31 |
| `o` | 年份中的天，从1到366 |
| `oo` | 年份中的天，从001到366 |
| `D` | 星期中的天的缩写名称（Mon、Tue等） |
| `DD` | 星期中的天的全写名称（Monday、Tuesday等） |
| `m` | 月份，从1到12 |
| `mm` | 月份，从01到12 |
| `M` | 月份的缩写名称（Jan、Feb等） |
| `MM` | 月份的全写名称（January、February等） |
| `y` | 两位数字的年份（12表示2012） |
| `yy` | 四位数字的年份（2012） |
| `@` | 从01/01/1970至今的毫秒数 |

你可以根据优先顺序，使用这些格式代码的组合来表示完整的日期（比如，天在月份之前或者之后），可以插入额外的字符来隔开日期字段，比如斜线（/）或者连字符（-）。

#### 3．管理日期选择

默认情况下，可以选择日历中所有的日期，包括当前月份的下个月或者上个月中的日期。可以通过指定最小或者最大日期来限制可以选择的日期。表8-6列出了日期选择的选项。

<center class="my_markdown"><b class="my_markdown">表8-6　管理日期选择的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.minDate` | 日历中可以选择的最小日期 |
| `options.maxDate` | 日历中可以选择的最大日期 |
| `options.defaultDate` | 当先前没有选择日期时，预先设置的默认日期。日历首次显示时会显示这个日期。默认情况下，是当前日期 |

这些选项的值都是“日期”，可以是 `Date` 对象（用 `new Date ()` 方法创建）、当前日期之前（如−2）或之后（如2）的天数，或者使用表8-7列出的形式之一的字符串。

<center class="my_markdown"><b class="my_markdown">表8-7　选择日期的字符串表示形式</b></center>

| 格式 | 功能 | 示例 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| `X` | 当前日期之后的 `X` 天（其中 `X` 范围从1到n） | 1, 2, 3 |
| `-X` | 当前日期之前的 `X` 天（其中 `X` 范围从1到n） | -1, -2, -3 |
| `Xm` | 当前日期之后的 `X` 个月（其中 `X` 范围从1到n） | 1m, 2m, 3m |
| `-Xm` | 当前日期之前的 `X` 个月（其中 `X` 范围从1到n） | -1m, -2m, -3m |
| `Xw` | 当前日期之后的 `X` 周（其中 `X` 范围从1到n） | 1w, 2w, 3w |
| `-Xw` | 当前日期之前的 `X` 周（其中 `X` 范围从1到n） | -1w, -2w, -3w |

任意天、周和月的组合可以产生一个相对于当前日期的日子。例如，1m+3、-1m-1w。

#### 4．管理日历事件

表8-8列出了可以用来管理日历事件的选项。

<center class="my_markdown"><b class="my_markdown">表8-8　管理日历事件的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.beforeShow` | `beforeShow ()` 方法在日历显示时会被调用。 |
| `options.beforeShowDay` | `BeforeShowDay (date)` 方法在显示日历中的每个日期时会被调用（ `date` 参数是一个Date类对象）。该方法必须返回一个数组来指定每个日期的信息，内容如下： | + 该日期是否可以被选择（数组的第一项，为 `true` 或 `false` ） | + 该日期单元格上使用的CSS类（数组的第二项，默认是""） | + 该日期单元格上显示的字符串提示信息（数组的第三项，默认值是""） |
| `options.onChangeMonthYear` | `OnChangeMonthYear (year, month)` 方法在日历中显示的月份或者年份改变时会被调用。当用户单击日历上方的按钮会调用该事件，或者当 `options.`   `changeMonth` 或 `options.`   `changeYear` 为 `true` 时，用户在下拉列表中选择了别的月份或者年份时也会调用该事件 |
| `options.onClose` | `onClose (dateText)` 方法在日历关闭时会被调用（选择了一个日期、在日历外单击或者按下了Esc按键时）。 `dateText` 参数是用于写入输入框的文本形式的日期（按照 `options.`   `dateFormat` 选项的格式） |
| `options.onSelect` | `onSelect (dateText)` 方法在选择了日历的日期时会被调用。 `dateText` 参数是用于写入输入框的文本形式的日期（按照 `options.`   `dateFormat` 选项的格式） |

jQuery UI只允许使用前面的选项中定义的事件方法（ `options.beforeShow` 等）。现在还不可以使用 `bind ()` 方法来管理日历事件。

