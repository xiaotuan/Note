### 14.3.2　使用promise

下面看看如何使用 `countdown` 函数。可以直接调用它并忽略promise部分：比如，直接调用 `countdown(5)` 。这里还是会有倒数的功能，并且不会被promise搞晕。但如果想用promise的特性呢？这个例子中展示了如何使用promise的返回值：

```javascript
countdown(5).then(
   function() {
      console.log("countdown completed successfully");
   },
   function(err) {
      console.log("countdown experienced an error: " + err.message);
   }
); 
```

在本例中，不用把返回的promise赋给一个变量，而是直接调用它的 `then` 处理器。这个处理器有两个回调：第一个是满足的回调，第二个是错误的回调。其中最多只会有一个函数被调用。promise也支持 `catch` 处理器，这样就可以把两个处理器分开了（在演示时，会把promise存在一个变量中）：

```javascript
const p = countdown(5);
p.then(function() {
      console.log("countdown completed successfully");
});
p.catch(function(err) {
      console.log("countdown experienced an error: " + err.message);
});
```

试着修改 `countdown` 函数，给它添加一个错误的情况。想象一下：如果我们很迷信，在数到数字13的时候就返回一个错误。

```javascript
function countdown(seconds) {
   return new Promise(function(resolve, reject) {
      for(let i=seconds; i>=0; i--) {
         setTimeout(function() {
            if(i===13) return reject(new Error("DEFINITELY NOT COUNTING THAT"));
            if(i>0) console.log(i + '...');
            else resolve(console.log("GO!"));
         }, (seconds-i)*1000);
      }
   });
} 
```

不妨动手试试这个例子。大家会看到一些有意思的行为。很显然，可以从小于13的任何数字开始倒数，这样就不会出错了。从13或是大于13的数字开始，则会在数到13的时候出错。但是，控制台会一直打log。调用 `reject` （或者 `resolve` ）并没能终止函数，它们只是修改了promise的状态。

显然 `countdown` 函数需要优化。通常，并不希望一个函数在被处理后还继续运行（不管是成功还是失败），但是countdown却继续运行了。之前早已提到过控制台中的log一点也不灵活，它们并不会真的提供想要的控制权。

promise提供了一个定义极其良好，并且可以安全地处理那些满足或者拒绝的异步任务的方式，但是它却没有（就目前而言）报告过程进度的能力。也就是说，promise只可能是满足或拒绝，绝不会出现“50%完成”。有的promise库中增加了一些很有用的功能，比如，可以报告过程，而且在未来，很可能JavaScript中的promise也会具备那些功能，不过现在，我们只能在没有这些功能的情况下工作。如果想要这些功能，需要继续学习下面的内容。

