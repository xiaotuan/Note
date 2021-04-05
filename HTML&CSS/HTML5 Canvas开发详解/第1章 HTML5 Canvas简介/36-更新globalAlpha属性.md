### 1.11.5　更新globalAlpha属性

由于本示例中的动画是由画布上文字的淡入和淡出组成的，因此在drawScreen()函数中的主要操作是根据fadeIn属性更新alpha的值。如果文字正在淡入（fadeIn为true），那么将alpha的值每次增加.01。如果alpha的值大于1（能够接受的最大值），那么将它重置为1，然后将fadeIn设置为false（这意味文字开始淡出）。如果fadeIn为false，那么进行相反的操作，当alpha属性为0时将fadeIn设置为true。在设置alpha属性的值之后，通过设置context.globalAlpha属性，将它应用到画布上。

```javascript
if (fadeIn) {
　　alpha += .01;
　　if (alpha >= 1) {
　　　　alpha = 1;
　　　　fadeIn = false;
　　}
} else {
　　alpha -= .01;
　　if (alpha < 0) {
　　　　alpha = 0;
　　　　fadeIn = true;
　　}
}
context.globalAlpha = alpha;
```

