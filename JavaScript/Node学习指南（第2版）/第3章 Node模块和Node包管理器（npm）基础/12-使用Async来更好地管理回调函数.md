[toc]

### 3.4.1　使用Async来更好地管理回调函数

第2章例2-11中的程序是使用异步模式实现的，其中每个函数被调用之后会把结果传给下一个函数。整个过程会一直持续，直到遇到错误。这样的模式有好几种，其中一些是另外一些的变形，而且叫法也不尽相同。

这个例子还展示了使用回调函数的一个严重问题：因为回调函数不断堆积而形成的“回调地狱”。

为了解决这个问题，最常用的模块就是Async模块。它会将传统的回调模式转化为更线性的和更好管理的模式。Async模块包括以下函数。

+ 瀑布模式（waterfall），函数被按顺序调用，所有的结果都被收集起来，然后以数组的形式传递给最后一个回调函数（这个模式也被其他一些人称为series或者sequence）。
+ 串行模式（series），函数被按顺序调用，然后，我们可以将调用结果组成数组传给最后一个回调函数。
+ 并行模式（parallel），函数被并行执行，完成之后结果被传递给最后一个回调函数（虽然在一些解释中，执行结果数组并不是模式的一部分）。
+ 前置条件循环模式（whilst），重复调用同一个函数，当先决条件为false或者有错误发生时，调用最后的回调函数。
+ 队列模式（queue），以某个并发量并行调用函数，新的函数将会进入执行队列，等待正在执行的函数完成。
+ 后置条件循环模式（until），重复调用同一个函数，当后决条件为false或者出现错误时，调用最后的回调函数。
+ 自动模式（auto），基于需求调用函数，每个函数会接收前一个回调函数的返回值。
+ 迭代器模式（iterator），每个函数会调用下一个函数，同时有访问下一个迭代器的权限。
+ 应用模式（apply），一个已有参数的可持续执行函数和控制流函数的组合。
+ nextTick模式（nextTick），在事件环的下一环中调用回调函数——基于Node中的process.next。

Async模块同时提供了管理列表的功能，比如它内部实现的forEach、map和filter方法，以及工具功能（包括针对memoizatio__n（记忆化）的功能）。然而，我们感兴趣的是它对于控制流的能力。

> <img class="my_markdown" src="../images/52.png" style="zoom:50%;" />
> Async有一个GitHub代码库。

让我们用npm来安装Async。如果要安装到全局环境，就是用-g参数。需要更新依赖的话，要加--save或--save-dev参数：

```python
npm install async
```

如前所述，Async为各种异步模式（包括串行、并行和瀑布式）提供控制流能力。例如，第2章中的示例代码所使用的模式与Async的瀑布式相匹配，因此我们将使用async.waterfall方法。在例3-5中，我使用async.waterfall并借助fs.readFile来打开和读取一个文件，并执行同步的字符串替换，然后使用fs.writeFile将该字符串写回文件。请特别注意程序中每个步骤使用的回调函数。

**例3-5　使用async.waterfall来异步读取、修改和写入文件内容**

```python
var fs = require('fs'),
    async = require('async');
async.waterfall([
   function readData(callback) {
      fs.readFile('./data/data1.txt', 'utf8', function(err, data){
           callback(err,data);
       }); 
   }, 
   function modify(text, callback) {
      var adjdata=text.replace(/somecompany\.com/g,'burningbird.net');
      callback(null, adjdata);
   },
   function writeData(text, callback) {
       fs.writeFile('./data/data1.txt', text, function(err) {
          callback(err,text);
       });
   } 
], function (err, result) {
      if (err) {
        console.error(err.message);
      } else {
        console.log(result);
      }
});
```

async.waterfall方法有两个参数：一个任务数组和一个可选的最终回调函数。每个异步任务函数都是async.waterfall数组的一个元素，每个函数也都需要一个回调作为其最后一个参数。正是这个回调函数允许我们将异步的回调函数的结果串起来，而不必使用嵌套函数。然而，正如你在代码中看到的，每个回调函数的处理方式都和使用嵌套回调的一样，也就是我们需要在每个函数中对错误进行测试。Async会检查每个回调函数的第一个参数是不是错误对象。如果我们在回调函数中传递了一个错误对象，那调用过程将立即结束，然后调用最后的回调函数。我们只能在最后回调的地方处理错误对象或最终结果。

> <img class="my_markdown" src="../images/53.png" style="zoom:50%;" />
> 例3-5使用了命名函数，而Async文档中使用的是匿名函数。命名函数可以简化调试和错误处理，二者的实际效果没有差别。

这个处理过程与我们在第2章中讲的内容类似，只是没有嵌套（并且必须在每个函数中测试错误）。它看起来更复杂，所以对于这种简单的嵌套回调，我不推荐使用它，但对于更复杂的嵌套回调就不一样了。例3-6完整复制了第2章中示例代码的功能，但是避免了回调嵌套和过多的缩进。

**例3-6　从目录获取对象、测试文件查找、读取文件、修改文件，最后写回文件并记录日志**

```python
var fs = require('fs'),
    async = require('async'),
    _dir = './data/';
var writeStream = fs.createWriteStream('./log.txt',
      {'flags' : 'a',
       'encoding' : 'utf8',
       'mode' : 0666});
async.waterfall([
   function readDir(callback) {
      fs.readdir(_dir, function(err, files) {
         callback(err,files);
      });
   }, 
   function loopFiles(files, callback) {
      files.forEach(function (name) {
         callback (null, name);
      });
   }, 
   function checkFile(file, callback) {
      fs.stat(_dir + file, function(err, stats) {
         callback(err, stats, file);
      });
   },
   function readData(stats, file, callback) {
      if (stats.isFile())
         fs.readFile(_dir + file, 'utf8', function(err, data){
           callback(err,file,data);
         });
   },
   function modify(file, text, callback) {
      var adjdata=text.replace(/somecompany\.com/g,'burningbird.net');
      callback(null, file, adjdata);
   },
   function writeData(file, text, callback) {
       fs.writeFile(_dir + file, text, function(err) {
          callback(err,file);
       });
   },
   function logChange(file, callback) {
       writeStream.write('changed ' + file + '\n', 'utf8',
                       function(err) {
          callback(err);
       });
   }
], function (err) {
         if (err) {
            console.error(err.message);
         } else {
            console.log('modified files');
         }
});
```

每一个功能都是从第2章的示例代码中得来的。fs.readdir方法用于获取目录对象数组。Node的forEach方法（非Async的forEach方法）用于访问每个特定的对象。fs.stats方法用于获取每个对象的stats信息。stats用于检查文件是否存在，每当找到一个文件，就打开该文件并且访问其数据，然后修改数据，并通过fs.writeFile将数据写回文件。该操作被记录在日志文件中，同时控制台会打印一条成功信息。

请注意，某些回调函数所接收的参数比其他的多。大部分函数都需要文件名和内容，所以对于最后几个函数，这两个参数都被传进去了。函数可以接收任意数量的参数，只要第一个参数是错误对象（或者没有错误的时候传递null），最后一个参数是回调函数即可。我们不需要在每个异步任务函数中检查错误，因为Async会在每个回调函数中检测错误对象，然后在发现错误时停止执行回调，并且调用最终回调函数。

其他的Async控制流方法，比如async.parallel和async.serial，都遵循这种写法，即以一个任务数组作为第一个参数，以一个可选的回调函数作为第二个参数。不过它们也都有各自处理异步任务的方式。

async.parallel方法会同时调用所有的异步函数，当所有函数都完成后，调用最终回调函数。在例3-7中，我们使用async.parallel来并行读取3个文件的内容。然而，示例代码中并没有使用函数数组的方式来调用，而是使用了Async中的另外一种方式：传递对象，每个回调函数都是对象中的一个属性。当3个任务都执行完毕后，最终结果被打印到控制台。

**例3-7　并行打开3个文件并读取内容**

```python
var fs = require('fs'),
    async = require('async');
async.parallel({
   data1 : function (callback) {
      fs.readFile('./data/fruit1.txt', 'utf8', function(err, data){
           callback(err,data);
       }); 
   }, 
   data2 : function (callback) {
      fs.readFile('./data/fruit2.txt', 'utf8', function(err, data){
           callback(err,data);
       });
   },
   data3 : function readData3(callback) {
      fs.readFile('./data/fruit3.txt', 'utf8', function(err, data){
           callback(err,data);
       });
   }, 
}, function (err, result) {
      if (err) {
         console.log(err.message);
      } else {
         console.log(result);
      }
});
```

对象数组作为执行结果被返回，每个结果都显示在对应的属性中。如果这3个文件如下：

+ fruit1.txt: apples；
+ fruit2.txt: oranges；
+ fruit3.txt: peaches。

那么运行例3-7所得到的结果就会是：

```python
{ data1: 'apples\n', data2: 'oranges\n', data3: 'peaches\n' }
```

测试Async中其他工作流的任务就留给各位读者当作练习吧。只要记住，使用Async控制流方法时，你需要给每个异步任务传一个回调函数，并在任务完成时调用这个回调函数，然后传给它一个错误对象（或者null）和你所需要的所有数据。

