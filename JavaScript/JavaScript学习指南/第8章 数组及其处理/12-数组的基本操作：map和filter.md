### 8.4　数组的基本操作：map和filter

在所有的数组操作中，大家会发现最有用的还是 `map` 和 `filter` 。这两个方法能做的事情绝对不能不提。

`map` 可以把元素转换成数组。至于转成什么类型的数组，这就是 `map` 的优美之处：类型由开发人员决定。大家有没有遇到过对象中含有数字，但是只需要数字的情况？有没有遇到过数组中包含函数，而需要promise的情况？map很容易满足这些需求。任何时候如果数组格式与所需要的格式不一样，就用 `map` 。 `map` 和 `filter` 都不会修改原始数组，而是返回数组的拷贝。来看一些例子：

```javascript
const cart = [ { name: "Widget", price: 9.95 }, { name: "Gadget", price: 22.95}];
const names = cart.map(x => x.name);            // ["Widget", "Gadget"]
const prices = cart.map(x => x.price);          // [9.95, 22.95]
const discountPrices = prices.map(x => x*0.8);  // [7.96, 18.36]
const lcNames = names.map(String.toLowerCase);  // ["widget", "gadget"]
```

大家可能会好奇 `lcNames` 是怎么工作的：它看起来跟其他数组不一样。这里讨论到的所有方法，包括 `map` ，都可以接收一个函数作为参数，而且它们不关心函数是以哪种方式传入的。在 `names` ， `prices` ，和 `discountPrices` 的例子中，都构造了自定义的方法（用箭头符号）。而在 `lcNames` 中，用了一个早已存在的方法， `String.toLowerCase` 。这个方法会接收一个字符串，返回该字符串的小写字符串。这使得可以很简单地写下 `names.map` ( `x` ⇒  `x.toLowerCase()` )，不过一定要知道，方法就是方法，无论它是哪种格式，理解这一点很重要。

数组每个元素在调用提供的方法时都会传入三个参数：元素本身、元素的下标，以及数组本身（这个不常用）。来看一下这个例子：items和其对应的prices分别在两个独立的数组中，将它们合并起来：

```javascript
const items = ["Widget", "Gadget"];
const prices = [9.95, 22.95];
const cart = items.map((x, i) => ({ name: x, price: prices[i]}));
// cart: [{ name: "Widget", price: 9.95 }, { name: "Gadget", price: 22.95 }]
```

这个例子有点复杂，不过它很好地演示了 `map` 函数的作用。在这里，不仅使用了元素本身（x），还有它的索引（i）。之所以需要索引是因为需要根据索引来关联 `items` 和 `prices` 中的元素。这里 `map` 通过从不同的数组中提取信息，从而把一个字符串类型的数组转化成了一个对象数组。（注意，在这里要把对象用小括号包裹起来，因为如果没有小括号，箭头操作符会把花括号中的内容当成程序块）。

`filter` ，顾名思义，它是用来删除数组中不需要的元素。像 `map` 一样，它返回一个删除了某些元素的数组。那么，哪些元素会被删除呢？同样，这也完全取决于开发人员。如果读者觉得这里会定义一个函数来决定哪些元素要被删除，那么值得恭喜，答对了！来一起看个例子吧：

```javascript
// 创建一副牌
const cards = [];
for(let suit of ['H', 'C', 'D', 'S']) // hearts, clubs, diamonds, spades
    for(let value=1; value<=13; value++)
        cards.push({ suit, value });
// 找到所有含有2的卡片：
cards.filter(c => c.value === 2);    // [
                                          //    { suit: 'H', value: 2 },
                                          //    { suit: 'C', value: 2 },
                                          //    { suit: 'D', value: 2 },
                                          //    { suit: 'S', value: 2 }
                                          // ]
// (简单起见，下面的代码中只列出数组长度)
// 找到所有方块：
cards.filter(c => c.suit === 'D');        // length: 13
// 找到所有花色牌
cards.filter(c => c.value > 10);          // length: 12
// 找到所有为红桃的花色牌
cards.filter(c => c.value > 10 && c.suit === 'H');  // length: 3
```

希望大家已经了解了如何将 `map` 跟 `filter` 结合起来使用从而产生良好的效果。例如，想为上述的卡片创建一个简短的介绍。这里将使用Unicode来表示牌的花色，还用到了“A”“J”“Q”“Q”表示王牌和人头牌。由于构造出的这个函数太长了，另外会创建一个单独的函数，而非一个匿名函数。

```javascript
function cardToString(c) {
   const suits={'H': '\u2665','C': '\u2663', 'D': '\u2666', 'S': '\u266 0'};
   const values = { 1: 'A', 11: 'J', 12: 'Q', 13: 'K' };
    // 每次调用cardToString的时候去构建值，不是一个高效的方式 
    // 如何找出一个高效的方法就作为读者练习吧
    for(let i=2; i<=10; i++) values[i] = i;
    return values[c.value] + suits[c.suit];
}
// 找到所有包含2的牌:
cards.filter(c => c.value === 2)
   .map(cardToString); // [ "2♥", "2♣", "2♦", "2♠" ] 
// 找到所有红桃的花色牌
cards.filter(c => c.value > 10 && c.suit === 'H') 
   .map(cardToString); // [ "J♥", "Q♥", "K♥" ] 
```

