`util.inspect()` 方法用于精确将对象转换成字符串，通过第二个参数 `options` 为对象的显示提供了景区的控制：

```js
var test = { 
   a: { 
      b: { 
        c: { 
         d : 'test' 
        } 
      } 
   } 
}
var str = require('util').inspect(test, {showHidden: true, depth: 4 });
console.log(str);
```

支持的参数如下所述。

+ `showHidden` ：是否显示非枚举或符号属性（默认是 `false` ）。
+ `depth` ：对要显示的对象进行递归的次数（默认是2）。
+ `colors` ：如果是true，输出样式就会用ANSI颜色代码（默认是 `false` ）。
+ `customInspect` ：如果是 `false` ，那么被检查对象上的自定义 `inspect` 函数就不会被调用（默认是 `false` ）。s