`window` 对象的 `setTimeout()` 方法可以注册一个函数，在给定的一段时间之后触发一个回调：

```js
// 等待两秒，然后说 hello
setTimeout(function() { alert("hello world"); }, 2000);
```

