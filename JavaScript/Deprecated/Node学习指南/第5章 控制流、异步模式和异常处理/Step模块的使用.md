`Step` 是一个用于简化串行和并行控制流的使用模块。通过下面这条 npm 指令可以安装它：

```console
$ npm install step
```

**示例5-7 使用 Step 执行串行异步任务**

```js
var fs = require('fs')
var step = require('step')

try {
  step(
    function readData() {
      fs.readFile('./data/data1.txt', 'utf8', this)
    },
    function modify(err, text) {
      if (err) throw err
      return text.replace(/somecompany\.com/g, 'burningbird.net')
    },
    function writeData(err, text) {
      if (err) throw err
      fs.writeFile('./data/data1.txt', text, this)
    }
  )
} catch (err) {
  console.error(err)
}
```

> 提示
> 欲了解更多信息，请参阅 step 在 GitHub 上的站点：<https://github.com/creationix/step>

在 `Step` 调用序列中，除第一个函数外，其余函数的第一个参数都应该是 error。

**示例5-8 使用 Step 的 group() 将异步处理分组**

```js
var fs = require('fs')
var step = require('step')

var files
var _dir = './data/'

try {
  step(
    function readDir() {
      fs.readdir(_dir, this)
    },
    function readFile(err, results) {
      if (err) throw err
      files = results
      var group = this.group()
      results.forEach(name => {
        fs.readFile(_dir + name, 'utf8', group())
      });
    },
    function writeAll(err, data) {
      if (err) throw err
      for (var i = 0; i < files.length; i++) {
        var adjdata = data[i].replace(/somecompany\.com/g, 'burningbird.net')
        fs.writeFile(_dir + files[i], adjdata, 'utf8', this)
      }
    }
  )
} catch(err) {
  console.log(err)
}
```

如果处理的数据数量是固定的，那么就可以进行硬编码并使用 `Step` 提供的 parallel 来实现。

**示例5-9 使用 Step 模块的 parallel 功能对一组文件进行读写操作**

```js
var fs = require('fs')
var step = require('step')

var files

try {
  step(
    function readFiles() {
      fs.readFile('./data/data1.txt', 'utf8', this.parallel())
      fs.readFile('./data/data2.txt', 'utf8', this.parallel())
      fs.readFile('./data/data3.txt', 'utf8', this.parallel())
    },
    function writeFiles(err, data1, data2, data3) {
      if (err) throw err
      data1 = data1.replace(/somecompany\.com/g, 'burningbird.net')
      data2 = data2.replace(/somecompany\.com/g, 'burningbird.net')
      data3 = data3.replace(/somecompany\.com/g, 'burningbird.net')

      fs.writeFile('./data/data1.txt', data1, 'utf8', this.parallel())
      fs.writeFile('./data/data2.txt', data2, 'utf8', this.parallel())
      fs.writeFile('./data/data3.txt', data3, 'utf8', this.parallel())
    }
  )
} catch (err) {
  console.log(err)
}
```
