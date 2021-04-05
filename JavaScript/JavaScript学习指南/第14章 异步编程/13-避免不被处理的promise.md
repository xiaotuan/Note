### 14.3.5　避免不被处理的promise

promise可以简化异步代码，同时确保回调函数不会被多次调用，但却不能避免那些因为promise没有被处理而产生的问题（没被处理指在这个promise中，既没有调用 `resolve` ，也没有调用 `reject` ）。这种错误很难被发现，因为它并没有显式的错误。在一个复杂的系统中，一个没有被处理的promise很容易丢失。

有一种方式可以避免这种错误，就是给promise一个特定的超时。如果promise没有在一段合理的时间内被处理，就会自动被拒绝。那么，什么是“一段合理的时间”呢，这需要视情况而定了。比如，有一个很复杂的算法需要执行10分钟，那就不要给它设置1秒的超时。

往launch函数中插入一个人工失败。假设火箭还处在实验阶段，而且有将近一半的时间都是失败的：

```javascript
function launch() {
   return new Promise(function(resolve, reject) {
      if(Math.random() < 0.5) return;    // rocket failure
      console.log("Lift off!");
      setTimeout(function() {
         resolve("In orbit!");
      }, 2*1000);    //火箭的确很快
  });
} 
```

在这个例子中，失败的方式不是很合理：因为没有调用 `reject` ，甚至没有在控制台打出任何log。只是悄悄地运行到一半时间的时候失败了。如果多运行几次这段代码，会发现它只是偶尔起作用，并且没有任何错误消息。这显然不是一个好的处理方式。

可以写一个函数来给promise添加一个超时：

```javascript
function addTimeout(fn, timeout) {
   if(timeout === undefined) timeout = 1000; // 默认超时
   return function(...args) {
        return new Promise(function(resolve, reject) {
          const tid = setTimeout(reject, timeout,
             new Error("promise timed out"));
          fn(...args)
             .then(function(...args){
                clearTimeout(tid);
                resolve(...args);
             })
             .catch(function(...args) {
                clearTimeout(tid);
                reject(...args);
             });
         ]};
    }
}
```

如果想说“哇哦……一个返回另一个函数的函数，被返回的函数又返回了一个promise，而这个promise又调用了返回另一个promise的函数……我要晕掉了！”这并不奇怪：因为给一个返回promise的函数添加超时并不是一件无关紧要的事情，它需要前面那些费解的部分。完全理解这个函数就留给那些想要更加深入学习的读者吧。不过这个函数的使用却很简单：可以给所有需要返回promise的函数添加超时。假如最慢的火箭需要10秒才能抵达同步轨道（怎么样，未来的火箭技术很厉害吧？），所以将超时设为11秒：

```javascript
c.go()
   .then(addTimeout(launch, 4*1000))
   .then(function(msg) {
      console.log(msg);
   })
   .catch(function(err) {
      console.error("Houston, we have a problem: " + err.message);
   });
```

这样的话promise链一定会被处理，即使 `launch` 函数的运行情况很糟糕。

