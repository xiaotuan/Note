

### 9.2　let和const

在过去，JavaScript的一个限制就是不能声明一个块内变量。所以ES6中最受欢迎的新功能之一就是 `let` 语句。使用 `let` ，我们可以在程序块内部声明一个变量，而它的作用域就限制在这个块内。如果我们使用 `var` 的话，100会像下面这样被打印出来：

```python
if (true) {
  var sum = 100;
} 
console.log(sum); // prints out 100
```

使用 `let` 时：

```python
"use strict";
if (true) {
  let sum = 100;
} 
console.log(sum);
```

你会得到完全不同的结果：

```python
ReferenceError: sum is not defined
```

你的程序必须使用严格模式，才能使用 `let` 。

除了块级作用域， `let` 和 `var` 还有一个区别。使用 `var` 定义的变量会被提升（hoist）到执行作用域的顶部，也就是任何代码被执行之前。结果就是控制台打印出 `undefined` ，但没有任何运行时的错误：

```python
console.log(test);
var test;
```

而下面使用了 `let` 的代码则会在运行时报一个 `ReferenceError` ，告诉你 `test` 尚未定义。

```python
"use strict";
console.log(test);
let test;
```

那么是否应该在所有的情况下都使用 `let` ？有人会说是的，也有人说不是。你可以二者都使用，在需要程序级或者函数级作用域的地方使用 `var` ，而在需要使用块作用域的地方使用 `let` 。实际上，你所在的组织会对代码的风格进行规定。或者如果你知道你的环境可以支持ES6，那么就使用 `let` ，拥抱新版本。

说完了 `let` ，再说说 `const` 。 `const` 会声明一个只读的变量。如果变量的值是一个基本类型，那么它就是不可变的。如果值是一个对象，你就无法将变量重新赋值为对象或基本类型，但是可以修改对象的已有字段。

在下面的例子中，如果你尝试将一个 `const` 重新赋值，那么赋值语句会失败，但不会报错：

```python
const MY_VAL = 10;
MY_VAL = 100; 
console.log(MY_VAL); // prints 10
```

一定要明白， `const` 是一个值的引用。如果你将数组或者对象赋值给一个 `const` ，你就可以修改这个对象或者数组的内容：

```python
const test = ['one','two','three']; 
const test2 = {apples : 1, peaches: 2};
test = test2; //fails
test[0] = test2.peaches;
test2.apples = test[2];
console.log(test); // [ 2, 'two', 'three' ]
console.log(test2); // { apples: 'three', peaches: 2 }
```

不幸的是，关于 `const` 的用法存在很多令人困惑的地方。因为 `const` 在基本类型和对象上的用法不同，而 `const` 这个词本身又暗含常量（静态）赋值的意思。但是，如果你使用 `const` 是为了让这个变量无法修改，那么在把对象赋值给 `const` 时，你可以在对象上调用 `object.freeze()` 方法，来保护对象的不可编辑性。

我注意到Node文档在引用模块时使用了 `const` 。虽然将对象赋值给 `const` 并不能防止对象被修改，但是只要看一眼就会明白，它从词法层面暗示了开发者：这个对象后面不会被重复赋值了。

> <img class="my_markdown" src="../images/92.png" style="zoom:50%;" />
> **深入了解 `const` 以及不可修改性的缺陷**
> 网络标准倡导者Mathias Bynens对 `const` 和不变性进行了深入的讨论。

和 `let` 一样， `const` 拥有块级作用域。和 `let` 不同的是，它不需要严格模式。

在程序中，你可以像在浏览器中使用 `let` 和 `const` 一样来使用它们，但我并未发现在Node中使用它们会有什么特别的优势。有些人说使用 `let` 和 `const` 会有性能上的提升，而另外一些人则持相反意见。除了代码体验外我并没有发现有什么不同。就像我前面说过的，可能你的研发团队会有不同的要求，你只需要满足要求就可以了。

