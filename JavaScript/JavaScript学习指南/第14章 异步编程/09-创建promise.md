### 14.3.1　创建promise

创建promise的方式很直接：创建一个带有函数的promise实例，它应该包含一个resolve（满足）和reject的回调（看吧，前面曾提醒过，就算使用了promise，还是需要回调函数）。继续看coundown函数，给它指定参数（这样就能设置5秒以上的倒计时了），当倒计时结束时返回一个promise：

```javascript
function countdown(seconds) {
   return new Promise(function(resolve, reject) {
      for(let i=seconds; i>=0; i--) {
         setTimeout(function() {
            if(i>0) console.log(i + '...');
            else resolve(console.log("GO!"));
         }, (seconds-i)*1000);
      } 
   });
} 
```

这个函数现在还不太灵活。大家并不想使用相同的方式，或者压根不想用控制台。如果想用countdown来更新网页中的DOM元素，效果可能就不太理想了。但这只是开始，它演示了如何创建一个promise。要注意 `resolve` （就像 `reject` ）是一个函数。大家可能会想“哈！可以多次调用resolve，从而跳出……呃，promise的promise。”的确可以多次调用 `resolve` 或者 `reject` ，甚至一起调用…但是只有第一次调用时会起作用。promise可以保证的是，不管谁使用了promise，都只会得到一个满足或者拒绝的响应（目前，所讲的函数中还未涉及拒绝的路径）。

