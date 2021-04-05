### 1.10.5　drawScreen()函数

下面开始编写drawScreen()函数。之前已经学习过其中的大部分代码了——代码几乎与“Hello World!”中的代码相同。例如，这里使用Canvas文本API在屏幕上绘制多个变量。仅需要设置一次context.textBaseline = 'top'，就可以对所有显示的文本生效。另外，还可以使用context.fillStyle改变颜色，使用ontext.font改变字体。

这里最有趣的事就是显示lettersGuessed数组的内容。在画布上，数组将显示为一组用逗号分隔的字符串，例如：

```javascript
Letters Guessed: p,h,a,d
```

为了输出这个字符串，只需使用lettersGuessed数组的toString()方法，即可以使用逗号间隔的方式打印出玩家猜到的数组。

```javascript
context.fillText ("Letters Guessed: " + lettersGuessed.toString(), 10, 260);
```

接下来，还需检测gameOver变量。如果结果为真，程序在屏幕上使用大字号（40px）显示文本“You Got It！”（你胜利了）。这样，用户就知道自己获胜了。

以下是函数的完整代码。

```javascript
function drawScreen(){
　　　 //背景
　　　 context.fillStyle = "#ffffaa";
　　　 context.fillRect(0, 0, 500, 300);
　　　 //边框
　　　 context.strokeStyle = "#000000";
　　　 context.strokeRect(5, 5, 490, 290);
　　　 context.textBaseline = "top";
　　　 //日期
　　　 context.fillStyle = "#000000";
　　　 context.font = "10px Sans-Serif";
　　　 context.fillText (today, 150 ,10);
　　　 //消息
　　　 context.fillStyle = "#FF0000";
　　　 context.font = "14px Sans-Serif"; 
　　　 context.fillText (message,125,30);
　　　 //猜测的次数
　　　 context.fillStyle = "#109910";
　　　 context.font = "16px Sans-Serif";
　　　 context.fillText ('Guesses: ' + guesses, 215, 50);
　　　 //显示Higher或Lower
　　　 context.fillStyle = "#000000";
　　　 context.font = "16px Sans-Serif";
　　　 context.fillText ("Higher Or Lower: " + higherOrLower, 150,125);
　　　 //猜过的字母
　　　 context.fillStyle = "#FF0000";
　　　 context.font = "16px Sans-Serif";
　　　 context.fillText ("Letters Guessed: " + lettersGuessed.toString(), 
　　　　　　　　　　　　　　　10, 260);
　　　 if (gameOver){
　　　　　 context.fillStyle = "#FF0000";
　　　　　 context.font = "40px _ sans-serif";
　　　　　 context.fillText ("You Got It!", 150, 180);
　　　 }
　 }
```

