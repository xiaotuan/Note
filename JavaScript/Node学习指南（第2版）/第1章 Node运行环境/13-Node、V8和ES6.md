[toc]

### 1.5　Node、V8和ES6

Node 背后有一套 JavaScript 引擎。大多数 JavaScript 的实现使用的引擎是 V8。V8 最初是由 Google 为 Chrome 开发的，在 2008 年开源了。V8 引擎是为了提高 JavaScript 的运行速度而创建的，它使用一个即时编译器（JIT）将 JavaScript 编译成机器代码而不是翻译它（多年来，JavaScript 一直是这样被执行的）。V8 引擎是用 C++ 编写的。

> <img class="my_markdown" src="../images/24.png" style="zoom:50%;" />
> **微软的 Node.js 分支**
> Microsoft 为 Node 创建了一个分支，以创建一个专门为物联网（IoT）设计的 JavaScript 引擎（名为Chakra）版本。我将在第 12 章中详细地介绍这个分支。

Node v4.0 发布的时候支持了 V8 4.5（也就是 Chrome 所使用的引擎版本）。Node 维护者也一直致力于在每个新版 V8 发布后提供支持。这意味着 Node 现在支持许多新的 ECMA-262 功能（也称为 ECMAScript 2015 或ES6）。

> <img class="my_markdown" src="../images/25.png" style="zoom:50%;" />
> **Node v6 的 V8 支持**
> Node v6 支持 V8 5.0 版本，而未来的 Node 版本也会支持对应的新版 V8。

在旧版 Node 中，要使用 ES6 的新特性，你需要在运行程序时加上 `harmony` 参数（ `--harmony` ）：

```python
node --harmony app.js
```

现在，ES6 新特性的支持基于以下几个标准（引用自 Node.js 文档）。

+ 所有 V8 认为稳定的已交付功能，在 Node.js 中都可以直接使用，不需要任何运行时的参数。
+ 待交付功能，也就是已经开发完毕，但是 V8 团队认为还不够稳定的功能，需要一个运行时参数： `--es_staging` （或者它的同义词 `--harmony` ）。
+ 开发中的功能可以使用每个功能对应的参数来开启（如 `--harmony_destructuring` ），但是不建议这样做，除非是用于测试。

我将会在第 9 章讲解 Node 对 ES6 的支持，以及如何高效地使用各项功能。现在，你可以快速了解一下以下内容，它们是 Node 所支持的 ES6 功能的一部分。

+ 类
+ `Promises` 对象
+ 符号
+ 箭头函数
+ `Generator` 函数
+ 数组
+ `let` 关键字
+ `spread` 操作符

