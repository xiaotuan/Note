### 9.1.2　Object.keys

`Object.keys` 提供了一种方式用来获取对象中所有可枚举的字符串属性，并将结果封装成一个数组。

```javascript
const SYM = Symbol();
const o = { a: 1, b: 2, c: 3, [SYM]: 4 };
Object.keys(o).forEach(prop => console.log('${prop}: ${o[prop]}'));
```

这个例子的结果跟使用 `for…in` 循环的结果一样（不需要检查 `hasOwnProperty` ）。当需要一个由对象中所有属性的键组成的数组时，使用它就会很方便。例如，它可以很容易地列出某个对象中所有以字符x开头的属性。

```javascript
const o = { apple: 1, xochitl: 2, balloon: 3, guitar: 4, xylophone: 5,};
Object.keys(o)
  .filter(prop => prop.match(/^x/))
  .forEach(prop => console.log('${prop}: ${o[prop]}'));
```

