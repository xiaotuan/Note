### 6.6.1　使用currentTime属性创建视频事件

第一种将视频与Canvas进行结合的方式是，在播放视频时使用currentTime属性触发事件。在播放视频时，currentTime属性不断变化，表示视频已经播放的时间。

在本示例中，将使用JavaScript创建一个动态对象，对象中包含以下属性。

+ time：触发事件的时间。
+ message：显示在画布上的文本消息。
+ x：文本消息位置的x轴坐标。
+ y：文本消息位置的y轴坐标。

首先，创建一个该对象的数组并将对象放入其中，数组名是messages。然后，创建4个事件，每个事件对应的currentTime的时间分别是0s、1s、4s和8s。事件发生时会显示消息。

```javascript
var messages = new Array(); 
　 messages[0] = {time:0,message:"", x:0 ,y:0};
　 messages[1] = {time:1,message:"This Is Muir Beach!", x:90 ,y:200};
　 messages[2] = {time:4,message:"Look At Those Waves!", x:240 ,y:240};
　 messages[3] = {time:8,message:"Look At Those Rocks!", x:100 ,y:100};
```

为了显示这些消息，需要在drawScreen()函数中调用一个for:next循环。在循环中检测messages数组中的每一个消息，查看视频的currentTime属性是否大于消息的time属性。如果大于，则说明需要显示消息。然后，使用Canvas环境的fillStyle属性和fillText方法将消息显示在画布上。最终结果如图6-8所示。

```javascript
for (var i =0; i < messages.length ; i++){
　　　　 var tempMessage = messages[i];
　　　　 if (videoElement.currentTime > tempMessage.time){
　　　　　　context.font = "bold 14px sans";
　　　　　　context.fillStyle　　= "#FFFF00";
　　　　　　context.fillText　(tempMessage.message,　tempMessage.x ,tempMessage.y);
　　　　 }
　　　}
```

![114.png](../images/114.png)
<center class="my_markdown"><b class="my_markdown">图6-8　通过事件在画布中的视频上叠加文字</b></center>

当然，这是一种非常简单的创建事件的方法。但是，有些细节还不够完美，例如在添加另一个消息后，之前的消息不会消失。本示例的重点在于，通过使用类似的代码，可以在播放视频时做几乎任何事情。例如，可以暂停视频，演示一个动画，并在动画完成后继续播放视频。或者在暂停时要求用户输入，然后加载另一个不同的视频。最重要的是，可以完全按照人们希望的方式与视频进行交互。这些事件的模式与刚刚介绍的示例非常相似。

例6-8提供了这个应用程序的完整源代码。

例6-8　创建简单的视频事件

```javascript
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CH6EX8 : Creating Simple Video Events</title>
<script src="modernizr.js"></script>
<script type="text/javascript">
window.addEventListener('load', eventWindowLoaded, false);
var videoElement;
var videoDiv;
function eventWindowLoaded(){
　 videoElement = document.createElement("video");
　 videoDiv = document.createElement('div');
　 document.body.appendChild(videoDiv);
　 videoDiv.appendChild(videoElement);
　 videoDiv.setAttribute("style", "display:none;");
　 var videoType = supportedVideoFormat(videoElement);
　 if (videoType == ""){
　　　alert("no video support");
　　　return;
　 }
　 videoElement.addEventListener("canplaythrough",videoLoaded,false);
　 videoElement.setAttribute("src", "muirbeach." + videoType);
}
function supportedVideoFormat(video){
　 var returnExtension = "";
　 if (video.canPlayType("video/webm")=="probably" ||
　　　 video.canPlayType("video/webm")== "maybe"){
　　　　 returnExtension = "webm";
　 } else if(video.canPlayType("video/mp4")== "probably" ||
　　　 video.canPlayType("video/mp4")== "maybe"){
　　　　 returnExtension = "mp4";
　 } else if(video.canPlayType("video/ogg")=="probably" ||
　　　 video.canPlayType("video/ogg")== "maybe"){
　　　　 returnExtension = "ogg";
　 }
　 return returnExtension;
}
function canvasSupport (){
　　 return Modernizr.canvas;
}
function videoLoaded(){
　 canvasApp();
}
function canvasApp(){
　if (!canvasSupport()){
　　　　　return;
　　　　}
　function　drawScreen (){
　　　//背景
　　　context.fillStyle = '#ffffaa';
　　　context.fillRect(0, 0, theCanvas.width, theCanvas.height);
　　　//边框
　　　context.strokeStyle = '#000000';
　　　context.strokeRect(5,　5, theCanvas.width-10, theCanvas.height-10);
　　　//video
　　　context.drawImage(videoElement , 85, 30);
　　　// 文本
　　　context.fillStyle　　= "#000000";
　　　context.font = "10px sans";
　　　context.fillText　("Duration:" + videoElement.duration,　10 ,280);
　　　context.fillText　("Current time:" + videoElement.currentTime,　260 ,280);
　　　context.fillText　("Loop: " + videoElement.loop,　10 ,290);
　　　context.fillText　("Autoplay: " + videoElement.autoplay,　80 ,290);
　　　context.fillText　("Muted: " + videoElement.muted,　160 ,290);
　　　context.fillText　("Controls: " + videoElement.controls,　240 ,290);
　　　context.fillText　("Volume: " + videoElement.volume,　320 ,290);
　　　//显示消息
　　　for (var i =0; i < messages.length ; i++){
　　　　 var tempMessage = messages[i];
　　　　 if (videoElement.currentTime > tempMessage.time){
　　　　　　context.font = "bold 14px sans";
　　　　　　context.fillStyle　　= "#FFFF00";
　　　　　　context.fillText　(tempMessage.message,　tempMessage.x ,tempMessage.y);
　　　　 }
　　　}
}
　 var messages = new Array(); 
　 messages[0] = {time:0,message:"", x:0 ,y:0};
　 messages[1] = {time:1,message:"This Is Muir Beach!", x:90 ,y:200};
　 messages[2] = {time:4,message:"Look At Those Waves!", x:240 ,y:240};
　 messages[3] = {time:8,message:"Look At Those Rocks!", x:100 ,y:100};
　 var theCanvas = document.getElementById('canvasOne');
　 var context = theCanvas.getContext('2d');
　 videoElement.play();
　 functiongameLoop(){
　　　window.setTimeout(gameLoop,20);
　　　drawScreen();
　 }
　 gameLoop();
}
</script>
</head>
<body>
<div style="position: absolute; top: 50px; left: 50px;">
<canvas id="canvasOne" width="500" height="300">
 Your browser does not support HTML 5 Canvas.
</canvas>
</div>
</body>
</html>
```

