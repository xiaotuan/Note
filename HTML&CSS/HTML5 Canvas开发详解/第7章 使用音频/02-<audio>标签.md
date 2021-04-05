### 7.1　<audio>标签

在HTML5中，<audio>标签的基本用法与<video>标签非常相似。唯一必需的属性是src，指向一个用于在浏览器中播放的音频文件。当然，如果在页面上能显示一些音频控制功能会更好。通过设置contorls布尔值就可以实现这个功能，就像在<video>标签中做的那样。

可以在支持.ogg音频文件回放的浏览器中加载例7-1中的代码，并将其用于播放song1.ogg。页面效果如图7-1所示。注意，不是所有的浏览器都支持全部的音频格式。

例7-1　HTML5音频基础用法

```javascript
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CH7EX1: Basic HTML5 Audio</title>
</head>
<body>
<div>
<audio src="song1.ogg" controls>
Your browser does not support the audio element.
</audio>
</div>
</body>
</html>
```

![123.png](../images/123.png)
<center class="my_markdown"><b class="my_markdown">图7-1　最基本的HTML5 <audio> 标签</b></center>

