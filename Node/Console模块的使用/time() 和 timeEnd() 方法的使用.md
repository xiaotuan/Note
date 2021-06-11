可以使用 `console.time()` 和 `console.timeEnd()` 方法来计算执行某段代码所需时间，例如：

```js
console.time('the-loop');
for (var i = 0; i < 10000; i++) {
   ;
}
console.timeEnd('the-loop');
```

输出结果如下：

```console
the-loop: 1.101ms
```

