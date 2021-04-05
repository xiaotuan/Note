### 19.6　展开jQuery对象

如果需要“展开”一个jQuery对象（访问底层的DOM元素），可以使用get方法。比如，为了获取第二个段落的DOM元素，可以这么做：

```javascript
const para2 = $('p').get(1);      // 第二个<p> (小标从零开始)
```

获得一个包含所有段落的DOM元素的数组：

```javascript
const paras = $('p').get();       // 包含所有<p>元素的数组
```

