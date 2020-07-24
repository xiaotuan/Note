<center><font size="5"><b>关于 swiper 组件显示效果问题</b></font></center>

[toc]

#### 问题描述

要求达到下面的效果：

![03](./images/03.jpg)

但是当该小程序在其他大屏幕设备下运行的时候，图片出现被裁剪和指示器跑到图片上的问题。如下所示：

![04](./images/04.jpg)

具体代码如下：

```xml
<block wx:for="{{listData}}" wx:key="itemlist">
  <!-- 菜单轮播图 -->
  <swiper indicator-dots="{{indicatorDots}}" autoplay="{{autoplay}}" interval="{{interval}}" duration="{{duration}}">
    <block wx:for="{{item.imgUrls}}" wx:for-item="imgItem" wx:key="{{item.id}}">
      <swiper-item>
        <image class="slide-image" src="{{imgItem.src}}"></image>
      </swiper-item>
    </block>
  </swiper>
</block>
```

```css
/* 轮播图样式 */
.slide-image{
  width:100%;
  height:280rpx;
}
```

#### 问题分析

这个应该是图片的尺寸与轮播组件尺寸不一致问题，上面的轮播组件使用默认的宽高，这个设置不透明。因此，在样式中给出轮播组件的宽高即可解决问题。

#### 解决方法

为 `swiper` 添加 `class` 属性：

```xml
<block wx:for="{{listData}}" wx:key="itemlist">
  <!-- 菜单轮播图 -->
  <swiper class="menu-swiper" indicator-dots="{{indicatorDots}}" autoplay="{{autoplay}}" interval="{{interval}}" duration="{{duration}}">
    <block wx:for="{{item.imgUrls}}" wx:for-item="imgItem" wx:key="{{item.id}}">
      <swiper-item>
        <image class="slide-image" src="{{imgItem.src}}"></image>
      </swiper-item>
    </block>
  </swiper>
</block>
```

为 `swiper` 添加宽高样式：

```css
/* 轮播图样式 */
.menu-swiper {
  width: 100vw;
  height: 360rpx;
}

.slide-image{
  width:100%;
  height:280rpx;
}
```

