### 6.4　使用JavaScript预加载视频

在对视频进行操作之前，通常需要预先加载视频。特别是在HTML5 Canvas中使用视频的时候，这是因为在大多数情况下，在画布中进行的视频操作比单纯播放视频要复杂得多。

本节将运用DOM和JavaScript创建一个可重用而且可扩展的预加载机制。尽管暂时还没有涉及到Canvas，但是这个过程是直接针对Canvas的。

为此，需要利用本章之前介绍的方法在HTML页面中嵌入一个视频。然后，添加一个id为loadingStatus的<div>标签。

提示

> 在实际情况中，也许不需要在HTML页面上显示加载进度。

当通过JavaScript接收视频数据时，<div>将显示视频加载进度的百分比。

```javascript
<div>
<video loop controls id="thevideo" width="320" height="240" preload="auto">
 <source src="muirbeach.webm" type='video/webm; codecs="vp8, vorbis"' >
 <source src="muirbeach.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"' >
 <source src="muirbeach.ogg" type='video/ogg; codecs="theora, vorbis"'>
</video>
</div>
<div id="loadingStatus">
0%
</div>
```

本书在前面曾经多次创建eventWindowLoaded()函数。本次需要使用JavaScript创建一个相同类型的函数，在HTML页面加载结束时调用这个函数。在event WindowLoaded()中需要创建两个事件处理函数，分别对应HTMLVideoElement对象的两个事件。

+ progress：在视频对象更新视频加载进度信息的时候触发该事件。该事件将用于更新id为loadingStatus的<div>标签中的文字。
+ canplaythrough：在视频已经加载足够播放全部视频的数据时触发该事件。通过这个事件可以得知什么时候开始播放视频。

以下是为这些事件创建的监听器的代码。

```javascript
function eventWindowLoaded(){
　 var videoElement = document.getElementById("thevideo");
　 videoElement.addEventListener('progress',updateLoadingStatus,false);
　 videoElement.addEventListener('canplaythrough',playVideo,false);   
}
```

当video对象触发progress事件时，将调用updateLoadingStatus()函数。这个函数将计算已经加载的字节数（videoElement.buffered.end(0)）与总字节数（videoElement. duration）比例，然后再乘以100，最终得到加载进度的百分比。通过将id设置为loadingStatus的<div>标签的innerHTML属性，将百分比显示出来，如图6-5所示。注意，此处仅显示加载进度。当视频加载完成时，还需要进行处理。

```javascript
function updateLoadingStatus(){
　 var loadingStatus = document.getElementById("loadingStatus");
　 var videoElement = document.getElementById("thevideo");
　 var percentLoaded = parseInt(((videoElement.buffered.end(0)/
　　　videoElement.duration)* 100));
　　document.getElementById("loadingStatus").innerHTML =　 percentLoaded + '%';
}
```

![111.png](../images/111.png)
<center class="my_markdown"><b class="my_markdown">图6-5　使用JavaScript预加载视频</b></center>

当video对象触发canplaythrough事件时，将调用playVideo()函数。playVideo()函数将调用video对象的play()方法，然后开始播放视频。

```javascript
function playVideo(){
　 var videoElement = document.getElementById("thevideo");
　 videoElement.play();
}
```

例6-5给出了预加载视频的完整代码。

例6-5　基本的HTML5预加载视频

```javascript
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CH6EX5: Basic HTML5 Preleoading Video</title>
<script type="text/javascript">
window.addEventListener('load', eventWindowLoaded, false); 
function eventWindowLoaded(){
　 var videoElement = document.getElementById("thevideo");
　 videoElement.addEventListener('progress',updateLoadingStatus,false);
　 videoElement.addEventListener('canplaythrough',playVideo,false);
}
function updateLoadingStatus(){
　 var loadingStatus = document.getElementById("loadingStatus");
　 var videoElement = document.getElementById("thevideo");
　 var percentLoaded = parseInt(((videoElement.buffered.end(0)/
　　　 videoElement.duration)* 100));
　　 document.getElementById("loadingStatus").innerHTML =　 percentLoaded + '%';
}
function playVideo(){
　 var videoElement = document.getElementById("thevideo");
　 videoElement.play();
}
</script>
</head>
<body>
<div>
<video loop controls id="thevideo" width="320" height="240" preload="auto">
 <source src="muirbeach.webm" type='video/webm; codecs="vp8, vorbis"' >
 <source src="muirbeach.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"' >
 <source src="muirbeach.ogg" type='video/ogg; codecs="theora, vorbis"'>
</video>
</div>
<div id="loadingStatus">
0%
</div>
</body>
</html>
```

提示

> 完成练习后，有一个坏消息要告诉读者。除了部分浏览器，示例CH6EX5.html中的代码可以在大多数HMTL5兼容的浏览器中正常运行。经过一些调查发现，Chrome跟IE10浏览器没有触发progress事件。与此同时，FireFox删除了load事件。这些问题之所以存在，其原因是一个简单的事实：HTML5的标准还没有完成。这是一个简单却重要的事实：在开发HTML5或Canvas应用时，标准可能一直在变化。这显然是不得不面对的问题。如果你正在开发HTML5或Canvas，你就得跟上它的步伐。

