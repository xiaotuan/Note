### 9.4.5　camera对象

用户所看到的可视窗口被称为camera（镜头）。它在每个时刻只显示基于区块的世界的一部分。用户可以通过按下方向键移动镜头，从而实现区块地图的滚动。

camera对象的属性如下所示。

```javascript
camera.height=theCanvas.height;
camera.width=theCanvas.width;
camera.rows=camera.height / world.tileHeight;
camera.cols=camera.width / world.tileWidth;
camera.dx=0;
camera.dy=0;
camera.x=0;
camera.y=0;
```

这里并没有给出camera的全部代码，仅仅给出了与移动和绘制相关的属性，当用户按下方向键时，将在setTimeOut函数中进行绘制。height和width属性的值就是Canvas的尺寸（160×160）。x和y的值表示镜头相对于游戏世界左上角的坐标。在粗糙滚动中，这个值就是0或32的倍数（区块的高和宽都是32）。镜头左上角在x轴方向的最大值是世界的宽度（本例中是480）减去镜头的宽度（本例中是160）。通过这种方式，镜头永远也不会绘制世界地图数组中不存在的区块。

精确滚动的原理与之相似，只不过camera左上角的坐标x和y的值可以是0到最大值之间的任意值。计算最大值的目的同样是为了确保不会在区块地图的右边和底边绘制不存在的区块。两者根本的差别在于：每次不再滚动32像素，而是1～32之间的任意值，甚至可以更多。但是，这样的结果相当于一个超级粗糙的滚动，在实际应用中是不会用到的。

dx和dy的值是当用户按键时，在每一帧中向x和y的移动的像素数。

正如读者所看到的，镜头会根据世界中定义的tileHeight和tileWidth动态计算所需要的行和列。接下来介绍游戏世界的World对象。

