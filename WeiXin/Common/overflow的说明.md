<center><font size="5"><b>overflow  的说明</b></font></center>

`overflow` 属性表示元素溢出后的处理方法，该属性只对直接子元素有效，不会对子元素的子元素有任何影响。例如：

```xml

<view class="content">
  <view class="list-item" wx:for="{{list}}" wx:key="id">
    <view class="list-item-l">
      <view>消费</view>
      <view class="list-item-time">{{item.pay_time}}</view>
    </view>
    <view class="list-item-r">
      <text>{{priceFormat(item.price)}}</text>
    </view>
  </view>
</view>

```

```css
.list-item {
  display: flex;
  height: 76rpx;
  padding: 42rpx 20rpx;
  border-bottom: 1rpx solid #ececec;
  overflow: hidden;
}

.list-item-l {
  flex: 1;
}

.list-item-r {
  line-height: 76rpx;
}
```

上面的 `list-item` 元素设置了 `overflow` 属性，如果是 `list-item-time` 元素溢出的话将不会被隐藏，如果需要在 `list-item-time`  溢出后被隐藏，需要将 `overflow` 属性移至 `list-item-l` 元素中即可。