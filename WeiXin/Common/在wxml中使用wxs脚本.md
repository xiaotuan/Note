<center><font size="5"><b>在 wxml 中使用 wxs 脚本</b></font></center>

```xml
<view>
    <text>等{{item.number}}件商品</text>
    <text class="list-item-price">{{priceFormat(item.price)}}</text>
</view>
<wxs module="priceFormat">
  module.exports = function(price) {
    return '￥ ' + parseFloat(price)
  }
</wxs>
```

##### WXS 语法参考

WXS（WeiXin Script）是小程序的一套脚本语言，结合 `WXML`，可以构建出页面的结构。

WXS 与 JavaScript 是不同的语言，有自己的语法，并不和 JavaScript 一致。

- [WXS 模块](https://developers.weixin.qq.com/miniprogram/dev/reference/wxs/01wxs-module.html)
- [变量](https://developers.weixin.qq.com/miniprogram/dev/reference/wxs/02variate.html)
- [注释](https://developers.weixin.qq.com/miniprogram/dev/reference/wxs/03annotation.html)
- [运算符](https://developers.weixin.qq.com/miniprogram/dev/reference/wxs/04operator.html)
- [语句](https://developers.weixin.qq.com/miniprogram/dev/reference/wxs/05statement.html)
- [数据类型](https://developers.weixin.qq.com/miniprogram/dev/reference/wxs/06datatype.html)
- [基础类库](https://developers.weixin.qq.com/miniprogram/dev/reference/wxs/07basiclibrary.html)