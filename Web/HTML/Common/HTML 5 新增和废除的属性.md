[toc]

### 1. 新增属性

#### 1.1 表单相关的属性

##### 1.1.1 autocomplete 属性

`autocomplete` 属性规定 `form` 或 `input` 域应该拥有自动完成功能。

`autocomplete` 适用于 `<form>` 标签，以及以下类型的 `<input>` 标签：`text`、`search`、`url`、`telephone`、`email`、`password`、`datepickers`、`range` 以及 `color`。

##### 1.1.2 autofocus 属性

`autofocus` 属性规定在页面加载时，域自动地获得焦点。

`autofocus `属性适用于所有 `<input>` 标签的类型。

##### 1.1.3 form 属性

`form` 属性规定输入域所属的一个或多个表单。

`form` 属性适用于所有 `<input>` 标签的类型。

##### 1.1.4 表单重写属性

表单重写属性（Form Override Attributes）允许用户重写 `form` 元素的某些属性设定。
表单重写属性有以下几个：

+ `formaction`——重写表单的 `action` 属性。　

+ `formenctype`——重写表单的 `enctype` 属性。　

+ `formmethod`——重写表单的 `method` 属性。　

+ `formnovalidate`——重写表单的 `novalidate` 属性。　

+ `formtarget`——重写表单的 `target` 属性。

表单重写属性适用于以下类型的 `<input>` 标签：`submit` 和 `image`。

##### 1.1.5 width 和 height 属性

`height` 和 `width` 属性规定用于 `image` 类型的 `<input>` 标签的图像高度和宽度。

`height` 和 `width` 属性只适用于 `image` 类型的 `<input>` 标签。

##### 1.1.6 list 属性

`list` 属性规定输入域的 `datalist`。`datalist` 是输入域的选项列表。

`list` 属性适用于以下类型的 `<input>` 标签：`text`、`search`、`url`、`telephone`、`email`、`date pickers`、`number`、`range` 以及 `color`。

##### 1.1.7 min、max 和 step 属性

`min`、`max` 和 `step` 属性用于为包含数字或日期的 `input` 类型规定限定（约束）。

`max` 属性规定输入域所允许的最大值。

`min` 属性规定输入域所允许的最小值。

`step` 属性为输入域规定合法的数字间隔（如果 `step="3"`，则合法的数是 -3、0、3、6等）。

`min`、`max` 和 `step` 属性适用于以下类型的 `<input>` 标签：`date pickers`、`number`以及 `range`。

##### 1.1.8 multiple 属性

`multiple` 属性规定输入域中可选择多个值。

`multiple` 属性适用于以下类型的 `<input>` 标签：`email` 和 `file`

##### 1.1.9 novalidate 属性

`novalidate` 属性规定在提交表单时不应该验证 `form` 或 `input` 域。

`novalidate` 属性适用于 `<form>` 以及以下类型的 `<input>` 标签：`text`、`search`、`url`、`telephone`、`email`、`password`、`date pickers`、`range` 以及 `color`。

##### 1.1.10 pattern 属性

`pattern` 属性规定用于验证 `input` 域的模式（ `Pattern` ）。模式是正则表达式。用户可以在 `JavaScript` 教程中学习到有关正则表达式的内容。

`pattern` 属性适用于以下类型的 `<input>` 标签：`text`、`search`、`url`、`telephone`、`email` 以及 `password`。

##### 1.1.11 placeholder 属性

`placeholder` 属性提供一种提示（ `hint` ），描述输入域所期待的值。

`placeholder` 属性适用于以下类型的 `<input>` 标签：`text`、`search`、`url`、`telephone`、`email` 以及 `password`。

##### 1.1.12 required 属性

`required` 属性规定必须在提交之前填写输入域（不能为空）。

`required` 属性适用于以下类型的 `<input>` 标签：`text`、`search`、`url`、`telephone`、`email`、`password`、`date pickers`、`number`、`checkbox`、`radio` 以及 `file`。

#### 1.2 链接相关属性

##### 1.2.1 media 属性

为 `a` 与 `area` 元素增加了 `media` 属性，该属性规定目标 `URL` 是为什么类型的媒介/设备进行优化的。只能在 `href` 属性存在时使用。

##### 1.2.2 hreflang 属性与 rel 属性

为 `area` 元素增加了 `hreflang` 属性与 `rel` 属性，以保持与 `a` 元素、`link` 元素的一致。

##### 1.2.3 size 属性

为 `link` 元素增加了新属性 `sizes`。该属性可以与`icon` 元素结合使用（通过 `rel` 属性），以指定关联图标（ `icon` 元素）的大小。

##### 1.2.4 target 属性

为 `base` 元素增加了 `target` 属性，主要目的是保持与 `a` 元素的一致性，同时 `target` 元素由于在 `Web` 应用程序中，尤其是在与 `iframe` 结合使用时，是非常有用的，所以不再是不赞成使用的元素了。

##### 1.2.5 其他属性

+ `reversed` 属性

  为 `ol` 元素增加 `reversed` 属性，它指定列表倒序显示。`li` 元素的 `value` 属性与 `ol` 元素的 `start` 属性因为它不是被显示在界面上的，所以不再是不赞成使用的了。

+ `charset` 属性

  为 `meta` 元素增加 `charset` 属性，因为这个属性已经被广泛支持了，而且为文档的字符编码的指定提供了一种比较良好的方式。

+ `type` 属性与 `label` 属性

  为 `menu` 元素增加了两个新的属性 `type` 与 `label`。`label` 属性为菜单定义了一个可见的标注，`type` 属性让菜单可以以上下文菜单、工具条或列表菜单 3 种形式出现。

+ `scoped` 属性

  为 `style` 元素增加 `scoped` 属性，用来规定样式的作用范围，譬如只对页面上某个树起作用。为 `script` 元素增加 `async` 属性，它定义脚本是否异步执行。

+ `manifest` 属性

  为 `html` 元素增加 `manifest` 属性，开发离线 `Web` 应用程序时它与 `API` 结合使用，定义一个 `URL`，在这个 `URL` 上描述文档的缓存信息。为 `iframe` 元素增加 `sandbox`、`seamless` 与 `srcdoc` 3 个属性，用来提高页面安全性，防止不信任的 `Web` 页面执行某些操作。

### 2. 废除的属性

<center><b>在 HTML 5 中被废除了的属性</b></center>

| 在 HTML 4 中使用的属性                                       | 使用该属性的元素                                             | 在 HTML 5 中的替代方案                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `rev`                                                        | `link`、`a`                                                  | `rel`                                                        |
| `charset`                                                    | `link`、`a`                                                  | 在被链接的资源中使用 `HTTP content-type` 头元素              |
| `shape`、`coords`                                            | `a`                                                          | 使用 `area` 元素代替 `a`                                     |
| `longdesc`                                                   | `img`、`iframe`                                              | 使用 `a` 元素链接到较长描述                                  |
| `target`                                                     | `link`                                                       | 多余属性，被省略                                             |
| `nohref`                                                     | `area`                                                       | 多余属性，被省略                                             |
| `profile`                                                    | `head`                                                       | 多余属性，被省略                                             |
| `version`                                                    | `html`                                                       | 多余属性，被省略                                             |
| `name`                                                       | `img`                                                        | `id`                                                         |
| `scheme`                                                     | `meta`                                                       | 只为某个表单域使用 `scheme`                                  |
| `archive`、`classid`、`codebase`、`codetype`、`declare`、`standby` | `object`                                                     | 使用 `data` 与 `type` 属性类调用插件。需要使用这些属性来设置参数时，使用 `param` 属性 |
| `valuetype`、`type`                                          | `param`                                                      | 使用 `name` 与 `value` 属性，不声明值的 `mime` 类型          |
| `axis`、`abbr`                                               | `td`、`th`                                                   | 使用以明确简洁的文字开头、后跟详述文字的形式。可以对更详细内容使用 `title` 属性，来使单元格式的内容变得简短。 |
| `scope`                                                      | `td`                                                         | 在被链接的资源中使用 `HTTP content-type` 头元素              |
| `align`                                                      | `caption`、`input`、`legend`、`div`、`h1`、`h2`、`h3`、`h4`、`h5`、`h6`、`p` | 使用 `CSS` 样式表代替                                        |
| `alink`、`link`、`text`、`vlink`、`background`、`bgcolor`    | `body`                                                       | 使用 `CSS` 样式表代替                                        |
| `align`、`bgcolor`、`border`、`cellpadding`、`cellspacing`、`frame`、`rules`、`width` | `table`                                                      | 使用 `CSS` 样式表代替                                        |
| `align`、`char`、`charoff`、`height`、`nowrap`、`valign`     | `tbody`、`thead`、`tfoot`                                    | 使用 `CSS` 样式表代替                                        |
| `align`、`bgcolor`、`char`、`charoff`、`height`、`nowrap`、`valign`、`width` | `td`、`th`                                                   | 使用 `CSS` 样式表代替                                        |
| `align`、`bgcolor`、`char`、`charoff`、`valign`              | `tr`                                                         | 使用 `CSS` 样式表代替                                        |
| `align`、`char`、`charoff`、`valign`、`width`                | `col`、`colgroup`                                            | 使用 `CSS` 样式表代替                                        |
| `align`、`border`、`hspace`、`vspace`                        | `object`                                                     | 使用 `CSS` 样式表代替                                        |
| `clear`                                                      | `br`                                                         | 使用 `CSS` 样式表代替                                        |
| `compact`、`type`                                            | `ol`、`ul`、`li`                                             | 使用 `CSS` 样式表代替                                        |
| `compact`                                                    | `dl`                                                         | 使用 `CSS` 样式表代替                                        |
| `campact`                                                    | `menu`                                                       | 使用 `CSS` 样式表代替                                        |
| `width`                                                      | `pre`                                                        | 使用 `CSS` 样式表代替                                        |
| `align`、`hspace`、`vspace`                                  | `img`                                                        | 使用 `CSS` 样式表代替                                        |
| `align`、`noshade`、`size`、`width`                          | `hr`                                                         | 使用 `CSS` 样式表代替                                        |
| `align`、`frameborder`、`scrolling`、`marginwidth`           | `iframe`                                                     | 使用 `CSS` 样式表代替                                        |
| `autosubmit`                                                 | `menu`                                                       |                                                              |

