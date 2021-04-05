### 9.1.1　for...in

for…in是枚举对象属性的传统方式。来看一个包含若干字符串属性和一个符号属性的对象的例子：

```javascript
const SYM = Symbol();
const o = { a: 1, b: 2, c: 3, [SYM]: 4 };
for(let prop in o) {
  if(!o.hasOwnProperty(prop)) continue;
  console.log(`${prop}: ${o[prop]}`);
} 
```

这似乎很直观，不过大家可能会好奇 `hasOwnProperty` 起什么作用。它解决了for…in循环内部可能存在的一个风险，本章后面讲解属性继承的时候会解答这个问题。这在个例子中，它不会对结果造成影响，可以暂时忽略它。然而，如果需要枚举其他类型的对象中的属性，尤其是从别处传来的对象，可能会得到一些意料之外的属性。所以鼓励大家养成使用 `hasOwnProperty` 的习惯。当然很快就会发现它的重要性，也将清楚在哪些情况下不需要使用它。

注意， `for…in` 循环不会枚举出键为符号的属性。

> <img class="my_markdown" src="../images/3.png" style="width:151px;  height: 145px; " width="10%"/>
> 虽然 `for…in` 也可以用来迭代数组，但这通常被认为是一个不好的实践。建议大家使用一般的for循环或forEach迭代数组。

