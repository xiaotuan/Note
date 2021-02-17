[toc]

### 1. 获取 HTML 元素

在 DOM 中有三种方法能够获取元素节点，分别是通过元素 ID、通过标签名称和通过类名称来进行获取。

#### 1.1 getElementById

`getElementById` 调用将返回一个对象，该方法只有一个参数：想要获得的那个元素的 id 属性的值，这个 id 属性值必须放在单引号或者双引号里，其使用方法如下所示：

```js
document.getElementById("purchases");
```

#### 1.2 getElementsByTagName

`getElementsByTagName` 方法返回一个对象数组，每个对象分别对应着文档里有着给定标签的一个元素。

```js
element.getElementsByTagName(tag);
```

这个数组里的每一个元素都是一个对象，可以使用 `getElementsByTagName` 方法结合循环语句与 typeof 操作符进行验证，其使用方法如下所示：

```js
for (var i = 0; i < document.getElementsByTagName("li").length; i++) {
    alert(typeof document.getElementsByTagName("li")[i])
}
```

应当注意的是，即使在整个文档中这个标签只有一个元素，`getElementsByTagName` 方法返回的也是一个数组，只是这个数组的长度为 1。

`getElementsByTagName` 方法允许把一个通配符作为它的参数。通配符 "*" 必须放在引号里面，这是为了让通配符与乘法操作符有所区别。下面的代码可以得到文档中总共有多少个元素节点。

```js
alert(document.getElementsByTag("*").length);
```

可以将 `getElementsByTagName` 与 `getElementById` 结合起来使用，比如想要得到某个 id 属性值为 purchases 的元素包含多少个列表项，其实现代码如下所示：

```js
var shop = document.getElementById("purchases");
var items = shop.getElementsByTagName("*");
alert(items.length);
```

#### 1.3 getElementsByClassName

`getElementsByClassName` 是 HTML 5 DOM 中新增了一个方法，其在 Internet Explorer 5/6/7/8 中无效，因此在使用时要注意兼容性。其使用方法如下所示：

```js
element.getElementsByClassName(class);
```

`getElementsByClassName` 方法还可查找那些带有多个类名的元素。如果要指定多个类名只需在字符串参数中用空格分隔开类名即可，使用方法如下所示：

```js
alert(document.getElementsByClassName("import sale").length);
```

由于兼容性问题，需要对齐自定义 `getElementsByClassName` 方法，其函数内容如下所示：

```js
function getElementsByClassName(node, classname) {
    // 如果浏览器支持 getElementsByClassName 解析
    if (node.getElementsByClassName) {
        return node.getElementsByClassName(classname);
    } else {
        var results = new Array();
        var elems = node.getElementsByTagName("*");
        for (var i = 0; i < elems.length; i++) {
            if (elems[i].className.indexOf(classname) != -1) {
                results[results.length] = elems[i];
            }
        }
        return results;
    }
}
```

### 2. 对 HTML 元素进行操作

#### 2.1 增加元素

如果需要向 HTML 中添加新元素，那么首先便需要创建该元素，然后向已存在的元素追加创建的新元素。

`document.createElement()` 方法和 `document.createTextNode()` 方法分别用来创建新的 Element 节点和 Text 节点，而方法 `node.appendChild()`、`node.insertBefore()` 和 `node.replaceChild()` 可以用来创建好的元素添加到一个文档，其具体实现方法如下：

① 首先需要创建一个新的元素，比如 `<p>`，其代码如下所示：

```js
var para = document.createElement("p");
```

② 如果需要向 `<p>` 元素中添加文本内容，必须先创建一个文本节点，代码如下所示：

```js
var node = document.createTextNode("这是创建的新段落。");
```

③ 然后将该文本节点追加到刚才创建的 `<p>` 元素中，代码如下所示：

```js
para.appendChild(node);
```

④ 最后必须向一个已有的元素追加这个新建的元素，其实现代码如下所示：

```js
var element = document.getElementById("div1");
element.appendChild(para);
```

#### 2.2 修改元素

##### 2.2.1 修改元素的内容

修改元素内容的最简单方法便是使用 innerHTML 属性，使用该属性可以对元素的内容重新赋值，从而达到修改元素内容的效果，其使用方法如下所示：

```js
document.getElementById(id).innerHTML = new HTML;
```

比如想要改变一个段落的内容，代码如下所示：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>改变元素内容</title>
        <script>
        	document.getElementById("p1").innerHTML = "New text!";
        </script>
    </head>
    <body>
        <p id="p1">Hello World!</p>
    </body>
</html>
```

##### 2.2.2 修改元素属性

`getAttribute` 是一个函数，它只有一个参数，即：查询的属性的名称，其使用方法如下所示：

```js
object.getAttribute(attribute);
```

`getAttribute` 方法不属于 document 对象，它只能通过元素节点对象调用，代码如下所示：

```js
var para = document.getElementsByTagName("p");
for (var i = 0; i < para.lenght; i++) {
    alert(para[i].getAttribute("title"));
}
```

`setAttribute()` 方法是用来设置属性的，它允许对属性节点的值做出修改，其使用方法如下所示：

```js
object.setAttribute(attribute, value);
```

下面一个例子用来展示 `setAttribute()` 方法改变了元素的 title 属性，代码如下所示：

```js
var shop = document.getElementById("purchases");
alert(shop.getAttribute("title"));
shop.setAttribute("title", "a list");
alert(shop.getAttribute("title"));
```

##### 2.2.3 删除元素

如果需要在 HTML 中删除元素，首先便需要获得该元素，然后得到该元素的父元素，最后通过 `removeChild` 方法删除该元素，其实现流程如下：

① 获得该元素，比如要获得 id 属性值为 div1 的元素，其代码如下所示：

```js
var child = document.getElementById("p1");
```

② 获得该元素的父元素，代码如下所示：

```js
var parent = document.getElementById("div1");
```

③ 从父元素中删除该元素，代码如下所示：

```js
parent.removeChild(child);
```

可以对以上代码进行优化，从而实现元素的删除，优化后的代码如下所示：

```js
var child = document.getElementById("p1");
child.parentNode.removeChild(child);
```

