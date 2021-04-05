### 4.2.6　for…in循环

`for…in` 循环是为那些循环对象中有一个属性key而设计的。语法是：

```javascript
for（变量in对象）
    语句
```

来看一个例子：

```javascript
const player = { name: 'Thomas', rank: 'Midshipman', age: 25 };
for(let prop in player) {
    if(!player.hasOwnProperty(prop)) continue;  // 代码解释如下
    console.log(prop + ': ' + player[prop]);
}
```

如果这里觉得有点困惑，别担心，在第9章中对这个例子有更多的了解。特别说明一下，调用 `player.hasOwnProperty` 并不是必须的，但是省略它却容易造成一个常见的错误，这个内容也将在第9章中介绍。现在，只需要知道它是一种循环控制流语句。

