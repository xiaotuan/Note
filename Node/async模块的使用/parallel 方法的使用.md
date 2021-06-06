`async.parallel` 方法会同时调用所有的异步函数，当所有函数都完成后，调用最终回调函数。下面脚本并行打开 3 个文件并读取内容：

```js
var fs = require('fs'),
    async = require('async');
async.parallel({
   data1 : function (callback) {
      fs.readFile('./data/fruit1.txt', 'utf8', function(err, data){
           callback(err,data);
       }); 
   }, 
   data2 : function (callback) {
      fs.readFile('./data/fruit2.txt', 'utf8', function(err, data){
           callback(err,data);
       });
   },
   data3 : function readData3(callback) {
      fs.readFile('./data/fruit3.txt', 'utf8', function(err, data){
           callback(err,data);
       });
   }, 
}, function (err, result) {
      if (err) {
         console.log(err.message);
      } else {
         console.log(result);
      }
});
```

如果这3个文件如下：

+ fruit1.txt: apples；
+ fruit2.txt: oranges；
+ fruit3.txt: peaches。

那么运行例3-7所得到的结果就会是：

```python
{ data1: 'apples\n', data2: 'oranges\n', data3: 'peaches\n' }
```
