所有对象都继承自 `Object.prototype`。任何以对象字面形式定义的对象，其 `[[Prototype]]` 的值都被设为 `Object.prototype`。

继承自 Object.prototype  的方法有：

| 方法名                 | 描述                                   |
| ---------------------- | -------------------------------------- |
| hasOwnProperty()       | 检查是否存在一个给定名字的自有属性     |
| propertyIsEnumerable() | 检查一个自有属性是否可枚举             |
| isPrototypeOf()        | 检查一个对象是否是另一个对象的原型对象 |
| valueOf()              | 返回一个对象的值表达                   |
| toString()             | 返回一个对象的字符串表达               |

你也可以定义自己的上面方法，例如：

```js
var book = {
    title: "The Principles of Object-Oriented JavaScript",
    toString: function() {
        return "[Book" + this.title + "]"
    }
};
var message = "Book = " + book;	// "Book = [Book The Principles of Object-Oriented JavaScript]"
console.log(message);
```

> 警告
>
> 所有的对象都默认继承自 `Object.prototype`，所以改变 `Object.prototype` 会影响所有的对象，这是非常危险的。