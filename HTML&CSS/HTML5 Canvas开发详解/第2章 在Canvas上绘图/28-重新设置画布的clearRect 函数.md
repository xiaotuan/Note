### 2.11.3　重新设置画布的clearRect 函数

clearRect() 函数可以指定起始点的x、y位置以及宽度和高度来清除画布，代码如下：

```javascript
var w=theCanvas.width; 
var h=theCanvas.height; 
context.clearRect(0,0,w,h);
```

尝试使用clearRect() 函数来绘制一个路径横跨画布的动画（见例 2-28）。通过使用第1章介绍的 setTimeOut()函数来完成动画。这个函数将重复地调用drawScreen()函数并更新路径的位置。由于这个操作相比在画布上一次绘制一个路径或图形要复杂得多，因此这里给出例子的完整代码，如下：

例2-28　使用clearRect()函数

```javascript
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Chapter 2 Example 28: Animating a Path</title>
<script src="modernizr.js"></script>
<script type="text/javascript">
window.addEventListener('load', eventWindowLoaded, false);
function eventWindowLoaded() {
　　canvasApp();
}
function canvasSupport () {
　　return Modernizr.canvas;
}
function canvasApp(){
　　if (!canvasSupport()) {
　　　　　　 return;
　　}else{
　　　　var theCanvas = document.getElementById('canvas');
　　　　var context = theCanvas.getContext('2d');
　　}
　　var yOffset=0;
　　function drawScreen(){
　　　　context.clearRect(0,0,theCanvas.width,theCanvas.height);
　　　 var currentPath=context.beginPath();
　　　 context.strokeStyle = "red"; 
　　　 context.lineWidth=5;
　　　 context.moveTo(0, 0+yOffset);
　　　 context.lineTo(50, 0+yOffset);
　　　 context.lineTo(50,50+yOffset);
　　　 context.stroke();
　　　 context.closePath();
　　　　　　　yOffset+=1;
}
```

在例2-28中，首先创建一个命名为yOffset的变量，并赋值为0。下一步，在draw Screen()函数中添加一个画布清除函数。然后绘制路径，并在y轴坐标值yOffset上累加。

如第1章所示，创建一个gameLoop()函数并调用一次，在该函数中使用setTimeout()函数每20ms递归调用自身，这将导致drawScreen()函数反复被调用。在draw Screen()函数的底部，只需每次将yOffset加1，就可以创建路径向下移动的动画效果。

