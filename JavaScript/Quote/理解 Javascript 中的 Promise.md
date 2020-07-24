<center><font size="5"><b>理解 Javascript 中的 Promise</b></font></center>

> 摘自：<https://segmentfault.com/a/1190000017312249>

## JavaScript中的 Promise

根据经验，对于JavaScript，我总是阅读来自MDN Web文档的文档。在所有资源中，我认为它们提供了最简洁的细节。我阅读了来自 [MDSN Web文档的promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) 介绍，并尝试了一些代码来掌握它。

理解承诺有两个部分。“创建 promises” 和 “处理 promises”。虽然我们的大多数代码通常会迎合其他库创建的 promises 的处理，但完全理解这些 promises 肯定会有所帮助。一旦你过了初学阶段，理解“创造promises ”同样重要。

## Promise 创建

让我们看一下创建新promis的语法

```javascript
new Promise( /* executor */ function(resolve, reject) { ... } );
```

构造函数接受一个名为executor 的函数。 此执行函数接受两个参数 resolve 和 reject，它们f都是函数。 Promise 通常用于更容易处理异步操作或阻塞代码，其示例包括文件操作，API调用，DB调用，IO调用等。这些异步操作的启动发生在执行函数中。如果异步操作成功，则通过 promise 的创建者调用resolve 函数返回预期结果，同样，如果出现意外错误，则通过调用 reject 函数传递错误具体信息。

```javascript
var keepsHisWord
keepsHisWord = true
promise1 = new Promise(function(resolve, reject) {
    if (keepsHisWord) {
        resolve("小智承诺坚持分享好的东西给大家")
    } else {
        reject("我没有做到！")
    }
})
console.log(promise1)
```



![图片描述](.\images\01.jpg)

由于该 promise 会立即执行，我们将无法检查该 promise 的初始状态。因此，让我们创造一个需要时间来执行的 promise，最简单的方法是使用 setTimeOut 函数。

```javascript
promise2 = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve({
      message: "小智承诺坚持分享好的东西给大家",
      code: "200"
    })
  }, 10 * 1000)
});
console.log(promise2)
```

上面的代码只是创建了一个在10秒后无条件执行 promise。 因此，我们可以检查promise 的状态，直到它被 resolve。

![图片描述](.\images\02.jpg)

一旦十秒钟过去，promise 就会执行 resolve。PromiseStatus 和 PromiseValue 都会相应地更新。如你所见，我们更新了 resolve 函数，以便传递 JSON 对象，而不是简单的字符串。这只是为了说明我们也可以在 resolve 函数中传递其他值。

![图片描述](.\images\03.jpg)

现在让我们看看一个 promise reject的例子。我们只要修改一下 keepsHisWord:

```javascript
keepsHisWord = false
promise3 = new Promise(function(resolve, reject) {
    if (keepsHisWord) {
        resolve("小智承诺坚持分享好的东西给大家")
    } else {
        reject("我没有做到！")
    }
})
console.log(promise3)
```

![图片描述](.\images\04.jpg)

我们可以看到 PromiseStatus 可以有三个不同的值，pending（进行中）、 resolved（已成功） 或 rejected（失败）。创建 promise 时，PromiseStatus 将处于 pending 状态，并且 PromiseValue 为 undefined，直到 promise 被 resolved 或 rejected 为止。 当 promise 处于 resolved 或 rejected 的状态时，就称为 settled（已定型）。 所以 promise 通常从 pending 态转换到 settled 状态。

既然我们知道 promise 是如何创建的，我们就可以看看如何使用或处理 promise。这将与理解 Promise 对象密切相关。

## 理解 Promise 对象

根据 MDN 文档

> Promise 对象表示异步操作的最终完成(或失败)及其结果值

Promise 对象具有静态方法和原型方法，Promise 对象中的静态方法可以独立应用，而原型方法需要应用于 Promise对象的实例。记住，普通方法和原型都返回一个 romise，这使得理解事物变得容易得多。

## 原型方法(Prototype Methods)

让我们首先从原型方法开始，有三种方法。重申一下，记住所有这些方法都可以应用于 Promise 对象的一个实例，并且所有这些方法依次返回一个 Promise。以下所有方法都为 promise 的不同状态转换分配处理程序。正如我们前面看到的，当创建一个 Promise 时，它处于 pending 状态。Promise 根据是否 fulfilled（已成功）或rejected（已失败），将运行以下三种方法中的一种或多种。

```javascript
Promise.prototype.catch(onRejected)

Promise.prototype.then(onFulfilled, onRejected)

Promise.prototype.finally(onFinally)
```

下图显示了 then 和 .catch 方法的流程。由于它们返回一个 Promise ，它们可以再次被链式调用。不管 promise 最后的状态，在执行完t hen 或 catch 指定的回调函数以后，都会执行finally方法指定的回调函数。

![图片描述](.\images\05.jpg)

这里有一个小故事。你是一个上学的孩子，你问你的妈妈要一个电话。她说:“这个月底我要买一部手机。”

让我们看看，如果承诺在月底执行，JavaScript中会是什么样子。

```javascript
var momsPromise = new Promise(function(resolve, reject) {
  momsSavings = 20000;
  priceOfPhone = 60000;
  if (momsSavings > priceOfPhone) {
    resolve({
      brand: "iphone",
      model: "6s"
    });
  } else {
    reject("我们没有足够的储蓄，让我们多存点钱吧。");
  }
});
momsPromise.then(function(value) {
  console.log("哇，我得到这个电话作为礼物 ", JSON.stringify(value));
});
momsPromise.catch(function(reason) {
  console.log("妈妈不能给我买电话，因为 ", reason);
});
momsPromise.finally(function() {
  console.log(
    "不管妈妈能不能给我买个电话，我仍然爱她"
  );
});
```

输出：

![图片描述](.\images\06.jpg)

如果我们把妈妈的礼物价值改为20万美元，那么妈妈就可以给儿子买礼物了。在这种情况下，输出将是

![图片描述](.\images\07.jpg)

接着 then方法的第一个参数是 resolved 状态的回调函数，第二个参数（可选）是 rejected 状态的回调函数。所以我们也可以这样写：

```javascript
momsPromise.then(
	function(value) {
        console.log("哇，我得到这个电话作为礼物 ", JSON.stringify(value))
    },
    function(reason) {
        console.log("妈妈不能给我买电话，因为 ", reason)
    }
)
```

但是为了代码的可读性，我认为最好将它们分开。

为了确保我们可以在浏览器中运行所有这些示例，或者在chrome中运行特定的示例，我要确保我们的代码示例中没有外部依赖关系。

为了更好地理解进一步的主题，让我们创建一个函数，该函数将返回一个 Promise，函数里随机执行 resolve 或者 rejected ，以便我们可以测试各种场景。

由于我们需要随机数，让我们先创建一个随机函数，它将返回x和y之间的随机数。

```javascript
function getRandomNumber(start = 1, end = 10) {
	// works whenboth start, end are >= 1 and end > start
    return parseInt(Math.random() * end) % (end - start + 1) + start
}
```

让我们创建一个函数，它将为我们返回 promise。让我们调用 promiseTRRARNOSG 函数，它是promiseThatResolvesRandomlyAfterRandomNumnberOfSecondsGenerator 的别名。这个函数将创建一个 promise，该 promise 将在 2 到 10 秒之间的随机数秒后执行 resolve 或 reject。为了随机执行resolve 和 reject，我们将创建一个介于 1 和 10 之间的随机数。如果生成的随机数大于 5，我们将执行 resolve ，否则执行 reject。

```javascript
function getRandomNumber(start = 1, end = 10) {
  //works when both start and end are >=1
  return (parseInt(Math.random() * end) % (end - start + 1)) + start;
}
var promiseTRRARNOSG = (promiseThatResolvesRandomlyAfterRandomNumnberOfSecondsGenerator = function() {
  return new Promise(function(resolve, reject) {
    let randomNumberOfSeconds = getRandomNumber(2, 10);
    setTimeout(function() {
      let randomiseResolving = getRandomNumber(1, 10);
      if (randomiseResolving > 5) {
        resolve({
          randomNumberOfSeconds: randomNumberOfSeconds,
          randomiseResolving: randomiseResolving
        });
      } else {
        reject({
          randomNumberOfSeconds: randomNumberOfSeconds,
          randomiseResolving: randomiseResolving
        });
      }
    }, randomNumberOfSeconds * 1000);
  });
});
var testProimse = promiseTRRARNOSG();
testProimse.then(function(value) {
  console.log("Value when promise is resolved : ", value);
});
testProimse.catch(function(reason) {
  console.log("Reason when promise is rejected : ", reason);
});
// 创建10个不同的promise
for (i=1; i<=10; i++) {
  let promise = promiseTRRARNOSG();
  promise.then(function(value) {
    console.log("Value when promise is resolved : ", value);
  });
  promise.catch(function(reason) {
    console.log("Reason when promise is rejected : ", reason);
  });
}
```

刷新浏览器页面并在控制台中运行代码，以查看resolve 和 reject 场景的不同输出。

## 静态方法

Promise对象中有四种静态方法。

前两个是帮助方法或快捷方式。 它们可以帮助您轻松创建 resolved 和 reject 方法。

```javascript
Promise.reject(reason)
```

粟子：

```javascript
var promise3 = Promise.reject("不感兴趣！")
promise3.then(function(value) {
    console.log("执行 resovle ", value)
})
promise3.catch(function(reason) {
    console.log("被拒绝了，原因 ")
})
```

```
Promise.resolve(value)
```

粟子：

```javascript
var promise4 = Promise.resolve(1);
promise4.then(function(value) {
    console.log("执行成功， 值为 ", value)
})
promise4.catch(function(reaason) {
    console.log("被拒绝了，原因 ", reason)
})
```

在旁注上，promise 可以有多个处理程序。因此，你可以将上述代码更新为：

```javascript
var promise4 = Promise.resolve(1)
promise4.then(function(value) {
    console.log("第一个 resolve 函数， 因为 ", value)
})
promise4.then(function(value) {
    console.log("第二个 resolve 函数，值为 ", value * 2)
})
promised4.catch(function(reason) {
    console.log("被拒绝，原因 ", reason)
})
```

输出：

![图片描述](.\images\08.jpg)

下面两个方法帮助你处理一组 promise 。当你处理多个promise 时，最好先创建一个promise 数组，然后对这些promise 集执行必要的操作。

为了理解这些方法，我们不能使用上例中的 promiseTRRARNOSG，因为它太随机了，最好有一些确定性的 promise ，这样我们才能更好理解 promise 行为。

让我们创建两个函数。一个会在n秒后执行resolve，另一个会在n秒后执行 reject。

```javascript
var promiseResolve = (promiseCrater = function(n = 0) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            resolve({
                resolvedAfterNSeconds: n
            })
        }, n * 1000)
    })
})
var promiseREject = (promiseCrater = function(n = 0) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            reject({
                rejectedAfterNSeconds: n
            })
        }, n * 1000)
    })
})
```

现在让我们使用这些帮助函数来理解 Promise.All

## Promise.All

根据 MDN 文档：

> Promise.all(iterable) 方法返回一个 Promise 实例，此实例在 iterable 参数内所有的 promise
> 都“完成（resolved）”或参数中不包含 promise 时回调完成（resolve）；如果参数中 promise
> 有一个失败（rejected），此实例回调失败（reject），失败原因的是第一个失败 promise 的结果。

例一：当所有的 promise 都执行完成了，这是最常用的场景。

```javascript
var promiseResolve = (promiseCrater = function(n = 0) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            resolve({
                resolvedAfterNSeconds: n
            })
        }, n * 1000)
    })
})
var promiseREject = (promiseCrater = function(n = 0) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            reject({
                rejectedAfterNSeconds: n
            })
        }, n * 1000)
    })
})

console.time("Promise.All")
var promisesArray = []
promisesArray.push(promiseResolve(1))
promisesArray.push(promiseResolve(4))
promisesArray.push(promiseResolve(2))
var handleAllPromises = Promise.all(promisesArray)
handleAllPromises.then(function(values) {
    console.timeEnd("Promise.All")
    console.log("所有的 promise 都执行完成了", values)
})
handleAllPromises.catch(function(reason) {
    console.log("其中一个promise失败了， 原因如下 ", reason)
})
```

![图片描述](.\images\09.jpg)

**我们需要从输出中得出两个重要的结论：**

1. 第三个 promise 需要2秒完成，第二个 promise 需要4秒。但是正如你在输出中看到的，promise
   的顺序在值中保持不变。
2. 我添加了一个计时器来确定 promise 执行所需要时间。如果 promise 是按顺序执行的，那么总共需要 1+4+2=7 秒，但是从计时器中我们看到它只需要4秒。这证明了所有的 promise 都是并行执行的。

例二：当数组不是 promise 的时候呢？(我认为这是最不常用的)

```javascript
console.time("Promise.All")
var promiseesArray = []
promisesArray.push(1)
promisesArray.push(4)
promisesArray.push(2)
var handleAllPromises = Promise.all(promisesArray)
handleAllPromises.then(function(values) {
    console.timeEnd("Promise.All")
    console.log("所有的 promise 都执行完成了", values)
})
handleAllPromises.catch(function(reason) {
    console.log("其中一个 promise 失败了，原因如下 ", reason)
})
```

输出：

![图片描述](.\images\10.jpg)

由于数组中没有 promise，因此将执行 promise 中的 resolve。

例一：其中一个 promise 状态最先为 resolve 状态

```javascript
console.time("Promise.All")
var promisesArray = [];
promisesArray.push(promiseResolve(1))
promisesArray.push(promiseResolve(5))
promisesArray.push(promiseREjject(2))
promisesArray.push(promiseResolve(4))
var handleAllPromises = Promise.all(promisesArray)
handleAllPromises.then(function(valuees) {
    console.timeEnd("Promise.All")
    consolee.log("所有的 promise 都执行完成了", values)
})
handleAllPromises.catch(function(reason) {
    console.timeEnd("Promise.All")
    console.log("其中一个promise失败了，原因如下 ", reason)
})
```

![图片描述](.\images\11.jpg)

## Promise.race

根据 MDN：

> Promise.race(iterable) 方法返回一个 promise，一旦迭代器中的某个promise解决或拒绝，返回的 promise就会解决或拒绝。

```
const p = Promise.race([p1, p2, p3]);
```

上面代码中，只要p1、p2、p3之中有一个实例率先改变状态，p的状态就跟着改变。那个率先改变的 Promise 实例的返回值，就传递给 p 的回调函数。

```javascript
console.time("Promise.race")
var promisesArray = []
promisesArray.push(promiseResolve(4))
promisesArray.push(promiseResolve(3))
promisesArray.push(promiseResolve(2))
promisesArray.push(promiseREject(3))
promisesArray.push(promiseResolve(4))
var promisesRace = Promise.race(promisesArray)
promisesRace.then(function(value) {
    console.timeEnd("Promise.race")
    console.log("率先改变的 Promise", values)
})
promisesRace.catch(function(reason) {
    console.timeEnd("Promise.race")
    console.log("其中一个promise失败了，原因如下 ", reason)
})
```

![图片描述](.\images\12.jpg)

所有的 promise 都是并行运行的。第三个 promise 在 2 秒内完成，所以是最先改变的就返回给Promise.race。

例二：其中一个 promise 状态最先为 reject 状态

```javascript
console.time("Promise.race")
var promisesArray = []
promisesArray.push(promiseResolve(4))
promisesArray.push(promiseResolve(6))
promisesArray.push(promiseResolve(5))
promisesArray.push(promiseREject(3))
promisesArray.push(promiseResolve(4))
var promisesRace = Promise.race(promisesArray)
promisesRace.then(function(values) {
    console.timeEnd("Promise.race")
    console.log("率先状态为 resolve 的 Promise", values)
})
promisesRace.catch(function(reason) {
    console.timeEnd("Promise.race")
    console.log("率先状态为 reject 的 Promise", reason)
})
```

![图片描述](.\images\13.jpg)

所有的 promise 都是并行运行的。第四个 promise 在 3 秒内完成，所以是最先改变的就返回给Promise.race。

## 使用 promise 的经验法则

1. 使用异步或阻塞代码时，请使用 promise。
2. 为了代码的可读性，resolve 方法对待 then, reject 对应 catch 。
3. 确保同时写入.catch 和 .then 方法来实现所有的 promise。
4. 如果在这两种情况下都需要做一些事情，请使用 .finally。
5. 我们只有一次改变每个promise (单一原则)。
6. 我们可以在一个promise 中添加多个处理程序。
7. Promise对象中所有方法的返回类型，无论是静态方法还是原型方法，都是Promise。
8. 在Promise.all中，无论哪个promise 首先未完成，promise 的顺序都保持在值变量中。