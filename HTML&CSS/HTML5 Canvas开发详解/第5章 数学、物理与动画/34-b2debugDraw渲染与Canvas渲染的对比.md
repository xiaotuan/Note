### 5.6.9　b2debugDraw渲染与Canvas渲染的对比

Box2D的b2debugDraw功能是一种测试物理世界的方法，可以在浏览器中查看其工作情况。它并不是程序的物理表现形式。通过使用debugDraw呈现创建的物体就能够以动态的方式查看它们。在示例CH5EX22.html中，展示了如何将Box2D应用到画布上。现在来看看创建的物理模型。

下面的代码可以称得上是b2debugDraw运行的标准范例。其中，SetSprite()函数将一个画布的环境作为参数。这意味着，画布将完全被b2debugDraw的输出所控制。这就是为什么这种方法仅用于测试的原因。SetScaleFactor()函数需要制定一个值（30），用于从像素转换为MTS单位。SetFillAlpha()函数用于设置对象被显示时的线条的透明度。类似的，SetLineThickness()函数用于设置线条的粗细。SetFlags()函数需要指定一个二进制标志位的显示参数：e_shapeBit表示绘制对象，e_jointBit表示绘制关节（由于本例中没有关节，因此看不到）。

```javascript
var debugDraw = new b2DebugDraw();
debugDraw.SetSprite (context2);
debugDraw.SetDrawScale(30);
debugDraw.SetFillAlpha(0.3);
debugDraw.SetLineThickness(1.0);
debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);
world.SetDebugDraw(debugDraw);
```

