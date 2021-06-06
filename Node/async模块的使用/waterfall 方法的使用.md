`async.waterfall` 方法有两个参数：一个任务数组和一个可选的最终回调函数。每个异步任务函数都是 `async.waterfall` 数组的一个元素，每个函数也都需要一个回调作为其最后一个参数。`async.waterfall` 方法会依次执行任务数组中的每个任务，`Async` 会检查每个回调函数的第一个参数是不是错误对象。如果我们在回调函数中传递了一个错误对象，那调用过程将立即结束，然后调用最后的回调函数。我们只能在最后回调的地方处理错误对象或最终结果。

下面的脚本使用 `async.waterfall` 来异步读取、修改和写入文件内容：

```js
var fs = require('fs'),
    async = require('async');
async.waterfall([
   function readData(callback) {
      fs.readFile('./data/data1.txt', 'utf8', function(err, data){
           callback(err,data);
       }); 
   }, 
   function modify(text, callback) {
      var adjdata=text.replace(/somecompany\.com/g,'burningbird.net');
      callback(null, adjdata);
   },
   function writeData(text, callback) {
       fs.writeFile('./data/data1.txt', text, function(err) {
          callback(err,text);
       });
   } 
], function (err, result) {
      if (err) {
        console.error(err.message);
      } else {
        console.log(result);
      }
});
```

下面代码从目录获取对象、测试文件查找、读取文件、修改文件，最后写回文件并记录日志：

```js
var fs = require('fs'),
    async = require('async'),
    _dir = './data/';
var writeStream = fs.createWriteStream('./log.txt',
      {'flags' : 'a',
       'encoding' : 'utf8',
       'mode' : 0666});
async.waterfall([
   function readDir(callback) {
      fs.readdir(_dir, function(err, files) {
         callback(err,files);
      });
   }, 
   function loopFiles(files, callback) {
      files.forEach(function (name) {
         callback (null, name);
      });
   }, 
   function checkFile(file, callback) {
      fs.stat(_dir + file, function(err, stats) {
         callback(err, stats, file);
      });
   },
   function readData(stats, file, callback) {
      if (stats.isFile())
         fs.readFile(_dir + file, 'utf8', function(err, data){
           callback(err,file,data);
         });
   },
   function modify(file, text, callback) {
      var adjdata=text.replace(/somecompany\.com/g,'burningbird.net');
      callback(null, file, adjdata);
   },
   function writeData(file, text, callback) {
       fs.writeFile(_dir + file, text, function(err) {
          callback(err,file);
       });
   },
   function logChange(file, callback) {
       writeStream.write('changed ' + file + '\n', 'utf8',
                       function(err) {
          callback(err);
       });
   }
], function (err) {
         if (err) {
            console.error(err.message);
         } else {
            console.log('modified files');
         }
});
```

