

### 11.2.1　使用Assert进行单元测试

断言测试（Assertion tests）指的是对表达式进行求值，验证其结果为 `true` 或者 `false` 。如果你测试的是一个函数调用的返回值，你可能需要先验证返回结果是一个数组（第一次断言）。而数组应该有一个确定的长度，你需要对长度进行验证（第二次断言）。后面的验证以此类推。有一个Node内置模块可以简化此类测试：Assert。它最初的设计目的是被Node内部使用，但是我们也可以使用它。只是你要明白，它并非一个真正的测试框架。

使用下面的代码来引入Assert模块：

```python
var assert = require('assert');
```

让我们从已有模块的测试代码中学习一下如何使用它。Node程序都是在模块的单元测试部分用到Assert模块的。比如，有一个叫test-utils.js的测试程序，可用来测试Utilities模块。下面的代码就是 `isArray` 方法的部分测试代码：

```python
// isArray
assert.equal(true, util.isArray([]));
assert.equal(true, util.isArray(Array()));
assert.equal(true, util.isArray(new Array()));
assert.equal(true, util.isArray(new Array(5)));
assert.equal(true, util.isArray(new Array('with', 'some', 'entries')));
assert.equal(true, util.isArray(context('Array')()));
assert.equal(false, util.isArray({}));
assert.equal(false, util.isArray({ push: function() {} }));
assert.equal(false, util.isArray(/regexp/));
assert.equal(false, util.isArray(new Error));
assert.equal(false, util.isArray(Object.create(Array.prototype)));
```

`assert.equal()` 方法和 `assert.strictEqual()` 方法都有两个必须的参数：一个期望的结果和一个能进行求值的表达式。在 `assert.equal isArray` 中，如果表达式求值的结果是 `true` ，同时期望的结果也是 `true` ，那么 `assert.equal` 方法执行成功，并且没有任何输出，也就是说结果是默认的。

但如果表达式求值的结果和期望值不同，那么 `assert.equal` 方法会产生一个异常。如果我将Node源码中 `isArray` 测试的第一行改成下面的语句：

```python
assert.equal(false, util.isArray([]));
```

那么执行结果就是：

```python
assert.js:89
  throw new assert.AssertionError({
  ^
AssertionError: false == true
    at Object.<anonymous> (/home/examples/public_html/
                         learnnode2/asserttest.js:4:8)
    at Module._compile (module.js:409:26)
    at Object.Module._extensions..js (module.js:416:10)
    at Module.load (module.js:343:32)
    at Function.Module._load (module.js:300:12)
    at Function.Module.runMain (module.js:441:10)
    at startup (node.js:134:18)
    at node.js:962:3
```

`assert.equal()` 和 `assert.strictEqual()` 方法还有第三个可选参数，即一个可以取代默认错误输出的消息：

```python
assert.equal(false, util.isArray([]), 'Test 1Ab failed');
```

当你需要一次运行多个测试的时候，这种方式对定位失败的测试很有用。关于这个消息（或者说标签）的用法，你可以看看node-redis的测试代码：

```python
assert.equal(str, results, label + " " + str +
               " does not match " + results);
```

当捕捉到异常并且打印消息时，就能看到这个消息了。

下面列出的Assert模块方法，虽然功能不尽相同（看名字就会知道），但接收的参数却都是一样的：

+ `assert.equal` ，当表达式求值的结果和给定的值不相等时失败；
+ `assert.strictEqual` ，当表达式求值的结果和给定的值不严格相等时失败；
+ `assert.notEqual` ，当表达式求值的结果和给定的值相等时失败；
+ `assert.notStrictEqual` ，当表达式求值的结果和给定的值严格相等时失败；
+ `assert.deepEqual` ，当表达式求值的结果和给定的值内容不一致时失败；
+ `assert.notDeepEqual` ，当表达式求值结果和给定的值内容一致时失败；
+ `assert.deepStrictEqual` ，类似于 `assert.deepEqual()` ，只不过数据比较是使用严格相等（===）来进行的；
+ `assert.notDeepStrictEqual` ，验证严格内容的不一致性<sup class="my_markdown">[1]</sup>。

带 `deep` 的方法都是用来处理比较复杂的对象的，比如数组和对象。下面的表达式使用了 `assert.deepEqual` ，并且返回了成功的结果：

```python
assert.deepEqual([1,2,3],[1,2,3]);
```

但是如果使用 `assert.equal` 方法的话就会返回失败。

剩下的 `assert` 方法所使用的参数就不太一样了。如果在调用 `assert` 时传入一个值和一个消息，那么相当于调用 `assert.isEqual` 并且传入 `true` 作为第一个参数。比如，下面的代码：

```python
var val = 3;
assert(val == 3, 'Test 1 Not Equal');
```

和下面的代码功能一样：

```python
assert.equal(true, val == 3, 'Test 1 Not Equal');
```

也可以使用 `assert.ok` 这个别名函数：

```python
assert.ok(val == 3, 'Test 1 Not Equal');
```

`assert.fail` 函数会抛出一个异常。它接收4个参数：一个值、一个表达式、一个消息和一个操作符。这个操作符的作用在于，如果消息参数不可用，则会使用操作符连接值和表达式，来生成一个消息。代码片段如下：

```python
try {
  var val = 3;
  assert.fail(val, 4, 'Fails Not Equal', '==');
} catch(e) {
  console.log(e);
}
```

控制台的消息内容是：

```python
{ [AssertionError: Fails Not Equal]
  name: 'AssertionError',
  actual: 3,
  expected: 4,
  operator: '==',
  message: 'Fails Not Equal',
  generatedMessage: false }
```

`assert.ifError` 方法接收一个值作为参数，只有当这个参数不为 `false` 时，才会抛出一个异常。Node文档提到，对于错误对象作为第一个参数的回调函数来说，这是一个很好的测试方法。

```python
assert.ifError(err); //throws only if true value
```

最后要介绍的是 `assert.throws` 方法和 `assert.doesNotThrow` 方法。前者期望抛出一个异常，后者则相反。两个方法都接收一段代码作为第一个参数，第二个参数和第三个参数是可选的，分别是一个错误对象和一个消息。这里所说的错误对象，可以是一个构造方法、正则表达式或是验证函数。在下面的代码片段中，由于第二个参数，也就是用来匹配错误信息的正则表达式并没有成功匹配错误信息，所以错误信息被打印出来了。

```python
assert.throws(
  function() {
    throw new Error("Wrong value");
  },
  /something/
);
```

借助Assert模块，你可以创建出健壮的单元测试。但是这个模块最大的限制在于，你需要对测试进行很多封装，这样你的整个测试脚本就不会因为一个测试失败就“全军覆没”。要解决这个问题，我们就需要一个稍微高级点的单元测试框架了，比如马上要讲到的Nodeunit。

