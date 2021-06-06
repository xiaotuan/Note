`async.serial` 方法与 `async.parallel` 方法类似，只是 `async.parallel` 以字典的形式创建任务列表，并以字典的形式返回结果；而 `async.serial` 方法以数组的形式创建任务列表，并以数组的形式返回结果；它们都是并行的执行任务列表；例如：

```js
var async = require("async");
async.series([
    function(callback) {
        // do some stuff
        callback(null,'one'); //如果有错误信息传err否则为空，传参数one
    },
    function(callback) {
        // do some more stuff ...
        callback(null, 'two');
    }],function(err, results) {
        console.log(results); //接收参数数组['one','two']，值是上面数组函数每个callback里面的参数
        console.log(err);     //捕获错误信息，如果没有则为空
    });
```

输出结果如下：

```
[ 'one', 'two' ]
null
```

