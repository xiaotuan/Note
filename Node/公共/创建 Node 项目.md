[toc]

### 1. 创建 Node 空项目

创建新的 `Node` 项目很简单：创建一个文件夹，运行 `npm init`。`npm` 命令会问几个问题，一直回答 `yes` 就可以了。

下面是一个完整的例子：

```shell
$ mkdir my_moudle
$ cd my_moudle
$ npm init -y
```

参数 `-y` 表示 `yes`。这样 `npm` 就会创建一个全部使用默认值的 `package.json` 文件。如果你想要更多的控制权，去掉参数 `-y`，你就能看到 `npm` 提出的一系列问题，包括授权许可、作者姓名等等。

### 2. 创建模块

如果模块是一个目录，`Node` 通常会在这个目录下找一个叫 `index.js` 的文件作为模块的入口。除非你再这个目录下一个叫 `package.json` 的文件里特别指明。要指定一个取代 `index.js` 的文件，`package.json` 文件里必须有一个用 `JavaScript` 对象表示数据定义的对象，其中有一个名为 `main` 的键，指明模块目录内主文件的路径。

下面是一个 `package.json` 文件的例子，它指定 `currency.js` 为主文件：

**package.json**

```json
{
  "name": "my_moudle",
  "version": "1.0.0",
  "description": "",
  "main": "currency.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

**currency.js**

```js
const canadianDollar = 0.91;

function roundTwo(amount) {
	return Math.round(amount * 100) / 100;
}

// canadianToUS 函数设定在 exports 模块中，所以引用这个模块的代码可以使用它
exports.canadianToUS = canadian => roundTwo(canadian * canadianDollar);

// USToCanadian 也设定在 exports 模块中
exports.USToCanadian = us => roundTwo(us / canadianDollar);
```

`exports` 对象上只设定了两个属性。也就是说引入这个模块的代码只能访问到 `canadianToUS` 和 `USToCanadian` 这两个函数。而变量 `canadianDollar` 作为私有变量仅作用在 `canadianToUS` 和 `USToCanadian` 的逻辑内部，程序不能直接访问它。

使用这个新模块要用到 `Node` 的 `require` 函数，该函数以所用模块的路径为参数。

> 注意：
>
> `require` 是 `Node` 中少数几个同步 `I/O` 操作之一。因为经常用到模块，并且一般都是在文件顶端引入，所以把 `require` 做成同步，有助于保持代码的整洁、有序，还能增强可读性。
>
> 但在 `I/O` 密集的地方尽量不要用 `require`。所有同步调用都会阻塞 `Node`，直到调用完成才能做其他事情。

下面这个是 `test-currency.js` 中的代码，它 `require` 了 `currency.js` 模块：

**test-currency.js**

```js
// 用路径 ./ 表明模块跟程序脚本放在同一目录下
const currency = require('./currency');

console.log('50 Canadian dollars equals this amount of US dollars: ');
// 使用 currency 模块的 canadianToUS 函数
console.log(currency.canadianToUS(50));
console.log('30 US dollars equals this amount of Canadian dollars: ');
// 使用 currency 模块的 USToCanadian 函数
console.log(currency.USToCanadian(30));
```

在引入模块时，`.js` 扩展名可以忽略。如果没有指明是 `js` 文件，`Node` 也会检查 `json` 文件，`json` 文件是作为 `JavaScript` 对象加载的。

如果想把这个模块放到子目录中，比如 `lib/`，只要把 `require` 语句改成下面这样就可以了：

```js
const currency = require('./lib/currency');
```

### 2. 运行 Node 项目

退到 Node 项目的上一级目录，然后执行 `node 项目目录名`。例如：

```shell
xiaotuan@xiaotuan:~/桌面$ node my_moudle
50 Canadian dollars equals this amount of US dollars: 
45.5
30 US dollars equals this amount of Canadian dollars: 
32.97
```

