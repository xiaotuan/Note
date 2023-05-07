[toc]

<center><b>HTML 表单元素</b></center>

| HTML 元素                                                | 类型属性          | 事件处理程序 | 描述和事件                                                   |
| -------------------------------------------------------- | ----------------- | ------------ | ------------------------------------------------------------ |
| `<input type="button">` 或<br />`<button type="button">` | "button"          | onclick      | 按钮                                                         |
| `<input type="checkbox">`                                | "checkbox"        | onchange     | 复选按钮                                                     |
| `<input type="file">`                                    | "file"            | onchange     | 载入 Web 服务器的文件的文件名输入域；它的 value 属性是只读的 |
| `<input type="hidden">`                                  | "hidden"          | none         | 数据由表单提交，但对用户不可见                               |
| `<option>`                                               | none              | none         | Select 对象中的单个选项；事件处理程序在 Select 对象上，而非单独的 Option 对象上 |
| `<input type="password">`                                | "password"        | onchange     | 密码输入框，输入的字符不可见                                 |
| `<input type="radio">`                                   | "radio"           | onchange     | 单选按钮，同时只能选定一个                                   |
| `<input type="reset">` 或<br />`<button type="reset">`   | "reset"           | onclick      | 重置表单的按钮                                               |
| `<select>`                                               | "select-one"      | onchange     | 选项只能单选的列表或下拉菜单（另见 `<option>`）              |
| `<select multiple>`                                      | "select-multiple" | onchange     | 选项可以多选的列表（见 `<option>`）                          |
| `<input type="submit">` 或<br />`<button type="submit">` | "submit"          | onclick      | 表单提交按钮                                                 |
| `<input type="text">`                                    | "text"            | onchange     | 单行文本输入域；type 属性缺少或无法识别时默认的 `<input>` 元素 |
| `<textarea>`                                             | "textarea"        | onchange     | 多行文本输入域                                               |

### 1. 表单和表单元素的属性

JavaScript 的 Form 对象支持两个方法：`submit()` 和 `reset()`，它们完成同样的目的。调用
Form 对象的 `submit()` 方法来提交表单，调用 `reset()` 方法来重置表单元素的值。  

所有（或多数）表单元素通常都有以下属性。如果一些元素有其他专用的属性：

+ type

  标识表单元素类型的只读的字符串。针对用 `<input>` 标签定义的表单元素而言，就是其 `type` 属性的值。  

+ form

  对包含元素的 Form 对象的只读引用，或者如果元素没有包含在一个 `<form>` 元素中则其值为 null。  

+ name 

  只读的字符串，由 HTML 属性 name 指定。  

+ value

  可读/写的字符串，指定了表单元素包含或代表的“值”。它就是当提交表单时发送到Web服务器的字符串，也是 JavaScript 程序有时候会感兴趣的内容。  

### 2. 表单和元素的事件处理程序

每个 Form 元素都有一个 `onsubmit` 事件处理程序来侦测表单提交，还有一个 `onreset` 事件处理程序来侦测表单重置。表单提交前调用 `onsubmit` 程序；它通过返回 false 能够取消提交动作。  

> 注意，`onsubmit` 事件处理程序只能通过单击“提交”按钮来触发。直接调用表单的 `submit()` 方法不触发 `onsubmit` 事件处理程序。  

`onreset` 事件处理程序在表单重置之前调用，通过返回 false 能够阻止表单元素被重置。  

> 注意：`onreset` 只能通过单击“重置”按钮来触发。直接调用表单的 `reset()` 方法不触发 `onreset` 事件处理程序。  

当用户与表单元素交互时它们往往会触发 `click` 或 `change` 事件，通过定义 `onclick` 或 `onchange` 事件处理程序可以处理这些事件。 一般来说，当按钮表单元素激活（甚至当通过键盘而不是实际的鼠标单击发生激活）时它们会触发 `click` 事件。当用户改变其他表单元素所代表的值时它们会触发`change` 事件。  

表单元素在收到键盘的焦点时也会触发 `focus` 事件，失去焦点时会触发 `blur` 事件。  

关于事件处理程序有一点非常重要，在事件处理程序代码中关键字`this` 是触发该事件的文档元素的一个引用。既然在 `<form>` 元素中的元素都有一个 `form` 属性引用了该包含的表单，这些元素的事件处理程序总是能够通过 `this.form` 来得到 Form 对象引用。

### 3. 按钮

> 注意，超级链接与按钮一样提供了 `onclick` 事件处理程序。当 `onclick` 事件所触发的动作可以概念化为“跟随此链接”时就用一个链接；否则，用按钮。  

提交和重置元素本就是按钮，不同的是它们有与之相关联的默认动作（表单的提交和重置）。如果`onclick` 事件处理程序返回 false，这些按钮的默认动作就不再执行了。可以使用提交元素的 `onclick` 事件处理程序来执行表单校验，但是更为常用的是使用 Form 对象本身的 `onsubmit` 事件处理程序来执行表单校验。  

### 4. 开关按钮

复选框和单选元素是开关按钮，或称有两种视觉状态的按钮：选中或未选中。  

单选和复选框元素都定义了 `checked` 属性。该属性是可读/写的布尔值，它指定了元素当前是否选中。 `defaultChecked` 属性也是布尔值，它是 HTML 属性 `checked` 的值；它指定了元素在第一次加载页面时是否选中。  

设置 `value` 只改变提交表单时发送到 Web 服务器的字符串。当用户单击单选或复选开关按钮，单选或复选框元素触发 `onclick` 事件。如果由于单击开关按钮改变了它的状态，它也触发 `onchange` 事件。（但注意，当用户单击其他单选按钮而导致这个单选按钮状态的改变，后者不触发 `onchange` 事件。）  

### 5. 文本域

`value` 属性表示用户输入的文本。通过设置该属性值可以显式地指定应该在输入域中显示的文
本。

在 HTML 5 中，`placeholder` 属性指定了用户输入前在输入域中显示的提示信息：  

```html
<input type="text" name="arrival" placeholder="yyyy-mm-dd" />
```

文本输入域的 `onchange` 事件处理程序是在用户输入新的文本或编辑已存在的文本时触发，它表明用户完成了编辑并将焦点移出了文本域。  

不同的文本输入元素定义 `onkeypress`、`onkeydown` 和 `onkeyup` 事件处理程序。可以从onkeypress或 `onkeydown` 事件处理程序返回 false，防止记录用户的按键。  

### 6. 选择框和选项元素

`Select` 元素表示用户可以做出选择的一组选项（用 `Option`元素表示）。浏览器通常将其渲染为下拉菜单的形式，但当指定其 `size` 属性值大于 1 时，它将显示为列表中的选项（可能有滚动）。`Select` 元素能以两种不同的方式运作，这取决于它的 `type` 属性值是如何设置的。如果 `<select>` 元素有 `multiple` 属性，也就是 `Select` 对象的 `type` 属性值为 “selectmultiple”，那就允许用户选取多个选项。否则，如果没有多选属性，那只能选取单个选项，它的 `type` 属性值为 “select-one”。  

当用户选取或取消选取一个选项时，Select 元素触发 `onchange` 事件处理程序。针对 “select-one” Select 元素，它的可读/写属性 `selectedIndex` 指定了哪个选项当前被选中。针对 “select-multiple” 元素，单个 `selectedIndex` 属性不足以表示被选中的一组选项。在这种情况下，要判定哪些选项被选中，就必须遍历 `options[]` 数组的元素，并检测每个 Option 对象的 `selected` 属性值。  

除了其 `selected` 属性，每个 Option 对象有一个 `text` 属性，它指定了在 Select 元素中的选项所显示的纯文本字符串。设置该属性可以改变显示给用户的文本。`value` 属性指定了在提交表单时发送到 Web 服务器的文本字符串，它也是可读/写的。  

除了设置 Option 对象的 `text` 属性以外，使用 `options` 属性的特殊功能可以动态改变显示在 Select 元素中的选项。通过设置 `options.length` 为一个希望的值可以截断 Option 元素数组，而设置`options.length` 为 0 可以从 Select 元素中移除所有的选项。设置 `options[]` 数组中某点的值为 null 可以从 Select 元素中移除单个 Option 对象。这将删除该 Option 对象，`options[]` 数组中高端的元素自动移下来填补空缺。

为 Select 元素增加一个新的选项，首先用 `Option()` 构造函数创建一个 Option 对象，然后将其添加到 `options[]` 属性中，代码如下：  

```js
// 创建一个新的选项
var zaire = new Option("Zaire",	// text 属性
                       "zaire", // value 属性
                       false,	// defaultSelected 属性
                       false);	// selected 属性
// 通过添加到 options 数组中，在 Select 元素中显示该选项
var countries = document.address.country;	// 得到 Select 对象
countries.options[countries.options.length] = zaire;
```

请牢记一点，这些专用的 Select 元素的 API 已经很老了。可以用那些标准的调用更明确地插入和移除选项元素：`Document.createElement()`、`Node.insertBefore()`、`Node.removeChild()` 等。  