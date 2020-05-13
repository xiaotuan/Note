<center><font size="5"><b>image 的使用</b></font></center>

`<image/>` 默认宽度为300px，默认高度为225px，属性如下：
+ `src` ：图片资源地址。
+ `mode` ：图片的裁剪、缩放模式。默认值为：`scaleToFill`。
+ `binderror` ：当错误发生时，发布到 App Service 的事件名，事件对象 `event.detail = { errMsg: 'something wrong'}`。
+ `bindload` ：当图片载入完毕时，发布到 App Service 的事件名，事件对象 `event.detail = { height: '图片高度px', width: '图片宽度px' }`。

`mode` 属性可使用的值有：

1. 缩放模式

+ `scaleToFill`：不保持纵横比缩放图片，使图片的宽高完全拉伸至填满 `image` 元素。
+ `aspectFit`：保持纵横比缩放图片，使图片的长边能完全显示出来。
+ `aspectFill`：保持纵横比缩放图片，只保证图片的短边能完全显示出来。
+ `widthFix`：宽度不变，高度自动变化，保持原图宽度不变，这时图片原有高度样式会失效。

2. 裁剪模式

+ `top`：不缩放图片，只显示图片的顶部水平中间区域。
+ `bottom`：不缩放图片，只显示图片的底部水平中间区域。
+ `center`：不缩放图片，只显示图片的中间区域。
+ `left`：不缩放图片，只显示图片的左边垂直中间区域。
+ `right`：不缩放图片，只显示图片的右边垂直中间区域。
+ `top left`：不缩放图片，只显示图片的左上边区域。
+ `top right`：不缩放图片，只显示图片的右上边区域。
+ `bottom left`：不缩放图片，只显示图片的左下边区域。
+ `bottom right`：不缩放图片，只显示图片的右下边区域。