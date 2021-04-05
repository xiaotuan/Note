### 3.11　null和undefined

JavaScript有两种特殊的类型， `null` 和 `undefined` ，它们两个都只有一个唯一的值，分别是 `null` 和 `undefined` 。这两者都表示不存在。实际上存在两种独特的数据类型就已经造成了很大的困惑，尤其是对于初学者。

一般的经验是， `null` 是给开发者用的，而 `undefined` 则是留给JavaScript用的，用来表示未赋值的内容。这并不是强制的规则，开发人员也可以随时使用undefined。但常识表明，应该非常谨慎地使用它。在以往的经验中，只有在有意的模仿变量未被赋值的时候，才会使用 `undefined` 。当需要表示一个变量的值未知或者不适用的时候，常见的做法是使用 `null` 。这似乎有点小题大做，但这确实很重要--建议编程新手在不确定该使用哪一个的时候使用null。注意，如果声明变量的时候没有赋值，变量会有一个默认的值 `undefined` 。下面例子使用了 `null` 和 `undefind` 的字面量：

```javascript
let currentTemp;              // 隐含值 undefined
const targetTemp = null;      // targetTemp 为 null -- "还不知道"
currentTemp = 19.5;           // currentTemp 此时已经有值
currentTemp = undefined;      // currentTemp 看上去跟未初始化一样，不推荐这么做
```

