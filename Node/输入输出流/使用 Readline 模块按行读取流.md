Node 为只读流提供了特定功能：`readline`。你可以使用如下代码来将 `Readline` 模块包含到你的程序中：

```js
var readline = require('readline');
```

一旦你在 Node 程序中包括这个模块并创建了接口来使用它，程序将不会终止，知道你关闭这个接口。

**示例：使用 Readline 库创建一个简单的命令驱动型用户界面**

```js
var readline = require('readline');

// create a new interface
var interface = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

// ask question
interface.question(">>What is the meaning of life? ", function(answer) {
    console.log("About the meaning of life, you said " + answer);
    interface.setPrompt(">> ");
    interface.prompt();
});

// function to close interface
function closeInterface() {
    console.log('Leaving interface...');
    process.exit();
}

// listen for .leave
interface.on('line', function(cmd) {
    if (cmd.trim() == '.leave') {
        closeInterface();
        return;
    } else {
        console.log("repeating command: " + cmd);
    }
    interface.setPrompt(">> ");
    interface.prompt();
});

interface.on('close', function() {
    closeInterface();
});
```

