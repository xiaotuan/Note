### 10.1.2　查看BSBingo.html的代码



提示

> 当设计一个面向iOS平台的应用程序时，实际上是针对Safari Mobile浏览器开发。这意味着不用面向所有兼容HTML5的设备，因此可以做出一些让步。当讨论<audio>标签使用时，读者就会注意到这点。

#### 1．TextButton.js文件

本节的BS Bingo游戏将在一个由25个方格组成的表格中进行。创建一个名为TextButton.js的类（实际上是一个对象原型）。通过这个类，可以使用文本创建按钮。这个类还有一个“按下”状态，将在按钮被单击时显示该状态。读者可以将代码文件与BSBingo文件一起保存在工程文件夹之中。以下是文件中的代码。

```javascript
function TextButton(x,y,text, width, height, backColor, strokeColor,   
　overColor, textColor){
　　this.x=x;
　　this.y=y;
　　this.text=text;
　　this.width=width;
　　this.height=height;
　　this.backColor=backColor;
　　this.strokeColor=strokeColor;
　　this.overColor=overColor;
　　this.textColor=textColor;
　　this.press=false;
}
TextButton.prototype.pressDown=function(){
　　if (this.press==true){
　　　　this.press=false;
　　}else{
　　　　this.press=true;
　　}
}
TextButton.prototype.draw=function(context){
　　context.save();
　　context.setTransform(1,0,0,1,0,0); // 重置形状变换矩阵
　　context.translate(this.x, this.y);
　　context.shadowOffsetX=3;
　　context.shadowOffsetY=3;
　　context.shadowBlur=3;
　　context.shadowColor="#222222";
　　context.lineWidth=4;
　　context.lineJoin='round';
　　context.strokeStyle=this.strokeColor;
　　if (this.press==true){
　　　　context.fillStyle=this.overColor;
　　}else{
　　　 context.fillStyle=this.backColor;
　　}
　　context.strokeRect(0, 0, this.width,this.height);
　　context.fillRect(0, 0, this.width,this.height);
　　//文本
　　context.shadowOffsetX=1;
　　context.shadowOffsetY=1;
　　context.shadowBlur=1;
　　context.shadowColor="#ffffff";
　　context.font =　"14px serif"
　　context.fillStyle = this.textColor;
　　context.textAlign="center";
　　context.textBaseline="middle";
　　var metrics = context.measureText(this.text)
　　var textWidth = metrics.width;
　　var xPosition =　this.width/2;
　　var yPosition = (this.height/2);
　　var splitText=this.text.split('\n');
　　var verticalSpacing=14;
　　for (var ctr1=0; ctr1<splitText.length;ctr1++){
　　　　context.fillText　( splitText[ctr1],　xPosition,   
　　　　yPosition+ (ctr1*verticalSpacing));
　　}
　　context.restore();
}
```

这个对象原型中包含了创建和绘制按钮，以及响应单击事件的函数。按钮是灰色的方形，上面显示黑色的文字。当用户单击时，按钮将用黄色背景绘制。在本书前面的章节介绍过所有这些绘制函数，如果读过这些章节，读者应该对这些代码很熟悉。如果还不熟悉，最好参考第2章，其中介绍了使用路径绘制对象以及对象阴影的方法。

下面快速浏览在创建bsbingo.html时会用到的其他函数。

#### 2．initLists()函数

initLists是读者遇到的第一个与游戏相关的函数。由于要实现的游戏比较简单，因此会创建一个单词列表，其中的单词都是一些常见的业务时髦语。standardJargonList是一个应用程序作用域范围的变量。这个变量保存一个一维的单词数组。这些词将被随机地放置在玩家的bingo卡片上。如果想针对其他类型的时髦口头语，可以添加更多列表的类型，例如纯IT流程用语、市场用语、运动用语等。

#### 3．initButtons()函数

这个函数创建一个由25个TextButton实例组成的表格。按钮的宽度是85像素，高度是25像素。这些按钮保存在一个应用程序作用范围的二维按钮数组中，可以通过[行][列]的语法形式访问它们。

#### 4．initSounds()函数

initSound函数只需要初始化一个声音。这个声音引用一个HTML5 <audio>标签。由于面向的是iOS平台，因此仅需要提供一个.mp3格式的声音，不需要.ogg和.wav的格式，因为不用针对其他浏览器。以下是HTML <audio>标签。

```javascript
<audio id="clicksound" preload="auto">
　　<source src="click.mp3" type="audio/mpeg" />
Your browser does not support the audio element.
</audio>
```

#### 5．chooseButtonsForCard()函数

此函数创建了一个名为tempArray的本地数组，用standardJargonList中的数据进行填充。接下来，这个函数将为组成bingo卡片的5行×5列的每一个方格，随机地从tempArray中选择一个元素。如果函数选择了一个单词，就会将这个单词从tempArray中删除。这样，这个单词就不会被重复选中了，保证卡片上没有重复的单词。

#### 6．drawScreen()函数

此函数遍历buttons二维数组，将初始的25个按钮和文字绘制在画布上。

#### 7．onMouseClick()函数

当用户在游戏屏幕上单击鼠标时，这个事件监听函数将判断25个方格中哪个按钮被点中了。程序将调用对应TextButton实例的pressDown()函数，然后调用draw()函数并传入环境对象中。

#### 8．onMouseMove()函数

当鼠标移动时，这个事件监听函数将把mouseX和mouseY的值设置为鼠标在画布上的当前位置。

