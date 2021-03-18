

### 9.5　使用Bluebird来实现promise

在Node开发的早期阶段，创造者针对应该使用回调函数还是 `promise` 进行了辩论。结果回调函数获得了胜利，实在是几家欢喜几家愁啊。

`promise` 现在是ES6的一部分了，所以你完全可以在Node程序中使用这个特性。但是，如果你要在Node核心功能中使用ES6的 `promise` ，要么你需要从头实现这个功能，要么就需要使用一个提供了 `promise` 支持的模块。虽然我已经在本书中尽量避免使用第三方模块，但是对于目前的情况，我还是建议使用模块。本节中，我们来了解一个很流行的 `promise` 模块：Bluebird。

> <img class="my_markdown" src="../images/95.png" style="zoom:50%;" />
> **使用Bluebird来提升性能**
> 使用Bluebird的另外一个原因是性能。Bluebird的作者在StackExchange中解释了原因。

与回调函数的嵌套使用不同，ES6的 `promise` 功能使用的是分支处理，一个分支用来处理成功，另一个用来处理失败。解释这个原理的最佳方式是使用一个典型的Node文件系统程序，然后将它 `promise` 化——也就是将回调函数修改为 `promise` 。

下面的程序展示了如何使用原生的回调函数。打开一个文件，读取内容，进行修改，然后将内容写回文件。

```python
var fs = require('fs');
fs.readFile('./apples.txt','utf8', function(err,data) {
   if (err) {
      console.error(err.stack);
   } else {
     var adjData = data.replace(/apple/g,'orange');
     fs.writeFile('./oranges.txt', adjData, function(err) {
        if (err) console.error(err);
     });
   }
});
```

即使是如此简单的例子，也包含了两层回调：读文件和将修改后的内容写回文件。

下面我们会使用Bluebird来将这个例子 `promise` 化。

在我使用的代码中，Bluebird的 `promisifyAll()` 函数会将所有的文件系统函数 `promise` 化。我们会使用支持 `promise` 的函数版本，也就是 `readFileAsync ()` ，而不是 `readFile()` 。

```python
var promise = require('bluebird');
var fs = promise.promisifyAll(require('fs'));
fs.readFileAsync('./apples.txt','utf8')
   .then(function(data) {
      var adjData = data.replace(/apple/g, 'orange');
      return fs.writeFileAsync('./oranges.txt', adjData);
   })
   .catch(function(error) {
      console.error(error);
   });
```

在本例中，当文件内容被读取时， `then()` 函数会处理数据读取成功的结果，而如果读取不成功， `catch ()` 方法会处理错误。如果读取成功了，那么数据会被修改。然后 `writeFile()` 的 `promise` 版本—— `writeFileAsync()` 会被调用，将数据写回文件。从上一个例子我们知道， `writeFile()` 方法会返回一个错误，这个错误事实上也会被 `catch()` 函数捕获并进行处理。

尽管嵌套回调的例子并不复杂，但可以很清楚地看到， `promise` 版本的代码整洁了很多。你也会明白嵌套问题是如何解决的：特别是，不管调用了多少个函数，全程都只需要一个错误处理函数。

有没有更复杂的例子呢？我修改了前面的代码，加入了一个新步骤，并创建一个子目录用来放置oranges.txt文件。在此代码中，你会发现里面有两次 `then()` 调用。第一个会处理成功创建子目录的结果，第二个则用来创建新的文件并写入修改后的数据。新目录是使用 `promise` 化的 `mkdirAsync()` 函数创建的，函数调用的结果会作为 `then ()` 函数的返回值。这一步是使多个 `promise` 能够正常工作的关键，因为下一个 `then()` 函数实际上是在被返回的函数上面调用的。被修改的数据仍然会被传递给 `promise` 函数，从而被写入文件中。而不管是读取文件产生的错误，还是创建目录产生的错误，都会被 `catch()` 函数处理。

```python
var promise = require('bluebird');
var fs = promise.promisifyAll(require('fs'));
fs.readFileAsync('./apples.txt','utf8')
   .then(function(data) {
      var adjData = data.replace(/apple/g, 'orange');
      return fs.mkdirAsync('./fruit/');
   })
   .then(function(adjData) {
      return fs.writeFileAsync('./fruit/oranges.txt', adjData);
   })
   .catch(function(error) {
      console.error(error);
   }); 
```

返回值为数组的情况该如何处理呢？比如使用 `readdir()` 函数来读取一个目录的所有内容。

那就是数组处理函数（如 `map()` ）发挥作用的时候了。在下面的代码中，目录的内容被作为数组返回给调用者，然后逐个打开每个文件，并对内容进行一定的修改，然后写入另一个目录中具有相同文件名的文件中。内部的 `catch()` 方法用来处理读取和写入文件的错误，外部的则用来处理目录访问的错误。

```python
var promise = require('bluebird');
var fs = promise.promisifyAll(require('fs'));
fs.readdirAsync('./apples/').map(filename => {
   fs.readFileAsync('./apples/'+filename,'utf8')
      .then(function(data) {
         var adjData = data.replace(/apple/g, 'orange');
         return fs.writeFileAsync('./oranges/'+filename, adjData);
      })
      .catch(function(error) {
         console.error(error);
      })
   })
   .catch(function(error) {
      console.error(error);
   })
```

关于Bluebird的功能和Node中的 `promise` ，我只讲了一点皮毛。在应用程序中，除了基本的ES6功能，最好也花点时间了解一下这两部分功能。



