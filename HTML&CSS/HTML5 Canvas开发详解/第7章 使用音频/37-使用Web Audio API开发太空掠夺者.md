### 7.7.2　使用Web Audio API开发太空掠夺者

接下来将使用Web Audio API开发新版的太空掠夺者。首先我们需要获取一个AudioContext对象。不过在写作本书时，仅有Chrome支持该接口，因此需要使用webkitAudioContext来代替AudioContext（尽管理论上Safari也支持该接口，但测试发现并不可行）。

```javascript
var audioContext = new webkitAudioContext();
```

生成一对用于存储音频缓存的变量（射击和爆炸）。

```javascript
var shootSoundBuffer;
var explodeSoundBuffer;
```

接着加载声音。为了让代码更加简明，创建一个函数用于加载音频。该函数仅接收一个名为url的参数，该参数则代表了声音文件的位置和文件名。在函数initApp()中，先获取audioType的值，然后再调用两个新的函数加载声音。

```javascript
audioType = supportedAudioFormat(tempSound);
loadExplodeSound("explode1." + audioType);
loadShootSound("shoot1."+ audioType);
```

下一步，创建加载声音的两个函数。首先，需要创建XMLHttpRequest()的一个实例，并设置responseType为arraybuffer，将其配置为二进制数据。XMLHttpRequest()新实现的数据加载方式允许加载二进制文件，如音频文件。

然后，通过设置内嵌匿名函数作为onload的回调函数，为已加载的音频创建一个缓冲区。在这个函数中，通过调用audioContext. decodeAudioData()函数将二进制文件加载到制定的音频缓存区中。

该方法共有以下3个参数：

（1）音频数据（生成一个XMLHttpRequest，并调用request.response获取）；

（2）成功回调函数（一个内嵌匿名函数，后面将会介绍）；

（3）失败回调函数，名为onSoundError()。

成功回调函数仅有一个参数，该参数为包含音频数据的缓冲区。将该缓冲区的值传递给shootSoundBuffer，就可以在游戏中通过调用shootSoundBuffer播放该声音。然后调用itemLoaded()函数，修改太空掠夺者游戏中loadCount变量的值。

```javascript
function loadShootSound(url) {
　　　　　 var request = new XMLHttpRequest();
　　　　　 request.open('GET', url, true);
　　　　　 request.responseType = 'arraybuffer';
　　　　　 request.onload = function() {
　　　　　　　　 audioContext.decodeAudioData(
　　　　　　　　 request.response, 
　　　　　　　　 function(buffer) {
　　　　　　　　 shootSoundBuffer = buffer;
　　　　　　　　 itemLoaded();
　　　　　　　　 }, onSoundError);
　　　 };
　　　request.send();
　　}
function onSoundError(e) {
　　alert("error loading sound")
}
```

接着为爆炸声创建类似的函数，唯一的区别是在成功回调函数里将缓冲区的值传递给explodeSoundBuffer。

```javascript
explodeSoundBuffer = buffer;
```

至此，在游戏中将音频的缓冲变量传递给函数playSound()，就可以播放音频。

```javascript
playSound(shootSoundBuffer);
```

由于不需要管理声音的众多复本，因此现在的playSound()函数和之前的函数已经完全不同。在该函数中，首先通过调用audioContext.createBufferSource()获取到AudioBufferSourceNode的实例，并将它保存到变量source中。这个对象中保存着即将播放的声音。接着，将此函数中传入的缓冲区对象赋值给source的buffer属性。这个缓冲区对象表示内存中的一个声音数据（射击声或爆炸声）。

然后，通过调用audioContext.connect()函数为音频设置播放器（在这就使用默认的播放器，即电脑的扬声器）。最后调用函数source.noteOn()，并传入参数0（0标志着立即播放）。

由于AudioBufferSourceNode实例的函数noteOn()仅在第一次调用时有效，因此无须保存该source实例。当再次需要播放音频时，则再次产生一个实例。此外，音频播放完毕，浏览器会自动收集并释放该引用。

```javascript
function playSound(soundBuffer) {
　　var source = audioContext.createBufferSource();
　　source.buffer = soundBuffer;
　　source.connect(audioContext.destination);
　　source.noteOn(0);
}
```

最后，为游戏添加自动射击功能。在此需添加两个变量：shootWaitFrames代表已等待时长，shootWait代表射击间隔。

```javascript
var shootWaitedFrames = 8;
var shootWait = 8;
```

然后，在函数drawScreen()中添加以下代码来实现这个功能。

```javascript
shootWaitedFrames++;
if (shootWaitedFrames > shootWait) {
　　　　 shoot();
　　　　 shootWaitedFrames = 0;;
}
```

通过计算函数drawScreen()的调用次数，当次数达到8次时，游戏会自动射击一发子弹。另外，可以通过修改shootWait的值来加快或减慢射击的速度。此外，还可以通过减小该值让声音更加频繁的出现，以此来达到测试Web Audio API的目的。

提示

> 在本书出版时，Chrome是唯一支持本例子的浏览器。另外，函数noteOn()将很快被函数start()取代。

读者可以运行本书代码包中的CH7EX10.html来体验新版的太空掠夺者。不过，在使用时还有一些需要注意的地方。

（1）需要在一个Web服务器上部署该例子，否则方法XMLHttpRequest()可能无法正常工作。

（2）如果不能正确加载音频，就需要在服务器的配置里上添加MIME类型。

正如读者所看到的，Web Audio API提供了一套在Canvas应用程序中高效播放声音的架构。利用Web Audio API可以实现很多功能，如添加过滤器以及获取音频数据进行可视化的音频处理等。在太空掠夺者的开发中，我们仅仅使用了该接口非常简单的功能。由于Web Audio API仍处於不断变化中，因此，查看W3C技术规范是了解和学习这项新技术的最好方法。

