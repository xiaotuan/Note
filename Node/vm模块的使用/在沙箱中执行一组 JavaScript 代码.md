[toc]

### 1. runInNewContext()

为了避免造成某些意料不到的结果，可以使用 `VM` 将该脚本与本地环境隔离开。脚本可以先使用 `vm.Script` 对象进行预编译，也可以作为 `vm` 的参数直接被调用。`script.runInNewContext()` 或 `vm.runInNewContext()` 可以在新的上下文中运行脚本，脚本无法访问局部变量或全局变量。

```js
var vm = require('vm')

var sanbox = {
    process: 'this body',
    require: 'that',
    console: console
}
vm.runInNewContext('console.log(process);console.log(require)', sanbox)
```

> 注意：使用 `vm.runInNewContext()` 方法创建的新上下文是没有任何方法和对象的，需要通过第二个参数  `sanbox` 将需要的方法和对象传入其中。比如上面的例子，如果在 `sanbox` 中没有传入 `console` 对象的话，在 `runInNewContext()` 方法中要执行的 `JavaScript` 脚本是不会执行的。

### 2. runInThisContext()

上面的代码无法为脚本代码创建一个全新的上下文的目的。如果希望脚本能够访问全局 `console` 对象（或其他对象），可以使用 `runInThisContext()` 函数。

```js
var vm = require('vm');
global.count1 = 100;
var count2 = 100;
var txt = 'if (count1 === undefined) var count1 = 0; count1++;' +
          'if (count2 === undefined) var count2 = 0; count2++;' +
          'console.log(count1); console.log(count2);';
var script = new vm.Script(txt);
script.runInThisContext({filename: 'count.vm'});
console.log(count1);
console.log(count2);
```

`filename` 选项用于指定运行脚本时在堆栈跟踪中显示的文件名，如果要为 `Script` 对象指定文件名，则一定要在创建 `Script` 对象时就指定，而不是在上想问函数调用时才指定：

```js
var vm = require('vm');
global.count1 = 100;
var count2 = 100;
var txt = 'count1++;' +
          'count2++;' +
          'console.log(count1); console.log(count2);';
var script = new vm.Script(txt, {filename: 'count.vm'});
try {
  script.runInThisContext();
} catch(err) {
  console.log(err.stack);
}
```

除了直接在程序中写脚本外，我们还可以从文件中加载脚本。假如要运行下面这段脚本：

```js
if (count1 === undefined) var count1 = 0; count1++;
if (count2 === undefined) var count2 = 0; count2++;
console.log(count1); console.log(count2);
```

我们可以使用这段代码来预编译并在沙箱中运行：

```js
var vm = require('vm');
var fs = require('fs');
global.count1 = 100;
var count2 = 100;
var script = new vm.Script(fs.readFileSync('script.js','utf8'));
script.runInThisContext({filename: 'count.vm'});
console.log(count1);
console.log(count2);
```

> 注意：沙漏中没有 `require` 方法，所有不能在执行的脚本文件中使用 `require` 方法。

### 3. runInContext()

`runInContext()` 函数同样支持 `runInThisContext()` 和 `runInNewContext()` 的 3 个选项。它会提供一个沙箱，但沙箱必须在函数调用之前进行语境化（显示地创建上下文）。

```js
var vm = require('vm');
var util = require('util');
var sandbox = {
     count1 : 1
    }; 
vm.createContext(sandbox);
if (vm.isContext(sandbox)) console.log('contextualized');
vm.runInContext('count1++; counter=true;',sandbox,
                {filename: 'context.vm'});
console.log(util.inspect(sandbox));
```

