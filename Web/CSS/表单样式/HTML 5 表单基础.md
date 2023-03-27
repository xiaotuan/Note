一般情况下，表单结构可分为以下 3 部分：　

+ 表单框：使用 `<form>` 标签定义，主要功能为定义提交表单的处理方法、URL 和字符编码等。　

+ 表单对象：包括文本框、密码框、隐藏域、多行文本框、复选框、单选按钮、下拉选择框、文件上传框、提交按钮、复位按钮和一般按钮等。　

+ 辅助对象：包括提示性标签 `<label>` 、表单对象分组标签 `<fieldset>`，用于表单结构的辅助设计。

<center><b>HTML 表单标签</b></center>

| 标签        | 说明                                   |
| ----------- | -------------------------------------- |
| \<form>     | 定义供用户输入的 HTML 表单             |
| \<input>    | 定义输入控件                           |
| \<textarea> | 定义多行的文本输入控件                 |
| \<button>   | 定义按钮                               |
| \<select>   | 定义选择列表（下拉列表）               |
| \<optgroup> | 定义选择列表中相关选项的组合           |
| \<option>   | 定义选择列表中的选项                   |
| \<label>    | 定义 input 元素的标注                  |
| \<fieldset> | 定义围绕表单中元素的边框               |
| \<legend>   | 定义 fieldset 元素的标题               |
| \<isindex>  | 定义与文档相关的可搜索索引。不赞成使用 |
| \<datalist> | HTML5 新增标签，定义下拉列表           |
| \<keygen>   | HTML5 新增标签，定义生成密钥           |
| \<output>   | HTML5 新增标签，定义输出的一些类型     |

<center><b>&lt;input&gt; 标签可定义的输入型表单对象</b></center>

| 表单对象                       | 说明                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| \<input type="text">           | 单行文本输入框                                               |
| \<input type="password">       | 密码输入框（输入的文字用点号表示）                           |
| \<input type="checkbox">       | 复选框                                                       |
| \<input type="radio">          | 单选按钮                                                     |
| \<input type="file">           | 文件域                                                       |
| \<input type="submit">         | 将表单（form）里的信息提交给表单属性 action 所指定的文件     |
| \<input type="reset">          | 将表单（form）里的信息清空，重新填写                         |
| \<input type="color">          | HTML5 新增对象，颜色选择器                                   |
| \<input type="date">           | HTML5 新增对象，日期选择器                                   |
| \<input type="time">           | HTML5 新增对象，时间选择器                                   |
| \<input type="datetime">       | HTML5 新增对象，UTC 日期时间选择器                           |
| \<input type="datetime-local"> | HTML5 新增对象，本地日期时间选择器                           |
| \<input type="week">           | HTML5 新增对象，选择第几周的文本框                           |
| \<input type="month">          | HTML5 新增对象，月份选择器                                   |
| \<input type="email">          | HTML5 新增对象，Email 输入框                                 |
| \<input type="tel">            | HTML5 新增对象，电话输入框                                   |
| \<input type="url">            | HTML5 新增对象，URL 输入框                                   |
| \<input type="number">         | HTML5 新增对象，只能输入数字的文本框                         |
| \<input type="range">          | HTML5 新增对象，拖动条或滑块                                 |
| \<input type="search">         | HTML5 新增对象，搜索文本框，与 `type="text"` 的文本框没有太大区别 |

