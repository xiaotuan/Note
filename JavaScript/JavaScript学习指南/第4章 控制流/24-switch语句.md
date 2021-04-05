### 4.2.5　switch语句

`if…else` 语句可以选择两条路径中的一条，而 `switch` 语句允许在一个单一的条件下采取多条路径。不过条件必须是比简单的真/假值更加多样化的值：对于一个 `switch` 语句来说，条件是一个可以计算值的表达式。如下 `switch` 语句的语法：

```javascript
switch（表达式）{
    case 值1：
        //当表达式的执行结果跟值1匹配的时候执行
        [break;]
    case 值2：
        //当表达式的执行结果跟值2匹配的时候执行
        [break;]
         …
    case 值N：
        //当表达式的执行结果跟值N匹配的时候执行
        [break;]
    default：
        //当表达式的结果跟任何一个值都不匹配的时候执行
       [break;]
}
```

JavaScript会计算表达式，选取第一个与结果匹配的分支，然后执行分支中的语句直到遇到 `break` 、 `return` 、 `continue` 、 `throw` 或者执行到 `switch` 语句的最后（后面会讲到这些概念）。如果觉得这些有点复杂，也没关系：因为很多开发人员经常碰到关于 `switch` 语句的错误，所以它颇受指责，这也是 `switch` 语句的缺点之一。所以新手通常都不喜欢用它。其实，如果能正确使用 `switch` 语句，它会成为一个非常有用工具，不过也得勤加练习，才能在恰当的场景发挥它的作用。

下面以一个很直观的例子开始 `switch` 语句的学习。在皇冠和锚游戏中，如果虚构的水手有多个迷信的数字，那么就可以用 `switch` 语句来合理的处理这个场景：

```javascript
switch(totalBet) {
    case 7:
        totalBet = funds;
        break;
    case 11:
        totalBet = 0; 
        break;
    case 13;
        totalBet = 0; 
        break;
    case 21:
        totalBet = 21;
        break; 
} 
```

注意当totalBet的值为11或13时，执行了相同的语句。这就是使用fall-through execution的地方。在前面说过，switch语句会一直执行，直到遇到break语句。利用这个特性的地方就叫作fall-through execution。

```javascript
switch(totalBet) {
    case 7:
        totalBet = funds;
        break;
    case 11:
    case 13:
        totalBet = 0;
        break;
    case 21:
        totalBet = 21;
        break; 
} 
```

到目前为止，代码看起来还非常直观。很显然，当托马斯拿出了11或者13便士时，他就会停止下注。但是如果13比11更不吉利呢？当拿到13时，不仅要停止下注，还要拿出1便士来做慈善。通过一些巧妙的安排来实现，可以这样做：

```javascript
switch(totalBet) {
    case 7:
        totalBet = funds;
        break;
    case 13:
        funds = funds - 1;  // 拿出一便士做慈善!
    case 11:
        totalBet = 0;
        break;
    case 21:
        totalBet = 21;
        break; 
} 
```

如果 `totalBet` 是13，就拿出一便士做慈善，但是因为这里没有 `break` 语句，会进入下一个case（11），紧接着把 `totalBet` 设为0。这是一段合法的JavaScript代码，此外，它也是正确的代码：它做了开发人员期望它做的事情。不过也存在缺点：看起来像是不小心写错了（即使它是正确的）。想象一下当另一个同事看到这段代码时，他可能会说“哎呀，这里少一个 `break` 语句。”然后加上一个 `break` 语句，如此一来这段代码就不正确了。所以很多人觉得比起它的好处，fall-through execution带来的麻烦更大，不过如果打算用这个特性，建议最好加上注释让代码的意图更明晰。

通常总是能够定义一种特殊的情况，称之为 `default` ，当其他情况都不匹配的时候，它就会被执行。普遍（不是必须的）的做法是在 `switch` 语句的最后放一个 `default` ：

```javascript
switch(totalBet) {
    case 7:
        totalBet = funds;
        break;
    case 13:
        funds = funds - 1;  // 拿出一便士做慈善！
    case 11:
        totalBet = 0; 
        break;
    case 21:
        totalBet = 21;
        break;
    default:
        console.log("No superstition here!");
        break; 
 } 
```

最后一个 `break` 其实可以省略，因为 `default` 后面并没有其他case，不过给每个case后面加上 `break` 是一个好习惯。即使在使用fall-through execution，也最好保持添加 `break` 语句的习惯：这样可以随时用注释替换break来激活fall-through execution，但是如果在正确的情况下省略break语句，那将成为一个很难定位的代码缺陷。这个规则也有一个例外：当在函数里使用 `switch` 语句的时候（详情见第6章），可以把break语句换成 `return` 语句（因为 `return` 语句会立刻结束函数执行）。

```javascript
function adjustBet(totalBet, funds) {
    switch(totalBet) {
        case 7:
            return funds;
        case 13:
            return 0;
        default:
            return totalBet;
    }
 } 
```

与往常一样，JavaScript并不关心开发人员使用了多少空格，所以为了使 `switch` 语句更简洁，通常会把 `break` （或 `return` ）语句跟case语句放在同一行。

```javascript
switch(totalBet) {
    case 7: totalBet = funds; break;
    case 11: totalBet = 0; break;
    case 13: totalBet = 0; break;
    case 21: totalBet = 21; break;
} 
```

注意，在这里选择在 `totalBet` 等于11或13的时候重复所要执行的操作：当每种case只有一条执行语句且整个 `switch` 语句没有fall-through execution的时候，为了让代码更加清晰，可以省略 `break` 语句占用的一行。

当想要基于一个表达式执行多个不同的动作时， `switch` 语句是最适合的。即便如此，在学习了第9章的动态分配后，依然会发现自己使用 `switch` 语句的频率降低了。

