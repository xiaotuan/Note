### 2.3　Canvas状态

在Canvas环境中绘图时，可以利用所谓的绘图堆栈状态。每个状态随时存储Canvas上下文数据。下面是存储在状态堆栈的数据列表。

+ 变换矩阵信息。例如旋转或平移时，使用context.rotate()方法和context.setTransform()方法。
+ 当前剪贴区域。
+ 画布属性的当前值，如下所示（但不局限于此）。

```javascript
——globalAlpha
——globalCompositeOperation
——strokeStyle
——textAlign, textBaseline
——lineCap, lineJoin, lineWidth, and miterLimit
——fillStyle
——font
——shadowBlur, shadowColor, shadowOffsetX, and shadowOffsetY
```

本章稍后会讲到这些状态。

