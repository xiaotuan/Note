### 1.10.6　导出Canvas到图像

之前，本章简要讨论了Canvas对象的toDataUrL()属性。这里将使用这个属性让用户能够随时创建一个游戏画面的图像，类似基于Canvas制作的游戏中的屏幕捕捉功能。

此处需要在HTML页面上创建一个按钮，用户单击该按钮就可以获得屏幕捕捉的图像。下面将这个按钮添加到<form>中，然后赋予其编号createImageData。

```javascript
<form>
<input type="button" id="createImageData" value="Export Canvas Image">
</form>
```

在init()函数中，通过document对象的getElementById()方法获得了这个表单元素的参考。然后，使用createImageDataPressed()方法为按钮的“单击”事件设置一个事件处理器。

```javascript
var formElement = document.getElementById("createImageData");
formElement.addEventListener('click', createImageDataPressed, false);
```

在canvasApp()函数中，定义createImageDataPressed()函数作为事件处理器。这个函数调用window.open()，并将Canvas.toDataUrl()方法的返回数值传送给窗口。由于这个数据表单是一个有效的.png，因此图像会在一个新窗口中显示。

```javascript
function createImageDataPressed(e){
　　window.open(theCanvas.toDataURL(),"canvasImage","left=0,top=0,width=" +
　　theCanvas.width + ",height=" + theCanvas.height +",toolbar=0,resizable=0");
　　}
```

提示

> 第3章将深入讨论这些过程。

