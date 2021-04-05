### 8.7.2　使用Alpha通道实现飞船淡入

在Geo Blaster Basic游戏中，当一个新的玩家飞船进入游戏屏幕时，采用从透明到不透明的淡入效果。例8-7展示了如何在游戏中创建透明变换。

使用画布的context.globalAlpha属性时，仅需要在绘制游戏图形之前为它设置一个0～1之间的数值。在代码中创建一个新的变量，命名为alpha。这个变量用于保存玩家飞船当前的不透明度。每次将它增加0.01，直到1为止。在实际创建游戏时，在它到达1时停止递增，然后开始游戏关卡。但是在这个演示中，仅仅是让这个过程不断重复。

例8-7　使用Alpha通道实现玩家飞船淡入

```javascript
//canvasApp级变量
　 var x = 50;
　 var y = 50;
　 var width = 20;
　 var height = 20;
　 var alpha = 0;
　 context.globalAlpha = 1;
　 function drawScreen(){
　　　context.globalAlpha = 1;
　　　context.fillStyle = '#000000';
　　　context.fillRect(0, 0, 200, 200);
　　　context.fillStyle = '#ffffff';
　　　context.font = '20px sans-serif';
　　　context.textBaseline = 'top';
　　　context.fillText ("Player Ship - alpha", 0, 180);
　　　context.globalAlpha = alpha;
　　　context.save(); //将当前画布状态保存到栈中
　　　context.setTransform(1,0,0,1,0,0); // 重置变换矩阵
　　　//将画布原点平移到玩家飞船中心
　　　context.translate(x+.5*width,y+.5*height);
　　　//绘制飞船
　　　context.strokeStyle = '#ffffff';
　　　context.beginPath();
　　　//将位置硬编码
　　　context.moveTo(0,-10);
　　　context.lineTo(9,9);
　　　context.lineTo(0,-1);
　　　context.moveTo(-1,-1);
　　　context.lineTo(-10,9);
　　　context.lineTo(-1,-10);
　　　context.stroke();
　　　context.closePath();
　　　//恢复上下文
　　　context.restore(); //将旧的状态恢复到屏幕
　　　//增加不透明度
　　　alpha+=.01;
　　　if (alpha > 1){
　　　alpha=0;
　　　}
　 }
```

