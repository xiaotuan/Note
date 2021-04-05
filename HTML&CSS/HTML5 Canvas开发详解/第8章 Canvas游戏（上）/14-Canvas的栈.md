### Canvas的栈

Canvas的状态可以保存在栈中，也可以从栈中读取Canvas的状态。这一点对于游戏对象应用形状变换以及动画效果是非常重要的。因为用户希望形状变换仅作用于当前的游戏对象，而不是整个画布。在游戏中使用Canvas栈的基本步骤如下。

（1）将当前的画布保存在栈中。

（2）进行变换并绘制游戏对象。

（3）从栈中取出已保存的画布。

作为示例，为玩家飞船设置一个基本的旋转。在每帧中将飞船旋转1°。将飞船绘制在画布的左上角之后，就把它移动到一个新的位置。之所以这样做，是因为使用飞船的左上角作为定位点进行基本旋转的。定位点就是用于旋转和缩放的轴心位置。所以，如果继续将飞船放置在点（0，0）的位置，并绕飞船的左上角旋转，那么在一半的时间中将看不到飞船。因为飞船超出了画布的左边界和上边界。因此，要将飞船放置在点（50，50）的位置。

使用与例8-4相同的HTML代码，仅修改drawCanvas()函数。为了简化这个示例，将删除shipState变量，仅使用静止状态。在drawScreen()函数上方添加以下3个新变量。

```javascript
var rotation = 0; // 保存玩家飞船当前的旋转角度
var x = 50; // 保存绘制飞船起始点的X轴坐标
var y = 50; // 保存绘制飞船起始点的Y轴坐标
```

例8-5给出了完整代码。

例8-5　旋转图像

```javascript
//canvasApp 一级变量
　 var rotation=0;
　 var x=50;
　 var y=50;
　 function drawScreen(){
　　　// 绘制背景和文字
　　　context.fillStyle = '#000000';
　　　context.fillRect(0, 0, 200, 200);
　　　context.fillStyle　　 = '#ffffff';
　　　context.font　　　　　 = '20px sans-serif';
　　　context.textBaseline　= 'top';
　　　context.fillText ("Player Ship - rotate", 0, 180);
　　　//形状变换
　　　var angleInRadians = rotation * Math.PI / 180;
　　　context.save(); //将画布状态保存到栈中
　　　context.setTransform(1,0,0,1,0,0); // 恢复初始值
　　　//将画布的原点平移到玩家的中央
　　　context.translate(x,y);
　　　context.rotate(angleInRadians);
　　　//绘制飞船
　　　context.strokeStyle = '#ffffff';
　　　context.beginPath();
　　　context.moveTo(10,0);
　　　context.lineTo(19,19);
　　　context.lineTo(10,9);
　　　context.moveTo(9,9);
　　　context.lineTo(0,19);
　　　context.lineTo(9,0);
　　　context.stroke();
　　　context.closePath();
　　　//恢复上下文
　　　context.restore(); //将原有状态恢复到屏幕
　　　//增加旋转角度
　　　rotation++;
}
```

可以看到，玩家飞船每次顺时针旋转 1°。正如之前多次提到过的那样，必须将角度转换为弧度，因为context.rotate()需要使用弧度进行旋转变换的运算。在下一节中，将深入讨论在Geo Blaster Basic游戏中用到的形状变换。

