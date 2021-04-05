### 14.2.1　setInterval和clearInterval

`setTimeout` 在运行过一次函数后就不再运行了。在此基础上，还有 `setInterval` 函数，它会每隔一段特定的时间运行回调函数，并且一直运行下去，直到调用 `clearInterval` 。这里有一个例子，每隔5秒钟运行一次函数直到一分钟结束，或者运行10次，以先到的为准：

```javascript
const start = new Date();
let i=0;
const intervalId = setInterval(function() {
   let now = new Date();
   if(now.getMinutes() !== start.getMinutes() || ++i>10)
      return clearInterval(intervalId);
   console.log('${i}: ${now}');
}, 5*1000); 
```

可以看到 `setInterval` 返回了一个ID，在后面可以用它来取消（停止）这次调用。与之对应的 `clearInterval` 在 `timeout` 之前停止本次调用也正是使用了这种方式。

> <img class="my_markdown" src="../images/2.png" style="width:116px;  height: 151px; " width="10%"/>
> `setTimeout` 、 `setInterval` 和 `clearInterval` 都定义在全局对象中（在浏览器中是 `window` ，在Node中是 `global` ）

