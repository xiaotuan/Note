**示例5-1 使用 Node promise**

```js
var fs = require('fs')

exports.read = test_and_load

function test_and_load(filename) {
  return new Promise(function (resolve, reject) {
    fs.stat(filename, function (err, stat) {
      if (err) {
        reject(err)
      } else {
        // Filter out non-files
        if (!stat.isFile()) {
          resolve()
          return
        }
        
        // Otherwise read the file in
        fs.readFile(filename, 'utf8', function (err, data) {
          if (err) {
            reject(err)
          } else {
            resolve(data)
          }
        })
      }
    })
  })
}
```

测试Promise：

```js
var File = require('./UsePromise.js')

File.read('dsf.txt').then(function(data) {
  console.log("data: " + data)
}).catch(function (err) {
  console.log("error: " + err)
})
```

**示例5-2  last callback functionality 的基本结构**

```js
var obj = function() {}

obj.prototype.doSomething = function (arg1, arg2_) {
  var arg2 = typeof(arg2_) === 'string' ? arg2_ : null
  
  var callback_ = arguments[arguments.length - 1]
  callback = (typeof(callback_) == 'function' ? callback_ : null)

  if (!arg2) {
    return callback(new Error('second argument missing or not a string'))
  }
  callback(arg1)
}

var test = new obj()

try {
  test.doSomething('test', 3.55, function (err, value) {
      if (err) throw err

      console.log(value)
  })
} catch(err) {
  console.error(err)
}
```


