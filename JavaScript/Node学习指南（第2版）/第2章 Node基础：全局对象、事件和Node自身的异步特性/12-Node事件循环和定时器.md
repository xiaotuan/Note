[toc]

### 2.3.4　Node事件循环和定时器

在浏览器里，我们可以用 `setTimeout()` 和 `setInterval()` 来作为定时器，Node中也有同样的功能。这两种定时器不完全相同，因为浏览器中的事件循环是由浏览器引擎维护的，而Node中的事件循环是由C++的库libuv来处理的，不过二者几乎没有差别。

Node的 `setTimeout()` 方法的第一个参数是一个回调函数，第二个参数是延迟时间（以ms为单位），同时还有一些可选的参数。

```python
setTimeout(function(name) {
             console.log('Hello ' + name);
           }, 3000, 'Shelley');
console.log("waiting on timer...");
```

参数列表中的名字会被当成参数传给 `setTimeout()` 中的回调函数。延迟时间被设为3 000ms。因为 `setTimeout()` 方法是异步的，所以 `console.log()` 几乎立刻就会打印“ `waiting on timer…` ”的信息。

如果在创建计时器时就将它赋给一个变量，那么就可以取消计时。我修改了前面的Node应用程序，加入了快速取消和打印消息功能。

```python
var timer1 = setTimeout(function(name) {
             console.log('Hello ' + name);
           }, 30000, 'Shelley');
console.log("waiting on timer...");
setTimeout(function(timer) {
             clearTimeout(timer);
             console.log('cleared timer');
           }, 3000, timer1);
```

这个计时器设置了一个很长的时间，足够新的计时器去调用回调函数来取消它了。

`setInterval ()` 函数的操作方式与 `setTimeout ()` 的类似，但有两个不同之处。首先， `setInterval ()` 函数在程序终止前会一直重复计时器。另外，可以使用 `clearInterval ()` 来清除定时器。接下来我们修改一下 `setTimeout ()` 的例子，用它来演示 `setInterval ()` ，从这里可以清楚地看到在定时器取消之前消息被打印了9次。

```python
var interval = setInterval(function(name) {
             console.log('Hello ' + name);
           }, 3000, 'Shelley');
setTimeout(function(interval) {
             clearInterval(interval);
             console.log('cleared timer');
           }, 30000, interval);
console.log('waiting on first interval...');
```

Node文档中提到， `setTimeout` 不能保证回调函数精准地在n ms时（无论n是多少）被调用。在浏览器中使用 `setTimeout ()` 也是一样的，我们不能绝对控制运行环境，有很多因素可能会导致定时器的轻微延迟。在大多数情况下，我们其实感受不到定时器在运行时的时间差。但是，如果创建动画，就可以清楚地看到时间差造成的影响了。

有两个Node中特有的函数（即 `ref ()` 函数和 `unref ()` 函数）可以与计时器、中间层一起使用，在调用 `setTimeout ()` 和 `setInterval ()` 时，这两个函数会被返回。如果在定时器上调用 `unref ()` ，同时它是事件队列中唯一的事件，则定时器被取消，程序也可以终止。如果在同一个计时器对象上调用 `ref ()` ，则程序会继续进行，直到定时器结束。

回到第一个例子，我们创建了一个比较长的定时器，接下来调用 `unref()` 看看会发生什么：

```python
var timer = setTimeout(function(name) {
             console.log('Hello ' + name);
           }, 30000, 'Shelley');
timer.unref();
console.log("waiting on timer...");
```

运行这段代码，它会在控制台中打印消息，然后退出。这是因为用来设置定时器的 `setTimeout()` 是这段程序的事件队列中唯一的事件。如果我们再添加一个事件呢？修改代码，添加 `interval` 和 `timeout` ，并在 `timeout` 上调用 `unref()` ：

```python
var interval = setInterval(function(name) {
             console.log('Hello ' + name);
           }, 3000, 'Shelley');
var timer = setTimeout(function(interval) {
            clearInterval(interval);
            console.log('cleared timer');
           }, 30000, interval);
timer.unref();
console.log('waiting on first interval...');
```

计时器可以继续运行，并清除中间层计时器。正是中间层触发的事件使得计时器继续运行直到计时器清除中间层。

Node中最后一组跟定时器相关的方法是Node特有的： `setImmediate()` 和 `clearImmediate()` 。 `setImmediate()` 可以创建一个事件，不过这个事件的优先级高于那些被 `setTimeout()` 和 `setInterval()` 创建的事件，而低于I/O事件。同时它们跟定时器无关。 `setImmediate()` 事件会在所有I/O事件发生后，且在任何定时器事件之前触发，并且它会保持在当前事件流中。如果在回调函数中调用它，那么它会在当前调用完成后被放进下一个事件循环中。这是一种不通过定时器而把事件添加到当前或者下一个事件循环中的方式。由于它的优先级比其他定时器事件更高，所以它比 `setTimeout (callback，0)` 更高效。

这与 `process.nextTick()` 函数很像，不同的是， `process.nextTick()` 中的回调函数会在当前事件循环结束和所有新的I/O事件之前调用一次。就像在第2.3.2节中演示过的，Node异步编程的应用范围很广泛。

