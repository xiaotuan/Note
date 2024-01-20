要创建只返回一个变量或函数的模块，你可能会以为只要把 `exports` 设定成你想返回的东西就行。但这样是不行的，因为 `Node` 觉得不能用任何其他对象、函数或变量给 `exports` 赋值。下面这个代码清单中的模块代码试图将一个函数赋值给 `exports` 是不行的：

```js
class Currency {
    constructor(canadianDollar) {
        this.canadianDollar = canadianDollar;
    }
    
    roundTwoDecimals(amount) {
        return Math.round(amount * 100) / 100;
    }
    
    canadianToUS(canadian) {
        return this.roundTwoDecimals(canadian * this.canadianDollar);
    }
    
    USToCanadian(us) {
        return this.roundTwoDecimals(us / this.canadianDollar);
    }
}

// 错误， Node 不允许重写 exports
exports = Currency;
```

为了让 `Currency` 模块的代码能用，需要把 `exports` 换成 `module.exports`。用 `module.exports` 可以对外提供单个变量、函数或者对象。如果你创建了一个既有 `exports` 又有 `module.exports` 的模块，那它会返回 `module.exports`，而 `exports` 会被忽略。

