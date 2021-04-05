### 14.3.4　promise链

promise的一个优点就是它可以被链式调用；也就是说，当一个promise被满足时，可以立即用它调用另一个返回promise的函数，以此类推。创建一个叫作 `launch` 的函数，来链式调用countdown：

```javascript
function launch() {
   return new Promise(function(resolve, reject) {
      console.log("Lift off!");
      setTimeout(function() {
         resolve("In orbit!");
      }, 2*1000);    // a very fast rocket indeed
   }); 
} 
```

此时链式调用countdown就很容易了：

```javascript
const c = new Countdown(5)
   .on('tick', i => console.log(i + '...'));
c.go()
   .then(launch)
   .then(function(msg) {
      console.log(msg);
   })
   .catch(function(err) {
      console.error("Houston, we have a problem....");
   }) 
```

promise链的一个好处是不用在每一步都捕获错误；如果错误可能发生在链中的任何一环，promise链都会停止，继而调到catch中。试试把countdown的迷信时间改成15秒，这时会发现launch函数永远都不会被调用。

