### 6.5　this关键字

在函数体中，有一个特殊的只读字段 `this` 。这个关键字通常与面向对象编程一起出现，在第9章会了解到更多关于this在面向对象中的用法。然而，在JavaScript中，this关键字还是有很多使用场景的。

`this` 关键字通常关联那些作为对象属性的函数。当方法被调用时， `this` 关键字的值就是被调用的对象：

```javascript
const o = {
   name: 'Wallace',
   speak() { return 'My name is ${this.name}!'; },
}
```

当调用 `o.speak()` 的时候， `this` 关键字跟 `o` 进行了绑定：

```javascript
o.speak();            // "My name is Wallace!
```

如何绑定this是由方法如何被调用所决定的，而非函数定义所决定，理解这一点非常重要。也就是说，在这里，this绑定到o上并不是因为speak是o的属性，而是因为它直接由o调用（o.speak）。如果把同一个函数赋值给一个对象，会发生什么呢？

```javascript
const speak = o.speak;
speak === o.speak;                // 为真; 两个变量都指向了同一个函数
speak();                          // "My name is !"
```

由于调用函数的方式，JavaScript并不知道原始函数是在o中定义的，所以this将会绑上undefined。

> <img class="my_markdown" src="../images/2.png" style="width:116px;  height: 151px; " width="10%"/>
> 如果以一种不清楚如何绑定 `this` 的方式来调用函数（就像前面的例子中调用函数变量 `speak` ）， `this` 的绑定就会变得很复杂。这取决于是否使用了严格模式，以及函数在哪里被调用。之所以刻意掩盖了这些细节是因为作者认为最好避开这种情况。如果想深入了解，可以参阅关于代码格式化的MDN文档。

方法这个叫法最初是与面向对象编程结合在一起的，在本书中，用它来表示那些作为对象属性的函数，同时它们被设计成可以直接从对象实例（就像 `o.speak()` ）中调用。如果一个函数不使用this，JavaScript就会将它当成一个普通函数，而不管它在哪里定义。

关于 `this` 变量的一个细节是，当在嵌套函数中访问它时经常会出错。下面这个例子就是在方法中使用了辅助函数：

```javascript
const o = {
    name: 'Julie',
    greetBackwards: function() {
       function getReverseName() {
          let nameBackwards = '';
          for(let i=this.name.length-1; i>=0; i--) {
               nameBackwards += this.name[i];
           }
           return nameBackwards;
        }
        return '${getReverseName()} si eman ym ,olleH';
    },
};
o.greetBackwards();
```

这里使用了嵌套函数， `getReverseName` ，是为了反序列名字。但是， `getReverseName` 并没有像所期望的那样运行：当调用 `o.greetBackwards()` 时，JavaScript像预期那样给 `this` 绑定了值。然而，在 `greetBackwards` 中调用 `getReverseName` 函数时， `this` 却绑到了其他地方<sup><a href="#anchor61" id="ac61"><sup class="my_markdown">[1]</sup></a></sup>。一个常用的解决方案给 `this` 赋另一个变量：

```javascript
const o = {
    name: 'Julie',
    greetBackwards: function() {
        const self = this;
        function getReverseName() {
           let nameBackwards = '';
           for(let i=self.name.length-1; i>=0; i--) {
              nameBackwards += self.name[i];
           }
           return nameBackwards;
        }
        return '${getReverseName()} si eman ym ,olleH';
    },
};
o.greetBackwards();
```

这是一个常用的技巧，通过它 `this` 会被赋值给 `self` 。箭头函数也可以用来解决这个问题，本章的后面会讲到。

