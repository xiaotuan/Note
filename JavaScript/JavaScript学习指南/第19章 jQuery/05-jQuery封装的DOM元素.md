### 19.4　jQuery封装的DOM元素

jQuery操作DOM的主要技巧是使用jQuery封装的DOM元素。任何使用jQuery的DOM操作，都是从一个“封装”了一系列DOM元素集合的jQuery对象开始（这里要注意，集合可能为空或只包含一个元素）。

jQuery函数（$或者jQuery）创建了一个jQuery包装的DOM元素集合（后面简称为“jQuery对象”，但要记住，jQuery对象持有一个DOM元素的集合）。jQuery函数的主要调用方式有两种：通过CSS选择器调用和通过HTML调用。

使用CSS选择器调用jQuery会返回一个与之匹配的jQuery对象（类似于document.querySelectorAll的返回结果）。例如，要获得一个匹配所有<p>标签的jQuery对象，只需要这样做：

```javascript
const $paras = $('p');
$paras.length;                         // 匹配的<p>标签数量
typeof $paras;                         // "object"
$paras instanceof $;                   // true
$paras instanceof jQuery;              // true
```

另一方面，使用HTML调用jQuery时，会根据提供的HTML创建一个新的DOM元素（类似于为某个元素设置innerHTML属性时所做的事情）

```javascript
const $newPara = $('<p>Newly created paragraph...</p>');
```

大家应该已经注意到，在这两个例子中，赋给jQuery对象的变量都以美元符号开头。虽然这不是必须的，但却是一个好的编程习惯。因为有了美元符号，就能迅速在代码中识别出jQuery对象。

