### 3.1.4　使用measureText

HTML5 Canvas环境对象包含一个有用的方法measureText()。当提供一个文本串时，它将在TextMetrics对象的表单中基于当前环境的设置（字体、大小等）返回一些关于该文本的属性。现在，TextMetrics对象只有一个属性：width。TextMetrics对象的Width属性给定了在画布上渲染时文本的确切像素宽度。它在居中文本时非常有用。

#### 1．用width居中文本

对于Text Arranger应用，这里使用TextMetrics对象将用户已经输入到textBox表单控件中的文本居中到画布。首先，通过message变量（其中包含了要显示的文本）传递给2D环境的measureText()方法的方式来获取TextMetrics的距离，并将其存储到名为metrics的变量中。

```javascript
var metrics =context.measureText(message);
```

然后，从metrics的width属性中获得文本的像素宽度，并将其存储到一个名为textWidth的变量中。

```javascript
var textWidth =metrics.width;
```

接下来，通过画布宽度的一半（theCanvas.width/2）来计算屏幕的中心。然后减去文本宽度的一半（textWidth/2）。这样做的目的是，在画布上的文本在没有任何对齐设置时显示为垂直左对齐（后面将详细介绍）。因此，为了居中文本，把它向左移动至自身宽度的一半，并且将文本的中心放到画布的绝对中心上。当程序允许用户选择文本的垂直对齐方式时，下一步将对它进行更新。

```javascript
var xPosition =(theCanvas.width/2) - (textWidth/2);
```

#### 2．计算文本的高度

为什么要获得文本的高度？其目的是当文本长度超过画布宽度时，可将文本截断变成多行，或者使它在屏幕上居中。当然，这就暴露了一个问题。TextMetrics对象不包含高度属性。也没有文本的字体大小的图片，因为它没有考虑到在字体下方画上基线的字体字形。虽然字体的大小可用于估算如何在屏幕中让字体纵向居中，但是如果考虑到需要把文本截成两行或者多行，那就没太大帮助了。因为还要考虑到字体的间隔，这可能是非常棘手的。

为了演示，下面将为文本创建一个yPosition变量，简单将文本定位到画布一半高度的位置上，而不是试图使用字体的大小垂直居中于画布上。字体的默认基准线是middle，这对于屏幕居中是非常棒的方法。下节将更多地讨论基准线。

```javascript
var yPosition =(theCanvas.height/2);
```

提示

> 在第11章的聊天室例子中，本书将为读者展示将文本分割为多行的例子。

