### 4.3.1　使用continue减少条件嵌套

常见的情况是，在循环体中，只希望在某些特定条件下继续执行循环体（尤其是当循环控制和条件控制结合起来的时候）。比如：

```javascript
while(funds > 1 && funds < 100) {
    let totalBet = rand(1, funds);
    if(totalBet === 13) {
        console.log("Unlucky!  Skip this round....");
    } else {
        // play... 
    } 
} 
```

这是一个典型的嵌套控制流：在 `while` 语句的循环体中，有一大部分语句在 `else` 中；在 `if` 语句只是简单调用了 `console.log` 。这里就可以使用 `continue` 语句使结构更加“扁平”：

```javascript
while(funds > 1 && funds < 100) {
    let totalBet = rand(1, funds);
    if(totalBet === 13) {
        console.log("Unlucky!  Skip this round....");
        continue; 
    } 
    // play... 
} 
```

在这个简单的例子中，使用 `continue` 并不能产生立竿见影的好处，但是想象一下，如果循环体不是1行，而是20行。从嵌套的控制流中删除这些行，会使代码更易于理解且大大提高了可读性。

