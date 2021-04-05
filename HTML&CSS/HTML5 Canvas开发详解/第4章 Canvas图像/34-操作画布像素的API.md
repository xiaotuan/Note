### 4.8.1　操作画布像素的API

操作画布像素API使用户可以利用CanvasPixelArray接口“取出”、“放入”、“变更”单个像素。ImageData是操作的基础对象类型，是用createImageData()函数调用创建的对象的一个实例。本节将从这里开始。

createImageData()函数设置了部分内存来存储单个像素的有价值数据，基于以下3个构造函数。

+ imagedata = context.createImageData(sw, sh)

sw和sh参数代表Image Data对象的width值和height值。例如，imagedata=createImage Data（100,100）将创建一个100 × 100的内存区域来储存像素数据。

+ imagedata = context.createImageData(imagedata)

imagedata参数代表ImageData的一个独立实例。这个构造函数使用与参数ImageData相同的宽和高创建了一个ImageData对象。

+ imagedata = context.createImageData()

这个构造函数返回一个ImageData实例。

#### 1．ImageData属性

ImageData对象包含以下3个属性。

+ ImageData.height：这个属性返回ImageData实例的高度像素值。
+ ImageData.width：这个属性返回ImageData实例的宽度像素值。
+ ImageData.data：这个属性返回一个像素的一维数组来代表图像数据。每个像素的图像数据以32位颜色信息存储。这意味着在这个数据数组中，每4个数字开始一个新的像素。数组中的4个元素分别代表单个像素的红、绿、蓝和alpha透明度值。

#### 2．取出图像数据

为从画布获取一组像素数据，并将其放入一个ImageData实例中，使用了getImageData()函数调用。

```javascript
imagedata = context.getImageData(sx, sy, sw, sh)

```

sx、sy、sw和sh定义了从画布复制到ImageData实例的源矩形的位置和尺寸。

提示

> 如果图像文件的原始域与Web页面的原始域不相同，系统将会弹出一个安全错误，从而影响本地文件（运行在读者自己的硬盘上，而不是本地运行在Web服务器上或是在远程服务器上）。大多数浏览器会将本地图像文件视为来自与Web页面不同的域。当在一个Web服务器上运行的时候，对本地文件不会弹出这个错误。当前版本的Safari（6.02）、火狐以及IE(10)对本地文件不会弹出这个错误。

#### 3．放入图像数据

为将ImageData实例的像素复制到画布上，可使用putImageData()函数调用。这个调用有以下两个不同的构造函数。

```javascript
context.putImageData (imagedata, dx, dy)
context.putImageData (imagedata, dx, dy [, dirtyX, dirtyY,dirtyWidth, dirtyHeight ])

```

第一个构造函数将整个ImageData实例简单地绘制到destinationX(dx)和destinationY (dy)位置处。第二个构造函数也是如此，但是允许传输“dirty矩形”，这是指将ImageData绘制到画布上的区域。

