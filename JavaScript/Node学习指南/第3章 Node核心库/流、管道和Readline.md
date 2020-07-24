`Node` 中所有流都支持一套基本的功能调用：

+ 可以通过 `setEncoding` 方法更改流数据所使用的编码方式；
+ 可以检查当前流是否可读，是否可写，或者是否可读写；
+ 可以捕捉流事件，如接收到新数据或连接关闭，并能为每个事件附加回调函数；
+ 可以挂起和恢复流；
+ 可以使用 pipe 将一个可读流与一个可写流连接起来。

```console
> process.stdin.resume()
> process.stdin.pipe(process.stdout)
```

如果你想让输出流保持打开状态并接收连续输入的数据，可以在调用 pipe 方法时传入参数 `{end: false}`：

```js
process.stdin.pipe(process.stdout, { end: false })
```

`Node` 还为只读流提供了 readline 模块：

```js
var readline = require('readline')
```

一旦在 `Node` 程序中包含 `Readline` 模块并创建了接口来使用它，程序将不会终止，直到你关闭这个接口。

**示例 3-8 使用 Readline 库创建一个简单的命令驱动型用户界面**

```js
var readline = require('readline')

// create a new interface
var interface = readline.createInterface(process.stdin, process.stdout, null)

// ask question
interface.question(">>What is the meaning of life? ", function (answer) {
   console.log("About the meaning of life, you said " + answer)
   interface.setPrompt(">>")
   interface.prompt()
})

// function to close interface
function closeInterface() {
   console.log('Leaving interface...')
   process.exit()
}

// listen for .leave
interface.on('line', function (cmd) {
   if (cmd.trim() == '.leave') {
      closeInterface()
      return
   } else {
      console.log('repeating command: ' + cmd)
   }
   interface.setPrompt(">>")
   interface.prompt()
})

interface.on('close', function () {
   closeInterface()
})
```