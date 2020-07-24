<center><font size="5"><b>设置 flex 两行之间的距离</b></font></center>

通过如下样式属性，我们可以实现依次显示组件的样式：

```css
.bottom-box{
  margin-top:40rpx;
  display: flex;
  width: 100%;
  padding: 0 20rpx;
  flex-direction: row ;
  flex-wrap:wrap;
  justify-content:space-between;
  box-sizing: border-box;
  
}
.bottom-pic{
  width: 49%;
  display:inline-block;
}
.btm-image{
  width:100%;
  height:170rpx
}
```

![07](./images/07.jpg)

从上图可以看出两行之间是有间距的，但是在样式代码中并没有相关的设置。如果需要使两行之间没有间距，可以在上面 `.bottom_pic` 的样式中添加 `margin-bottom: -4px;` 属性即可：

```css
.bottom-pic{
  width: 49%;
  display:inline-block;
  margin-bottom: -4px;
}
```

> 上面设置的 `-4px` 是通过测试出来的，在微信小程序的模拟器中测试通过。

同理也可以通过上面的方式增大两行之间的间距。