使用 `console.dir()` 打印日志的方法如下：

```js
var util = require('util');
var today = new Date();
var test = { 
   a: { 
      b: { 
        c: { 
         d : 'test' 
        }, 
        c2 : 3.50 
      }, 
      b2 : true 
   }, 
   a2: today 
} 
util.inspect.styles.boolean = 'blue';
// output with util.inspect direct formatting
var str = util.inspect(test, {depth: 4, colors: true });
console.log(str);
// output using console.dir and options
console.dir(test, {depth: 4, colors: true});
// output using basic console.log
console.log(test);
// and JSON stringify
console.log(JSON.stringify(test, null, 4));
```

> 提示：
>
> `console.dir()` 函数支持 `util.inspect()` 中的3种属性： `showHidden` 、 `depth` 和 `colors` 。它不支持 `customInspect` 。如果将 `customInspect` 属性设为 `true` ，意味着这个对象会提供自己的检查函数。

