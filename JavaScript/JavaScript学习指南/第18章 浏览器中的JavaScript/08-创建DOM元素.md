### 18.7　创建DOM元素

大家已经知道如何通过设置元素的innerHTML属性来隐式地创建DOM节点。其实还可以通过 `document.createElement` 来显式地创建节点。这个函数可以创建一个新元素，但它并不会将元素添加到DOM中，必须再单独做一次添加操作。下面，创建两个段落元素，分别作为 `<div id="content">` 中的第一个元素和第二个元素：

```javascript
const p1 = document.createElement('p');
const p2 = document.createElement('p');
p1.textContent = "I was created dynamically!";
p2.textContent = "I was also created dynamically!"; 
```

为了把新创建的元素添加到DOM中，这里要用到 `insertBefore` 和 `appendChild` 方法。首先，需要获取父元素（ `<div id="content">` ）和它的第一个子节点：

```javascript
const parent = document.getElementById('content');
const firstChild = parent.childNodes[0];
```

现在可以添加新创建的元素：

```javascript
parent.insertBefore(p1, firstChild);
parent.appendChild(p2);

```

`insertBefore` 接收两个参数，第一个是要插入的新元素，第二个是“参考节点”，新元素会插入到参考节点之前。 `appendChild` 则很简单，它会把指定元素作为节点的最后一个子节点插入。

