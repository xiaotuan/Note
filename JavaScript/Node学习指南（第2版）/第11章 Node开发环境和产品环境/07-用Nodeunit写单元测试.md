

### 11.2.2　用Nodeunit写单元测试

Nodeunit提供了用一段脚本跑多个测试的方法。脚本写好之后，每个测试都会按顺序执行，测试结果也会以一种和谐的方式展现出来。要使用Nodeunit，先要通过npm来进行全局安装：

```python
[sudo] npm install nodeunit –g
```

Nodeunit提供了一种无须try/catch封装就可以简单运行一系列测试的方法。它支持Assert模块中提供的所有方法，还提供了另外一些方法来控制测试的运行。在测试脚本中，测试以测试用例的形式被组织起来，每个测试用例会被导出为一个对象方法。每个测试用例都有一个控制对象，一般命名为 `test` 。测试用例中第一个被调用的方法就是 `test` 元素的 `expect` 方法。这个方法用来告诉Nodeunit，在这个测试用例中，期望运行多少个测试方法。最后一个被调用的方法是 `test` 元素的 `done` 方法。这个方法用来告诉Nodeunit，测试用例已经运行结束。这两个方法中间调用的所有内容都是实际运行的单元测试：

```python
module.exports = {
   'Test 1' : function(test) {
      test.expect(3); // three tests
      ... // the tests
      test.done();
   },
   'Test 2' : function (test) {
      test.expect(1); // only one test
      ... // the test
      test.done();
   }
};
```

输入 `nodeunit` ，后面跟测试脚本的文件名，就可以运行这些测试了：

```python
nodeunit thetest.js
```

例11-1中包含了一个虽然小、但很完整的测试脚本，其中包含了6个断言。例11-1包含两个单元测试，分别标记为 `Test 1` 和 `Test 2` 。第一个单元测试会运行4个独立的测试，而第二个单元测试会运行两个。 `expect` 方法的调用反映出这个单元测试里面运行了多少个测试方法。

**例11-1　一个有两个单元测试、6个断言的Nodeunit测试脚本**

```python
var util = require('util');
module.exports = {
    'Test 1' : function(test) {
        test.expect(4);
        test.equal(true, util.isArray([]));
        test.equal(true, util.isArray(new Array(3)));
        test.equal(true, util.isArray([1,2,3]));
        test.notEqual(true, 1 > 2);
        test.done();
    },
    'Test 2' : function(test) {
        test.expect(2);
        test.deepEqual([1,2,3], [1,2,3]);
        test.ok('str' === 'str', 'equal');
        test.done();
    }
};
```

使用Nodeunit运行例11-1测试脚本的结果如下：

```python
thetest.js
✔ Test 1 
✔ Test 2 
OK: 6 assertions (12ms)
```

位于测试前面的字符用以表示测试是否成功：一个对勾表示成功，一个叉号表示失败。因为本例中所有的测试都通过了，所以并未出现错误信息和调用栈信息。

> <img class="my_markdown" src="../images/112.png" style="zoom:50%;" />
> Nodeunit可以支持CoffeeScript的应用程序。

