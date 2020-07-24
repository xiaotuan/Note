<center><font size="5"><b>margin 中 auto 属性的说明</b></font></center>

margin:auto 属性可以让元素水平居中，但是不能让元素垂直居中。下面是它的工作原理说明：

定义 auto 元素，因元素类型和上下文而异。在边距中，auto 可以表示两种情况：占用可用空间或0 px。这两个将为元素定义不同的布局。

+ 自动占用可用空间

这我们利用auto最常见的用法。通过分配 auto 元素的左右边距，它们可以平等地占据元素容器中的可用水平空间——因此元素将居中。

```xml
<div id="outer">
<div id="inner"></div>
</div>
```

```css
#inner {
  margin: auto;
  width: 250px;
  height: 125px;
  background-image: linear-gradient(45deg, #84ECEF 10%, #F8F62F 60%, #FDC018);
}

#outer {
  height: 500px;
  width: 500px;
  background: #1F1D20;
  background-image: linear-gradient(#757575 1px, transparent 1px), linear-gradient(90deg, #757575 1px, transparent 1px);
  background-size: 25px 25px;
}
```



但是，这只适用于水平边距，它不适用于浮动和内联元素，并且它本身也不能用于绝对和固定定位元素。

由于auto左右边距均匀地占据“可用”空间，当你auto只给出其中一个时，你认为会发生什么？

左边距或右边距auto将占据所有“可用”空间，使元素看起来像是向右或向左偏移。

```xml
<div id="outer">
<div id="inner"></div>
</div>
```

```css
#inner {
  margin-right: auto;
  width: 250px;
  height: 125px;
  background-image: linear-gradient(45deg, #84ECEF 10%, #F8F62F 60%, #FDC018);
}

 

#outer {
  height: 500px;
  width: 500px;
  background: #1F1D20;
  background-image: linear-gradient(#757575 1px, transparent 1px), linear-gradient(90deg, #757575 1px, transparent 1px);
  background-size: 25px 25px;
}
```



+ “auto”为0px

如前所述，auto在浮动，内联和绝对元素中不起作用。所有这些元素已经决定了它们的布局，所以没有auto用于边距并期望它像这样集中。

这将破坏使用类似float的最初目的。因此设置这些元素的auto值为0px。

auto如果它没有宽度，也不会对典型的块元素起作用。到目前为止我向你展示的所有例子都有宽度。

值的宽度auto将具有0px边距。块元素的宽度通常覆盖其整个容器，它是auto或100%，因此margin:auto将被设置为0px。

+ auto设置垂直会是怎样的呢？

auto在顶部和底部边距中总是计算为0px（绝对元素除外）。W3C规范说它是这样的：

“如果”margin-top“或”margin-bottom“为”auto“，则其使用值为0”

到目前为止，为什么这没有说。这可能是因为典型的垂直页面流，页面大小在高度方面增加。因此，相对于页面本身而言，将元素垂直居中于其容器中不会使其显示为居中，这与水平完成（在大多数情况下）不同。

也许是因为同样的原因，他们决定为绝对元素添加一个例外，它可以在整个页面的高度垂直居中。

这也可能是由于边缘坍塌效应（相邻元素“边缘”的崩溃），这是垂直边距的另一个例外。

然而，后者似乎是一个不太可能的情况 - 因为不会折叠其边距的元素 - 如Floats和overflow其他元素visible，仍然为其分配0px垂直边距auto。

+ 以绝对定位元素为中心

由于绝对定位元素恰好存在异常，我们将使用auto值垂直和水平居中。但在此之前，我们需要找出margin:auto实际工作的时间，就像我们希望它在绝对定位的元素中一样。

这是另一个W3C规范的用武之地：

“如果”left“，”width“和”right“中的所有三个都是”auto“：首先将”margin-left“和”margin-right“的任何”auto“值设置为0 ... ”

“如果三者中没有一个是”自动“：如果”margin-left“和”margin-right“都是”auto“，则在额外约束条件下解决方程式，即两个边距得到相等的值”

这几乎说，对水平auto的利润率，抓住间隔相等，则对值left，width并且right不应该auto，他们的默认值。因此，我们所要做的就是在绝对定位的元素中赋予它们一些价值。left并且right应该具有相同的值以实现完美的居中。

该规范还提到了垂直边距类似的东西。

“如果”top“，”height“和”bottom“中的所有三个都是auto，则将”top“设置为静态位置...”

“如果三者中没有一个是”自动“：如果”margin-top“和”margin-bottom“都是”auto“，则在额外约束下解决方程式，即两个边距得到相等的值......”

因此，对于一个绝对元件被垂直居中，其top，height和bottom值不应该auto。

现在结合所有这些，这是我们将得到的：

```xml
<div id="outer">
<div id="inner"></div>
</div>
```

```css
#inner {
  margin: auto;
  position: absolute;
  left: 0px;
  right: 0px;
  bottom: 0px;
  top: 0px;
  width: 250px;
  height: 125px;
  background-image: linear-gradient(45deg, #84ECEF 10%, #F8F62F 60%, #FDC018);
}

#outer {
  position: relative;
  height: 500px;
  width: 500px;
  background: #1F1D20;
  background-image: linear-gradient(#757575 1px, transparent 1px), linear-gradient(90deg, #757575 1px, transparent 1px);
  background-size: 25px 25px;
}
```



**最后**

如果您想要将页面上的元素向右或向左偏移而没有包含它的其他元素（就像浮点数一样），请记住有auto用于边距的选项。

将元素转换为绝对定位只是为了使它可以垂直居中可能不是一个好主意。还有其他选项，如flexbox和CSS变换，更适合那些。

   