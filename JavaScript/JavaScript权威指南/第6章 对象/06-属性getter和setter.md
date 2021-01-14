如果属性同时具有 getter 和 setter 方法，那么它是一个读/写属性。如果它只有 getter 方法，那么它是一个只读属性。如果它只有 setter 方法，那么它是一个只写属性（数据属性中有一些例外），读取只写属性总是返回 undefined。

定义存取器属性最简单的方法是使用对象直接量语法的一种扩展写法：

```js
var o = {
    // 普通的数据属性
    data_prop: value,
    // 存取器属性都是成对定义的函数
    get accessor_prop() { /* 这里是函数体 */ },
    set accessor_prop(value) { /* 这里是函数体 */ }
}
```

```js
var p = {
    // x 和 y 是普通的可读写的数据属性
    x: 1.0,
    y: 1.0,
    // r 是可读性的存取器属性，它有 getter 和 setter
    // 函数体结束后不要忘记带上逗号
    get r() {
        return Math.sqrt(this.x * this.x + this.y * this.y);
    },
    set r(newvalue) {
        var oldvalue = Math.sqrt(this.x * this.x + this.y * this.y);
        var ratio = newvalue /oldvalue;
        this.x *= ratio;
        this.y *= ratio;
    },
    // theta 是只读存取器属性，它只有 getter 方法
    get theta() {
        return Math.atan2(this.y, this.y);
    }
};
```

在函数体内的 this 指向表示这个点的对象。

和数据属性一样，存取器属性是可以继承的。

```js
var q = inherit(p);	// 创建一个继承 getter 和 setter 的新对象
q.x = 1, q.y = 1;	// 给 q 添加两个属性
console.log(q.r);	// 可以使用继承的存取器属性
console.log(q.theta);
```

```js
// 这个对象产生严格自增的序列号
var serialnum = {
    // 这个数据属性包含下一个序列号
    // $ 符号暗示这个属性是一个私有属性
    $n: 0,
    // 返回当前值，然后自增
    get next() {
        return this.$n++;
    },
    // 给 n 设置新的值，但只有当它比当前值大时才设置成功
    set next(n) {
        if (n >= this.$n) this.$n = n;
        else throw "序列号的值不能比当前值小";
    }
};
```

```js
// 这个对象有一个可以返回随机数的存取器属性
// 例如，表达式 "random.octet" 产生一个随机数
// 每次产生的随机数都在 0 ~ 255 之间
var random = {
    get octet() {
        return Math.floor(Math.random() * 256);
    },
    get uint16() {
        return Math.floor(Math.random() * 65536);
    },
    get int16() {
        return Math.floor(Math.random() * 65536) - 32768;
    }
};
```



