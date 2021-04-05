### 18.4　DOM中的“Get”方法

DOM提供了“get”方法，可以帮助快速定位指定的HTML元素。

第一个方法是 `document.getElementById` 。页面中的每个HTML元素都可以指定一个独一无二的ID，而 `document.getElementById` 可以通过一个元素的ID来获取它。

```javascript
document.getElementById('content');     // <div id="content">...</div>
```

> <img class="my_markdown" src="../images/3.png" style="width:151px;  height: 145px; " width="10%"/>
> 浏览器并不会强制要求给元素指定唯一的ID（虽然HTML检查器会发现这个问题），所以保证每个元素拥有唯一的ID是开发人员义不容辞的责任。随着web页面结构复杂度的增加（页面中的组件也可能来自多个代码源），避免出现重复ID的困难性也随之升高。所以，作者建议大家在使用ID时小心一些，节省一些。

`document.getElementsByClassName` 会返回通过class名查找到的元素集合。

```javascript
const callouts = document.getElementsByClassName('callout');
而`document.getElementsByTagName`则返回符合给定tag名称的元素集合。
const paragraphs = document.getElementsByTagName('p');
```

> <img class="my_markdown" src="../images/3.png" style="width:151px;  height: 145px; " width="10%"/>
> 所有返回集合的DOM方法返回的都不是一个JavaScript数组，而是一个HTMLCollection的实例，这是一个“类似数组”的对象。可以在for循环中迭代它们，但却不能使用 `Array.prototype` 方法（同样不能使用的方法还有 `map` ,  `filter` 和 `reduce` ）。通过使用展开操作符（ `spread operator` ），可以把一个HTMLCollection转化成数组： `[...document.getElementsByTagName(p)]` 。

