### 3.13　Number, String和Boolean对象

本章一开始就提到：数字、字符串和布尔型都有对应的对象类型（ `Number` ， `String` ， `Boolean` ）。这些对象有两个用途：一是存储特殊值（比如 `Number. INFINITY` ），二是以函数的形式提供某些功能。看看下面的例子：

```javascript
const s = "hello";
s.toUpperCase();                     // "HELLO"
```

这个例子中， `s` 看起来像是一个对象（就好像它有一个函数属性，这里在访问它的函数属性）。但事实很清楚： `s` 是基本的字符串类型。那么这是怎么回事呢？JavaScript所做的事情就是创建了一个临时的 `String` 对象（该对象有一个 `toUpperCase` 函数）。一旦这个函数被调用了，该临时对象就会被删除。为了证明这一点，来尝试给字符串指定一个属性：

```javascript
const s = "hello";
s.rating = 3;                       // 咦，竟然没报错，成功了?
s.rating;                           // undefined
```

JavaScript允许这么做，这看起来像是给字符串 `s` 指定了一个属性。而实际上，是在给JavaScript创建的临时String对象指定了一个属性。这个对象在使用后会立刻被删除，这就是为什么 `s.rating` 返回的结果是 `undefined` 。

JavaScript的这个行为对程序员来说是透明的，程序员几乎不用（如果有）去思考它，但是了解JavaScript在背后做了什么是非常有用的。

