如果在 HTML 文档中用 `id` 属性来为元素命名，并且如果 Window 对象没有此名字的属性，`Window` 对象会赋予一个属性，它的名字是 `id` 属性的值，而它们的值指向表示文档元素的 `HTMLElement` 对象。例如，如果文档包含一个 `<button id="okay"/>` 元素，可以通过 `window.okay` 来引用此元素。

> 警告：如果 `Window` 对象已经具有此名字的属性，这就不会发生。比如，`id` 是 `history`、`location` 或 `navigator` 的元素，就不会以全局变量的形式出现，因为这些 ID 已经占用了。

可以通过 `document.getElementById()` 方法，用 HTML 的 `id` 属性来查找文档元素：

```js
var ui = [ "input", "prompt", "heading" ];	// 数组中存放要查找的元素 id
ui.forEach(function(id) {	// 用每个 id 查找对应的元素
	ui[id] = document.getElementById(id);	// 将其存放在一个属性中
});
```

以下 HTML 元素如果有 `name` 属性的话，也会这样表现：

```
<a> <applet> <area> <embed> <form> <frame> <frameset> <iframe> <img> <object>
```

如果上面的元素有多于一个相同的 `name` 属性（或者一个元素有 `name` 属性，而另一个元素具有相同值的 `id` 属性），具有该名称的隐式全局变量会引用一个类数组对象，这个类数组对象的元素是所有命名的元素。

有 `name` 或 `id` 属性的 `<iframe>` 元素是个特殊的例子。为它们隐式创建的变量不会引用表示元素自身的 `Element` 对象，而是引用表示 `<iframe>` 元素创建的嵌套浏览器窗体的 `Window` 对象。