### 3.1.2　在Text Arranger中处理基本文本

Text Arranger将允许用户通过调用context.fillText()设置显示的文本字体。为此，本节将创建一个名为message的变量，用来存储用户提供的文本。随后再调用context.fillText()使用该变量。Context.fillText()位于第1章中介绍过的标准drawScreen()方法的内部，并会在整本书中继续使用它。

```javascript
var message ="your text";
...
function drawScreen() {
　...
　context.fillStyle = "#FF0000";
　context.fillText (message, 100, 80);
}
```

要把画布上显示的文本改成用户输入的文本，本节需要为文本框keyup事件创建一个事件处理程序。这意味着无论何时文本框中的文本发生任何改变，都会调用事件处理程序函数。

为了实现这一功能，这里使用<input>表单元素在HTML<form>中命名文本框。注意，id设置的值是textBox。同时要注意的是，设置placeholder=""的属性。这是HTML5的一个新属性，所以不一定能在每个浏览器中运行。也可用value=""来替代，并且不会影响该应用程序的执行。

```javascript
<form>
　Text: <input id="textBox" placeholder="your text"/>
　<br>
</form>
```

