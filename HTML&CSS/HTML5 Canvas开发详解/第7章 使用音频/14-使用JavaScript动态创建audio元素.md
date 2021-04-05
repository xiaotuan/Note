### 7.4.1　使用JavaScript动态创建audio元素

动态创建audio元素的第一个步骤是定义一个名为audioElement的全局变量。在画布应用中使用这个变量保存HTMLAudioElement对象的实例。在HTML页面中，audio元素就是DOM对象HTMLAudioElement的实例。如果嵌入在HTML页面中，可将其引用为audio对象。如果是在JavaScript中动态创建的，就将其引用为HTMLAudioElement对象的实例。它们在本质上是一样的。

提示

> 不用为使用全局变量而感到焦虑。本章的结尾将展示一种可以将画布应用中的全局变量转换为局部变量的方法。

接下来，为window的load事件创建一个事件处理函数，名为eventWindowLoaded()。在这个函数中，调用DOM对象document的createElement()函数，传递audio作为参数值，以指定要创建的元素类型。这个方法可以动态创建一个audio对象，并将其放入DOM中。如果将这个对象赋值给audioElement变量，就可以通过调用DOM对象ducument.body的appendChild()方法将其动态地加入到HTML页面中。

```javascript
window.addEventListener('load', eventWindowLoaded, false);
var audioElement;
function eventWindowLoaded(){
　 audioElement = document.createElement("audio");
　 document.body.appendChild(audioElement);
```

然而，只是动态创建一个audio元素还不够，还需要将audioElement变量所代表的HTMLAudioElement对象的src属性设置为一个合法的音频文件才能加载并播放声音。但是，这里有一个问题：不知道当前的浏览器能够支持什么类型的音频文件。这里将创建一个名为supportedAudioForma()的函数来获取这个信息。将这个函数的返回值定义为一个字符串，这个字符串就代表了要加载的文件类型的扩展名。当得到这个扩展名时，就把它和要加载的音频名字连接起来，通过调用HTMLAudioElement对象的setAttribute()方法赋值给src属性。

```javascript
var audioType = supportedAudioFormat(audioElement);
```

如果supportedAudioFormat()函数没有返回一个合法的扩展名，程序将会出现错误，并终止运行。有一个简单的方法可以处理这种情况：使用alert()函数弹出警告消息，然后调用return语句从函数中退出。这是一个行之有效地终止程序运行的方法。虽然这种处理方式不够健壮，但是鉴于是示例的缘故，这样做是可以的。

```javascript
if (audioType == ""){
　 alert("no audio support");
　 return;
}
audioElement.setAttribute("src", "song1." + audioType);
```

最后，将像处理视频那样监听音频元素的canplaythrough时间，并在音频就绪时播放它。

```javascript
audioElement.addEventListener("canplaythrough",audioLoaded,false);
```

