`Async` 模块提供了对集合的管理功能，例如 each、map 和 filter。此外它还提供了一些实用功能，例如 memoization。然而，此刻我们关心的是它对流程控制的支持。

安装 `Async` 模块

```console
$ npm install async
```

**示例5-10 使用 async.waterfall 异步实现读取，修改和写入文件内容**

```js
var fs = require('fs')
var async = require('async')

try {
  async.waterfall([
    function readData(callback) {
      fs.readFile('./data/data1.txt', 'utf8', function (err, data) {
        callback(err, data)
      })
    },
    function modify(text, callback) {
      var adjdata = text.replace(/somecompany\.com/g, 'burningbird.net')
      callback(null, adjdata)
    },
    function writeData(text, callback) {
      fs.writeFile('./data/data1.txt', text, function (err) {
        callback(err, text)
      })
    }
  ], function (err, result) {
    if (err) throw err
    console.log(result)
  })
} catch(err) {
  console.log(err)
}
```

`async.waterfall` 方法有两个参数：一个任务数组以及一个可选的最终回调函数。

callback 需要一个 error 对象作为第一参数。如果我们传递一个 error 对象给 callback 函数，整个处理过程将会在这一点结束，而最终回调函数（ waterfall 方法的第二个参数）会被调用。

**示例5-11 从目录中获取对象，测试并寻找文件；读取文件内容，修改并写回；记录修改日记**

```js
var fs = require('fs')
var async = require('async')

var _dir = './data/'
var modified = []

var writeStream = fs.createWriteStream('./log.txt', {
  'flags': 'a',
  'encoding': 'utf8',
  'mode': 0666
})

try {
  async.waterfall([
    function readDir(callback) {
      fs.readdir(_dir, function (err, files) {
        callback(err, files)
      })
    },
    function loopFiles(files, callback) {
      async.forEachOf(files, function (value, key, callback) {
        async.waterfall([
          function checkFile(callback) {
            fs.stat(_dir + value, function(err, stats) {
              callback(err, stats, value)
            })
          },
          function readData(stats, file, callback) {
            if (stats.isFile()) {
              fs.readFile(_dir + file, 'utf8', function (err, data) {
                callback(err, file, data)
              })
            }
          },
          function modify(file, text, callback) {
            var adjdata = text.replace(/somecompany\.com/g, 'burningbird.net')
            callback(null, file, adjdata)
          },
          function writeData(file, text, callback) {
            fs.writeFile(_dir + file, text, function (err) {
              callback(err, file)
            })
          },
          function logChange(file, callback) {
            writeStream.write('changed ' + file + '\n', 'utf8', function (err) {
              callback(err, file)
              modified.push(file)
            })
          }
        ], function (err, result) {
          if (err) throw err
          console.log('modified ' + result)
          callback(err, modified)
        })
      }, function (err) {
        if (err) throw err
        callback(err, modified)
      })
    },
  ], function (err, result) {
    if (err) throw err
    console.log('modified ' + result)
  })
} catch (err) {
  console.log(err)
}
```

我们可以在方法间传递任何数据，只要第一个参数是 error 对象（如果没有错误产生，则为 null ），并保证每个函数的最后一个参数是 callback 函数。

我们不必在每个异步任务函数中进行错误检查，因为 Async 会在每个 callback 被调用时检查 error 对象，如果发生错误，则停止处理并调用最终回调函数。

`async.parallel` 方法会一次性调用所有异步任务，当所有任务执行完毕时，将调用最终回调函数。

**示例5-12 使用并行方式打开三个文件并读取内容**

```js
var fs = require('fs')
var async = require('async')

try {
  async.parallel({
    data1: function (callback) {
      fs.readFile('./data/data1.txt', 'utf8', function (err, data) {
        callback(err, data)
      })
    },
    data2: function (callback) {
      fs.readFile('./data/data2.txt', 'utf8', function(err, data) {
        callback(err, data)
      })
    },
    data3: function readData3(callback) {
      fs.readFile('./data/data3.txt', 'utf8', function (err, data) {
        callback(err, data)
      })
    }
  }, function (err, result) {
    if (err) throw err
    console.log(result)
  })
} catch (err) {
  console.log(err)
}
```
