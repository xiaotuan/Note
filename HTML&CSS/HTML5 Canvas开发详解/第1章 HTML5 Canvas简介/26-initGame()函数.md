### 1.10.3　initGame()函数

initGame()函数为玩家初始化游戏。以下是两段重要的代码。第一段代码从字母数组中找出一个随机字母，然后将其储存在letterToGuess变量中。

```javascript
var letterIndex = Math.floor(Math.random()* letters.length);
letterToGuess = letters[letterIndex];
```

第二段代码为DOM的window对象添加了一个事件监听器，以“监听”键盘的keydown事件。当某个键被按下时，将调用eventKeyPressed事件处理函数检测按下的字母。

```javascript
window.addEventListener("keydown",eventKeyPressed,true);
```

以下是函数的全部代码。

```javascript
function initGame(){
　 var letterIndex = Math.floor(Math.random()* letters.length);
　 letterToGuess = letters[letterIndex];
　 guesses = 0;
　 lettersGuessed = [];
　 gameOver = false;
　 window.addEventListener("keydown",eventKeyPressed,true);
　 drawScreen();
}
```

