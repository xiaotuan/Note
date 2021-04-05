### 4.2.7　for…of循环

`for...of` 运算符是ES6中的新语法，它提供了另一种在集合中遍历元素的方法。它的语法是：

```javascript
for（变量 of 对象）
    语句
```

`for..of` 循环可以用在数组上，但一般它可以用于遍历任何可迭代的对象（详情见第9章）。下面这个例子使用 `for..of` 来循环一个数组中的内容：

```javascript
const hand = [randFace(), randFace(), randFace()];
for(let face of hand)
    console.log('You rolled...${face}!');
```

如果要遍历一个数组，但不需要知道每个元素的索引， `for..of` 是一个绝佳的选择。如果需要知道索引，就用常规 `for` 循环：

```javascript
const hand = [randFace(), randFace(), randFace()];
for(let i=0; i<hand.length; i++)
    console.log('Roll ${i+1}: ${hand[i]}');
```

