### 4.2.2　链式if…else语句

链式 `if..else` 语句并不是一种特殊的语法：它只是一系列简单的 `if..else` 语句的集合，其中的每个 `else` 字句包含了另一个 `if..else` 语句。这是一种非常值得一提的通用模式。比如，如果托马斯的迷信行为延续了整个星期，而且每到周三，他只拿一便士下注。这段逻辑用 `if..else` 来写就是这样的：

```javascript
if(new Date().getDay() === 3) {   // new Date().getDay() 返回当前所在的星期
    totalBet = 1;                 // 的数字，星期天是0
} else if(funds === 7) {
    totalBet = funds;
} else {
    console.log("No superstition here!");
} 
```

按照这种方式组合了 `if..else` 语句后，就有了三种选择。聪明的读者可能意识到这种做法违反了自己建立的规则（不要把单行语句和块语句放在一起），这种情况是一个特例：它是一个很常见的模式，并且代码清晰易读。这个例子也可以用块语句重写为：

```javascript
if(new Date().getDay() === 3) {
    totalBet = 1;
} else {
    if(funds === 7) {
        totalBet = funds;
    } else {
        console.log("No superstition here!");
    }
} 
```

不难看出，这样写并没有使代码更清楚，而且代码更加冗长了。

