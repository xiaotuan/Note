[toc]

> 权威参考：<http://www.w3.org/TR/css-transforms-1/>。

`CSS3` 变形包括 `3D` 变形和 `2D` 变形，`3D`变形使用基于 `2D` 变形的相同属性。

`CSS 2D Transform` 获得了各主流浏览器的支持，但是 `CSS 3D Transform` 支持程度不是很完善。考虑到浏览器兼容性，`3D` 变形在实际应用时应添加私有属性，并且个别属性在某些主流浏览器中并未得到很好的支持，简单说明如下：

+ 在 `IE 10+` 中，`3D` 变形部分属性未得到很好的支持。
+ `Firefox 10.0` 至 `Firefox 15.0` 版本的浏览器，在使用 `3D` 变形时需要添加私有属性 `-moz-`，但从 `Firefox 16.0+` 版本开始无须添加浏览器私有属性。
+ `Chrome 12.0+` 版本中使用 `3D` 变形时需要添加私有属性 `-webkit-`。
+ `Safari 4.0+` 版本中使用 `3D` 变形时需要添加私有属性 `-webkit-`。
+ `Opera 15.0+` 版本才开始支持 `3D` 变形，使用时需要添加私有属性 `-webkit-`。
+ 移动设备中 `iOS Safari 3.2+`、`Android Browser 3.0+`、`Blackberry Browser 7.0+`、`Opera Mobile 24.0+`、`Chrome for Android 25.0+` 都支持 `3D` 变形，但在使用时需要添加私有属性 `-webkit-`；`Firefox for Android 19.0+` 支持 `3D` 变形，且无须添加浏览器私有属性。