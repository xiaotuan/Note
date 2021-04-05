### 1.10.4　eventKeyPressed()函数

当玩家按下一个键时将调用此函数，这个函数包含了游戏中的大部分操作。JavaScript中的每个事件处理函数都会传递event对象。该对象中包含发生事件的相关信息，这里使用e参数表示该对象。

首先检测gameOver变量是否为false，如果是false，则继续检测玩家按下的是哪个键。以下代码实现了该功能：第一行代码从事件中获得按键值，并将其转换为一个字母表中的字母，用于与letterToGuess中存储的字母进行比较。

```javascript
var letterPressed = String.fromCharCode(e.keyCode);
```

下一行代码将这个字母转换为小写字母。如果玩家不小心打开大写锁定键也可以检测大写字母。

```javascript
letterPressed = letterPressed.toLowerCase();
```

接下来，增加guesses变量的计数，用于显示猜测次数。然后，使用Array.push()方法将字母添加到lettersGuessed数组。

```javascript
guesses++;
lettersGuessed.push(letterPressed);
```

检测游戏的当前状态，给予玩家反馈。首先，测试letterPressed与letterToGuess是否相同，如果相同玩家就赢了。

```javascript
if (letterPressed == letterToGuess){
　 gameOver = true;
```

如果玩家没赢，程序需要分别获得letterToGuess以及letterPressed在数组letters中的索引。下面将用这些数值计算是应该显示“Higher”还是“Lower”，或者显示“That is not a letter.”（这不是一个字母）。为此，这里使用数组的indexOf()方法获得每个字母的对应索引。由于数组是按字母顺序排列的，因此判断显示哪条信息会非常容易。

```javascript
} else {
　 letterIndex = letters.indexOf(letterToGuess);
　 guessIndex = letters.indexOf(letterPressed);
```

现在来进行检测。首先，如果guessIndex小于0，意味着indexOf()返回了−1，也就是说，按键不是一个字母，那么就显示一条错误信息。

```javascript
if (guessIndex < 0){
　 higherOrLower = "That is not a letter";
```

剩下的测试就简单了。如果guessIndex大于letterIndex，就把higherOrLower文本设为“Lower”。反之，若guessIndex小于letterIndex，就把higherOrLower文本设为“Higher”。

```javascript
　 } else if (guessIndex > letterIndex){
　　　higherOrLower = "Lower";
　 } else {
　　　higherOrLower = "Higher";
　 }
}
```

最后，调用drawScreen()在屏幕上进行绘制。

```javascript
drawScreen();
```

以下是函数的全部代码。

```javascript
function eventKeyPressed(e){
　　　if (!gameOver){
　　　　 var letterPressed = String.fromCharCode(e.keyCode);
　　　　 letterPressed = letterPressed.toLowerCase();
　　　　 guesses++;
　　　　 lettersGuessed.push(letterPressed);
　　　　 if (letterPressed == letterToGuess){
　　　　　　gameOver = true;
　　　　 } else {
　　　　　　letterIndex = letters.indexOf(letterToGuess);
　　　　　　guessIndex = letters.indexOf(letterPressed);
　　　　　　Debugger.log(guessIndex);
　　　　　　if (guessIndex < 0){
　　　　　　　 higherOrLower = "That is not a letter";
　　　　　　} else if (guessIndex > letterIndex){
　　　　　　　 higherOrLower = "Lower";
　　　　　　} else {
　　　　　　　 higherOrLower = "Higher";
　　　　　　}
　　　　 }
　　　　 drawScreen();
　　　　 }
　　　}
```

