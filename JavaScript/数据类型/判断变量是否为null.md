判断一个值是否为空类型的最佳方法是直接和 null 比较：

```js
console.log(value === null);	// true or false
```

>   注意： 必须使用三等号进行判断，因为双等号会进行类型转换。

