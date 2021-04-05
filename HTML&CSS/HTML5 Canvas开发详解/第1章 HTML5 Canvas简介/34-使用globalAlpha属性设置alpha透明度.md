### 1.11.3　使用globalAlpha属性设置alpha透明度

之所以选择使用context.globalAlpha属性设置动画是因为它非常容易解释，非常适合在Canvas上制作一个动画效果的展示。context.globalAlpha属性用于在画布上设置透明度。这个属性可以接受0～1之间的数字，表示设置给属性之后绘制对象的不透明度的百分比。例如：

```javascript
context.globalAlpha = 0;
```

上面的代码将会设置后续渲染的对象的不透明度为0%，即完全透明。

```javascript
context.globalAlpha = 1;
```

上面的代码将会设置后续渲染的对象为100%不透明，即透明度是0%。

```javascript
context.globalAlpha = .5;
```

上面的代码将会设置后续渲染的对象为50%不透明，即50%透明。

通过在循环中修改这些值，就可以在画布上绘制出淡入淡出的效果。

提示

> context.globalAlpha属性会影响后续绘制的所有对象。因此，如果不希望在绘制对象时使用上一个对象绘制时的context.globalAlpha属性值，则需要在将对象绘制在画布上之前重置该属性的值。

