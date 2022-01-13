`JavaScript` 所有的函数作用域内都有一个 this 对象代表调用该函数的对象。在全局作用域中，this 代表全局对象（浏览器中的 window）。当一个函数作为对象的方法被调用时，默认 this 的值等于那个对象。

```js
var person = {
    name: "Nicholas",
    sayName: function() {
        console.log(this.name);
    }
};
person.sayName();   // output "Nicholas"
```

