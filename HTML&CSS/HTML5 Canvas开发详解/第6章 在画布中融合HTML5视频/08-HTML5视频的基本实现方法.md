### 6.3　HTML5视频的基本实现方法

在<video>标签最简单的用法中，只需要指定一个合法的src属性就可以了。例如，如果在加利佛尼亚旧金山北部Muir海滩拍摄了一段海浪拍击礁石的视频，并且将它编码为H.264的.mp4文件，可以采用如下代码。

```javascript
<video src="muirbeach.mp4" />
```

提示

> 如果想查看基本代码的示例，请在下载的代码中找到CH6EX1.html文件。

在一个HMTL5内嵌的视频中，可以设置许多属性。这些属性实际上是被HTMLVide oElement对象实现的HTMLMediaElement接口的一部分。其中一些比较重要的属性如下。

+ src：要播放的视频的URL地址。
+ autoplay：设置为true或false。当加载结束后，强制自动播放视频。
+ loop：设置为true或false。当视频结束播放后，从视频开始循环播放。
+ volume：设置为0～1之间的数字。设置播放视频的音量。
+ poster：设置一个图片的URL地址。当加载视频时，显示该图片。

当通过JavaScript播放视频以及与Canvas结合时，还会用到一些HTMLVideoElement的方法。

+ play()：用于启动视频播放。
+ pause()：用于暂停视频播放。

此外，还有以下一些用于检查视频状态的属性。

+ duration：视频的长度，单位是秒。
+ currentTime：视频的当前播放时间，单位是秒。这个属性与duration结合可以实现一些有趣的效果，本章后面将会介绍。
+ ended：返回值为true或false，取决于视频是否已经播放结束。
+ muted：返回值为true或false，用于查询播放中的视频是否静音。
+ paused：返回值为true或false，用于查询视频当前是否被暂停。

提示

> HTMLVideo还有许多属性，关于属性的详细信息请访问w3的官方网站。

